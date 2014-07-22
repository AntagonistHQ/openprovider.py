# coding=utf-8

"""
Contains a Response class for representing responses from the API.
"""

import lxml
import lxml.objectify


class Response(object):
    """
    Represents a response from OpenProvider. Unwraps the code, desc and data
    fields in the response to attributes.
    """

    def __init__(self, tree):
        self.tree = tree

        self.reply = self.tree.reply
        self.code = self.tree.reply.code
        self.desc = self.tree.reply.desc
        self.data = self.tree.reply.data

        try:
            self.array = self.tree.reply.array[0]
        except AttributeError:
            self.array = []

    def as_model(self, klass):
        """Turns a model-style response into a single model instance."""
        return klass(self.data)

    def as_models(self, klass):
        """Turns an array-style response into a list of models."""
        try:
            return [klass(mod) for mod in self.tree.reply.data.results.array[0].item]
        except AttributeError:
            return []

    def __str__(self):
        return lxml.etree.tostring(self.tree, pretty_print=True)

    def dump(self):
        return lxml.etree.dump(self.tree)
