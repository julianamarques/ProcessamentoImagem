import numpy as np
import cv2 as cv


def main():
    imagem = cv.imread('imagem.jpg', 1)
    img_tons_cinza = cv.cvtColor(imagem, cv.COLOR_RGB2GRAY)
    img_blur = cv.blur(img_tons_cinza,(10,10))
    img_gaussian_blur = cv.blur(img_tons_cinza,(10,10),1)
    img_median_blur = cv.medianBlur(img_tons_cinza,9)
    
    cv.imshow('ORIGINAL', imagem)
    cv.imshow('TONS DE CINZA', img_tons_cinza)
    cv.imshow('BLUR', img_blur)
    cv.imshow('GAUSSIAN BLUR', img_gaussian_blur)
    cv.imshow('MEDIAN BLUR', img_median_blur)

    cv.waitKey(0)
    cv.destroyAllWindows()

    cv.imwrite('tonsCinza.jpg', img_tons_cinza)
    cv.imwrite('blur.jpg', img_blur)
    cv.imwrite('gaussianBlur.jpg', img_gaussian_blur)
    cv.imwrite('medianBlur.jpg', img_median_blur)

if __name__ == "__main__":
    main()