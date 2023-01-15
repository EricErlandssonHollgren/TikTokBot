import pyttsx3
import json
import json_parser as parser


def generate_speech(json_object, id):
    mapping = []
    with open(json_object,'r', encoding='UTF-8') as f:
        data = json.load(f)

    for post in data:
        if post['id'] == id:
            _create_file(post['content'], str(id)+'.mp3')
                
    for post in data:
        if post['id'] == id:
            word_90_segments = parser.splitter(90, post['content'])
            print("Generating speech...")
            for i, segment in enumerate(word_90_segments):
                _create_file(segment, str(id)+'_'+str(i)+'.mp3')
                mapping.append(str(id)+'_'+str(i)+'.mp3')
            return mapping
    
    raise Exception("Post not found")

#90 words then split

def _create_file(text, name):
    engine = pyttsx3.init()
    engine.setProperty('rate', 180)
    engine.setProperty('volume', 0.5)

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.save_to_file(text, './audio_files/'+name)
    engine.runAndWait()
    return engine.getProperty('rate') * len(text.split())


    