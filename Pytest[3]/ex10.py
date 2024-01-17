

def test_length_input_phrase():
    pharase = input("Please, enter your phrases: ")
    assert len(pharase) <= 15, 'Your Pharase have over 15 simbols'