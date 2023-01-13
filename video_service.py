import moviepy.editor as mp
import os

def generate(video, audio, text, audio_mapping):
    #video
    #f'./audio_files/'
    #["...","..."]
    #['3_0.mp3', '3_1.mp3', '3_2.mp3', '3_3.mp3']
    
   
    text_audio_file_clips = []
    for file in audio_mapping:
        text_audio_file_clips.append(mp.AudioFileClip(audio+file))
    
    aud = mp.AudioFileClip(audio+audio_mapping[0][0]+".mp3")
    vid = mp.VideoFileClip(video)

    if aud.duration > 180:
        raise Exception("Video too long to upload")

    original_audio = vid.audio
    original_audio = original_audio.set_duration(aud.duration)
    original_audio = original_audio.volumex(0.1)

    new_audio = mp.CompositeAudioClip([original_audio, aud])

    vid = vid.set_audio(new_audio)
    
    vid = vid.resize((1080,1920))
    
    finished_clips = []
    start_time = 0
    for i, clip in enumerate(text_audio_file_clips):
        txt_clip = mp.TextClip(text[i], fontsize=36, color='black', bg_color='white', font='Amiri-Bold', method='caption', size=(800,0), align='center')
        
        txt_clip = txt_clip.set_duration(clip.duration-1)
        txt_clip = txt_clip.set_position('center')
        txt_clip = txt_clip.set_start(start_time)
        
        start_time += clip.duration
        finished_clips.append(txt_clip)
        txt_clip.close()

    tc = mp.concatenate_videoclips(finished_clips)
    tc = tc.set_position('center')
    
    vid = mp.CompositeVideoClip([vid, tc])
    vid = vid.set_fps(30)
    vid = vid.set_duration(aud.duration)
    
    vid.write_videofile("./out_files/generated_video"+str(audio_mapping[0][0])+".mp4")
    aud.close()
    vid.close()
    new_audio.close()


def generate_video(video, audio, text, audio_mapping):
    print("Generating video...") 
    generate(video=video, audio=audio, text=text, audio_mapping=audio_mapping)
    
    
    
