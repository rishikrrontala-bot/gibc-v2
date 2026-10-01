#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
ffmpeg -hide_banner -loglevel warning -y -i /tmp/withheld-screen.mp4 -i submission/video/narration.wav -vf "drawbox=x=0:y=ih-108:w=iw:h=108:color=0x30212d@0.96:t=fill,subtitles=submission/video/captions.srt:force_style='FontName=DejaVu Sans,FontSize=8,PrimaryColour=&H00EBEFF4,Outline=0,Shadow=0,MarginV=6,MarginL=20,MarginR=20'" -map 0:v:0 -map 1:a:0 -c:v libx264 -preset fast -crf 26 -af loudnorm=I=-16:TP=-1.5:LRA=11 -c:a aac -b:a 128k -shortest -movflags +faststart submission/video/demo.mp4
ffprobe -v error -show_entries format=duration,size -show_entries stream=codec_name,width,height -of json submission/video/demo.mp4
