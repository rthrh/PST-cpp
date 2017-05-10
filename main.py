import cv2
import numpy as np
from pst import *
import time
from matplotlib import pyplot as plt
    
    
def calc_stuff(shape):
    L = 0.5

    x = np.linspace(-L, L, shape[1])
    y = np.linspace(-L, L, shape[0])

    X, Y = np.meshgrid(x, y) #meshgrid

    THETA, RHO = np.arctan2(Y, X), np.hypot(X, Y)

    X_step = x[1]-x[0]
    Y_step = y[1]-y[0]

    fx = np.linspace(-L/X_step, L/X_step, len(x))
    fy = np.linspace(-L/Y_step, L/Y_step, len(y))

    fx_step = fx[1]-fx[0]
    fy_step = fy[1]-fy[0]

    FX, FY = np.meshgrid(fx_step, fy_step)

    FTHETA, FRHO = np.arctan2(FY, FX), np.hypot(FX, FY) #meshgrid
    
    return [THETA,RHO,FTHETA,FRHO]
    
    
    
    
if __name__ == "__main__":
    feed = cv2.VideoCapture(0) 
    frameNum = 0
    num_frames = 120
    kernel = np.ones((3,3),np.uint8)
    
    while True:
        # Start time
        start = time.time()
    
        frameNum += 1
        
        original_image = feed.read()[1]
        # current_frame = cv2.imread('lena.png')
        
        current_frame = original_image
        current_frame = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)
        
        # Phase Stretch Transform
        # COEFFS = calc_stuff(current_frame.shape[:])
        COEFFS = []
        frameNum = 1
        pst_frame = pst(current_frame, frameNum, COEFFS, lpf=0.5, phase_strength=0.9, warp_strength=0.9, thresh_min=-0.6, thresh_max=0.9, morph_flag=False)
        
        #morphological filter
        im_dil = cv2.dilate(current_frame, kernel, iterations=1)
        im_ero = cv2.erode(current_frame, kernel, iterations=1)
        morph_frame = im_dil - im_ero
        
        #Diff: PST - morph_filter
        # diff = morph_frame.astype(float) - pst_frame
        diff = cv2.absdiff(np.float32(morph_frame), np.float32(pst_frame))
        
        # End time
        end = time.time()
        # Time elapsed
        seconds = end - start
        print ("Time taken : {0} seconds".format(seconds))
        # Calculate frames per second
        fps  = 1 / seconds;
        print ("Estimated frames per second : {0}".format(fps))

        
        # print (pst_frame.dtype)
        # print (morph_frame.dtype)
        # break
        #display
        # cv2.imshow('original_image', original_image)
        cv2.imshow('morph_frame', morph_frame)
        cv2.imshow('pst_frame', pst_frame)
        cv2.imshow('diff', diff)
        
        
        
        
        # plt.subplot(231),plt.imshow(original_image,'gray'),plt.title('ORIGINAL')
        # plt.subplot(232),plt.imshow(current_frame,'gray'),plt.title('current_frame')
        # plt.subplot(233),plt.imshow(im_dil,'gray'),plt.title('im_dil')
        # plt.subplot(234),plt.imshow(im_ero,'gray'),plt.title('im_ero')
        # plt.subplot(235),plt.imshow(morph_frame,'gray'),plt.title('morph_frame')
        # plt.subplot(236),plt.imshow(pst_frame,'gray'),plt.title('pst_frame')
        
        # plt.show()
        
        
        # keyboard control
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
        elif cv2.waitKey(1) & 0xFF == ord('r'):
            feed = cv2.VideoCapture(0) 
            frameNum = 0