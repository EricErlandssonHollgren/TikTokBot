import moviepy.editor as mp
import moviepy.video.fx.all

def merge_video_audio(video, audio, text):
    aud = mp.AudioFileClip(audio)
    vid = mp.VideoFileClip(video)

    vid = vid.set_audio(aud)
    vid = vid.set_duration(aud.duration)
    vid = vid.resize((1080,1920))
    
    text_clip = mp.TextClip(text, fontsize=36, color='white', font='Amiri-Bold')
    text_clip = text_clip.set_duration(vid.duration)
    text_clip = text_clip.set_position('center')
    text_clip = text_clip.set_start(0)

    #vid = mp.CompositeVideoClip([vid, text_clip])
    #Rate = 3.0 words/second
    return vid

def generate_video(video, audio, text): 
    vid = merge_video_audio(video=video, audio=audio, text=text)
    print("Generating video...")
    vid.write_videofile(str(id)+".mp4", temp_audiofile='./tmp/tempaud.m4a', codec='libx264', audio_codec='aac', remove_temp=True)
