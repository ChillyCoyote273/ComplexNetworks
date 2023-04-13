import numpy as np


p = .0025
n = 1000


def f(x: float) -> float:
    return (1 - p + p * x) ** (n - 1)


def g(x: float) -> float:
    return 1 - np.exp(-n * p * x)


def main() -> None:
    x_dot = 0
    for i in range(100):
        x_dot = f(x_dot)
        print(x_dot)
    print(.000038/x_dot * 100)


if __name__ == "__main__":
    main()
