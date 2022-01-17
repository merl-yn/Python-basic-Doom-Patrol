import unittest
import functions_for_testing as fft


class FunctionsTest(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(fft.suma(4, 5), 9)
        self.assertNotEqual(fft.suma(3, 4), 4)
        self.assertEqual(fft.suma(10, 15), 25)
        self.assertEqual(fft.suma(100, 150), 250)

    def test_dif(self):
        self.assertEqual(fft.dif(5, 1), 4)
        self.assertEqual(fft.dif(15, 3), 12)
        self.assertEqual(fft.dif(150, 250), -100)

    def test_multiple(self):
        self.assertEqual(fft.multiple(5, 2), 10)
        self.assertEqual(fft.multiple(25, 4), 100)

# added unittest for div function
    def test_div(self):
        self.assertEqual(fft.div(10, 5), 2)
        self.assertEqual(fft.div(300, 150), 2)
        self.assertEqual(fft.div(117334, 578), 203)
        self.assertNotEqual(fft.div(14, 7), 8)
