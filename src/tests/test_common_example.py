import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from common import example

def test_something():
    assert True, "A comment to show if the test fails"

	
def test_common_example_hello_world():
    assert example.hello_world() == "Hello World", "The Hello World strings should be the same"
	
#def test_that_fails():
#    assert False, "We expected this to fail"
