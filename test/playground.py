from pythonicspring import SpringApplication

if __name__ == '__main__':
    app = SpringApplication()
    print(f'bean by id: ClassAAA  ---   {app.get_bean_by_id("ClassAAA").get_bean_name()}')
    print(f'beans by type: ClassA  ---   {app.get_beans_by_type("ClassA")[0].get_bean_name()}')
    print(f'var of bean by type: ClassB  ---   {app.get_beans_by_type("ClassB")[0].__dict__}')
    print(f'var of bean by type: ClassC  ---   {app.get_beans_by_type("ClassC")[0].__dict__}')
    print(f'result of bean type: ClassB.get_app()  ---   {app.get_beans_by_type("ClassB")[0].get_app()}')
    print(f'result of bean type: ClassC.class_b  ---   {app.get_beans_by_type("ClassC")[0].class_b}')
