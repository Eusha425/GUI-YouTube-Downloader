from pytube import YouTube
  
def yt_download(link):

    vid_link = link  
    # creating YouTube Object
    youtube_object = YouTube(vid_link)

    # creating stream object
    stream_object = youtube_object.streams

    # highest progressive video quality available
    highest_quality = stream_object.get_highest_resolution()
    highest_quality.download()