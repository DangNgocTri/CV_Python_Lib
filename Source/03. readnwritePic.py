import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import os

# from PIL import Image
# pic = Image.open('Photos\Dog.jpg')
# pic_arr = np.asarray(pic)
# repr(pic)
# pic.show()

def readImage():
    root = os.getcwd()
    imgPath = os.path.join(root, 'Photos\Dog.jpg')
    img = cv.imread(imgPath)
    debug = 1
    cv.imshow('img',img)
    cv.waitKey(0)
    # img = cv.imread("image.jpg")
    # img = cv.cvtColor(img, cv.COLOR_BGR2RGB)  # Chuyển sang RGB để hiển thị đúng màu
    # plt.imshow(img)
    # plt.axis('off')  # Ẩn trục tọa độ
    # plt.show()
def writeImage():
    root = os.getcwd()
    imgPath = os.path.join(root, 'Photos\Dog.jpg')
    img = cv.imread(imgPath)
    if img is None:
        print("Không thể đọc ảnh. Kiểm tra đường dẫn!")
        return
    
    # Giới hạn vùng từ hàng 100, cột 100 đến hết
    img[100:, 100:, 0] = np.clip(img[100:, 100:, 0] + 20, 0, 255)  # Kênh Blue
    img[100:, 100:, 2] = np.clip(img[100:, 100:, 2] + 10, 0, 255)  # Kênh Red

    # Hiển thị ảnh sau khi chỉnh sửa
    cv.imshow("Modified Image", img)

    outPath = os.path.join(root, 'Photos\DogOutput.jpg')
    cv.imwrite(outPath, img)
    print(f"Ảnh đã được lưu tại {outPath}")
    # Chờ người dùng nhấn phím để đóng cửa sổ ảnh
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    # readImage()
    writeImage()