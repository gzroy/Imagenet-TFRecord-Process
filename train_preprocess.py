import os
 
filelist = os.popen("tar -tf ILSVRC2012_img_train.tar").readlines()
 
num = 0
for item in filelist:
    tarfile = item.strip()
    folder = tarfile[:-4]
    os.popen("mkdir data/"+folder+"/")
    os.popen("tar xf ILSVRC2012_img_train.tar "+tarfile)
    os.popen("tar xf "+tarfile+" -C data/"+folder+"/")
    os.popen("rm -f "+tarfile)
    num += 1
    print "processing %i/1000\r" %num,
