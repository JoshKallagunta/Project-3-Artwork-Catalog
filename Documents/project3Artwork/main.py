from peewee import *
from artworkCatalog import (ArtistData,ArtworkData)
import dbArtwork 
import inputAddArtwork

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





    return user_input_choice



def create_menu():
    print('Add a new artist ')
    print('Add a new artwork ')
    print('Delete an artwork ')

    get_user_choice = int(input('Please enter your choice: '))

    return get_user_choice


if __name__ == '__main__':
    main()








