# encoding: utf8
from __future__ import unicode_literals
import os

os.system( "ffmpeg -r 10 -i graph/%03d.png -y -vcodec libx264 -pix_fmt yuv420p graph.mp4" )
