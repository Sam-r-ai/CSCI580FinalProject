#Author @Sam-r-ai
#11/14/2024

import os
from PIL import Image
import shutil


input_folder = r'C:\Users\user\Desktop\folderWithAllData'
#makes a copy to the output folder so that input folder is a backup in case something goes wrong
output_folder = r'C:\Users\user\Desktop\resizedData'

def resize_images(input_folder, output_folder, size=(28, 28)):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)
        
        # Check if the file is an image
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            try:
                # Copy the original image to the output folder for backup
                backup_path = os.path.join(output_folder, filename)
                shutil.copy(file_path, backup_path)
                
                # Open the copied image file
                with Image.open(backup_path) as img:
                    # Resize the image
                    img_resized = img.resize(size)
                    
                    # Save the resized image in the output folder
                    img_resized.save(backup_path)
                    print(f"Resized and saved {filename} to {output_folder}")
            except Exception as e:
                print(f"Failed to process {filename}: {e}")

resize_images(input_folder, output_folder)
