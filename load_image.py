import pymysql
import pymysql.cursors
from PIL import Image
import PIL.Image


db = pymysql.connect(user='nao', password='control1234',
                              host='localhost',
                              database='nao_db')
cur=db.cursor()
query = ("INSERT INTO images(image) VALUES (%s)")

img_path = "/home/sorelys/Documents/PF/image2text/imagenes/6.jpg"

image = Image.open(img_path)
#image.show()
blob_value = open(img_path, 'rb').read()  
args = (blob_value, )
cur.execute(query,args)
db.commit();
print("Listo")
db.close();