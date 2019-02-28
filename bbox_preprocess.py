import xml.etree.ElementTree as ET
import os
 
xmlRootDir = 'bbox/'
dirs = os.listdir(xmlRootDir)
files = os.listdir('bbox/'+dirs[0]+'/')
 
def parseXML(filename):
    bbox = [[],[],[],[]]
    tree = ET.parse(filename)
    root = tree.getroot()
    size = root.find('size')
    width = float(size.find('width').text)
    height = float(size.find('height').text)
    for node in root.iter("object"):
        bndbox = node.find('bndbox')
        xmin = max(float(bndbox.find('xmin').text)/width, 0.0)
        ymin = max(float(bndbox.find('ymin').text)/height, 0.0)
        xmax = min(float(bndbox.find('xmax').text)/width, 1.0)
        ymax = min(float(bndbox.find('ymax').text)/height, 1.0)
        bbox[0].append(xmin)
        bbox[1].append(ymin)
        bbox[2].append(xmax)
        bbox[3].append(ymax)
    return bbox
 
bboxfile = open('bbox_train.csv', 'w')
content = ''
i = 0
for folder in dirs:
    i+=1
    folderpath = xmlRootDir + folder + '/'
    files = os.listdir(folderpath)
    for xmlfile in files:
        bbox = parseXML(folderpath+xmlfile)
        content += xmlfile
        for j in range(4):
            content += ','+';'.join([str(x) for x in bbox[j]])
        content += '\n'
    print("processing %i/1000\r"%i, end="")
bboxfile.writelines(content)
bboxfile.close()
