from annocation.Autowired import Autowired
from annocation.Service import Service
from test.src import ClassB


@Service
class ClassC:

    @Autowired(bean_modules=[ClassB])
    def __init__(self):
        pass
