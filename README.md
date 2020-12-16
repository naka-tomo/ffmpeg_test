# ffmpeg_test
ffmpegを使った動画編集についてよく使う機能をまとめました．

## 動画の一部を切り出し [(code)](clip_video.py)
例：[元動画](https://github.com/naka-tomo/ffmpeg_test/raw/main/video.mp4)から開始時間から指定した長さを切り出した[動画](https://github.com/naka-tomo/ffmpeg_test/raw/main/clip.mp4)を生成

## 連番画像からの動画生成 [(code)](make_graph_video.py)
例：[連番の画像](graph)から[動画](https://github.com/naka-tomo/ffmpeg_test/raw/main/graph.mp4)を生成

## 2つの動画の結合 [(code)](stack_videos.py)
例：[元動画](https://github.com/naka-tomo/ffmpeg_test/raw/main/video.mp4)と[グラフ動画](https://github.com/naka-tomo/ffmpeg_test/raw/main/graph.mp4)を時間を揃えて結合した[動画](https://github.com/naka-tomo/ffmpeg_test/raw/main/stack.mp4)を生成
