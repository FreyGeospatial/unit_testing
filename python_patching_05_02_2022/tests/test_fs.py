from python_patching_05_02_2022 import fs
import unittest
from unittest import mock

class TestExamples(unittest.TestCase):
    @mock.patch('python_patching_05_02_2022.fs.check_output', return_value=b'foo\nbar\n')
    def test_print_contents_of_cwd_success(self, mock_check_output): # arbitrary mock name, "mock_check_output". Could be literally anything
        actual_result = fs.print_content_of_cwd() # we are patching a function that exists inside of fs.print_content_of_cwd(), and giving it a new value

        expected_directory = b'foo'
        self.assertIn(expected_directory, actual_result)
