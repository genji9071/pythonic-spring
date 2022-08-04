from functools import partial
from types import ModuleType
from typing import List

from utils.GlobalInjector import global_injector


def Autowired(func=None, bean_modules: List[ModuleType] = [], bean_ids: List[str] = []):
    if func is None:
        return partial(Autowired, bean_modules=bean_modules, bean_ids=bean_ids)

    def wrap(*args, **kwargs):
        slots = {}
        bean_set = set(bean_ids + list(map(lambda x: x.__name__.replace(".", "_"), bean_modules)))
        for bean_id in bean_set:
            bean = global_injector.get("__bean_factory__").get_bean_by_name(bean_id)
            if not bean:
                bean = global_injector.get("__bean_factory__").add_bean_to_factory(bean_id)
            slots[bean_id] = bean
        args[0].__dict__.update(slots)
        return func(*args, **kwargs)

    return wrap
