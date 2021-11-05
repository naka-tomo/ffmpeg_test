#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import cv2

# 動画の長さを取得
def get_video_len( name ):
    video = cv2.VideoCapture(name)
    count = video.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = video.get(cv2.CAP_PROP_FPS)
    video.release()
    return count/fps

def stack(input_vid1, input_vid2, axis, height, width, duration, out_vid ):
    if axis==0:
        stack = "vstack"
        size = f"{width}:-1"
    elif axis==1:
        stack = "hstack"
        size = f"-1:{height}"

    ratio1 = duration/get_video_len(input_vid1)
    ratio2 = duration/get_video_len(input_vid2)

    com = f'ffmpeg -i {input_vid1} -i {input_vid2} -filter_complex "'
    com += f"[0:v]setpts=PTS*{ratio1}, scale={size} [v0];"    # resize
    com += f"[1:v]setpts=PTS*{ratio2}, scale={size} [v1];"    # resize
    com += f'[v0][v1]{stack}" {out_vid}'

    print(com)
    os.system( com )



input_video1 = "video.mp4" 
input_video2 = "graph.mp4" 
output_video = "stack.mp4"
output_duration = 30

# 縦に結合する場合
output_width = 320
output_height = -1

# 横に結合する場合
#output_width = -1
#output_height = 350

# 縦に結合
stack( input_video1, input_video2, 0, output_height, output_width, 10, "stack.mp4" )

# 横に結合
#stack( input_video1, input_video2, 1, output_height, output_width, 10, "stack.mp4" )