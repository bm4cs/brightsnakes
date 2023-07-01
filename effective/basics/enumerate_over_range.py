from random import randint


def main():
    random_bits = 0

    # range is good fit for simple numeric iteration
    for i in range(32):
        if randint(0, 1):
            random_bits |= 1 << i
    print(bin(random_bits))

    # 'in' for data structure iteration
    flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']
    for flavor in flavor_list:
        print(f'{flavor} is delicious')

    # stick with enumerate which yields both index and item
    it = enumerate(flavor_list)
    print(next(it))
    print(next(it))

    # notice the tuple results, these supports unpacking (destructuring)
    for i, flavor in enumerate(flavor_list):
        print(f'{i + 1}: {flavor}')
