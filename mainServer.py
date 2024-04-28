from PIL import Image
import os
import config as cfg
import shutil
import time

def makeFolder(name):
    path = f'{cfg.pathMade}{name}'
    try:
        os.mkdir(path)
        print(f"Folder {name} created")
    except:
        print(f"Folder {name} already exists")

def scanForNewImages():
    doneImages = []
    try:
        toMakeImages = os.listdir(cfg.pathToMake)#get all images in the toMake folder
    except:
        os.mkdir(cfg.pathToMake)
        toMakeImages = os.listdir(cfg.pathToMake)#get all images in the toMake folder
        print("toMake folder created")
    try:
        for imageFolder in os.listdir(cfg.pathMade): #get all folders from the made folder
            if os.path.isdir(imageFolder):
                doneImages.append(imageFolder)
    except:
        os.mkdir(cfg.pathMade)
        print("Made folder created")
    for image in toMakeImages:
        if image.split()[0] in doneImages:
            toMakeImages.remove(image)

    print(f"Images to make: {toMakeImages}")
    return toMakeImages

def makeImage(imageName, size):
    #print(f"Making image {imageName} with size {size}")
    imageRaw = Image.open(f'{cfg.pathToMake}/{imageName}')
    image = imageRaw.convert('RGBA')
    if image.size[0] > image.size[1]:
        scale = image.size[0]/size
        image = image.resize((int(image.size[0]/scale), int(image.size[1]/scale)))
    else:
        scale = image.size[1]/size
        image = image.resize((int(image.size[0]/scale), int(image.size[1]/scale)))

    image2 = Image.new('RGBA', (size, size))
    image2.paste(image, (int((size - image.size[0]) / 2), int((size - image.size[1]) / 2)))
    image2.save(f'{cfg.pathMade}/{imageName.split('.')[0]}/{imageName.split('.')[0]}{size}.png')
    print(f"Image {imageName.split('.')[0]} of size {size} made")

if __name__ == "__main__":
    while True:
        imagesToMake = scanForNewImages()
        if imagesToMake != []:
            for image in imagesToMake:
                makeFolder(image.split('.')[0])
                shutil.copyfile(image, f'{cfg.pathMade}/{image.split('.')[0]}/{image.split('.')[0]}Original.png')
                for size in cfg.sizes:
                    makeImage(image, size)
                    pass
                    
                os.remove(f'{cfg.pathToMake}{image}')
        time.sleep(cfg.timeToWait)