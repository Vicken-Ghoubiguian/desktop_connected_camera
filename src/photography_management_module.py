import cv2
from pygame import mixer

def shoot_a_photo_function(desired_title, desired_format, desired_frame, desired_audio_file = 'sounds/1_second_long_old_camera_sound.mp3'):

	mixer.init()

	mixer.music.load(desired_audio_file)

	mixer.music.play()

	cv2.imwrite(desired_title + desired_format, desired_frame)
