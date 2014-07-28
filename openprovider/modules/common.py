# coding=utf-8

"""
Functionality useful in all the modules.
"""


class Module(object):
    """Superclass for all module classes."""

    def __init__(self, parent=None):
        self.parent = parent

    def request(self, tree, **kwargs):
        """Alias for OpenProvider.request."""
        return self.parent.request(tree, **kwargs)
