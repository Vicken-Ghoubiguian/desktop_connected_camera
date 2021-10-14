# desktop_connected_camera

## Contents

1. [Introduction]()
2. [Presentation]()
3. [Project's structure]()
4. [How was this project developed ?]()
5. [How does this project work ?]()
6. [How to use it ?]()
7. [A few examples]()
8. [Useful links]()
9. [Conclusion]()

This project is a fork of the connected camera project's software core.

It's a project specifically for linux distributions:

This piece of software has the following features:

1. can take photos,

1. can shoot videos,

1. can add decorations to take the photo or shoot the video,

1. can modify mode among the following: normal, cartoonized without colors, cartoonized with colors,

1. can share videos or photos on different social networks (Facebook, Twitter, LinkedIn, YouTube and Instagram).

This application can take photos in this format: `'.jpg'`, `'.jpeg'`, `'.jpe'`, `'.jp2'`, `'.png'`, `'.tiff'`, `'.tif'`, `'.bmp'`, `'.dib'`, `'.pbm'`, `'.pgm'`, `'.ppm'`.

This application can record videos in this format: `'.avi'`, `'.mp4'`.

To use this application, follow this steps:

1. go to the desktop_connected_camera from where you clone this repository, by using this command: cd desktop_connected_camera,

1. inside the desktop_connected_camera, run the main.py script using this following command:

`python3 main.py -output_video_name desired_video_name -output_video_format desired_video_format -photo_name desired_photo_name -photo_format desired_photo_format`

Default values for these parameters are:

1. `-output_video_name`: Store the video name informed by the user
  default value: `outputVideo`,

2. `-output_video_format`: Store the video name informed by the user
  default value: `'.avi'`

3. `-photo_name`: Store the photo name informed by the user
  default value: `'monImg'`,

4. `-photo_format`: Store the photo format informed by the user
  default value: `'.jpg'`.

__Warning:__ This application launchs only on python3.
