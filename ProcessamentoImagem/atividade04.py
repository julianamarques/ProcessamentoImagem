import numpy as np
import cv2 as cv

def main():
    escala()

def get_imagem():
    imagem = cv.imread('imagem.jpg', 0)

    return imagem


def translacao():
    img = get_imagem()
    rows,cols = img.shape
    M = np.float32([[1,0,100],[0,1,50]])
    dst = cv.warpAffine(img,M,(cols,rows))
    cv.imshow('ORIGINAL', img)
    cv.imshow('TRANSLACAO', dst)
    cv.waitKey(0)
    cv.destroyAllWindows()


def escala():
    img = get_imagem()
    height,width = img.shape[:2]
    res = cv.resize(img,(2*width,2*height),interpolation=cv.INTER_CUBIC)
    cv.imshow('ORIGINAL', img)
    cv.imshow('ESCALA', res)
    cv.waitKey(0)
    cv.destroyAllWindows()
    

def rotacao():
    img = get_imagem()
    rows,cols = img.shape
    M = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),42,1)
    dst = cv.warpAffine(img,M,(cols,rows))
    cv.imshow('ORIGINAL', img)
    cv.imshow('ROTACIONADA', dst)
    cv.waitKey(0)
    cv.destroyAllWindows()


def espelhamento():
    img = get_imagem()
    horizontal_img = img.copy()
    vertical_img = img.copy()
    horizontal_img = cv.flip(img, 0)
    vertical_img = cv.flip(img, 1)
    cv.imshow('ORIGINAL', img)
    cv.imshow('ESPELHAMENTO', vertical_img)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()