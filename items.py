# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import peewee

db = peewee.SqliteDatabase("entreprises.db")


class DebutItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class Entreprise(scrapy.Item):
    nom = scrapy.Field()
    produit = scrapy.Field()
    lieu = scrapy.Field()
    contact = scrapy.Field()


class ModelEntreprise(peewee.Model):
    nom = peewee.CharField(verbose_name='nom', max_length=255)
    produit = peewee.CharField(verbose_name='produit', max_length=255)
    lieu = peewee.CharField(verbose_name='lieu', max_length=255)
    contact = peewee.CharField(verbose_name='contact', max_length=255)
    
    class Meta:
        database = db

