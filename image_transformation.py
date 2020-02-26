import cv2
import numpy


def rotate_image(img_path: str, orientation: dict) -> numpy.ndarray:
    img = cv2.imread(img_path, 0)
    rows, cols = img.shape

    roll = orientation.get("roll")

    rot_matrix = cv2.getRotationMatrix2D((cols/2, rows/2), roll, 1)
    dst = cv2.warpAffine(img, rot_matrix, (cols, rows))

    # Uncomment this for testing
    # cv2.imshow('img', dst)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return dst


if __name__ == "__main__":
    test_data = {
        "pitch": 0,
        "yaw": 0,
        "roll": 330
    }

    new_img = rotate_image('./images/img_downscale_30.jpg', test_data)
