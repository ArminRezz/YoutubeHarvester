import re

# GET SUBTIUTLES OF YOUTUBE VIDEO WITH this command --->
# yt-dlp --write-auto-sub --skip-download --sub-lang en --output "%(title)s.%(ext)s" "https://www.youtube.com/watch?v=BaW_jenozKc"

def convert_vtt_to_essay(vtt_file_path, output_file_path):
    with open(vtt_file_path, 'r', encoding='utf-8') as vtt_file:
        lines = vtt_file.readlines()

    essay_lines = []
    for line in lines:
        # Remove timestamps
        line = re.sub(r'^\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}', '', line)
        # Remove alignment and position information
        line = re.sub(r'align:start position:\d+%', '', line)
        # Remove HTML-like tags
        line = re.sub(r'<[^>]+>', '', line)
        # Strip leading/trailing whitespace
        line = line.strip()

        if line:  # Only add non-empty lines
            essay_lines.append(line)

    # Join the lines into a single essay format with each line on a new line
    essay = '\n'.join(essay_lines)  # {{ edit_1 }}

    # Remove duplicates from the essay
    unique_lines = []  # {{ edit_2 }}
    seen_lines = set()  # {{ edit_3 }}

    for line in essay.splitlines():  # {{ edit_4 }}
        if line and line not in seen_lines:  # Only add non-empty and unique lines
            unique_lines.append(line)
            seen_lines.add(line)  # {{ edit_5 }}

    # Write the unique lines to the output file
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write('\n'.join(unique_lines))  # {{ edit_6 }}

# Example usage
vtt_file_path = '/home/arminrez/YoutubeMusicScript/subtitles.en.vtt'  # Replace with your .vtt file path
output_file_path = 'subtitles1.txt'  # Updated to reflect unique output
convert_vtt_to_essay(vtt_file_path, output_file_path)