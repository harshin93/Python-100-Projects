'''
Credit Card Validator - Takes in a credit card number from a common credit card vendor
(Visa, MasterCard, American Express, Discover) and validates it to make sure that it
is a valid number
'''


def validator(valid_card):
    '''
    Function will take the last digit of the card number and match it with card vendor
    '''
    last_digit = int(valid_card[-1])
    ans = "invalid"
    if last_digit == 1:
        ans = "visa"
    elif last_digit == 2:
        ans = "master_card"
    elif last_digit == 3:
        ans = "discover"
    elif last_digit == 4:
        ans = "amex"
    return ans


def test_validator():
    '''
    test function will test two possible test cases to check
    '''
    cards = [("321654646465465465", "invalid"), ("6546546546466541", "visa")]
    for card in cards:
        assert validator(card[0]) == card[1]


if __name__ == "__main__":
    test_validator()
