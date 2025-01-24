from moviepy.video.io.VideoFileClip import VideoFileClip

# 输入视频文件路径
input_video_path = "./static/videos/courtyard_random.mp4"
# 输出视频文件路径
output_video_path = "./static/videos/courtyard_random_cut.mp4"

# 加载视频
video = VideoFileClip(input_video_path)

# 裁剪视频，从3秒到7秒
cropped_video = video.subclip(1.37, 15.15)

# 写入输出文件
cropped_video.write_videofile(output_video_path, codec="libx264")