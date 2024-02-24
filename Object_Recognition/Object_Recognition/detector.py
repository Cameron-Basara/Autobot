from imageai.Detection import ObjectDetection
import cv2

cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop)
cap.set(3 , 1920) # setting the width
cap.set(4 , 1080) # setting the height
cap.set(14, 0) # setting the gain
cap.set(15, -3) # setting the expsoure
ret,frame = cap.read() # return a single frame in variable `frame`


while(True):
    cv2.imwrite('input/capimg.jpg', frame) # saving the image
    break

cap.release()

#----------------------------------------------------------------------------------------------------

detector = ObjectDetection()

model_path = "./models/yolo-tiny.h5"
input_path = "./input/capimg.jpg"   # setting the input for the object detector
output_path = "./output/newimage.jpg"

detector.setModelTypeAsTinyYOLOv3()
detector.setModelPath(model_path)
detector.loadModel()
detection = detector.detectObjectsFromImage(input_image=input_path, output_image_path=output_path)


word = []
person = "name"

for eachItem in detection:
    print(eachItem[person] , " : ", eachItem["percentage_probability"])
    word.append(eachItem[person])

face = "person"

face_number = word.count(face)


if face_number > 1: # what happens if more than one person is standing infront of the camera
    print ("too many people!")

elif face in word:  # what happens if only one person is standing infront of the camera
    print("You have been registered for the shopping cart!")

else:               # what happens if no one is standing infront of the camera
    print("I don't see anyone yet!")
