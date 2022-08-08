from pythonicspring import Service


@Service(bean_id='ClassAAA')
class ClassA:
    param1: str
    param2: int

    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2
