from api import YaUploader
import unittest


class TestCreatePath(unittest.TestCase):

    def test_create_path_1(self):
        self.assertEqual(YaUploader.create_path('File'), 201)

    def test_create_path_2(self):
        self.assertEqual(YaUploader.create_path('File2'), 204)

    def test_create_path_3(self):
        self.assertEqual(YaUploader.create_path('File3'), 500)