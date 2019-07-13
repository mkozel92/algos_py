import unittest

from dynamic_programming.longest_common_subsequence import longest_common_subsequence, longest_common_subsequence_rec


class TestLongestCommonSubsequence(unittest.TestCase):

    def test_lcs(self):
        first_string = "some string here"
        second_string = "some other string here"
        third_string = "a bit different one"

        mem = {}
        self.assertEqual(longest_common_subsequence(first_string, second_string),
                         longest_common_subsequence_rec(first_string, second_string,
                                                        len(first_string) - 1,
                                                        len(second_string) - 1,
                                                        mem))

        mem = {}
        self.assertEqual(longest_common_subsequence(first_string, third_string),
                         longest_common_subsequence_rec(first_string, third_string,
                                                        len(first_string) - 1,
                                                        len(third_string) - 1,
                                                        mem))

        mem = {}
        self.assertEqual(longest_common_subsequence(third_string, second_string),
                         longest_common_subsequence_rec(third_string, second_string,
                                                        len(third_string) - 1,
                                                        len(second_string) - 1,
                                                        mem))
