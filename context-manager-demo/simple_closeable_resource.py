from contextlib import contextmanager
from typing import ContextManager, Self


class MyCounter(ContextManager):
    def __init__(self, num:int):
        self.num = num

    def __enter__(self):
        print("started counter")
        return self
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type is Exception:
            print(exc_value)
        
        print("closing counter")
        return True
    
    def increment(self) -> Self:
        self.num += 1
        return self
    
    def decrement(self) -> Self:
        self.num -= 1
        return self

    def show_count(self):
        print(f"current count is: {self.num}")
    
    def break_counter(self):
        raise Exception("Oh dear, something went wrong")
    

@contextmanager
def create_counter(num:int=0):
    try:
        print("starting counter")
        yield AnotherCounter(num)
    finally:
        print("closed counter")


class AnotherCounter:
    def __init__(self, num:int) -> None:
        self.num = num

    def increment(self) -> Self:
        self.num += 1
        return self
    
    def decrement(self) -> Self:
        self.num -= 1
        return self

    def show_count(self):
        print(f"current count is: {self.num}")
    
    def break_counter(self):
        raise Exception("Oh dear, something went wrong")