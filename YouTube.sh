ffmpeg -f v4l2 -input_format mjpeg -s 1080x720 -framerate 25 -i /dev/video0 -stream_loop -1 -i /home/pi/audio1.mp3 -vcodec libx264 -g 60 -preset veryfast -f flv rtmp://a.rtmp.youtube.com/live2/SECRET-KEY-HERE
