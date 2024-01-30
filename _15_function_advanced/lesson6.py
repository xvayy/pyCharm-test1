def add_all(*args):
    print(args)
    sum = 0
    for num in args:
        sum += num
    return sum




values = [12,3,43,54,64,46]
values1 = [121,31,431,541,641,416]
print(add_all(*values, *values1))


def intro(**kwargs):
    print(kwargs)
    print(type(kwargs))


intro(name="Yuliia", age = 18, city= "lviv")



auto = {
    "marka": "audi",
    "year": 1999,
    "color": "black",
    "ownwrs": 5,
}

def modify(old_dict: dict, **kwargs) -> tuple[dict, bool]:
    is_modified = False
    for key, value in kwargs.items():
        if(old_dict.get(key) != value):
            old_dict[key] = value
            is_modified = True

    return old_dict, is_modified

product, was_mod = modify(auto, color="red")

print(product)
print(was_mod)