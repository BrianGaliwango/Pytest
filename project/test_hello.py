from hello import more_hello, more_goodbye


def test_more_hello():
    assert "Hello, world!" == more_hello()


def test_more_goodbye():
    assert "Good bye" == more_goodbye()
