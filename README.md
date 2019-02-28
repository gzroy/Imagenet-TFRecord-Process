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

The "tfrecord_test.py" is used to test the tfrecord, it test if the images can be read from the tfrecord sucessfully.
