import unittest
from unittest.mock import patch
from meClass.mock_learn import num


class MyTestCase(unittest.TestCase):

    @patch("meClass.mock_learn.num.multiply", autospec=True)
    def test_add_and_multiply2(self, mock_multiply):
        x = 3
        y = 5
        mock_multiply.return_value = 15

        addition, multiple = num.add_and_multiply(x, y)
        # print(num.multiply(x, y))
        # assert num.multiply(x, y) == 15
        # mul = num.multiply(x, y)

        mock_multiply.assert_called_with(3, 5)

        self.assertEqual(8, addition)
        self.assertEqual(15, multiple)


if __name__ == "__main__":
    unittest.main()