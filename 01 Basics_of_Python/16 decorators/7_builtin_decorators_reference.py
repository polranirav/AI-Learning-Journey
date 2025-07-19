class MyClass:
    @staticmethod
    def static_method():
        print("I'm static")

    @classmethod
    def class_method(cls):
        print("I'm class method from", cls.__name__)

obj = MyClass()
obj.static_method()
obj.class_method()