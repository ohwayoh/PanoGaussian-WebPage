from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.fx.all import speedx

# 输入视频文件路径
input_video_path = "./static/videos/courtyard_random_cut.mp4"
# 输出视频文件路径
output_video_path = "./static/videos/courtyard_random_cut2.mp4"

# 加载视频
video = VideoFileClip(input_video_path)

# 计算加速倍数
speed_factor = 10 / 8  # 原始时长10秒，加速至8秒

# 加速视频
accelerated_video = video.fx(speedx, speed_factor)

# 写入输出文件
accelerated_video.write_videofile(output_video_path, codec="libx264")