from moviepy.editor import TextClip, CompositeVideoClip, AudioFileClip
from gtts import gTTS
import os

def generate_video(text, output_path="output.mp4"):
    # تحويل النص لصوت
    tts = gTTS(text, lang='en')
    audio_file = "tts.mp3"
    tts.save(audio_file)

    # عمل فيديو من خلفية سوداء ونص
    clip = TextClip(text, fontsize=60, color='white', size=(1280, 720), method='caption')
    duration = AudioFileClip(audio_file).duration
    clip = clip.set_duration(duration).set_position('center')

    audioclip = AudioFileClip(audio_file)
    videoclip = clip.set_audio(audioclip)
    videoclip.write_videofile(output_path, fps=24)

    os.remove(audio_file)
    return output_path
