# ARREGLAR EL TEXTO
OLD_VOCAB_FILE = "word_counts.txt"
NEW_VOCAB_FILE = "word_counts2.txt"

with open(OLD_VOCAB_FILE) as f:
  lines = list(f.readlines())

def clean_line(line):
  tokens = line.split()
  return "%s %s" % (eval(tokens[0]), tokens[1])

newlines = [clean_line(line) for line in lines]

with open(NEW_VOCAB_FILE, "w") as f:
  for line in newlines:
    f.write(line + "\n")


# ARREGLAR EL CHECKPOINT

OLD_CHECKPOINT_FILE = "/home/sorelys/im2txt/model/train/model.ckpt-3000000"
NEW_CHECKPOINT_FILE = "/home/sorelys/im2txt/model/train/model.ckpt-3000000"

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