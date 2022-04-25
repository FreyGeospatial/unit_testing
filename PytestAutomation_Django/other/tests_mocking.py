# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 09:26:14 2022

@author: jordan.frey
"""

from unittest.mock import patch, MagicMock
from utils import foo

# this mockup will "mock out" the execution of db_write and replace it's return value with a val of 42
# patching replace the return value of a specific function (e.g., utils.db_write())
# replace the occurance of the function or object we are patching with an object of our choice
@patch("utils.db_write", MagicMock(return_value=42)) # first argument is the path of the function being mocked (package.module.ClassName)
def test_mock_out_db_write():                       # we are telling the test to replace return val of db_write with 42, from print statement
    assert foo() == 42                              # ***REMEMBER!*** the path is the location where the function is USED, NOT DEFINED!