from App.Test.cashback import cashback

def test_cashback_under_limit():
    result = cashback(1_000)

    assert 50 == result
