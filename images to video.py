import ffmpeg

(
    ffmpeg
        .input('C:\\Users\\Work\\PycharmProjects\\ms-reading\\img\\spec_sequence\\*.png', framerate=30)
        .output('C:\\Users\\Work\\PycharmProjects\\ms-reading\\img\\video.mp4')
        .run()
)
