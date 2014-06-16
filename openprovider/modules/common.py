# coding=utf-8


class Module(object):
    parent = None

    def with_parent(self, parent):
        self.parent = parent
        return self
