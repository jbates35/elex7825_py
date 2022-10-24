import numpy as np
import cv2, PIL, os
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd

class Camera:
    
    def __init__(self, cam=0, size_square = 0.06, size_mark = 0.03, filename=".\cam_param.txt", size=np.zeros((1000,600), dtype = "uint8")):
        # Camera selection on computer
        self.cam = cam
        self.video_capture = cv2.VideoCapture(cam)
        
        # Initial cv mat
        self.size = size 
        
        #measurements for grids and checkers
        self.size_square = size_square
        self.size_mark = size_mark
        
    def calculate_extrinsic(self):
        pass
    
    def calculate_intrinsic(self):
        pass
    
    def save_cam_param(self, filename, cam, dist):
        pass
    
    def load_cam_param(self, filename, cam, dist):
        pass
    
    def create_charuco(self):
        aruco_dict = cv2.
    
    def calibrate_charuco(self):
        pass
    
    def detect_charuco(self):
        pass    
    
    def transform_to_image(self, mat, pt):
        pass
    
    def update_settings(self, im):
        pass
    
    
        

if __name__ == "__main__":
    _virtualcam = Camera(cam=0)
    