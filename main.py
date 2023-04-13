import numpy as np


def main() -> None:
    x = np.array([
        0.383375, 0.827, 1
	])
    
    A = np.array([
        [0.433, -0.125, 0.5],
        [0.25, 0.2165, 0]
	])
    B = np.array([
        [0, -0.5, 0.5],
        [0.5, 0, 0.5]
	])
    C = np.array([
        [0.5, 0, 0.25],
        [0, 0.5, 0.5]
	])
    
    a = A.dot(x)
    b = B.dot(x)
    c = C.dot(x)
    
    print(f'a: {a}')
    print(f'b: {b}')
    print(f'c: {c}')


if __name__ == "__main__":
    main()
