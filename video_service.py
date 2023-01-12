import moviepy.editor as mp
import moviepy.video.fx.all

def generate(video, audio, text):
    aud = mp.AudioFileClip(audio)
    vid = mp.VideoFileClip(video)
    
    original_audio = vid.audio
    original_audio = original_audio.set_duration(aud.duration)
    original_audio = original_audio.volumex(0.1)
    new_audio = mp.CompositeAudioClip([original_audio, aud])

    vid = vid.set_audio(new_audio)
    vid = vid.set_duration(aud.duration)
    
    vid = vid.resize((1080,1920))
    
    text_clip = mp.TextClip(text, fontsize=36, color='black', bg_color='white', font='Amiri-Bold', method='caption', size=(800,0), align='center')
    text_clip = text_clip.set_duration(vid.duration)
    text_clip = text_clip.set_position('center')
    text_clip = text_clip.set_start(0)

    vid = mp.CompositeVideoClip([vid, text_clip])
    
    vid.write_videofile("./out_files/test.mp4")
        
    vid.close()

def generate_video(video, audio, text):
    print("Generating video...") 
    generate(video=video, audio=audio, text=text)
    
    
