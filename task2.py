import random


def gen_random_array(n: int, key: int):

    if (n < 1) or not (1 <= key <= 4):
        raise ValueError('Max element must be greater than 1 and the key must be in [1; 4]')

    if key == 1:
        arr = [None] * n
        indexes = list(range(n))

        for num in range(1, n + 1):
            curr_index = random.sample(indexes, 1)[0]
            arr[curr_index] = num
            indexes.remove(curr_index)

    elif key == 2:
        arr = []
        indexes = list(range(n))
        random.shuffle(indexes)

        for num in range(1, n + 1):
            curr_index = indexes.pop()
            while len(arr) <= curr_index:
                arr.append(None)
            arr[curr_index] = num

    elif key == 3:
        arr = random.sample(range(1, n + 1), n)

    elif key == 4:
        arr = list(range(1, n + 1))
        random.shuffle(arr)

    return arr


if __name__ == '__main__':
    max_elem = int(input('Enter the max value in array: '))
    choose = random.randint(1, 4)
    random_arr = gen_random_array(max_elem, choose)
    print(random_arr)
