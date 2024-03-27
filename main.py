from pytube import YouTube

youtube_video_url = "https://www.youtube.com/watch?v=h3bTwCqX4ns&list=PL4-IK0AVhVjNDRHoXGort7sDWcna8cGPA"

yt = YouTube(youtube_video_url)

stream = yt.streams.get_highest_resolution()

stream.download("myVideo")

