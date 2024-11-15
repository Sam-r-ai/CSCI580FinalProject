#!/usr/bin/python3

#from PIL import Image
import random
import torch
import matplotlib.pyplot as plt
from torchvision import transforms, datasets


folder_path = 'training_data/'
pixels_size = 28

#   The transform is here to make sure the data 
#   is correct before it gets made to to TENSOR
transform = transforms.Compose([
    transforms.Resize((pixels_size, pixels_size)),
    transforms.ToTensor(),
    transforms.Grayscale()
])

#   get all the files in the folder and 
#   then make them all into tesnor data
#   for PYtorch to process 
dataset = datasets.ImageFolder(folder_path, transform=transform)
dataloader = torch.utils.data.DataLoader(dataset, batch_size=111, shuffle=False)

#   here the images will have a matrix of all the data as a TENSOR
images, labels = next(iter(dataloader)) 

#   the arrays for the images and lables are 
#   from the folder name and then indexed into the array
#   the len should be the number of files 
#   then show the image with plt change the way the matrix is 
#   with permute and then make the cmap gray to get the right colors
print('\n\n *Number of samples: ', len(images))
index = random.randint(0, int(len(images)))
image = images[index]
label = labels[index]
print("   Image Size: ", image.size())
print("  Image label: ", label)
plt.title(str(label))
plt.imshow(image.permute(1,2,0), cmap='gray')
plt.axis('off')
plt.show()
