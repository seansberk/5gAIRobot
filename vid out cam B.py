from picamera import PiCamera
from time import sleep

camera = PiCamera()
# Step 5: Adjustments for camera quality

# Step 1: Preview Camera for 5 seconds before shut off
camera.start_preview()
# Step 4: Record a 5 second Video
camera.start_recording('/home/pi/Documents/Camera Testing/videoB.h264')
sleep(300)
camera.stop_recording()

camera.stop_preview()

