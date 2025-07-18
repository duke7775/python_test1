#说明：爬虫下载YouTube视频
import yt_dlp

def download_youtube_video(url, output_path='.'):
    """
    下载YouTube视频。

    Args:
        url (str): 视频的URL。
        output_path (str, optional):  下载视频保存的路径。默认为当前目录。
    """
    ydl_opts = {
        'outtmpl': f'{output_path}/%(title)s-%(id)s.%(ext)s',  # 下载的视频文件名格式
        'noplaylist': True,  # 不下载播放列表
        'quiet': True,  # 禁止输出详细信息
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"视频已成功下载到 {output_path}")
    except Exception as e:
        print(f"下载失败: {e}")

def main():
    video_url = input("请输入YouTube视频的URL: ")
    download_path = input("请输入下载保存的目录（默认为当前目录）: ")
    if not download_path:
        download_path = "."

    download_youtube_video(video_url, download_path)

if __name__ == "__main__":
    main()    
