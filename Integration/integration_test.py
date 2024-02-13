import details

def test_is_valid_email():
    # assert details.is_valid_email("testmyemail.com")

    assert details.is_valid_email("testmyemail@gmail.com")

def test_is_valid_phone_number():
    # assert details.is_valid_phone_number(+17898527869)
    assert details.is_valid_phone_number(+78985278999888889969)
