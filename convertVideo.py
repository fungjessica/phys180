
# Program To Read video 
# and Extract Frames 
  
import cv2 
import os

# Function to extract frames 
def FrameCapture(path): 
  
    # Path to video file 
    vidObj = cv2.VideoCapture(path) 
    frames = "frames"
    os.makedirs(frames, exist_ok=True)
    # Used as counter variable 
    count = 0
  
    # checks whether frames were extracted 
    success = 1
  
    while success: 
  
        # vidObj object calls read 
        # function extract frames 
        success, image = vidObj.read() 
  
        # Saves the frames with frame-count 
        cv2.imwrite(os.path.join(frames, "frame%d.jpg" % count), image) 
  
        count += 1
  
  
# Driver Code 
if __name__ == '__main__': 
    pathie = os.path.join("videos", "IMG_5729.mov")
    # Calling the function 
    FrameCapture(pathie) 