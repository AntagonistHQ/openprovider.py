from . import betamaxed


@betamaxed
def test_customer_search(api):
    r = api.customers.search_customer()
    assert len(r) >= 1


@betamaxed
def test_customer_search_non_existing(api):
    r = api.customers.search_customer(email_pattern="doesntexist.com")
    assert len(r) == 0
