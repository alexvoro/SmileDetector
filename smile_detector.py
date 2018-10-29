import Tkinter as tk
from threading import Timer

import cv2
import numpy as np
import sys

facePath = "/usr/local/Cellar/opencv/3.3.1_1/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml"
smilePath = "/usr/local/Cellar/opencv/3.3.1_1/share/OpenCV/haarcascades/haarcascade_smile.xml"
faceCascade = cv2.CascadeClassifier(facePath)
smileCascade = cv2.CascadeClassifier(smilePath)


root = tk.Tk() 
root.title('Smile detector')
resultLabel = tk.Label(root, fg="dark green")
resultLabel.pack()
resultLabel.config(text="...")

def start_video(timerText):
	if timerText == "":
		timerText = "5"
	count_smiles(int(timerText))

sF = 1.05
smilesCount = 0
noSmilesCount = 0

def show_resultLabel(percentage):
	global resultLabel
	label_text = "in total you were smiling " + str(percentage) + " % of the given time"
	resultLabel.config(text=label_text)
  
def count_smiles(timerLength):
	global isVideoCaptureActive
	isVideoCaptureActive = True
	
	capture = cv2.VideoCapture(0)
	#capture.set(3,640)
	capture.set(4,480)
	
	global smilesCount
	global noSmilesCount
	smilesCount = 0
	noSmilesCount = 0

	def timeout():
		global isVideoCaptureActive
		isVideoCaptureActive = False
		difference  = (smilesCount * 100) / (smilesCount + noSmilesCount);
		
		show_resultLabel(difference)
		
		print smilesCount
		print noSmilesCount
		print "percetange:", difference, "%"
		capture.release() 

	t = Timer(timerLength, timeout)
	t.start()
	
	while isVideoCaptureActive:
		ret, frame = capture.read() # Capture frame-by-frame
		img = frame
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		faces = faceCascade.detectMultiScale(
			gray,
			scaleFactor= sF,
			minNeighbors=8,
			minSize=(55, 55),
			flags=cv2.CASCADE_SCALE_IMAGE
		)

		# For each found face, draw a rectangle around it
		for (x, y, w, h) in faces:
			cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
			roi_gray = gray[y:y+h, x:x+w]
			roi_color = frame[y:y+h, x:x+w]

			smile = smileCascade.detectMultiScale(
				roi_gray,
				scaleFactor= 1.7,
				minNeighbors=22,
				minSize=(25, 25),
				flags=cv2.CASCADE_SCALE_IMAGE
				)

			# Print the text to smile, if no smiles are found
			if len(smile) == 0:
				noSmilesCount = noSmilesCount + 1 
				cv2.putText(frame, "SMILE!",(x,y), cv2.FONT_HERSHEY_SIMPLEX, 2, 155, 10)

			# Count each found smile
			for (x, y, w, h) in smile:
				smilesCount = smilesCount + 1
				print "Found", smilesCount, "smiles!"
				cv2.putText(frame, "smile detected :)",(x,y), cv2.FONT_HERSHEY_SIMPLEX, 2, 155, 10)
				cv2.rectangle(roi_color, (x, y), (x+w, y+h), (255, 255, 0), 1)
				
		cv2.imshow('Smile :)', frame)
		c = cv2.waitKey(7) % 0x100
		if c == 27:
			break 

labelEntry = tk.Label(root, text='Insert timer inteval and click Start', fg="dark green")
labelEntry.pack()
e = tk.Entry(root, text='5', width=50)
e.pack()

buttonStart = tk.Button(root, text='Start', width=25, command= lambda: start_video(e.get()))
buttonStart.pack()
root.mainloop()
