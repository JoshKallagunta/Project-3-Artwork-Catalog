from peewee import *
from artworkCatalog import (ArtistData,ArtworkData)
import dbArtwork 
import inputAddArtwork


#While true loop using if/elif statements for the UI menu so that I dont need to import ui
#based off of reading_list menu
def main():

    while True:
        user_input_choice = create_menu()
        dbArtwork.create_table()

        if user_input_choice == 1:
            inputAddArtwork.adding_artist_from_user()
        elif user_input_choice == 2:
            inputAddArtwork.adding_new_artwrk_from_user()
        elif user_input_choice == 3:
            inputAddArtwork.deleting_artwork_from_user()
        elif user_input_choice == 4:
            inputAddArtwork.search_artwork_from_user()

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


if __name__ == '__main__':
    main()








