def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("Adding sprinkles")
        func(*args, **kwargs)
        print("Sprinkles added")
    return wrapper


def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("Adding fudge")
        func(*args, **kwargs)
        print("Fudge added")
    return wrapper


@add_sprinkles
@add_fudge
def make_ice_cream(flavor):
    print(f"Making ice cream {flavor} flavor")


make_ice_cream("vanilla")
