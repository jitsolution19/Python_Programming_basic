'''
Created on 06-Dec-2024

@author: jeete
'''
import cv2

# Read an image from file
image = cv2.imread('D:\Pre Bill\IMG_20221006_224303.jpg')

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not read the image.")
    exit()

# Create a resizable window
cv2.namedWindow('Loaded Image', cv2.WINDOW_NORMAL)

# Set the window size to desired dimensions (e.g., 800x600)
cv2.resizeWindow('Loaded Image', 800, 600)

# Display the image in a window
cv2.imshow('Loaded Image', image)

# Wait for a key press indefinitely or for a specific amount of time (milliseconds)
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()
