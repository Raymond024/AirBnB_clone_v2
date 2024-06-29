#!/usr/bin/python3
""" defines unitest for or amenity class """
import os
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ test for ammenity class  """

    def __init__(self, *args, **kwargs):
        """ intializes test class """

        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ name type test """
        new = self.value()
        self.assertEqual(type(new.name), str)

    if
        os.getenv('HBNB_TYPE_STORAGE') != 'db'
    else
                         type(None))
