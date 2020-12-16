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


# 動画の長さと幅・高さを変換
def conv_len_and_width( input_vid, out_vid, out_width, out_height, out_len ):
    in_len = get_video_len(input_vid)
    ratio = out_len/in_len
    print(in_len, ratio)
    os.system("ffmpeg -i %s -y -vf setpts=PTS*%lf,scale=%d:%d %s" % (input_vid, ratio, out_height, out_width, out_vid))
    
def stack( input_vid1, input_vid2, axis, out_vid ):
    if axis==0:
        axis_str = "vstack"
    elif axis==1:
        axis_str = "hstack"
    
    os.system('ffmpeg -i %s -i %s -y -filter_complex "%s" %s' % (input_vid1, input_vid2, axis_str, out_vid) )
 

input_video1 = "video.mp4" 
input_video2 = "graph.mp4" 
output_video = "stack.mp4"
output_duration = 30

# 縦に結合する場合
output_width = 700
output_height = -1

# 横に結合する場合
#output_width = -1
#output_height = 350


# 2つの動画の幅（または高さ）と長さを合わせる
conv_len_and_width( input_video1, "tmp1.mp4", output_height, output_width, output_duration )
conv_len_and_width( input_video2, "tmp2.mp4", output_height, output_width, output_duration )

# 縦に結合する場合
stack( "tmp1.mp4", "tmp2.mp4", 0, output_video )

# 横に結合する場合
#stack( "tmp1.mp4", "tmp2.mp4", 1, output_video )