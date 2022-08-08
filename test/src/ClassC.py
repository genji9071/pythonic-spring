from pythonicspring import Autowired
from pythonicspring import Service
from test.src import ClassB, ClassA


@Service
class ClassC:
    class_a: ClassA = None
    class_b: ClassB = None

    @Autowired(bean_modules={"class_b": ClassB}, bean_ids={"class_a": "ClassAAA"})
    def __init__(self):
        pass
