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

def tile_videos( files, tile_width, tile_height, tile_size, outfile, duration=None ):
    num_viodes = len(files)

    com = "ffmpeg "

    # 入力ファイル設定
    for f in files:
        com += " -i " + f

    # フィルタ開始
    com += ' -filter_complex "'

    # サイズを縮小
    for i in range(num_viodes):
        if duration==None:
            com += f" [{i}:v] setpts=PTS-STARTPTS, scale={tile_width}x{tile_height} [{i}v2];"
        else:
            ratio = duration/get_video_len(files[i])
            com += f" [{i}:v] setpts=PTS*{ratio}, scale={tile_width}x{tile_height} [{i}v2];"


    # 配置(4*3)を決定
    com += "".join( [ f"[{i}v2]" for i in range(num_viodes)] )
    com += f"xstack=inputs={num_viodes}:layout="

    n = 0
    posisions = []
    for i in range(tile_size[0]):
        for j in range(tile_size[1]):
            x = j*tile_width
            y = i*tile_height
            posisions.append( f"{x}_{y}" )

            n += 1
            if n==num_viodes:
                break

        if n==num_viodes:
            break
    com += "|".join( posisions )

    # フィルタ終了
    com += '" '

    # 出力先
    com += f" -an {outfile}"

    print(com)
    os.system(com)
    print(com)


files = [
    "clip.mp4", 
    "graph.mp4",
    "overlay1.mp4", 
    "stack.mp4",
    "video.mp4", 
]
# 各動画100*100にして，縦3枚，横2枚配置
tile_videos( files, 100, 100, (3, 2), "tile.mp4" )

# 各動画100*100にして，縦3枚，横2枚配置，全ての動画の長さを10秒にする
#tile_videos( files, 100, 100, (3, 2), "tile.mp4", 10 )