from core.SpringApplication import SpringApplication

if __name__ == '__main__':
    app = SpringApplication()
    try:
        from core.BeanFactory import BeanFactory

        bean_factory = BeanFactory(None, None)
        print(f"BeanFactory init check failed!")
    except Exception as ex:
        print(f"BeanFactory init check pass!")

    try:
        from core.BeanFactory import BeanFactory

        bean = BeanFactory.add_bean_to_factory("testBean", None)
        print(f"BeanFactory add_bean_to_factory check failed!")
    except Exception as ex:
        print(f"BeanFactory add_bean_to_factory check pass!")

    try:
        from core.BeanFactory import BeanFactory

        bean = BeanFactory.get_bean_by_name("ClassAAA")
        print(f"BeanFactory get_bean_by_name check failed!")
    except Exception as ex:
        print(f"BeanFactory get_bean_by_name check pass!")

    try:
        from core.BeanFactory import BeanFactory

        bean = BeanFactory.get_beans_by_type("ClassA")
        print(f"BeanFactory get_beans_by_type check failed!")
    except Exception as ex:
        print(f"BeanFactory get_beans_by_type check pass!")

    try:
        from core import BeanFactory

        bean = BeanFactory._beans_dict_
        print(f"BeanFactory _beans_dict_ check failed!")
    except Exception as ex:
        print(f"BeanFactory _beans_dict_ check pass!")
