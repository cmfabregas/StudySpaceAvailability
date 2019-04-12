##takes picture
from picamera import PiCamera
import time
import io

class TakeImage:

    def __init__(self,camera):
        camera.resolution = (1600,1200)
        camera.start_preview()
        time.sleep(10)
        camera.capture('example.jpg')
        camera.stop_preview()
