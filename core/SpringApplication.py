import sys
from typing import Optional, List

from core.BeanFactory import BeanFactory


class SpringApplication:
    _bean_factory_: BeanFactory

    def __init__(self, scan_regex: Optional[List[str]] = None):
        instance_path = sys._getframe(1).f_code.co_filename
        self._bean_factory_ = BeanFactory(instance_path, scan_regex)

    def get_bean_by_id(self, bean_id: str):
        return BeanFactory.get_bean_by_name(bean_id)

    def get_beans_by_type(self, cls: str):
        return BeanFactory.get_beans_by_type(cls)
