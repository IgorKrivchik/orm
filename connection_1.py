from peewee import *

from connection_2 import Tabl_2
database= MySQLDatabase ("mybd",
    user= "root",
    password="stels2011",
    host= "localhost")

class Tabl(Model):
    Part_ID = IntegerField()
    Part = CharField()
    Cat = IntegerField()

    class Meta:
        database = database

#Tabl.create_table()
P1 = Tabl(Part_ID = 1, Part = "квартиры", Cat = 505)
P2 = Tabl(Part_ID = 2, Part = "автомашины", Cat = 205)
P3 = Tabl(Part_ID = 3, Part = "доски", Cat = 10)
P4 = Tabl(Part_ID = 4, Part = "шкафы", Cat = 30)
P5 = Tabl(Part_ID = 5, Part = "книги", Cat = 160)

# P1.save()
# P2.save()
# P3.save()
# P4.save()
# P5.save()

for New_Tabl in Tabl.select().join(Tabl_2).where(Tabl.Cat == Tabl_2.Catnumb):
    print (New_Tabl.Cat,New_Tabl.id,New_Tabl.Part)