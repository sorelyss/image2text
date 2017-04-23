import pymysql
import pymysql.cursors
from PIL import Image
import PIL.Image
from io import BytesIO

import tensorflow as tf

db = pymysql.connect(user='nao', password='control1234',
                              host='localhost',
                              database='nao_db')
cur=db.cursor()
query = ("SELECT id,image FROM images ORDER BY id DESC LIMIT 1")

cur.execute(query)
data=cur.fetchall()
file_like=BytesIO(data[0][1])
print(type(file_like.getvalue()).__name__)
print(type(file_like).__name__)
img=PIL.Image.open(file_like)
#print(img)
#image = tf.image.decode_jpeg(str(list(img.getdata())),channels=None);
#image = tf.Variable(str(list(img.getdata())))
#print(type(image).__name__)
img.show()
print(data[0][0])
#print(list(img.getdata()))

#with tf.image.decode_jpeg(img.getdata()) as f:
#	image = f.read()


db.close();