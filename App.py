import configparser
import RedditApi as api
import json_parser as parser
import tts_service as tts
import video_service as video
import sys

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

def generate_json_file():
    client_id,client_secret,user_agent = init_config()
    reddit = api.get_reddit_instance(user_agent, client_id, client_secret)
    hot_posts = api.get_hot_posts(reddit, 'StoryTime', 2)
    parser.parse_to_json(hot_posts)

def generate_tts(id):
    duration = tts.generate_speech('./json_data/data.json', id)
    return duration

def generate_video(id,text):
    video.generate_video(video='./video_files/Default.mp4', audio=f'./audio_files/{id}.mp3', text=text)

#TODO interesting chat gpt answers reddit?
if __name__ == "__main__":
        generate_json_file()
        id = 0
        duration = generate_tts(id)
        generate_video(id, parser.get_content_from_json(id))