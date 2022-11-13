from unittest import TestCase

from hr.basic import SubStringTest


class Test(TestCase):
    def test_count_substring(self):
        ans = SubStringTest.count_substring('ABCDCDC', 'CDC')
        self.assertEqual(ans, 2)


class Test1(TestCase):
    def test_count_substring(self):
        ans = SubStringTest.count_substring('I am an Indian, by birth.', 'Birth')
        self.assertEqual(ans, 0)
