class Person:
    age:int
    name:str
    is_programmer:bool

    def __init__(self, age:int, name:str, i:bool):
        self.age = age
        self.name = name
        self.is_programmer = i

    def log(file:str="file.csv"):
        def log_decorator(func):
           def wrapper_func(self, thing:str=""):
                job = "programmer" if self.is_programmer else "not programmer"
                activity = thing.lower() if len(thing) > 0 else "unknown"

                with open(file, "a") as f:
                    f.write(f"{self.name},{self.age},{job},{activity}\n")

                func(thing)
           return wrapper_func
        return log_decorator
    
    @log("test.txt")
    def do_thing(thing:str):
        print("DECORATOR DID THE WORK")


t = Person(30, "Ed", True)

t.do_thing("Eating dinner")