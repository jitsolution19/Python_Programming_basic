import cv2

# Load the pre-trained Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Read the input image
image = cv2.imread('D:\Photos\Jitendra\Jitu Europe Trip\IMG_9116.jpg')
# image = cv2.imread('D:\Photos\Jitendra\Jitu Europe Trip\IMG_8249.jpg')
# image = cv2.imread('D:\Photos\Jitendra\Jitu Europe Trip\IMG_E8661.jpg')

# Check if the image is loaded successfully
if image is None:
    print("Error: Could not load the image.")
    exit()

# Convert the image to grayscale (Haar cascades work on grayscale images)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.3, minNeighbors=7, minSize=(200, 200))

# Get the number of faces detected
num_faces = len(faces)
print(f"Number of faces detected: {num_faces}")

# Draw rectangles around the detected faces
for (x, y, w, h) in faces:
    
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)


# Resize the image to fit inside a window while maintaining the aspect ratio
window_width, window_height = 2000, 800  # Desired window size
height, width = image.shape[:2]

# Calculate the scaling factor to fit the image into the window
scaling_factor = min(window_width / width, window_height / height)

# Resize the image
resized_image = cv2.resize(image, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)

# Display the output image
cv2.imshow('Detected Faces (Resized)', resized_image)

# # Display the output image
# cv2.imshow('Detected Faces', image)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
