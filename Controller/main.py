from path import __PATH__
from text import __EXTRACT__
from database import __DATABASE__
from datetime import datetime

# VARIABLE
__IMAGEDIR__ = r'/home/sad/Pictures/rok_picture/'


#  OBJECTS
path = __PATH__()
extract = __EXTRACT__(__IMAGEDIR__)
database = __DATABASE__('localhost', 'qwerty00', '123456.', 'mystats')


# GET PATH
path.set_path(__IMAGEDIR__)
__IMAGE__ = path.get_files()


# EXTRACT DATA FROM IMAGE WITH PIL AND PYTESSERACT
__DATA__ = [extract.get_image(i) for i in __IMAGE__]
__DATA__ = [i.replace('\n\x0c', '') for i in __DATA__]
__DATA__.append(datetime.today().strftime('%Y-%m-%d'))
print(__DATA__)

#adding information in database 
db = database.connection()
database.add(db,__DATA__)