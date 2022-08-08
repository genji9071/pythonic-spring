from pythonicspring import SpringApplication

if __name__ == '__main__':
    app = SpringApplication()
    try:
        from pythonicspring.core.BeanFactory import BeanFactory

        bean_factory = BeanFactory(None, None)
        print(f"BeanFactory init check failed!")
    except Exception as ex:
        print(f"BeanFactory init check pass!")

