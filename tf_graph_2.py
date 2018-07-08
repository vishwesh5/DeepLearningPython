# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 08:42:44 2018

@author: Vishwesh
"""

import tensorflow as tf

a = tf.constant(5.0)
b = tf.constant(3.0)
c = tf.multiply(b,a)
d = tf.sin(c)
e = tf.divide(b,d)

with tf.Session() as sess:
    outs = sess.run(e)

print("outs = {}".format(outs))