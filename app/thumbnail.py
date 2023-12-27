import requests
import ffmpeg
import sys


def generate_thumbnail(video_filename):
    thumbnail_filename = "/tmp/thumbnail.jpg"
    probe = ffmpeg.probe(video_filename)
    time = float(probe['streams'][0]['duration']) // 2
    width = probe['streams'][0]['width']

    ffmpeg.input(video_filename, ss=time).filter('scale', width, -1).output(thumbnail_filename,
                                                                            vframes=1).overwrite_output().run(capture_stdout=True, capture_stderr=True)

    return thumbnail_filename
