"""Provides Image Manipulation Module

Functions provided in this module alter the input images
to then pass to object detection algorithms
"""
# ================ Built-in Imports ================

from sys import stderr

# ================ Third Party Imports ================

from numpy import ndarray
from cv2 import imread, getRotationMatrix2D, warpAffine

# ================ Authorship ================

__author__ = "Gregory Sanchez"


def rotate_image(img_path: str, orientation: dict) -> ndarray:
    """Rotate Image

    @param: img_path (str): path to the image to rotate
    @param: orientation (dict): orientation data of the vessel

    @return: numpy array with the (un)altered image
    """
    img = imread(img_path, 0)
    rows, cols = img.shape

    try:
        roll = orientation["roll"]
        rot_matrix = getRotationMatrix2D((cols/2, rows/2), roll, 1)
        dst = warpAffine(img, rot_matrix, (cols, rows))
    except KeyError as err:
        print("Key Error: unknown key {0}".format(err), file=stderr)
        dst = img

    return dst


if __name__ == "__main__":
    from cv2 import imshow, waitKey, destroyAllWindows

    test_data = {
        "pitch": 0,
        "yaw": 0,
        "roll": 330
    }

    new_img = rotate_image('./images/img_downscale_30.jpg', test_data)

    imshow('img', new_img)
    waitKey(0)
    destroyAllWindows()
