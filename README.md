# Imagenet-TFRecord-Process
The codes for processing the Imagenet 2012 competetion dataset, transfer to the Tensorflow TFRecord that to ease the training and testing.

The Imagenet dataset can be downloaded via below URLs:

Train dataset:
http://www.image-net.org/challenges/LSVRC/2012/nnoupb/ILSVRC2012_img_train.tar

Validation dataset:
http://www.image-net.org/challenges/LSVRC/2012/nnoupb/ILSVRC2012_img_val.tar

Train dataset bounding box files:
http://www.image-net.org/challenges/LSVRC/2012/nnoupb/ILSVRC2012_bbox_train_v2.tar

The "train_preprocess.py" is used to uncompress the train dataset tar file, which includes 1000 folder, each relate to a category and stores the images.

The "bbox_preprocess.py" is used to parse the bbox xml files and write the result into a CSV file for later process.

The "tfrecord_process.py" is used to process the train dataset and validation dataset, you can specify how many CPU cores used to run in parellel. The program will tranfer every 1000 images into one tfrecord file. Which can greatly improve the later training and evaluating process.

In my computer using 4 CPU cores takes around 1 hour to process the whole 146G train dataset files.As below result:
Start processing train data using 4 CPU cores:
PID10501:320291/320291|PID10503:320291/320291|PID10505:320291/320291|PID10507:320294/320294|
Process finish, total process 1281167 images in 4113 seconds
Start processing validation data using 4 CPU cores:
PID11270:12500/12500|PID11272:12500/12500|PID11274:12500/12500|PID11276:12500/12500|
Process finish, total process 50000 images, using 161 seconds

The "tfrecord_test.py" is used to test the tfrecord, it test if the images can be read from the tfrecord sucessfully.
