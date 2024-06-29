#!/usr/bin/python3
""" defines unittest for review class """
import os
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ review for test class """
    def test_user_id(self):
        """ tests review user_id attributes"""
        new = self.value()
        self.assertEqual(type(new.user_id), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_text(self):
        """ tests review text attributes"""
        new = self.value()
        self.assertEqual(type(new.text), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))
        
    def __init__(self, *args, **kwargs):
        """ review class initilization"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ tests review place_id attributes"""
        new = self.value()
        self.assertEqual(type(new.place_id), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))
