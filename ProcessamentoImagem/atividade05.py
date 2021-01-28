import numpy as np
import cv2 as cv

def main():
    imagem = cv.imread('imagem.jpg', 1)
    
    # SISTEMAS DE CORES
    cv.imshow('ORIGINAL', imagem)
    cv.imshow('TONS DE CINZA', cv.cvtColor(imagem, cv.COLOR_RGB2GRAY))
    cv.imshow('HSV', cv.cvtColor(imagem, cv.COLOR_RGB2HSV))

    # SEPARAÇÃO DE CANAIS RGB
    channels = cv.split(imagem)
    cv.imshow('ORIGINAL', imagem)
    cv.imshow('BLUE', channels[0])
    cv.imshow('GREEN', channels[1])
    cv.imshow('RED', channels[2])

    # SALVANDO AS IMAGENS
    cv.imwrite('tonsCinza.jpg', cv.cvtColor(imagem, cv.COLOR_RGB2GRAY))
    cv.imwrite('hsv.jpg', cv.cvtColor(imagem, cv.COLOR_RGB2HSV))
    cv.imwrite('blueChannel.jpg', channels[0])
    cv.imwrite('greenChannel.jpg', channels[1])
    cv.imwrite('redChannel.jpg', channels[2])

    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()