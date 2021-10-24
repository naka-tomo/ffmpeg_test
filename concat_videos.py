#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os


def concat_videos( video_files, out_name ):
    with open("list.txt", "w") as fw:
        for f in video_files:
            fw.write( "file " + f + "\n" )
        
    com = "ffmpeg -f concat -i list.txt -c copy %s" % (out_name)
    os.system( com )


concat_videos( ["video.mp4", "video.mp4", "video.mp4"], "concat.mp4" )