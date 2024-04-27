#from PIL import Image
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
    newImages = os.listdir(cfg.pathToMake)
    
    return images

print(scanForNewImages())
