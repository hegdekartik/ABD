
# Program To Read video 
# and Extract Frames 
import cv2 
  
      
# Path to video file 
vidObj = cv2.VideoCapture(path) 
  
# Used as counter variable 
count = 0
  
# checks whether frames were extracted 
success = 1
  
while success: 
  # vidObj object calls read 
  # function extract frames 	
  success, image = vidObj.read() 
  
  # Saves the frames with frame-count 
  cv2.imwrite("frame%d.jpg" % count, image) 
  
count += 1
  
# Driver Code 
if __name__ == '__main__': 
  
    # Calling the function 
    FrameCapture("/home/kartikhegde/opencv/airbubble/vtest1.webm") 

