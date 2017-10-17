import tensorflow as tf

def classify(features, labels):
    sess = tf.Session()

    #Tensorflow placeholder (the tensors to hold our data)
    x = tf.placeholder(tf.float32, [None, 11])

    #Weights
    W = tf.Variable(tf.zeros([11,2]))

    #biases
    b = tf.Variable(tf.zeros([2]))

    #activation function
    y_values = tf.add(tf.matmul(x, W), b)
    y= tf.nn.softmax(y_values)

    #Tensorflow placeholder (the tensor to hold our labels)
    y_ = tf.placeholder(tf.float32, [None,2])

    saver = tf.train.Saver()
    saver.restore(sess, "./models/classifier.ckpt")

    input_data = format_features(features)
    prediction = sess.run(y, feed_dict={x: input_data})[0]

    confidence = -1
    pred = 'ERROR'

    if prediction[0]>=prediction[1]:
        confidence=prediction[0]
        pred=labels[0]
    else:
        confidence=prediction[1]
        pred=labels[1]
    return pred, confidence

def format_features(features):
    row = []
    row.append(features['product_ids'])
    row.append(features['numbers'])
    row.append(features['invoice_ids'])
    row.append(features['nouns'])
    row.append(features['verbs'])
    row.append(features['adjectives'])
    row.append(features['conjunctions'])
    row.append(features['small_blocks'])
    row.append(features['med_blocks'])
    row.append(features['large_blocks'])
    row.append(features['total_words'])
    input_data=[row]

    return input_data


