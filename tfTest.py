import tensorflow as tf
hello = tf.constant('hello')
sess = tf.Session()
print(sess.run(hello))
a = tf.constant(2)
b = tf.constant(3)
print(sess.run(a+b))