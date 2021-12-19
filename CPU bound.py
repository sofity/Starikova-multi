from hashlib import md5
from random import choice
import concurrent.futures


def miner(n):
    while True:
        s = "".join([choice("0123456789") for i in range(50)])
        h = md5(s.encode('utf8')).hexdigest()

        if h.endswith("00000"):
            return s + ' ' + h


def main():
    with concurrent.futures.ProcessPoolExecutor(max_workers=100) as executor:
        for token in zip(executor.map(miner, range(5))):
            print(token)


if __name__ == '__main__':
    main()