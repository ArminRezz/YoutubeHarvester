import yt_dlp

def download_subtitles(video_url, txt_file):
    ydl_opts = {
        'writesubtitles': True,
        'subtitleslangs': ['en'],
        'skip_download': True,
        'outtmpl': 'subtitles.%(ext)s',
        'writeautomaticsub': True,
        'postprocessors': [{
            'key': 'FFmpegSubtitlesConvertor',
            'format': 'srt',
        }],
        'verbose': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

    # Convert VTT to TXT
    vtt_file = 'subtitles.en.vtt'
    with open(vtt_file, 'r', encoding='utf-8') as vtt, open(txt_file, 'w', encoding='utf-8') as txt:
        for line in vtt:
            if not line.strip().isdigit() and '-->' not in line:
                txt.write(line)

if __name__ == "__main__":
    video_url = 'https://www.youtube.com/watch?v=9miVG2xT5jY&t=4310s'  # Replace with your video URL
    txt_file = 'subtitles.txt'

    download_subtitles(video_url, txt_file)

    print(f"Subtitles have been saved to {txt_file}")