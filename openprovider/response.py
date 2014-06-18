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
        if isinstance(source, six.string_types):
            # The source looks stringy, parse it
            self.tree = lxml.objectify.fromstring(source)
        else:
            # Not stringy, probably file-like, let lxml handle it
            self.tree = lxml.objectify.parse(source).getroot()

        self.reply = self.tree.reply
        self.code = self.reply.code
        self.desc = self.reply.desc
        self.data = self.reply.data

    def __str__(self):
        return lxml.etree.tostring(self.tree, pretty_print=True)
