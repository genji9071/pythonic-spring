# pythonic-spring  
用python实现spring，结合flask或者fastapi等使用，可以像springboot一样统一管理类的生成和调用，相比较原先python通过在类声明外面整实例的情况，防止了写代码时循环调用的风险，也可以为java中比较常见的多态和继承在python中的实战化做基底。


## 0.0.0.1:

两个装饰器：

- Service：装饰class，根据spring.json自动生成bean，并通过BeanFactory注册
- Autowired：装饰__init__方法，根据bean_modules和bean_ids自动注入注册的bean到类中。

SpringApplication：构建即使用，支持输入通配扫描代码并延迟import, 提供了bean_id和type两种找bean的方式

spring.json：扫描并反序列，供BeanFactory读取

## 使用方法  
### 创建实例

    app = SpringApplication(）
### 声明需要bean化的类，使用类装饰器：Service  
### 声明类内需要引用的bean，在__init__方法上使用装饰器：Autowired

    @Service
    class ClassA：
    
        class_b: ClassB
        class_c: ClassC
        
        @Autowired(bean_ids=['class_b', 'class_c'])
        def __init__(self):
            pass
            
        def foo(self):
            result = class_b.spam()
            pass
    
    

## 一个例子：

test/playground.py



