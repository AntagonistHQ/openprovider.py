from tests import betamaxed


@betamaxed
def test_search_extension(api):
    """Search should return something sensible."""
    r = api.extensions.search_extension(with_usage_count=True)
    assert r[0].usage_count is not None


@betamaxed
def test_retrieve_extension(api):
    """Retrieve should return a proper Extension."""
    r = api.extensions.retrieve_extension("nl", with_description=True)
    assert r.description is not None
