from peewee import *
from artworkCatalog import *
import dbArtwork 
import inputAddArtwork

#Used reading_list main as reference: https://github.com/claraj/hello_sqlite_python/blob/master/peewee_orm/reading_list/main.py


#While true loop using if/elif statements for the UI menu so that I dont need to import ui
#based off of reading_list menu
def main():

    while True:
        user_input_choice = create_menu()
        dbArtwork.create_table()

        if user_input_choice == 1:
            adding_artist_from_user()
        elif user_input_choice == 2:
            adding_new_artwrk_from_user()
        elif user_input_choice == 3:
            deleting_artwork_from_user()
        elif user_input_choice == 4:
            search_artwork_from_user()

    return user_input_choice


#Menu that the user sees, gets input based off the number, returns the user choice so that the 
#main method will execute what the user chose 
def create_menu():
    print('1: Add a new artist ')
    print('2: Add a new artwork ')
    print('3: Delete an artwork ')
    print('4: Search for an artwork')

    get_user_choice = int(input('Please enter your choice: '))

    return get_user_choice



#Method for adding an artist, getting user input, and saving to the ArtistData table
#called in main.py class for the UI 
def adding_artist_from_user():
    try:
        artistName = input('Enter an artist''s name: ')
        artistEmail = input('Enter the artist''s email address: ')
        artworkCatalog.ArtistData(artistName, artistEmail)
    except:
        print("This Artist has already been entered")

#Method for adding an artwork, getting user input, saving to ArtworkData table 
#called in main.py class for the UI 
def adding_new_artwrk_from_user():
    try:
        album_artist = input('Enter the artist''s name for the album: ')
        album_name = input('Enter the name of the album: ')
        album_price = float(input('Enter the price of the album: '))
        album_stock = bool(input('Has the album been sold? (NO = True, YES = False): '))
        artworkCatalog.ArtworkData(album_artist, album_name, album_price, album_stock)
    except:
        print('This artwork already exixsts, please enter a unique one. ')

#Method for deleting an artwork, getting the user input for which artwork to be deleted
#Deleted from the ArtworkData table
#called in main.py class for the UI 
def deleting_artwork_from_user():
    try:
        album_name = input('Enter the artwork name you want to delete: ')
        artworkCatalog.ArtworkData.deleting_artwork(album_name)
    except:
        print('Please enter the artwork name again: ')

#Method for searching for an artwork using the artist's name
#searches the Artwork table
#called in main.py class for the UI 
def search_artwork_from_user():
    try:
        artwork_artist_name_search = input('Enter the artist name you would like yo search by: ')
        artworkCatalog.ArtworkData.search_for_artwork_available(artwork_artist_name_search)
    except:
        print('Sorry, couldn''t find artist, please enter another')


if __name__ == '__main__':
    main()








