from functools import partial
from types import ModuleType
from typing import Dict
from typing import Optional, List

from pythonicspring.core.BeanFactory import BeanFactory
from pythonicspring.utils.GlobalInjector import global_injector


class SpringApplication:
    __instance__ = None
    __bean_factory__: BeanFactory

    def __init__(self, scan_regex: Optional[List[str]] = None):
        if not SpringApplication.__instance__:
            SpringApplication.__instance__ = self
            self.__bean_factory__ = BeanFactory(self, scan_regex)

    def get_bean_by_id(self, bean_id: str):
        return self.__bean_factory__.get_bean_by_name(bean_id)

    def get_beans_by_type(self, cls: str):
        return self.__bean_factory__.get_beans_by_type(cls)


def Autowired(func=None, bean_modules: Dict[object, ModuleType] = {}, bean_ids: Dict[object, str] = {}):
    if func is None:
        return partial(Autowired, bean_modules=bean_modules, bean_ids=bean_ids)

    def do_inject(bean_obj, bean_id, slots):
        bean = global_injector.get("__bean_factory__").get_bean_by_name(bean_id)
        if not bean:
            bean = global_injector.get("__bean_factory__").add_bean_to_factory(bean_id)
        slots[bean_obj] = bean

    def wrap(*args, **kwargs):
        if func.__name__ != '__init__':
            print("Autowired should be used for __init__ func!")
        else:
            slots = {}
            for bean_obj in bean_modules:
                bean_id = bean_modules[bean_obj].__name__.replace(".", "_")
                do_inject(bean_obj, bean_id, slots)
            for bean_obj in bean_ids:
                bean_id = bean_ids[bean_obj]
                do_inject(bean_obj, bean_id, slots)
            args[0].__dict__.update(slots)
        return func(*args, **kwargs)

    return wrap


def Service(cls=None, *, bean_id=None):
    if cls is None:
        return partial(Service, bean_id=bean_id)
    if bean_id is None:
        bean_id = cls.__module__.replace(".", "_")
    global_injector.get("__bean_factory__").add_bean_to_factory(bean_id, cls)
    return cls
