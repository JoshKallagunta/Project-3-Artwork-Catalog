from peewee import *
from artworkCatalog import (ArtistData,ArtworkData)
import dbArtwork 

def adding_artist_from_user():
    try:
        artistName = input('Enter an artist''s name: ')
        artistEmail = input('Enter the artist''s email address: ')
        artworkCatalog.ArtistData(artistName, artistEmail)
    except:
        print("This Artist has already been entered")

