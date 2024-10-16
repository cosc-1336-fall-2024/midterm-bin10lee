#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from question_b.question_b import get_fahrenheit
from src.question_a.question_a import test_config, use_local_variable

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())
        
    def test_local_variable(self):
        num=100
        use_local_variable(num)
        self.assertNotEqual(100,num)

    def test_get_fahrenheit(self):
        self.assertEqual (32, get_fahrenheit(0))
        self.assertEqual (41, get_fahrenheit(5))
        self.assertEqual (50, get_fahrenheit(10))


