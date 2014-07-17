# coding=utf-8

from openprovider.modules import common
from openprovider.models import Extension


class ExtensionModule(common.Module):
    """Bindings to API methods in the extension module."""

    def search_extension(self, limit=100, offset=0, **kw):
        """Search the list of available extensions."""

        e = self.e
        response = self.request(e.searchExtensionRequest(
            e.limit(limit),
            e.offset(offset),
            e.withDescription(int(kw.get('with_description', 0))),
            e.withPrice(int(kw.get('with_price', 0))),
            e.withUsageCount(int(kw.get('with_usage_count', 0))),
        ))
        return response.as_models(Extension)

    def retrieve_extension(self, name, **kw):
        """Retrieve details on a single extension."""

        e = self.e
        response = self.request(self.e.retrieveExtensionRequest(
            self.e.name(name),
            e.withDescription(int(kw.get('with_description', 0))),
            e.withPrice(int(kw.get('with_price', 0))),
            e.withUsageCount(int(kw.get('with_usage_count', 0))),
        ))

        return response.as_model(Extension)
