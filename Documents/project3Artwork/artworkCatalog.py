import sqlite3
from peewee import *
from dbConfig import (database_path)


class databaseModel(Model):
    class Meta:
        db = SqliteDatabase(database_path)


class ArtistData(databaseModel):
    artistName = CharField()
    artistEmail = CharField()

    def __str__(self):
        return f'ID {self.id}, Artist Name: {self.artistName}, Artist Email: {self.artistEmail}'


class ArtworkData(databaseModel):
    name_of_artist = ForeignKeyField(ArtistData, to_field= 'artistName')
    name_of_artwork = CharField()
    price_of_artwork = FloatField()
    availability_of_artwork = BooleanField(default = True)

    def __str__(self):
        return f'Artist Name: {self.name_of_artist}, Artwork Name: {self.name_of_artwork}, Price : ${self.price_of_artwork}, Available: {self.availability_of_artwork} '




#Adding a new artist and getting user input 
#name = input('Enter an artist''s name: ')
#email = input('Enter the artist''s email address: ')

#Adding a new album by an artist
#albumArtist = input('Enter the artist''s name for the album: ')
#albumName = input('Enter the name of the album: ')
#albumPrice = float(input('Enter the price of the album: '))
#albumStock = int(input('Has the album been sold? Enter 0 for NO or 1 for YES: '))




