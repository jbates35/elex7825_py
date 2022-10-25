import numpy as np
import cv2
from cv2 import aruco
import cvui
from math import cos, sin, radians
import argparse
import pickle

#note, some stuff sourced from https://github.com/ddelago/Aruco-Marker-Calibration-and-Pose-Estimation
#if you have questions, they may be answered there

# Classes for more organized functions in the camera class
class Intrinsic:
    def __init__(self, focus=3, pixel=0.0000046, principal=(500,300)):
        self.mat_type = "Intrinsic"

        self.focus = focus
        self.pixel = pixel
        self.principal = principal

        self.__create_matrix()

    def __create_matrix(self):
        mat1 = [
            [1/self.pixel, 0, self.principal[0]],
            [0, 1/self.pixel, self.principal[1]],
            [0, 0, 1]
        ]
        mat2 = [
            [self.focus/1000, 0, 0, 0],
            [0, self.focus/1000, 0, 0],
            [0, 0, 1, 0]
        ]
        self.mat = np.matmul(mat1, mat2)

    def mat(self):
        self.__create_matrix()
        return self.mat


class Extrinsic:
    def __init__(self, roll=0, pitch=0, yaw=0, x=0, y=0, z=0):
        self.mat_type = "Extrinsic"

        self.roll = roll
        self.pitch = pitch
        self.yaw = yaw
        self.x = x
        self.y = y
        self.z = z

        self.__create_mats()

    def __create_mats(self):
        # create rotational mat
        sx = sin(radians(self.roll))
        cx = cos(radians(self.roll))
        sy = sin(radians(self.pitch))
        cy = cos(radians(self.pitch))
        sz = sin(radians(self.yaw))
        cz = cos(radians(self.yaw))

        self.rmat = [
            [cz * cy,   cz * sy * sx - sz * cx,     cz * sy * cx + sz * sx,     0],
            [sz*cy,      sz*sy*sx + cz*cx,           sz*sy*cx-cz*sx,            0],
            [-1 * sy,    cy * sx,                    cy * cx,                   0],
            [0,          0,                          0,                         1]
        ]

        #create translational mat
        self.tmat = [
            [1, 0, 0, self.x],
            [0, 1, 0, self.y],
            [0, 0, 1, self.z],
            [0, 0, 0, 1]
        ]

        #create combined mat
        self.mat = np.matmul(self.tmat, self.rmat)

    def mat(self, mat_type=''):
        self.__create_mats()

        if mat_type=='r':
            return self.rmat
        elif mat_type=='t':
            return self.tmat
        else:
            return self.mat


class Camera:
    
    def __init__(self, cam=0, size_square=0.06, size_mark=0.03, file_name=".\\cam_param.txt"): #, size=np.zeros((1000,600), dtype="uint8")):
        # Camera selection on computer
        self.cam = cam
        #self.video_capture = cv2.VideoCapture(cam)
        
        # Initial cv mat
        #self.size = size

        # File for saving file
        self.file_name = file_name

        #measurements for grids and checkers
        self.size_square = size_square
        self.size_mark = size_mark

        #default ui/cam variables
        self.cam_int_settings = Intrinsic()
        self.cam_ext_settings = Extrinsic(
            roll=0,
            pitch=0,
            yaw=0,
            x=0,
            y=0,
            z=500
        )

    def save_cam_param(self, filename, cam, dist):
        pass
    
    def load_cam_param(self, filename, cam, dist):
        pass
    
    def create_charuco(self):
        # Create ChArUco board, which is a set of Aruco markers in a chessboard setting
        # meant for calibration
        # the following call gets a ChArUco board of tiles 5 wide X 7 tall
        gridboard = aruco.CharucoBoard_create(
            squaresX=6,
            squaresY=8,
            squareLength=self.size_square,
            markerLength=self.size_mark,
            dictionary=aruco.Dictionary_get(aruco.DICT_5X5_50))

        # Create an image from the gridboard
        img = gridboard.draw(outSize=(988, 1400))
        cv2.imwrite("charuco.jpg", img)

        # Display the image to us
        cv2.imshow('Gridboard', img)
        # Exit on any key
        cv2.waitKey(0)
        cv2.destroyAllWindows()

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
    _virtualcam.create_charuco()
    