# H265-Converter
Simple script to convert mp4 and mkv files to h265 or HEVC.
Install python.
Install ffmpeg (https://ffmpeg.org/) and add it to path.
Features.
If the original filename contains x264,h264 or any word compatible with x264 it will be replaced with x265 after hevc conversion.Also script deletes the original video file from directory.Also the script renames the subtitle file also to the new video filename if available.
The script uses ultrafast preset for encoding.If you need to change the preset or do modifications edit lines 19 and 40 from the script.You can fine more presets and command arguments from https://ffmpeg.org/documentation.html.
