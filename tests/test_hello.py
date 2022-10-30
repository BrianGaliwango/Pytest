from hello import more_hello, more_goodbye, how_many


def test_more_hello():
    assert "Hello, world!" == more_hello()


def test_more_goodbye():
    assert "Good bye" == more_goodbye()
    
def test_how_many():
    assert "How many are you?" == how_many()    
 
