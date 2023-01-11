import pyttsx3
import json

def generate_speech(json_object, id):
    with open(json_object,'r', encoding='UTF-8') as f:
        data = json.load(f)
    
    for post in data:
        '''with open('./subtitles/subtitles.txt','r', encoding='UTF-8') as f:
            all_content = f.read()
            divided_content = all_content.split('\n\n')
        return _create_file(divided_content[int(id)], str(id)+'.mp3')'''
        if post['id'] == id:
            return _create_file(post['content'], str(id)+'.mp3')
    raise Exception("Post not found")
        
def _create_file(text, name):
    print("Generating speech...")
    engine = pyttsx3.init()
    engine.setProperty('rate', 180)
    engine.setProperty('volume', 0.9)

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.save_to_file(text, './audio_files/'+name)
    engine.runAndWait()
    return engine.getProperty('rate') * len(text.split())


    