from unittest import TestCase
from main import generator


class TestPageRequester(TestCase):
    def test_len_password(self):
        self.password = generator()
        expected_result = 18
        self.assertAlmostEqual(len(self.password), expected_result, delta=6)

