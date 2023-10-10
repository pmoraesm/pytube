from pytube import Playlist
import ffmpeg


def get_video(video):
    try:
        v = video.streams.filter(res="1080p").first().download(filename_prefix='v')
    except Exception:
        print(Exception)
    else:
        return v

def get_audio(video):
    try:
        a = video.streams.filter(only_audio=True).first().download(filename_prefix='a')
    except Exception:
        print(Exception)
    else:
        return a

def merge (video_file, audio_file, outpath):
    try:
        video_stream = ffmpeg.input(video_file)
        audio_stream = ffmpeg.input(audio_file)
        ffmpeg.output(audio_stream, video_stream, outpath).run()
    except Exception:
        print(Exception)



def main():
    p = Playlist('https://www.youtube.com/playlist?list=PLPiVB8DFbmLZMQmqyIj2dkQoE1zEP42M1')

    episode = 0
    for video in p.videos:
        episode += 1
        video_path = get_video(video)
        audio_path = get_audio(video)
        print(f'Merging {video_path} and {audio_path}')
        merge(video_file=video_path, audio_file=audio_path, outpath=f'/Users/paulo/Movies/s02e{episode:02d}.mp4')


if __name__ == '__main__':
    main()
