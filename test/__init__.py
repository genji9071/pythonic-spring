from core.SpringApplication import SpringApplication



if __name__ == '__main__':
    app = SpringApplication(scan_regex=["test.src.ClassB"])