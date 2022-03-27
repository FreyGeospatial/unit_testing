import os
import unittest

#os.getcwd()
#os.chdir("youtube_corey_schafer")

import calc # can import it like this since it's in the same directory


class TestCalc(unittest.TestCase): # when creating a class, we can inherit methods from other classes
                                    # so this method is kinda like a child class of the larger
                                    # unittest.TestCase parent class
    def test_add(self): # MUST have prefix test_ ...followed by the method describing what we wanna test
        result = calc.add(10, 5)
        self.assertEqual(result, 15)
    
