YouTube Playlist to MP3 Downloader
Description
This script allows users to download entire playlists from YouTube as MP3 files.
It's a straightforward tool designed for music lovers who want to have their favorite tracks offline.

Features
Downloads all videos in a specified YouTube playlist.
Converts videos to MP3 format for easy playback.
Saves downloaded files in a designated folder.
Usage
Install Dependencies: Make sure you have pytube and pydub installed.

bash
Copy code
pip install pytube pydub
Set Up Your Playlist URL: Replace the playlist_url variable in the script with your desired YouTube playlist link.

Run the Script: Execute the script to start downloading.

Known Issues
Regex Recognition Error
YouTube periodically updates its website, which can break the regex patterns used in the script to extract video URLs. This may lead to errors such as:

lua
Copy code
Error downloading video: get_throttling_function_name: could not find match for multiple
Workaround
If you encounter this issue, you may need to modify the cipher.py file located in the pytube package. Specifically, you may need to adjust regex patterns that match the throttling function. Look for the line that defines the function pattern and ensure it is up-to-date.
The modification I made this time was to change the lines at 272 and 273 to the following:

r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&.*?\|\|\s*([a-z]+)',
r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])\([a-z]\)',

ENJOY THE FREE MUSIC!
