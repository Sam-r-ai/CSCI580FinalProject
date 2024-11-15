#Author@ Sam-r-ai
#11/14/2024

import os

# Specify the directory path and digit label
directory_path = r"/Users/alexander/Desktop/Numbers/9"  # Replace with the path to your images

def rename_images(directory, digit_label):
    # Get all files in the directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    # Filter out files that are images (by common image file extensions)
    image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]
    
    # Rename each image
    for i, filename in enumerate(image_files, start=1):
        old_path = os.path.join(directory, filename)
        extension = os.path.splitext(filename)[1]
        new_filename = f"{digit_label}.{i}{extension}"
        new_path = os.path.join(directory, new_filename)
        os.rename(old_path, new_path)
        print(f"Renamed '{filename}' to '{new_filename}'")

    print(f"Renaming completed. {len(image_files)} images renamed successfully.")

digit_label = input("Enter the digit represented in the images (0-9): ")

# Validate the digit label
if digit_label.isdigit() and 0 <= int(digit_label) <= 9:
    rename_images(directory_path, digit_label)
else:
    print("Please enter a valid digit (0-9).")
