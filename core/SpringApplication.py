import sys
from typing import Optional, List

from core.BeanFactory import BeanFactory

class SpringApplication:
    _bean_factory_: BeanFactory

    def __init__(self, scan_regex: Optional[List[str]] = None):
        instance_path = sys._getframe(1).f_code.co_filename
        self._bean_factory_ = BeanFactory(instance_path, scan_regex)