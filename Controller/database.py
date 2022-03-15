
from distutils import errors
import mysql.connector

class __DATABASE__:

    def __init__(self, __HOST__, __USERNAME__, __PASSWORD__, __DATABASE__):
        self.__HOST__ = __HOST__
        self.__USERNAME__ = __USERNAME__
        self.__PASSWORD__ = __PASSWORD__
        self.__DATABASE__ = __DATABASE__
    
    def connection(self):
        con = mysql.connector.connect (
            host = self.__HOST__,
            user = self.__USERNAME__,
            password = self.__PASSWORD__,
            database = self.__DATABASE__
        )
        return con
    
    def add(self, __, __DATA__):

        ID_LILITH = __DATA__[4]
        NAME = __DATA__[1]
        POWER = __DATA__[5]
        T4 = __DATA__[3]
        T5 = __DATA__[2]
        TOTAL_POWER = __DATA__[6]
        DEATH = __DATA__[0]
        DATE_UPDATE = __DATA__[7]


        try:
            cur = __.cursor()
            sql = "INSERT INTO STAT(ID_LILITH, NAME, POWER, T4_KILLS, T5_KILLS, TOTAL_KILLS, DEATH, DATE_UPDATE) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val = (ID_LILITH, NAME, POWER, T4, T5, TOTAL_POWER, DEATH, DATE_UPDATE,)
            cur.execute(sql, val)
            __.commit()

        except errors.DataEroor as e:
            print(e)