from bank import vaule

def test_здравствуйте():
    assert vaule("Здравствуйте, Боб!") == 0

def test_здрасти():
    assert vaule("Здрасти, Боб!") == 20

def test_hello():
    assert vaule("Hello, Harry!") == 100
