import unittest

from ..task import print_common_chars


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_add(self):
        res = print_common_chars("ababca", "cbbbc")
        self.assertEqual(res, "bbc", msg="solution is = {}".format(res))
