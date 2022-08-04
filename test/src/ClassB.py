from annocation.Autowired import Autowired
from annocation.Service import Service
from test.src import ClassC


@Service
class ClassB():

    @Autowired(bean_modules=[ClassC])
    def __init__(self):
        pass
