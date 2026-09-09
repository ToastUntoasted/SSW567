import unittest
import classify_triangle

class TestTriangles(unittest.TestCase):
    def test_invalid_input(self):
        self.assertEqual(classify_triangle.classify_triangle(-1, 2, 3), ['InvalidInput', 'NotRight'])
        self.assertEqual(classify_triangle.classify_triangle(0, 2, 3), ['InvalidInput', 'NotRight'])
        self.assertEqual(classify_triangle.classify_triangle(1, -2, 3), ['InvalidInput', 'NotRight'])
        self.assertEqual(classify_triangle.classify_triangle(1, 2, -3), ['InvalidInput', 'NotRight'])

    def test_not_a_triangle(self):
        self.assertEqual(classify_triangle.classify_triangle(1, 2, 3), ['NotATriangle', 'NotRight'])
        self.assertEqual(classify_triangle.classify_triangle(5, 1, 1), ['NotATriangle', 'NotRight'])

    def test_equilateral(self):
        self.assertEqual(classify_triangle.classify_triangle(3, 3, 3), ['Equilateral', 'NotRight'])

    def test_isosceles(self):
        self.assertEqual(classify_triangle.classify_triangle(3, 3, 4), ['Isosceles', 'NotRight'])
        self.assertEqual(classify_triangle.classify_triangle(4, 3, 3), ['Isosceles', 'NotRight'])
        self.assertEqual(classify_triangle.classify_triangle(3, 4, 3), ['Isosceles', 'NotRight'])

    def test_scalene(self):
        self.assertEqual(classify_triangle.classify_triangle(3, 4, 5), ['Scalene', 'Right'])
        self.assertEqual(classify_triangle.classify_triangle(5, 12, 13), ['Scalene', 'Right'])
        self.assertEqual(classify_triangle.classify_triangle(7, 24, 25), ['Scalene', 'Right'])


if __name__ == '__main__':
    unittest.main()