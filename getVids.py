### UTILIZING PYTUBEFIX which is a fork of pytube that is more frequently maintained
### It also seems faster

from pytubefix import Playlist, YouTube
from pytubefix.cli import on_progress

import os

def download_video_as_mp4(video_urls, download_folder):
    """Download each video as MP4 and save in the specified folder."""
    os.makedirs(download_folder, exist_ok=True)  # Create the folder if it doesn't exist
    for url in video_urls:
        try:
            yt = YouTube(url, on_progress_callback=on_progress)  # Create YouTube object with progress callback
            print(f"Downloading: {yt.title}")
            ys = yt.streams.get_highest_resolution()  # Get the highest resolution video stream
            ys.download(output_path=download_folder)  # Download the video
        except Exception as e:
            print(f"Error downloading {url}: {e}")  # Log the error with the URL

######################## Make Changes Here !!! ###########################
# Replace with your playlist URL
playlist_url = 'https://www.youtube.com/playlist?list=PL54F1A17800EB6BF6'
pl = Playlist(playlist_url)

# Extract video URLs from the playlist
video_urls = [video.watch_url for video in pl.videos]  # Get the URLs of the videos

# Folder to save downloaded MP4 files
download_folder = 'mp4s'

download_video_as_mp4(video_urls, download_folder)  # Pass the list of URLs