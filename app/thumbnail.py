from ffmpeg import FFmpeg


def generate_thumbnail(video_filename):
    thumbnail_filename = "/tmp/thumbnail.jpg"

    ffmpeg = (
        FFmpeg()
        .option('y')
        .input(video_filename, {
            "ss": "5"
        })
        .output(
            thumbnail_filename,
            {
                "filter:v": "scale=1280:-1",
                "frames:v": "1",
            },
        )
    )
    ffmpeg.execute()

    return thumbnail_filename
