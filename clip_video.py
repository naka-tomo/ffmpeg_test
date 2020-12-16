# encoding: utf8
from __future__ import unicode_literals
import os

def clip_video( src, dst, start, duration ):
    os.system( "ffmpeg -i %s -t %d -ss %d -y %s" % (src, duration, start, dst) )

def main():
    # video.mp4の5秒から10秒間をclip.mp4に保存
    clip_video( "video.mp4" , "clip.mp4", 5, 10 )


if __name__ == '__main__':
    main()