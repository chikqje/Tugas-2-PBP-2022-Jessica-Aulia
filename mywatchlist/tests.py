import json
from lib2to3.pgen2.token import EQUAL
from xml.dom import xmlbuilder
from django.test import TestCase
from django.http import HttpResponse
from django.test import Client

# Create your tests here.

class WatchListTest(TestCase):
    # def setup(html):
    # def setup(self):
    #     self.html = "/mywatchlist/html/"
    #     self.xml  = "/mywatchlist/xml/"
    #     self.json = "/mywatchlist/json/"

    def test_html(self):
        c = Client().get("/mywatchlist/html/")
        print("Method: test_html.")
        self.assertEqual(c.status_code,200)

    def test_xml(self):
        c = Client().get("/mywatchlist/xml/")
        print("Method: test_xml.")
        self.assertEqual(c.status_code,200)

    def test_json(self):
        c = Client().get("/mywatchlist/json/")
        print("Method: test_json.")
        self.assertEqual(c.status_code,200)