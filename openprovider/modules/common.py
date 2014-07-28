# coding=utf-8

"""
Functionality useful in all the modules.
"""

import lxml


class Module(object):
    """Superclass for all module classes."""

    e = lxml.objectify.ElementMaker(annotate=False)

    def __init__(self, parent=None):
        self.parent = parent

    def request(self, tree, **kwargs):
        """Alias for OpenProvider.request."""
        return self.parent.request(tree, **kwargs)
