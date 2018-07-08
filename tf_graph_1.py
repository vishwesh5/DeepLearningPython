# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 08:36:17 2018

@author: Vishwesh
"""

import tensorflow as tf

a = tf.constant(5)
b = tf.constant(3)
d = tf.add(a,b)
c = tf.multiply(b,a)
f = tf.add(d,c)
e = tf.subtract(d,c)
g = tf.divide(f,e)

with tf.Session() as sess:
    outs = sess.run(g)
print("outs = {}".format(outs))