# coding=utf-8

"""
Functionality useful in all the modules.
"""

import lxml


class Module(object):
    """Superclass for all module classes."""

    parent = None
    e = lxml.objectify.ElementMaker(annotate=False)

    def with_parent(self, parent):
        """Set our parent to the given OpenProvider instance."""
        self.parent = parent
        return self

    def request(self, tree, **kwargs):
        """Alias for OpenProvider.request."""
        return self.parent.request(tree, **kwargs)
