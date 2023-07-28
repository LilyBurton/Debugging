from lib.debugging_hello import *
def test_debugging_hello():
    result = say_hello("Lily")
    assert result == "hello Lily"