import praw

def get_reddit_instance(user_agent, client_id, client_secret):
    reddit = praw.Reddit(user_agent=user_agent, client_id=client_id, client_secret=client_secret)
    return reddit

def get_hot_posts(reddit,subreddit, limit=10):
    hot_posts = [{"id":id,"title":p.title, "post_id":p.id} for id,p in enumerate(reddit.subreddit(subreddit).hot(limit=limit))]
    #generate_content_file(reddit,hot_posts)
    for i,post in enumerate(hot_posts):
        print("Downloading post: ", i+1, " of ", len(hot_posts),"...")
        post['content'] = _get_content(reddit,post['post_id'])
    return hot_posts

def generate_content_file(reddit,hot_posts):
    with open('./subtitles/.','w', encoding='UTF-8') as f: 
        for i,post in enumerate(hot_posts):
            print("Downloading post: ", i+1, " of ", len(hot_posts),"...")
            triplets = _splitTextToTriplet(_get_content(reddit,post['post_id']))
            '''minutes = 0
            for j,triplet in enumerate(triplets):
                f.write('\n')
                f.write(f'{j+1}'+'\n')
                if j < 10: 
                    f.write(f'00:0{minutes}:0{j%60},000 --> 00:0{minutes}:0{(j+1)%60},000\n')
                else:
                    f.write(f'00:0{minutes}:{j%60},000 --> 00:0{minutes}:{(j+1)%60},000\n')
                if j == 60:
                    minutes += 1
                f.write(triplet)
                f.write('\n')'''
            

def _splitTextToTriplet(string):
    words = string.split()
    grouped_words = [' '.join(words[i: i + 3]) for i in range(0, len(words), 3)]
    return grouped_words


def _get_content(reddit,post_id):
    submission = reddit.submission(id=post_id)
    return submission.selftext
