import tensorflow as tf
import cv2
import numpy as np
import os
 
def _parse_function(example_proto):
    features = {"image": tf.FixedLenFeature([], tf.string, default_value=""),
                "height": tf.FixedLenFeature([1], tf.int64, default_value=[0]),
                "width": tf.FixedLenFeature([1], tf.int64, default_value=[0]),
                "channels": tf.FixedLenFeature([1], tf.int64, default_value=[3]),
                "colorspace": tf.FixedLenFeature([], tf.string, default_value=""),
                "img_format": tf.FixedLenFeature([], tf.string, default_value=""),
                "label": tf.FixedLenFeature([1], tf.int64, default_value=[0]),
                "bbox_xmin": tf.VarLenFeature(tf.float32),
                "bbox_xmax": tf.VarLenFeature(tf.float32),
                "bbox_ymin": tf.VarLenFeature(tf.float32),
                "bbox_ymax": tf.VarLenFeature(tf.float32),
                "text": tf.FixedLenFeature([], tf.string, default_value=""),
                "filename": tf.FixedLenFeature([], tf.string, default_value="")
               }
    parsed_features = tf.parse_single_example(example_proto, features)
    
    xmin = tf.expand_dims(parsed_features["bbox_xmin"].values, 0)
    xmax = tf.expand_dims(parsed_features["bbox_xmax"].values, 0)
    ymin = tf.expand_dims(parsed_features["bbox_ymin"].values, 0)
    ymax = tf.expand_dims(parsed_features["bbox_ymax"].values, 0)
    
    bbox = tf.concat(axis=0, values=[ymin, xmin, ymax, xmax])
    bbox = tf.expand_dims(bbox, 0)
    bbox = tf.transpose(bbox, [0, 2, 1])
    
    height = parsed_features["height"]
    width = parsed_features["width"]
    channels = parsed_features["channels"]
 
    image_decoded = tf.cast(tf.image.decode_jpeg(parsed_features["image"], channels=3), tf.float32)
    begin, size, bbox_for_draw = tf.image.sample_distorted_bounding_box(tf.shape(image_decoded),
                                                                        bounding_boxes=bbox,
                                                                        min_object_covered=0.2,
                                                                        seed=123,
                                                                        use_image_if_no_bounding_boxes=True)
    images = tf.expand_dims(image_decoded, 0)
    new_bbox = tf.concat([bbox, bbox_for_draw],axis=1)
    image_bbox = tf.cast(tf.image.draw_bounding_boxes(images, new_bbox), tf.uint8) 
    return image_bbox
 
with tf.device('/cpu:0'):
    dataset_train = tf.data.TFRecordDataset('train_1.tfrecord')
    dataset_train = dataset_train.map(_parse_function)
    iterator = tf.data.Iterator.from_structure(dataset_train.output_types, dataset_train.output_shapes)
    #img, height, width, channels, colorspace, img_format, label, xmin, ymin, xmax, ymax, text = iterator.get_next()
    image_bbox = iterator.get_next()
    train_init_op = iterator.make_initializer(dataset_train)
 
sess = tf.Session()
sess.run(train_init_op)
image_bbox_run = sess.run(image_bbox)
img=cv2.cvtColor(image_bbox_run[0],cv2.COLOR_RGB2BGR)
cv2.imshow("image", img)
if cv2.waitKey(5000):
    cv2.destroyAllWindows()
cv2.destroyAllWindows()
