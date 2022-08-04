from functools import partial

from core.BeanFactory import BeanFactory


def Service(cls=None, *, bean_id=None):
    if cls is None:
        return partial(Service, bean_id=bean_id)
    if bean_id is None:
        bean_id = cls.__module__.replace(".", "_")
    BeanFactory.add_bean_to_factory(bean_id, cls)
    return cls
