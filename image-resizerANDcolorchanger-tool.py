#Author @Sam-r-ai
#11/14/2024

import os
from PIL import Image, ImageOps

input_folder = r'/Users/alexander/Desktop/Numbers'
#makes a copy to output folder so that input folder remains as backup in case something goes wrong
output_folder = r'/Users/Alexander/Desktop/Alexander-Dataset'

def resize_and_invert_images(input_folder, output_folder, size=(28, 28)):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)
        
        # Check if the file is an image
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            try:
                # Open the image file
                with Image.open(file_path) as img:
                    # Resize the image
                    img_resized = img.resize(size)
                    
                    # Convert image to grayscale
                    img_gray = img_resized.convert("L")
                    
                    # Invert the colors
                    inverted_image = ImageOps.invert(img_gray)
                    
                    # Increase brightness of the white numbers without thresholding
                    brightened_image = inverted_image.point(lambda x: min(255, x * 1.5))  # Increase brightness slightly
                    
                    # Convert to RGB to save as a regular image format
                    final_image = brightened_image.convert("RGB")
                    
                    # Save the resized and inverted image in the output folder
                    final_image.save(os.path.join(output_folder, filename))
                    print(f"Resized, inverted, and saved {filename} to {output_folder}")
            except Exception as e:
                print(f"Failed to process {filename}: {e}")

resize_and_invert_images(input_folder, output_folder)
