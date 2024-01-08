from simple_closeable_resource import MyCounter, create_counter

with MyCounter(0) as t:
    print("working with counter")
    t.increment()
    t.show_count()
    t.increment()
    t.show_count()

with MyCounter(0) as t:
    print("working with counter")
    t.increment()
    t.show_count()
    t.increment()
    t.show_count()
    t.break_counter()

with create_counter(5) as c:
    c.increment()
    c.increment()
    c.show_count()
    # c.break_counter()