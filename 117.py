import os 
import cv2 

path="album/"
images=[]

for i in os.listdir(path):
   # print(i)

    name,extention=os.path.splitext(i)

    if extention in ['.jpg','.png']:
        file_name= path+"/"+i
        print(file_name)

        images.append(file_name)
count=len(images)
print(count)

frame = cv2.imread(images[0])
width,hieght,channels=frame.shape
size=(width,hieght)
print(size)

out=cv2.VideoWriter("project.avi",cv2.VideoWriter_fourcc(*"DIVX"),0.8,size)

for i in range(0, count-1):
    frame=cv2.imread(images[i])
    out.write(frame)
out.release()
print("album is created")