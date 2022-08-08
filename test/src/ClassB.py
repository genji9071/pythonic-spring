from pythonicspring import Autowired
from pythonicspring import Service
from pythonicspring import SpringApplication
from test.src import ClassC


@Service
class ClassB():
    class_c: ClassC = None

    @Autowired(bean_modules={"class_c": ClassC})
    def __init__(self):
        pass

    def get_app(self):
        return SpringApplication()
