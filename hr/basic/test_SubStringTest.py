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

    def test_count_substring2(self):
        ans = SubStringTest.count_substring('ThIsisCoNfUsInG', 'is')
        self.assertEqual(ans, 1)

    def test_count_substring2(self):
        ans = SubStringTest.count_substring('AbBaAbBaAbBa', 'Ab')
        self.assertEqual(ans, 3)



