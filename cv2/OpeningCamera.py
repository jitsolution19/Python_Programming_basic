'''
Created on 06-Dec-2024

@author: jeete
'''

import cv2  # Import cv2 directly without renaming for simplicity
print(cv2.__version__)  # Should print 4.9.0.80
# Open video capture (0 for the primary webcam)
vid = cv2.VideoCapture(0)

# Check if the video capture is opened successfully
if not vid.isOpened():
    print("Error: Could not open video source")
    exit()

while True: 
    # Capture the video frame by frame
    ret, frame = vid.read()

    # Check if the frame was captured successfully
    if not ret:
        print("Error: Could not read frame")
        break

    # Display the resulting frame
    cv2.imshow('frame', frame)
    
    # The 'q' button is set as the quitting button
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

# Release the capture object and close windows
vid.release()
cv2.destroyAllWindows()
