from pytube import Playlist, YouTube
from pydub import AudioSegment
import os
import re

def get_video_links_from_playlist(playlist_url):
    """Extract video URLs from a YouTube playlist."""
    playlist = Playlist(playlist_url)
    return [video.watch_url for video in playlist.videos]

def download_video_as_mp3(video_urls, download_folder):
    """Download each video as MP3 and save in the specified folder."""
    os.makedirs(download_folder, exist_ok=True)  # Create the folder if it doesn't exist
    for url in video_urls:
        try:
            yt = YouTube(url)
            sanitized_title = sanitize_title(yt.title)
            print(f"Downloading: {sanitized_title}")

            audio_stream = yt.streams.filter(only_audio=True).first()
            if audio_stream is None:
                print(f"No audio stream available for {sanitized_title}. Skipping...")
                continue
            
            audio_file = audio_stream.download(output_path=download_folder, filename=f"{sanitized_title}.mp4")
            mp3_file = os.path.join(download_folder, f"{sanitized_title}.mp3")
            
            # Convert to MP3
            AudioSegment.from_file(audio_file).export(mp3_file, format="mp3")
            os.remove(audio_file)  # Remove the .mp4 file
            print(f"Downloaded and converted: {mp3_file}")

        except Exception as e:
            print(f"Error downloading {url}: {e}")

def sanitize_title(title):
    """Sanitize the title to create a valid filename."""
    return re.sub(r'[<>:"/\\|?*]', '', title)

# Replace with your playlist URL
playlist_url = 'https://www.youtube.com/playlist?list=PLBSOUwqQZcrxJdRzTUXFtRFejpD6uujNg'
video_urls = get_video_links_from_playlist(playlist_url)

# Folder to save downloaded MP3 files
download_folder = 'downloaded_mp3s'

download_video_as_mp3(video_urls, download_folder)
