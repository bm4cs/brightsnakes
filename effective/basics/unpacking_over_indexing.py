def main():
    snack_calories = {"aussielent": 500, "popcorn": 80, "nuts": 190}

    items = tuple(snack_calories.items())
    auslent, *_ = items  # splat operator

    # could do this
    first = auslent[0]
    second = auslent[1]
    print(f"{first} {second}")

    # but assignment unpacking is nicer
    first, second = auslent
    print(f"{first} {second}")

    # newcomers bubble sort
    def bubble_sort(a):
        for _ in range(len(a)):
            for i in range(1, len(a)):
                if a[i] < a[i - 1]:
                    temp = a[i]
                    a[i] = a[i - 1]
                    a[i - 1] = temp

    names = ["pretzels", "carrots", "arugula", "bacon"]
    bubble_sort(names)
    print("index bubble", names)

    # with unpacking can do this in-place
    def bubble_sort(a):
        for _ in range(len(a)):
            for i in range(1, len(a)):
                if a[i] < a[i - 1]:
                    a[i - 1], a[i] = a[i], a[i - 1]

    bubble_sort(names)
    print("in-place bubble", names)

    # unpacking shines in the target list of a for loop
    for i, (name, cals) in enumerate(items, 1):
        print(f"#{i}: {name} has {cals} calories")
