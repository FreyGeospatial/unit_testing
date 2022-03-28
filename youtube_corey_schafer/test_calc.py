import os
import unittest

# https://www.youtube.com/watch?v=6tNS--WetLI

#os.getcwd()
#os.chdir("youtube_corey_schafer")

import calc # can import it like this since it's in the same directory


class TestCalc(unittest.TestCase): # when creating a class, we can inherit methods from other classes
                                    # so this method is kinda like a child class of the larger
                                    # unittest.TestCase parent class
    def test_add(self): # MUST have prefix test_ ...followed by the method describing what we wanna test
        result = calc.add(10, 5)
        self.assertEqual(result, 15)
        
  ###################################################################   
    def add_test(self): # example of test that would NOT run due to \
                        # improper prefix (does not start with "test_").
                        # See terminal output- this will not show up
        result = calc.add(10, 5)
        self.assertEqual(result, 15)
        
  ###################################################################
    
    def test_addFail(self): # example of failed test
        result = calc.add(10, 5)
        self.assertEqual(result, 999)
        
 ####################################################################
 
    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        
  ####################################################################  
    
    def test_divide(self):
        self.assertEqual(calc.divide(5, 2), 2.5)
        self.assertRaises(ValueError, calc.divide, 10, 0) # tests to see if our value error exception is raised
        
    
# we could run this test using just
# python -m unittest test_calc.py
# the "-m" command imports a module or package
# for you, and then runs the package(?) as a 
# script. See here: https://stackoverflow.com/questions/22241420/execution-of-python-code-with-m-option-or-not

# to run the test using $ python test_calc.py,
# or even from within our editor (Spyder in my case),
# we need to perform an initial code set up- see below:

# if we run this module directly, then run the code
# within the conditional, which is unittest.main().
# AND... unittest.main() will run all of our tests.
# After inserting this code, $ python test_calc.py
# should run our test just fine. And it does!
if __name__ == '__main__':
    unittest.main() 