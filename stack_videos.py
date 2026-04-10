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
    return count/fps, fps

def stack(input_vid1, input_vid2, axis, height, width, duration, out_vid ):
    if axis==0:
        stack = "vstack"
        size = f"{width}:-2"
    elif axis==1:
        stack = "hstack"
        size = f"-2:{height}"

    len1, fps1 = get_video_len(input_vid1)
    len2, fps2 = get_video_len(input_vid2)
    print(len1, fps1)

    ratio1 = duration/len1
    ratio2 = duration/len2

    sample_fps1 = min(fps1, max(30 * ratio1, 1))
    sample_fps2 = min(fps2, max(30 * ratio2, 1))
    print(sample_fps1, fps1, ratio1)

    com = f'ffmpeg -i {input_vid1} -i {input_vid2} -filter_complex "'
    com += f"[0:v]fps={sample_fps1:.3f}, setpts=PTS*{ratio1}, scale={size}, trim=duration={duration},fps={30} [v0];"    # resize
    com += f"[1:v]fps={sample_fps2:.3f}, setpts=PTS*{ratio2}, scale={size}, trim=duration={duration},fps={30} [v1];"    # resize
    com += f'[v0][v1]{stack}" -c:v libx264 -pix_fmt yuv420p {out_vid}'

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