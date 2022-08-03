# pythonic-spring

## 0.0.0.1:  
两个装饰器：  
- Service：装饰class，根据spring.json自动生成bean，并通过BeanFactory注册
- Autowired：装饰__init__方法，根据bean_modules和bean_ids自动注入注册的bean到类中。   

SpringApplication：构建即使用，支持输入通配扫描代码并延迟import, 提供了bean_id和type两种找bean的方式   

spring.json：扫描并反序列，供BeanFactory读取  

## 使用方法
    app = SpringApplication()

## 一个例子：
test/playground.py



