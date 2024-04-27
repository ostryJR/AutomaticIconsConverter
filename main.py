from PIL import Image
import os
import config as cfg

def makeFolder(name):
    path = f'{cfg.pathMade}{name}'
    try:
        os.mkdir(path)
        print(f"Folder {name} created")
    except:
        print(f"Folder {name} already exists")

def scanForNewImages():
    toMakeImages = os.listdir(cfg.pathToMake)#get all images in the toMake folder
    doneImages = []
    for imageFolder in os.listdir(cfg.pathMade): #get all folders from the made folder
        if os.path.isdir(imageFolder):
            doneImages.append(imageFolder)
    for image in toMakeImages:
        if image.split()[0] in doneImages:
            toMakeImages.remove(image)

    print(f"Images to make: {toMakeImages}")
    return toMakeImages

def makeImage(imageName, size):
    #print(f"Making image {imageName} with size {size}")
    image = Image.open(f'{cfg.pathToMake}{imageName}')
    image = image.resize((size, size))
    image.save(f'{cfg.pathMade}/{imageName.split('.')[0]}/{imageName.split('.')[0]}{size}.png')
    print(f"Image {imageName.split('.')[0]} of size {size} made")

if __name__ == "__main__":
    imagesToMake = scanForNewImages()

    for image in imagesToMake:
        makeFolder(image.split('.')[0])
        for size in cfg.sizes:
            makeImage(image, size)
            pass
            
        os.remove(f'{cfg.pathToMake}{image}')
