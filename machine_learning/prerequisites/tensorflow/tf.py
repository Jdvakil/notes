import tensorflow as tf
import numpy as np
import os


rank_0_tensor = tf.constant(5) #scalar value -- no axes contains single value
print(rank_0_tensor)

rank_1_tensor = tf.constant([2.0, 3.0, 4.0]) #vector -- has one axis
print(rank_1_tensor)

rank_2_tensor = tf.constant([[3,4], [5,6]], dtype=tf.float32) # matrix -- has two axes (3x2)
print(rank_2_tensor)


rank_3_tensor = tf.constant([
    [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]], 
    [[20,21,22,23,24],[25,26,27,28,29],[30,31,32,33,34],[35,36,37,38,39]],
    [[40,41,42,43,44],[45,46,47,48,49],[50,51,52,53,54],[55,56,57,58,59]]
]) # three matrices of 4x5 matrix
print(rank_3_tensor)

np_arr = np.array(rank_1_tensor) #convert tensor to numpy arrays
print(np_arr)

np_arr_2 = rank_2_tensor.numpy() #use tensor to convert to numpy 
print(np_arr_2)

np_1_arr = np.array([1,2,3])
np_to_tf = tf.convert_to_tensor(np_1_arr)

print(f"Before: {type(np_1_arr)}, After: {type(np_to_tf)}")

tf_ones = tf.ones([2,2]) #tensor for ones
print(tf_ones)

tf_add = tf.add(rank_2_tensor, tf_ones) #add two tensors
print(tf_add)

print(tf.reduce_max(tf_add)) #get the max value 

print(tf.math.argmax(tf_add)) #get index of the max value

print(tf.nn.softmax(tf_add))


rank_4_tensor = tf.zeros([3, 2, 4, 5]) #Tensor for all zeroes

print("Type of every element:", rank_4_tensor.dtype)
print("Number of axes:", rank_4_tensor.ndim)
print("Shape of tensor:", rank_4_tensor.shape)
print("Elements along axis 0 of tensor:", rank_4_tensor.shape[0])
print("Elements along the last axis of tensor:", rank_4_tensor.shape[-1])
print("Total number of elements (3*2*4*5): ", tf.size(rank_4_tensor).numpy())


x = tf.constant([[1], [2], [3]])
print(x.shape)

print(tf.reshape(x, [1,3]))