import sys

def get_builtin_dict():
    try:
        return sys.modules['__builtin__'].__dict__
    except KeyError:
        return sys.modules['builtins'].__dict__

class global_injector:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.builtin_dict = get_builtin_dict()
        for name in kwargs:
            self.builtin_dict[name] = kwargs[name]

    @staticmethod
    def get(name):
        return get_builtin_dict()[name]

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        for name in self.kwargs:
            self.builtin_dict.pop(name)

