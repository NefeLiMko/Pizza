import unittest
from pizzabot import *


class ValidateArgs(unittest.TestCase):

    def test_valid_args_fail(self):
        args = ["1", "2"]
        with self.assertRaises(SystemExit):
            valid_args(args)


class ValidateGrid(unittest.TestCase):

    def test_invalid_grid_fail_letters(self):
        size = "fxf"
        with self.assertRaises(SystemExit):
            valid_grid(size)

    def test_invalid_grid_fail_zero(self):
        size = "0x0"
        with self.assertRaises(SystemExit):
            valid_grid(size)

    def test_invalid_grid_fail_single_zero(self):
        size = "0x5"
        with self.assertRaises(SystemExit):
            valid_grid(size)


class ValidateLocation(unittest.TestCase):

    def test_invalid_location_brackets(self):
        size = "5x5"
        locations = "(5,5"
        with self.assertRaises(SystemExit):
            valid_locations(size, locations)

    def test_invalid_location_brackets_2(self):
        size = "5x5"
        locations = "5,5)"
        with self.assertRaises(SystemExit):
            valid_locations(size, locations)
            print('alushta')

    def test_invalid_location_empty(self):
        size = "5x5"
        locations = "(,5)"
        with self.assertRaises(SystemExit):
            valid_locations(size, locations)

    def test_out_of_delivery_area(self):
        size = "5x5"
        locations = "(1,7)"
        with self.assertRaises(SystemExit):
            valid_locations(size, locations)


class TestDelivery(unittest.TestCase):

    def test_delivery_success(self):
        locations = ['(5,5)']
        self.assertEqual(delivery(locations), "EEEEENNNNND")

    def test_delivery_success_2(self):
        locations = ['(1,3)', '(4,4)']
        self.assertEqual(delivery(locations), "ENNNDEEEND")

    def test_delivery_success_3(self):
        locations = ['(0,0)', '(1,3)', '(4,4)', '(4,2)', '(4,2)', '(0,1)', '(3,2)', '(2,3)', '(4,1)']
        self.assertEqual(delivery(locations), "DENNNDEEENDSSDDWWWWSDEEENDWNDEESSD")

    def test_delivery_success_4(self):
        locations = ['(1,3)', '(1,3)']
        self.assertEqual(delivery(locations), "ENNNDD")


if __name__ == '__main__':
    unittest.main()
