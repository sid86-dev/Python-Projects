from moviepy.editor import*

mp4_file = 'Steam_Trim.mp4'

mp3_file = 'steam - 2010 prod(Two o Ten prod).mp3'


videoClip = VideoFileClip(mp4_file)

audioclip = videoClip.audio

audioclip.write_audiofile(mp3_file)

audioclip.close()

videoClip.close()