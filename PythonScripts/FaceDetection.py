import cv2
import sys

def DetectFace(image_path):

    # image_path = sys.argv[1]

    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=3,
        minSize=(30, 30)
    )

    num_faces = len(faces)
    print("[INFO] Found {0} Faces!".format(num_faces))



    zoom = 70

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x-zoom, y-zoom), (x + w + zoom, y + h + zoom), (0, 255, 0), 2)

        # Save each face individually
        roi_color = image[(y-zoom):y + h + zoom, (x-zoom):x + w +zoom]
        print("[INFO] Object found. Saving locally.")
        # cv2.imwrite(str(w) + str(h) + '_faces.jpg', roi_color)
        cv2.imwrite("cropped_image.png", roi_color)

    # status = cv2.imwrite('output.png', image)
    # print("[INFO] Image output.png written to filesystem: ", status)


    return num_faces

