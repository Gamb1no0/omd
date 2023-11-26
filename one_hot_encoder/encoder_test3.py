import unittest
from one_hot_encoder import fit_transform


class TestFT(unittest.TestCase):
    """Test fit_transform with unittest"""
    def test_ft1(self):
        """Test 1"""
        cities = ['London', 'New York','London', 'Moscow']
        exp_transformed_cities = [
            ('London', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('London', [0, 0, 1]),
            ('Moscow', [1, 0, 0]),
        ]
        transformed_cities = fit_transform(cities)

        self.assertEqual(exp_transformed_cities, transformed_cities)

    def test_ft2(self):
        """Test 2"""
        tf_obj = fit_transform(['Tree', 'Sun'])

        self.assertNotEqual(tf_obj[0][1], tf_obj[1][1])

    def test_ft3(self):
        """Test 3"""
        tf_obj = fit_transform(['Three', 'Two', 'One'])
        self.assertIsInstance(tf_obj, list)

    def test_ft4(self):
        """Test 4"""
        tf_obj = fit_transform(['Three', 'Two', 'One'])
        self.assertTrue(len(tf_obj), 3)

    def test_ft5(self):
        """Test 5"""
        with self.assertRaises(TypeError) as exc:
            fit_transform([[0, 3], 'Sun'])
        self.assertEqual(str(exc.exception), 'unhashable type: \'list\'')


if __name__ == '__main__':
    unittest.main()