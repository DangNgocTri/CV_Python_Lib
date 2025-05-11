import cv2 as cv
import numpy as np

if __name__ == '__main__':
    print(cv.__version__)
mylist = [1, 2, 3]
# print(type(mylist))
myarray = np.array(mylist)
# print(myarray)
# print(type(myarray))
np.random.seed(101)
arr = np.random.randint(0,100,10)
print(arr)
# print("Max la", arr.max())
# print("vi tri", arr.argmax())
# print("Min la", arr.min())
# print("vi tri", arr.argmin())
# print("Trung binh =", arr.mean())
arr1 = arr.reshape(2,5)
# print(arr1)
mat1 = np.arange(0,49).reshape(7,7)
# print(mat1)
# print(mat1[0,:])
mat2 = np.random.randint(0,200,100).reshape(10,10)
# print(mat2)
