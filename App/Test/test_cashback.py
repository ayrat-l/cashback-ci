from App.Test.cashback import cashback

def test_cashback_under_limit():
    result = cashback(1_000)

    assert 50 == result

def cashback_over_limit():
    result = cashback(1_000_000)

    assert 3_000 == result
