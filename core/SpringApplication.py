from typing import Optional, List

from core.BeanFactory import BeanFactory


class SpringApplication:
    __bean_factory__: BeanFactory

    def __init__(self, scan_regex: Optional[List[str]] = None):
        self.__bean_factory__ = BeanFactory(self, scan_regex)

    def get_bean_by_id(self, bean_id: str):
        return self.__bean_factory__.get_bean_by_name(bean_id)

    def get_beans_by_type(self, cls: str):
        return self.__bean_factory__.get_beans_by_type(cls)
