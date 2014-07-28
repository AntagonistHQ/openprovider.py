# coding=utf-8

from openprovider.modules import E, common
from openprovider.models import Extension


class ExtensionModule(common.Module):
    """Bindings to API methods in the extension module."""

    def search_extension(self, limit=100, offset=0, **kw):
        """Search the list of available extensions."""

        response = self.request(E.searchExtensionRequest(
            E.limit(limit),
            E.offset(offset),
            E.withDescription(int(kw.get('with_description', 0))),
            E.withPrice(int(kw.get('with_price', 0))),
            E.withUsageCount(int(kw.get('with_usage_count', 0))),
        ))
        return response.as_models(Extension)

    def retrieve_extension(self, name, **kw):
        """Retrieve details on a single extension."""

        response = self.request(E.retrieveExtensionRequest(
            E.name(name),
            E.withDescription(int(kw.get('with_description', 0))),
            E.withPrice(int(kw.get('with_price', 0))),
            E.withUsageCount(int(kw.get('with_usage_count', 0))),
        ))

        return response.as_model(Extension)
