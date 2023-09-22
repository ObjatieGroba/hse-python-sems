import unittest
import test_module


class TestTestTestMethods(unittest.TestCase):
    def tearDown(self) -> None:
        pass

    def setUp(self) -> None:
        pass

    def test_simple(self):
        a = test_module.ToBeTested(1)
        self.assertEqual(a.data, 1)

    def test_not_simple(self):
        self.assertEqual(2, 1)

    def test_skipped(self):
        raise unittest.SkipTest

    def not_test_simple(self):
        print(1)


if __name__ == '__main__':
    unittest.main()
