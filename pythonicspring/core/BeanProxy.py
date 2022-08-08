class BeanProxy:

    def __init__(self, bean=None, bean_id=None):
        self._bean_ = bean
        self._bean_id_ = bean_id

    def inject_bean(self, bean, bean_id):
        if self._bean_:
            raise ValueError("Bean already existed...")
        self._bean_ = bean
        self._bean_id_ = bean_id

    def get_bean_name(self):
        return self._bean_id_

    def is_injected(self):
        return self._bean_ is not None

    def __getattr__(self, name):
        return getattr(self._bean_, name)

    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            setattr(self._bean_, name, value)

    def __delattr__(self, name):
        if name.startswith('_'):
            super().__delattr__(name)
        else:
            delattr(self._bean_, name)

    @property
    def __class__(self):
        return self._bean_.__class__

    @property
    def __dict__(self):
        return self._bean_.__dict__

    def __str__(self):
        return f"BeanProxy@@[{self._bean_.__str__()}]"

    def __repr__(self):
        return f"BeanProxy@@[{self._bean_.__repr__()}]"
