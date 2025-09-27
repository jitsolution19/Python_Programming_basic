'''
Created on 06-Dec-2024

@author: jeete
'''
# from PIL import Image

# Load the image file
image_path = "D:\Photos\Jitendra\Jitu Europe Trip\IMG_E9146.jpg"  # Replace with your image file path
image = Image.open(image_path)

# Get dimensions
width, height = image.size

print(f"Width: {width}px, Height: {height}px")