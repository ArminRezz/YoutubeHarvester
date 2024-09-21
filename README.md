# 🎵 YouTube Playlist to MP3 Downloader

This script allows users to download entire playlists from YouTube as MP3 files. It's a straightforward tool designed for music lovers who want to have their favorite tracks offline.

---

## ✨ Features

- **Batch Download**: Downloads all videos in a specified YouTube playlist.
- **MP3 Conversion**: Converts videos to MP3 format for easy playback.
- **Organized Storage**: Saves downloaded files in a designated folder.

---

## ⚙️ Usage

1. **Install Dependencies**: Make sure you have `pytube` and `pydub` installed.
   ```bash
   pip install pytube pydub
   
## ⚠️ Known Issues

### Regex Recognition Error

YouTube periodically updates its website, which can break the regex patterns used in the script to extract video URLs. This may lead to errors such as:


### Workaround

If you encounter this issue, you may need to modify the `cipher.py` file located in the `pytube` package. Specifically, you may need to adjust regex patterns that match the throttling function. Look for the line that defines the function pattern and ensure it is up-to-date.

**The modification I made this time was to change the lines at 272 and 273 to the following:**
```python
r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&.*?\|\|\s*([a-z]+)',
r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])\([a-z]\)',
