import cv2
import pytesseract
import argparse
import sys
import glob
import os
import time

def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('-img', '--image', required=False, type=str, help="The image to run tesseract OCR on")
    parser.add_argument('-imgs', '--folder', required=False, type=str, help="The folder to look for images to run pytesseract OCR on")
    args = parser.parse_args()
    if args.image is None and args.folder is None:
        parser.print_help()
        sys.exit(0)
    return args

def main():
    args = getArgs()
    if args.image:
        # Perform OCR on the given image
        readImgAndDoOCR(args.image)
    else:
        # Read all file paths in folder
        images = glob.glob(os.path.join(args.folder, '*.jpeg'))

        # Perform OCR on all the images
        for path in images:
            readImgAndDoOCR(path)

def readImgAndDoOCR(path):
    img = cv2.imread(path)
    t1 = time.time()
    ocr_utput = doOCR(img)
    t2 = time.time()
    print(f'{t2-t1} {path}: "{ocr_utput}"')

def doOCR(img):
    img = cleanImg(img)
    return pytesseract.image_to_string(img)

def cleanImg(img):
    # Clean image
    # t1 = time.time()
    # Write cleaned image to cleaning_stages folder
    # t2 = time.time()
    # total_time = t2-t1 # Subtract this from the total computation time.
    return img # No cleaning for now

main()