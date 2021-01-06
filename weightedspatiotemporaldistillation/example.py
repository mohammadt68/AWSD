import glob
import cv2
from weightedspatiotemporaldistillation import get_awsd


def main():
    frames = glob.glob('./example_frames/*.jpg')
    frames = [cv2.imread(f) for f in frames]

    out_image = get_awsd(frames, normalized=True)
    cv2.imshow('', out_image)
    cv2.waitKey()


if __name__ == '__main__':
    main()
