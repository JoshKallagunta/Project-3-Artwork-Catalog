from unittest import TestCase
from peewee import *
from main import (main,create_menu)
from artworkCatalog import (ArtistData,ArtworkData)
import dbArtwork
from dbConfig import database_path

#Based this testing model off of:
#http://docs.peewee-orm.com/en/latest/peewee/database.html#testing-peewee-applications

test_db = SqliteDatabase(database_path)

test_tables = [ArtistData , ArtworkData]

class Test_Artwork_Catalog(TestCase):
    def setUp(self):

        test_db.bind(test_tables, bind_refs= False, bind_backrefs= False)

        test_db.connect()
        test_db.create_tables(test_tables)

    def drop_tables_for_testing(self):
        test_db.drop_tables(test_tables)

#Adding artist info for testing purposes
    def add_test_artist(self):
        self.add_artist_data_1 = ArtistData(artistName = 'Josh Kalla', artistEmail = 'josh.kalla@gmail.com')
        self.add_artist_data_2 = ArtistData(artistName = 'Jake Johnson', artistEmail = 'jake.johnson@gmail.com')

        self.add_artist_data_1.save()
        self.add_artist_data_2.save()

#Adding an artwork for testing purposes
    def add_test_artwork(self):
        self.add_artwork_1 = ArtworkData(name_of_artist = 'Josh Kalla', name_of_artwork = 'testArtwork', price_of_artwork = '10', availability_of_artwork = 'True')
        self.add_artwork_1.save()

#Testing the an addition to the ArtistData table
    def test_add_artist(self, dbArtwork):
        self.new_artist = ArtistData(artistName = 'James Kalla', artistEmail = 'james.kalla@gmail.com')
        self.new_artist.save()
        self.assertTrue(dbArtwork.adding_artist(self.new_artist))
        self.assertEqual(1, dbArtwork.artist_count())

#Testing the additon of an artwork to the ArtWork table
    def test_add_artwork(self, dbArtwork):
        self.new_artwork = ArtworkData(name_of_artist = 'James Kalla', name_of_artwork = 'James Album', price_of_artwork = '12', availability_of_artwork = 'True')
        self.new_artist.save()
        self.assertTrue(dbArtwork.adding_artwork(self.new_artwork))

    





