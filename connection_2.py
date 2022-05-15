from peewee import *
database= MySQLDatabase ("mybd",
    user= "root",
    password="stels2011",
    host= "localhost")

class Tabl_2(Model):
    Catnumb = IntegerField()
    Cat_name = CharField()
    price = FloatField()

    class Meta:
        database = database

#Tabl_2.create_table()

P1 = Tabl_2(Catnumb = 10, Cat_name = "стройматериалы", price = 105.00)
P2 = Tabl_2(Catnumb = 505, Cat_name = "недвижимость", price = 210.00)
P3 = Tabl_2(Catnumb = 205, Cat_name = "транспорт", price = 160.00)
P4 = Tabl_2(Catnumb = 30, Cat_name = "мебель", price = 77.00)
P5 = Tabl_2(Catnumb = 45, Cat_name = "техника", price = 65.00)

P1.save()
P2.save()
P3.save()
P4.save()
P5.save()