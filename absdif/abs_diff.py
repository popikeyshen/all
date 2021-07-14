import cv2
import numpy as np

def get_img_diff_index(img1, img2):
    """
   Returns difference index of two images, values closer to 0 means that they are more similar
   :param np.ndarray img1:
   :param np.ndarray img2:
   :return float:

   """
    # size = 832
    # im1 = cv2.resize(img1.copy(), (size, size))
    # im2 = cv2.resize(img2.copy(), (size, size))
    #cv2.imshow('image1', img1)
    #cv2.imshow('image2', img2)
    fr_sub = cv2.subtract(img1, img2)
    fr_diff = cv2.absdiff(img1, img2)



    diff = fr_diff*(fr_diff>30)

    cv2.imshow('fr_sub', fr_sub)
    cv2.imshow('fr_diff', fr_diff)
    cv2.imshow('diff', diff)
    cv2.waitKey(0)
    cv2_mean = cv2.mean(fr_diff)
    return diff #fr_diff  # cv2_mean[0] + cv2_mean[1] + cv2_mean[2]



im1 = cv2.imread("cat.jpg")
im2 = cv2.imread("cat2.jpg")

get_img_diff_index(im1, im2)
