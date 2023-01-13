import configparser
import RedditApi as api
import json_parser as parser
import tts_service as tts
import video_service as video
import sys
import os
'''
********************************
*    Console Line arguments    *
-genjson [number of posts]     *
-novid                         *
********************************
'''
client_id = "client_id"
client_secret = "client_secret"
user_agent = "user_agent"

def init_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    client_id = config['reddit']['client_id']
    client_secret = config['reddit']['client_secret']
    user_agent = config['reddit']['user_agent']
    return client_id, client_secret, user_agent

def generate_json_file(count,subreddit = 'StoryTime'):
    client_id,client_secret,user_agent = init_config()
    reddit = api.get_reddit_instance(user_agent, client_id, client_secret)
    hot_posts = api.get_hot_posts(reddit, subreddit, count)
    parser.parse_to_json(hot_posts)

def generate_tts(id):
    mapping = tts.generate_speech('./json_data/data.json', id)
    return mapping

def generate_video(id,text,audio_mapping):
    video.generate_video(video='./video_files/Default.mp4', audio=f'./audio_files/', text=text, audio_mapping=audio_mapping)
       
def delete_audio_files():
    folder = './audio_files/'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)

if __name__ == "__main__":
    id = 0
    if len(sys.argv) > 1:
        if sys.argv[1] == '-genjson':
            generate_json_file(int(sys.argv[2]))
        elif sys.argv[1] == '-novid':
            mapping = generate_tts(id)
    else:
        mapping = generate_tts(id)
        generate_video(id = id, text=parser.get_90_content_from_json(id), audio_mapping=mapping)