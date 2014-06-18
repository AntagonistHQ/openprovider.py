# coding=utf-8

import lxml


class Module(object):
    parent = None
    e = lxml.objectify.ElementMaker(annotate=False)

    def with_parent(self, parent):
        self.parent = parent
        return self

    def request(self, tree, **kwargs):
        return self.parent.request(tree, **kwargs)
