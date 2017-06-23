# image2text
Implementation of Google's im2txt model for tensorflow (Updated for Python 3.5.2 and TensorFlow 1.0.1)

## Requirements
<li>Python 3.5
<li>TensorFlow 1.0.1 (pip install tensorflow)
<li>im2txt pretrained model you can find some of them <a href="https://github.com/tensorflow/models/issues/466">here</a>. I used <a href="https://drive.google.com/file/d/0B_qCJ40uBfjEWVItOTdyNUFOMzg/view">this (3m steps)</a>.

## Getting Started
Following the steps in the issue cited before, it can be fixed the version problems of the pretrained models. Just run the next snippets at the respectively file locations.

In order to update the vocabulary file:
```python
OLD_VOCAB_FILE = "word_counts.txt" # the path of the vocabulary file
NEW_VOCAB_FILE = "word_counts3.txt" # the path for the fixed vocabulary file

with open(OLD_VOCAB_FILE) as f:
  lines = list(f.readlines())

def clean_line(line):
  tokens = line.split()
  return "%s %s" % (eval(tokens[0]), tokens[1])

newlines = [clean_line(line) for line in lines]

with open(NEW_VOCAB_FILE, "w") as f:
  for line in newlines:
    f.write(line + "\n")
```

In order to update the checkpoint file:
```python
OLD_CHECKPOINT_FILE = "model.ckpt-3000000" # the path of the checkpoint
NEW_CHECKPOINT_FILE = "model.ckpt-3000000" # the path for the fixed checkpoint

import tensorflow as tf
vars_to_rename = {
    "lstm/BasicLSTMCell/Linear/Matrix": "lstm/basic_lstm_cell/weights",
    "lstm/BasicLSTMCell/Linear/Bias": "lstm/basic_lstm_cell/biases",
}
new_checkpoint_vars = {}
reader = tf.train.NewCheckpointReader(OLD_CHECKPOINT_FILE)
for old_name in reader.get_variable_to_shape_map():
  if old_name in vars_to_rename:
    new_name = vars_to_rename[old_name]
  else:
    new_name = old_name
  new_checkpoint_vars[new_name] = tf.Variable(reader.get_tensor(old_name))

init = tf.global_variables_initializer()
saver = tf.train.Saver(new_checkpoint_vars)

with tf.Session() as sess:
  sess.run(init)
  saver.save(sess, NEW_CHECKPOINT_FILE)
```

Finally, ensure that the path files are fine in the jupyter notebook (final_project.ipynb) and run it. I used the font _Aaargh.ttf_ for the visualization of the captions. You can get it <a href="http://www.dafont.com/es/aaargh.font">here</a>.
Another way to run the project is by typing at the termianl ```python3 -m im2txt.run_inference``` which will run the file inside the im2txt folder. 
The notebook is based on run_inference.py, and the last one is almost the same that can be found in the im2txt documentation.


In the notebook, you will see the editable parts of the code in order to implement the algorithm.
