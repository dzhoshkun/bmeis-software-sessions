import unittest


class TestExample(unittest.TestCase):
    """
    This is an example template of what at TestCase subclass would look like. We use setUp() to create test data when
    the tests start, and tearDown() to cleanup when the tests are done. Individual unit tests are defined as methods
    starting with "test_". You can run this in PyCharm by opening the file then in the menu select "Run" followed by
    "Run 'Unitests for..." or pressing Shift+F10. 
    """

    def setUp(self):
        """This is not a test but a method for setting up data for tests."""
        self.someData = "data goes here"

    def test_thing(self):
        self.assertTrue(True)

    def test_other_thing(self):
        self.assertFalse(False)

    def test_yet_another_thing(self):
        self.assertEqual(1, 1)

    def test_with_data(self):
        self.assertFalse(self.someData == "not that string")
