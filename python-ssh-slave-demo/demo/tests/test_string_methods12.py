import unittest

class TestStringMethods12(unittest.TestCase):

    def test_upper12(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper12(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split12(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
