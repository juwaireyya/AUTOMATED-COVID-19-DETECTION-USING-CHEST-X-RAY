 
import os 
import io
import unittest
from flask import Flask
#from flask_testing import TestCase
from test import app
from io import BytesIO
from django.test import TestCase 



class TestCase(unittest.TestCase):
    def test_home(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
    ## Ensure that home page load
    def test(self):
        tester = app.test_client(self)
        response = tester.get('/message', content_type='html/text')
        self.assertTrue(b'Contact Us'in response.data)
    ## Ensure that predict page load
    def test_Yes_No_page(self):
        tester = app.test_client(self)
        response = tester.get('/B2', content_type='html/text')
        self.assertIn(b'Yes', response.data)
    ## Ensure that  folderImg page load
    def test_I_am_SoftWare(self):
        tester = app.test_client(self)
        response = tester.get('/folderImg', content_type='html/text')
        self.assertIn(b'Rebuild', response.data)
    ## Ensure that  uplode page load
    def test_I_am_Radiologist(self):
        tester = app.test_client(self)
        response = tester.get('/upload', content_type='html/text')
        self.assertIn(b'Import Image', response.data)
    ## Ensure that  sucssuful page load
    def test_sucssuful_page(self):
        tester = app.test_client(self)
        response = tester.get('/B6', content_type='html/text')
        self.assertIn(b'OK', response.data)

    #@app.route("/uploader", methods = ['GET', 'POST'])
    def uploader(self):
       if request.method == 'POST':
           f = request.files['file']
           if f.filename == '':
              resp = jsonify({'message' : 'No file selected for uploading'})
              resp.status_code = 400
              self.assertIn(b'OK', resp.data)
           else :
          	  return print ("yes")

    
if __name__ == '__main__':
    unittest.main()
