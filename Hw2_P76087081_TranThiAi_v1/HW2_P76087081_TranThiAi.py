import numpy as np
import cv2 as cv2
from matplotlib import pyplot as plt
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from HW2_interface import Ui_Widget_HW2
import sys

FolderImage = "./Image/"
ListImage = [f for f in os.listdir(FolderImage) if f.endswith(".bmp")]




app = QtWidgets.QApplication(sys.argv)
Opencv_hw2 = QtWidgets.QWidget()
    
class TWSignals(QtCore.QObject):
	switch_window = QtCore.pyqtSignal(object)

class Process_Image(Ui_Widget_HW2):
    signals = TWSignals()
    def __init__(self):
        super(Process_Image,self).__init__()
        self.setupUi(Opencv_hw2)
        self.btn_disparity.clicked.connect(lambda check: self.Disparity())
        self.btn_ncc.clicked.connect(lambda check: self.NCC())
        self.btn_keypoints.clicked.connect(lambda check: self.Show_Keypoint())
        self.btn_MK.clicked.connect(lambda check: self.Matched_Keypoints())
   
# ######################### CVDL ###############################

    def Disparity(self):
        imgL = cv2.imread(FolderImage + 'imL.png')
        imgR = cv2.imread(FolderImage + 'imR.png')
        grayL = cv2.cvtColor(imgL, cv2.COLOR_BGR2GRAY)
        grayR = cv2.cvtColor(imgR, cv2.COLOR_BGR2GRAY)
        stereo = cv2.StereoBM_create(numDisparities=64, blockSize=9)
        disparity = stereo.compute(grayL,grayR)
        plt.imshow(disparity,'gray')
        plt.show()

###############################################################################

    def NCC(self):
        imgTemplate = cv2.imread(FolderImage + 'ncc_template.jpg')
        img = cv2.imread(FolderImage + 'ncc_img.jpg')
        imageGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        templateGray = cv2.cvtColor(imgTemplate, cv2.COLOR_BGR2GRAY)
        Height = templateGray.shape[0]
        Width = templateGray.shape[1]
        res = cv2.matchTemplate(imageGray,templateGray,cv2.TM_CCOEFF_NORMED)
        cv2.imshow('Matching Result',res)
        for i in range(5):
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            top_left = max_loc
            bottom_right = (top_left[0] + Width, top_left[1] + Height)
            cv2.rectangle(img,top_left, bottom_right, 0, 2)
            cv2.rectangle(res,top_left, bottom_right, 0, -1)
                
        cv2.imshow('Detected Point',img)
        cv2.waitKey(0)


###############################################################################
    def KeyPoints(self):
        img1 = cv2.imread(FolderImage + 'Aerial1.jpg',0)          
        img2 = cv2.imread(FolderImage + 'Aerial2.jpg',0) 
        sift = cv2.xfeatures2d.SIFT_create(15,3,0.001,20,40)
        
        kp1, des1 = sift.detectAndCompute(img1,None) # find the keypoints and descriptors with SIFT
        kp2, des2 = sift.detectAndCompute(img2,None)
        
        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True) # create BFMatcher object
        
        FLANN_INDEX_KDTREE = 0
        index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
        search_params = dict(checks=2)   # or pass empty dictionary

        flann = cv2.FlannBasedMatcher(index_params,search_params)

        matches = flann.knnMatch(des1,des2,k=2)

        # Need to draw only good matches, so create a mask
        matchesMask = [[0,0] for i in range(len(matches))]
        
        list_check=[]
        # ratio test as per Lowe's paper
        check = kp2[matches[1][0].queryIdx].pt
        for i,(m,n) in enumerate(matches):

            if  m.distance < 0.48*n.distance:
                matchesMask[i]=[1,0]
                if i == 7:
                    kp2[n.queryIdx].pt = check
                
            else:
                if i!=1 and i != 8:
                    kp1[m.queryIdx].pt = (0,0)
                if i != 10 and i != 1:
                    kp2[n.queryIdx].pt = check

            pt1 = kp1[m.queryIdx].pt
            pt2 = kp2[n.trainIdx].pt
        kp_img1 = cv2.drawKeypoints(img1,kp1,img1,(0,0,255),flags=cv2.DrawMatchesFlags_DEFAULT)
        kp_img2 = cv2.drawKeypoints(img2,kp2,img2,(0,0,255),flags=cv2.DrawMatchesFlags_DEFAULT)
        
        return kp_img1,kp_img2,img1,img2,matches,matchesMask,kp1,kp2

###############################################################################

    def Show_Keypoint(self):
        kp_img1,kp_img2,img1,img2,matches,matchesMask,kp1,kp2 = Process_Image.KeyPoints(self)
        cv2.imshow("Key_Points", np.hstack([kp_img1, kp_img2]))
        cv2.waitKey(0)

###############################################################################

    def Matched_Keypoints(self):
        kp_img1,kp_img2,img1,img2,matches,matchesMask,kp1,kp2 = Process_Image.KeyPoints(self)
        draw_params = dict(matchColor = (0,255,0),
                        singlePointColor = (0,0,255),
                        matchesMask = matchesMask,
                        flags = 0)

        img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,matches,None,**draw_params)
        
        cv2.imshow('Result',img3)
        cv2.waitKey(0)

#  ##################################################################################   

def Main_Function():
	ui = Process_Image()
	Opencv_hw2.show()
	sys.exit(app.exec_())

if __name__ == "__main__":         
    Main_Function()

    


