# -*- coding: utf-8 -*-


class Tentacle(object):

    def __init__(self, elements):
        self.elements = elements

    def check(self):
        for element in self.elements:
            self._check_element(element)

    def _check_element(self, element):
        raise NotImplementedError
