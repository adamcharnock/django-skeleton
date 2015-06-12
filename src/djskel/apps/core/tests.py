from django.test import TestCase

class AnimalTestCase(TestCase):
    def setUp(self):
        pass

    def test_example(self):
        self.assertEqual(0b100, 4)