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

    tree = None
    reply = None
    code = None
    desc = None
    data = None

    def __init__(self, tree):
        self.tree = tree

        self.reply = self.tree.reply
        self.code = self.reply.code
        self.desc = self.reply.desc
        self.data = self.reply.data

    def __str__(self):
        return lxml.etree.tostring(self.tree, pretty_print=True)
