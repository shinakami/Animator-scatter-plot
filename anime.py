import cv2
import imageio
import numpy as np
import matplotlib.pyplot as plt
import os
from time import sleep
from tqdm import tqdm

os.system('cls')
def get_images_from_video(video_name, time_F):
    video_images = []
    vc = cv2.VideoCapture(video_name)
    c = 1
    
    if vc.isOpened(): 
        rval, video_frame = vc.read()
    else:
        rval = False

    while rval:   
        rval, video_frame = vc.read()
        
        if(c % time_F == 0): 
            video_images.append(video_frame)     
        c = c + 1
    vc.release()
    
    return video_images

time_F = 1
video_name = 'super idol.mp4' 
video_images = get_images_from_video(video_name, time_F) 
print("Start")



img_gif = []
video_L = int(len(video_images))
print(video_L)
with tqdm(total=video_L) as pbar: 
    for i in range(video_L):
        
        img_gif.append('')
        width = int(video_images[i].shape[1] * 0.35)
        height = int(video_images[i].shape[0] * 0.35)
        img_re = cv2.resize(video_images[i], (width, height), interpolation=cv2.INTER_CUBIC)
        img_re = img_re[:, :, [2, 1, 0]]
        fig = plt.figure(figsize=(10, 8))
        plt.title('Python super idol', fontsize=20)
        plt.xlim(0, width)
        plt.ylim(height, 0)
        plt.xlabel('X')
        plt.ylabel('Y')
        for j in range(height):
            for k in range(width):

                plt.scatter(k, j, s=5, color=tuple(img_re[j, k, :]/255))
                

        plt.savefig('superidol'+str(i)+'.png', dpi=200)

        img_gif[i] = 'superidol'+str(i)+'.png'
        pbar.update(1)
gif_i = []
for p in img_gif:
    gif_i.append(imageio.imread(p))
imageio.mimsave("superidol.gif", gif_i, duration=0.0001, fps=60)
print("OK!")

