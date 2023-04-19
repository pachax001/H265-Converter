import os
import glob
import subprocess

def convert_mkv_to_h265():
    for file in glob.glob('*.mkv'):
        
        if 'x265' in file or 'X265' in file or 'HEVC' in file or 'hevc' in file:
            continue
        if 'HDTV.x264' in file:
            new_file = file.replace('HDTV.x264', 'HDTV.x265')
        elif 'x264' in file or 'h264' in file or 'X264' in file or 'H264' in file or 'hdtv' in file or 'Hdtv' in file or 'HDTV' in file or 'hdt' in file:
            new_file = file.replace('x264', 'x265').replace('h264', 'x265').replace('X264', 'x265').replace('H264', 'x265').replace('hdtv', 'HDTV.x265').replace('Hdtv', 'HDTV.x265').replace('HDTV', 'HDTV.x265').replace('hdt', 'HDTV.x265')
        else:
            if any(x in file for x in ['H264', 'h264', 'X264', 'x264', 'HEVC', 'hevc', 'X265', 'x265', 'HDTV', 'hdtv', 'Hdtv', 'Hdt']):
                new_file = os.path.splitext(file)[0] + '.mkv'
            else:
                new_file = os.path.splitext(file)[0] + '.x265.mkv'
        subprocess.run(['ffmpeg', '-i', file, '-c:v', 'libx265', '-preset', 'ultrafast', '-c:a', 'copy', new_file])
        srt_file = os.path.splitext(file)[0] + '.srt'
        if os.path.exists(srt_file):
            new_srt_file = os.path.splitext(new_file)[0] + '.srt'
            os.rename(srt_file, new_srt_file)
        os.remove(file)

def convert_mp4_to_h265():
    for file in glob.glob('*.mp4'):
        
        if 'x265' in file or 'X265' in file or 'HEVC' in file or 'hevc' in file:
            continue
        if 'HDTV.x264' in file:
            new_file = file.replace('HDTV.x264', 'HDTV.x265')
        elif 'x264' in file or 'h264' in file or 'X264' in file or 'H264' in file:
            new_file = file.replace('x264', 'x265').replace('h264', 'x265').replace('X264', 'x265').replace('H264', 'x265').replace('hdtv', 'HDTV.x265').replace('Hdtv', 'HDTV.x265').replace('HDTV', 'HDTV.x265').replace('hdt', 'HDTV.x265')
        else:
            if any(x in file for x in ['H264', 'h264', 'X264', 'x264', 'HEVC', 'hevc', 'X265', 'x265', 'HDTV', 'hdtv', 'Hdtv', 'Hdt']):
                new_file = os.path.splitext(file)[0] + '.mkv'
            else:
                new_file = os.path.splitext(file)[0] + '.x265.mkv'
        subprocess.run(['ffmpeg', '-i', file, '-c:v', 'libx265', 'preset', 'ultrafast', '-c:a', 'copy', new_file])
        srt_file = os.path.splitext(file)[0] + '.srt'
        if os.path.exists(srt_file):
            new_srt_file = os.path.splitext(new_file)[0] + '.srt'
            os.rename(srt_file, new_srt_file)
        os.remove(file)

choice = input('Enter your choice (1.Convert mkv to h265 mkv, 2.Convert mp4 to h265 mkv): ')
if choice == '1':
    convert_mkv_to_h265()
elif choice == '2':
    convert_mp4_to_h265()
else:
    print('Invalid choice!')
