from pds4_tools import pds4_read   
import numpy as np
import png
import glob

def read_pds(path):
    data = pds4_read(path, quiet=True)
    img = np.array(data[0].data)
    return img    

#def export_img8(name,img):             #8bit
#    img8=np.array(np.uint8(img/4))
#    png.from_array(img8,'L').save(name)

def export_img16(name,img):
    img16=np.array(np.uint16(img*32))
    png.from_array(img16,'L').save(name)

for p in glob.glob('*.2BL'):
    img = read_pds(p)
    export_img16(f"{p}.png", img)
