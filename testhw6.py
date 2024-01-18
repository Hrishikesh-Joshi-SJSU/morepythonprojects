import unittest
import homework6
from copy import deepcopy

class MostWordsTestCase(unittest.TestCase):
    def setUp(self):
        """Creating strings for test methods"""
        self.one_arg_str = "Hello world"
        self.one_arg = "Bye bye world"
        self.two_arg = "One small step for man"
        self.three_arg = "To be or not to be that is the question"
        self.four_arg  = "Peace"
    def test_without_arguments(self):

        self.assertIsNone(homework6.most_words())
        # checks that the most_words() without an argument returns None
    def test_with_one_argument(self):

        self.assertEqual(self.one_arg_str, homework6.most_words(
            self.one_arg_str))

    def test_with_many_arguments(self):
        self.assertEqual(self.three_arg, homework6.most_words(
        self.one_arg, self.two_arg, self.three_arg, self.four_arg))
class FinalGradeTestCase(unittest.TestCase):
    def setUp(self):
        """Creating dictionaries for the test methods"""
        self.empty = dict()
        self.nonempty = {"Alpha": 100, "Beta": 95, "Gamma": 45, "Delta":
            46, "Zeta": 0, "Iota": 1}
        self.nonempty_copy = {key: self.nonempty[key] for key in
                              self.nonempty}

        self.expected_default_output = {"Alpha": 101, "Beta": 96,
                                    "Gamma": 46, "Delta": 47,
                    "Zeta": 1, "Iota": 2}
        self.expected_nonempty_output = {"Alpha": 102, "Beta": 97,
                                   "Gamma": 47, "Delta": 48,
                                   "Zeta": 2, "Iota": 3}
        self.default = {key: self.nonempty[key] for key in
                              self.nonempty}
        self.default_copy = deepcopy(self.default)
        self.expected_default_output = {"Alpha": 101, "Beta": 96,
                                        "Gamma": 46, "Delta": 47,
                                        "Zeta": 1, "Iota": 2}
    def test_empty_dictionary(self):
        self.assertFalse(homework6.final_grade(self.empty))
        # checks that None is returned by final_grade with no argument
        self.assertFalse(homework6.final_grade(self.empty) is
                         self.empty)
        ''' checks that the empty dictionary returned is not the same 
        as the argument dictionary'''
    def test_nonempty_dictionary(self):
        self.assertEqual(homework6.final_grade(self.nonempty, 2),
                         self.expected_nonempty_output)
        '''checks that the dictionary returned is the same as the 
        expected return value. checks that the dictionary put as an
        argument is not changed'''
        self.assertEqual(self.nonempty, self.nonempty_copy)
    def test_default_argument(self):
        self.assertEqual(homework6.final_grade(self.default),
                         self.expected_default_output)
        self.assertEqual(self.default, self.default_copy)
        '''checks that the dictionary returned is the same as the 
               expected return value. checks that the dictionary put as 
               an argument is not changed'''
if __name__ == '__main__':
    unittest.main()
