from annocation.Autowired import Autowired
from annocation.Service import Service
from test.src import ClassA, ClassB


@Service
class ClassC:

    @Autowired(bean_modules=[ClassA, ClassB])
    def __init__(self):
        pass

