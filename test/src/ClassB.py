from annocation.Autowired import Autowired
from annocation.Service import Service


@Service
class ClassB():

    @Autowired(bean_ids=["ClassAAA"])
    def __init__(self):
        pass
