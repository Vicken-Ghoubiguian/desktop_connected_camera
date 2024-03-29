# desktop_connected_camera

## Contents

1. [Introduction](#introduction)
2. [Presentation](#presentation)
3. [Project's structure](#project_s_structure)
4. [How was this project developed ?](#how_was_this_project_developed)
5. [How does this project work ?](#how_does_this_project_work)
6. [How to use it ?](#how_to_use_it)
7. [A few examples](#a_few_examples)
8. [Useful links](#useful_links)
9. [Conclusion](#conclusion)

<a name="introduction"></a>
## Introduction

<a name="presentation"></a>
## Presentation

This project is a fork of the [connected camera project](https://github.com/Vicken-Ghoubiguian/connected_camera)'s developed-in-Python software core.

<a name="project_s_structure"></a>
## Project's structure

<a name="how_was_this_project_developed"></a>
## How was this project developed ?

<a name="how_does_this_project_work"></a>
## How does this project work ?

<a name="how_to_use_it"></a>
## How to use it ?

<a name="a_few_examples"></a>
## A few examples

<a name="useful_links"></a>
## Useful links

<a name="conclusion"></a>
## Conclusion

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
