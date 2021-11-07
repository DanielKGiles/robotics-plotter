import tkinter
import cv2
import PIL.Image
import PIL.ImageTk
import time

# Needed to import custom-made modules
import sys
sys.path.append('../PythonScripts/')
import FaceDetection

import os
cwd = os.getcwd()
print("APP CURRENT WORKING DIRECTORY")
print(cwd)

import ImplementingLinedraw
from SendDataToPi import send_draw_rectangle, send_erase
class App:
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source

        # Change the background color of the app
        window.configure(bg='#a8e6ae')

         # open video source (by default this will try to open the computer webcam)
        self.vid = MyVideoCapture(self.video_source)
 
         # Create a canvas that can fit the above video source size
        self.canvas = tkinter.Canvas(window, width = self.vid.width, height = self.vid.height)
        self.canvas.pack()

        # A label to display output to the user
        self.label=tkinter.Label(window, text='Welcome! Center your face in the camera and take a snapshot to begin drawing, or select another option.', width=200, bg='#a8e6ae')
        self.label.pack(anchor=tkinter.CENTER, expand=True, pady=10)
        self.label.config(font=("Courier", 16))

        # Button that lets the user take a snapshot
        self.btn_snapshot=tkinter.Button(window, text="Snapshot", width=50, command=self.snapshot)
        self.btn_snapshot.pack(anchor=tkinter.CENTER, expand=True, pady=0)

        # Button that lets the user plot the calibration rectangle
        self.btn_calibration_rectangle=tkinter.Button(window, text="Draw a calibration rectangle", width=50, command=self.draw_rectangle)
        self.btn_calibration_rectangle.pack(anchor=tkinter.CENTER, expand=True, pady=0)

        # Button that lets the user send their own file
        self.btn_eraser=tkinter.Button(window, text="Choose file to draw", width=50, command=self.choose_file)
        self.btn_eraser.pack(anchor=tkinter.CENTER, expand=True, pady=0)

        # Button that lets the user erase the board
        self.btn_file_lookup=tkinter.Button(window, text="Move arms to erase board", width=50, command=self.erase)
        self.btn_file_lookup.pack(anchor=tkinter.CENTER, expand=True, pady=0)
        


        # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = 15
        self.update()
 
        self.window.mainloop()


    def draw_rectangle(self):
        self.label.config(text = "The robot will begin drawing a rectangle shortly...")
        send_draw_rectangle()
        self.label.config(text = "Rectangle complete! Select another option to continue.")

    def choose_file(self):
        ...

    def erase(self):
        send_erase()
        
 
    def snapshot(self):
         # Get a frame from the video source
        ret, frame = self.vid.get_frame()
 
        if ret:
            #  cv2.imwrite("frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
            cv2.imwrite("snapshot.png", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

            num_faces = FaceDetection.DetectFace("snapshot.png")

            if num_faces == 0:
                self.label.config(text = "0 Faces Detected. Please try again.")
            elif num_faces > 1:
                self.label.config(text = "{} faces dectected. Only one face can be present. Please try again.".format(num_faces))
            elif num_faces == 1:
                self.label.config(text = "One face detected! Beginning drawing now...")
                
                ImplementingLinedraw.SketchAndVisualize("./cropped_image.png")
    
    def update(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()
 
        if ret:
             self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
             self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)
 
        self.window.after(self.delay, self.update)
 
 
class MyVideoCapture:
    def __init__(self, video_source=0):
         # Open the video source
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)
 
         # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
 
    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                 # Return a boolean success flag and the current frame converted to BGR
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret, None)
 
    # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()
 
# Create a window and pass it to the Application object
App(tkinter.Tk(), "Tkinter and OpenCV")
