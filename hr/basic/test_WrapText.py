from unittest import TestCase

from hr.basic import WrapText


class Test(TestCase):
    def test_wrap(self):
        ans=WrapText.wrap('ABCDEFGHIJKLIMNOQRSTUVWXYZ',4)
        print(ans)



