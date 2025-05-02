# -*- coding: utf-8 -*-
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi

def get_youtube_transcript(video_url):
    try:
        # 获取视频ID
        yt = YouTube(video_url)
        video_id = yt.video_id
        
        # 获取字幕
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['zh', 'en'])
        
        # 合并所有文本
        full_text = " ".join([item['text'] for item in transcript])
        
        return full_text
        
    except Exception as e:
        print(u"发生错误: {}".format(e))
        return None

if __name__ == "__main__":
    video_url = input(u"请输入YouTube视频URL: ")
    transcript = get_youtube_transcript(video_url)
    
    if transcript:
        print(u"\n视频文字内容:")
        print(transcript)

        # 新增：保存到txt文件
        with open("youtube_transcript.txt", "w", encoding="utf-8") as f:
            f.write(transcript)
        print(u"\n字幕已保存到 youtube_transcript.txt 文件")
    else:
        print(u"无法获取视频字幕")