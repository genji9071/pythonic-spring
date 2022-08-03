# coding=utf-8
from abc import ABCMeta


class IBean(metaclass=ABCMeta):
    _bean_name_: str

    def get_bean_name(self):
        return self._bean_name_
