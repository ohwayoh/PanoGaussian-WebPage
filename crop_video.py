from moviepy.editor import VideoFileClip, vfx

# 输入视频文件路径
input_video_path = "./static/videos/Classroom_random.mp4"
# 输出视频文件路径
output_video_path = "./static/videos/Classroom_random_cut.mp4"

# 加载视频
video = VideoFileClip(input_video_path)

# 获取视频的分辨率
width, height = video.size
print(f"视频分辨率: {width}x{height}")

# 裁剪视频，指定裁剪区域 (x1, y1, x2, y2)
# 例如，裁剪左上角(100, 50)到右下角(400, 300)
cropped_video = video.fx(vfx.crop, x1=4, y1=0, x2=width-4, y2=height)

print(cropped_video.size)

# 写入输出文件
cropped_video.write_videofile(output_video_path, codec="libx264")