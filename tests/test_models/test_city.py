#!/usr/bin/python3
"""defines unittest for city class """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ test for city class """

    def __init__(self, *args, **kwargs):
        """ intializes class test """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ testin type for state id """
        new = self.value()
        self.assertEqual(type(new.state_id), str)
        if 
        os.getenv('HBNB_TYPE_STORAGE') != 'db'
    else
    type(None))

    def test_name(self):
        """ name type test """
        new = self.value()
        self.assertEqual(type(new.name), str)
        if os.getenv('HBNB_TYPE_STORAGE') != 'db'
        else type(None))
