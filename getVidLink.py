from pytubefix import YouTube  # Updated import
from pydub import AudioSegment
import os

def download_youtube_content(link, download_type='video'):
    yt = YouTube(link)
    
    if download_type == 'video':
        stream = yt.streams.get_highest_resolution()
        stream.download()
        print(f"Downloaded video: {yt.title}.mp4")
    elif download_type == 'mp3':
        stream = yt.streams.filter(only_audio=True).first()
        audio_file = stream.download(filename='temp_audio')
        AudioSegment.from_file(audio_file).export(f"{yt.title}.mp3", format="mp3")
        os.remove(audio_file)  # Remove temporary audio file
        print(f"Downloaded audio: {yt.title}.mp3")
    else:
        print("Invalid download type. Use 'video' or 'mp3'.")

if __name__ == "__main__":
    link = input("Enter the YouTube link: ")
    download_type = input("Enter download type (video/mp3): ").strip().lower()
    download_youtube_content(link, download_type)