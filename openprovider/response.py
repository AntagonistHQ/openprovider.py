# coding=utf-8

import six
import lxml
import lxml.objectify


class Response(object):
    tree = None
    reply = None
    code = None
    desc = None
    data = None

    def __init__(self, source):
        self.tree = lxml.objectify.fromstring(source)

        self.reply = self.tree.reply
        self.code = self.reply.code
        self.desc = self.reply.desc
        self.data = self.reply.data

    def __str__(self):
        return lxml.etree.tostring(self.tree, pretty_print=True)
