import unittest

from misc.replace_whitespaces import replace_whitespaces


class TestReplaceWhitespaces(unittest.TestCase):

    def setUp(self) -> None:
        self.some_string = list('this is a test      ')
        self.correctly_replaced = ['t', 'h', 'i', 's', '%', '2', '0', 'i', 's', '%',
                                   '2', '0', 'a', '%', '2', '0', 't', 'e', 's', 't']

    def test_replace(self):
        replace_whitespaces(self.some_string)
        self.assertEqual(self.some_string, self.correctly_replaced)