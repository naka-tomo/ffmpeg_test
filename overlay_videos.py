#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

def overlay_videos( out_name, main_video,  w, h, x, y, overlayed_video1, overlayed_video2=None ):
    com = f'ffmpeg -i {main_video} -i {overlayed_video1} '

    if overlayed_video2!=None:
        com += f'-i {overlayed_video2}'
    
    com += ' -filter_complex "'
    com += f'[1:v]scale={w}:{h}[small1],'
    com += f'[0:v][small1]overlay=x={x}:y={y}[out1], '
    com += f'[out1]drawbox={x}:{y}:{w}:{h}:black:8'

    if overlayed_video2!=None:
        com += '[out2],'
        com += f'[2:v]scale={w}:{h}[small2], '
        com += f'[out2][small2]overlay=x={x}:y={y+h}[out3], '
        com += f'[out3]drawbox={x}:{y+h}:{w}:{h}:black:8'

    com += f'" -preset ultrafast ' + out_name

    os.system(com)

# グラフを重ねる
overlay_videos( "overlay1.mp4" , "video.mp4", 400, 80, 0 , 0, "graph.mp4" )

# グラフを２つ重ねる
#overlay_videos( "overlay2.mp4" , "video.mp4", 400, 80, 0 , 0, "graph.mp4", "graph.mp4" )