from peewee import *
from artworkCatalog import (ArtistData,ArtworkData)
from dbConfig import database_path

#Using
db = SqliteDatabase(database_path)
#Connection to the db
db.connect()

#Creating the tables from my classes in artworkCatalog
#Those tables being ArtistData and ArtworkData
def create_table():
    with db:
        db.create_tables([ArtistData, ArtworkData])

#Adding an artist to the Artistdata table
def adding_artist(artistName, artistEmail):
    adding_artist = ArtistData( artistName = artistName, artistEmail = artistEmail )
    adding_artist.save()

#Adding artwork to the ArtworkData table
def adding_artwork(name_of_artist, name_of_artwork, price_of_artwork, availability_of_artwork):
    adding_artwork = ArtworkData( name_of_artist = name_of_artist, name_of_artwork = name_of_artwork,price_of_artwork = price_of_artwork, availability_of_artwork = availability_of_artwork)
    adding_artwork.save()

#Deleting an artwork using the name_of_artwork object, in table ArtworkData
def deleting_artwork(name_of_artwork):
    ArtworkData.delete().where(ArtworkData.name_of_artwork == name_of_artwork).execute()


def search_for_artwork_available(artistName):

    search = ArtworkData.select().where((ArtworkData.name_of_artist == artistName ) | (ArtworkData.availability_of_artwork == True))

    #For loop, using the varible is_artwork_available is using the search string to 
    #search ArtworkData for the specific artwork, prints the result (is_artwork_available)
    for is_artwork_available in search:
        print (is_artwork_available)














