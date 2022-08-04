from functools import partial

from utils.GlobalInjector import global_injector


def Service(cls=None, *, bean_id=None):
    if cls is None:
        return partial(Service, bean_id=bean_id)
    if bean_id is None:
        bean_id = cls.__module__.replace(".", "_")
    global_injector.get("__bean_factory__").add_bean_to_factory(bean_id, cls)
    return cls
