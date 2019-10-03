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

def adding_new_artwrk_from_user():
    try:
        album_artist = input('Enter the artist''s name for the album: ')
        album_name = input('Enter the name of the album: ')
        album_price = float(input('Enter the price of the album: '))
        album_stock = bool(input('Has the album been sold? (NO = True, YES = False): '))
        artworkCatalog.ArtworkData(album_artist, album_name, album_price, album_stock)
    except:
        print('This artwork already exixsts, please enter a unique one. ')

def deleting_artwork_from_user():
    try:
        album_name = input('Enter the artwork name you want to delete: ')
        artworkCatalog.ArtworkData.deleting_artwork(album_name)
    except:
        print('Please enter the artwork name again: ')





