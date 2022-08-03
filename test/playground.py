from core.SpringApplication import SpringApplication

if __name__ == '__main__':
    app = SpringApplication()
    bean_1 = app.get_bean_by_id("ClassAAA")
    bean_2 = app.get_beans_by_type("ClassA")
    print('init done')
