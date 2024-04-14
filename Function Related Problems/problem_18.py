def InputMatrix() -> list:

    mat = [[int(col) for col in input().split()] for _ in range(3)]
    scaler = int(input())
    return [mat, scaler]

def ShowMatrix(mat: list) -> None:
    print('Original:')
    for row in mat:
        print(*row)

def ScalarMultiply(mat: list, scaler: int) -> None:
    result = [[0 for col in range(len(mat[0]))] for row in range(len(mat))]

    for row in range(len(mat)):
        for col in range(len(mat[0])):
            result[row][col] += mat[row][col] * scaler
    print(f'Multiplied by {scaler}:')
    for row in result:
        print(*row)

def main():
    matrix_data = InputMatrix()
    mat = matrix_data[0]
    ShowMatrix(mat)
    print()
    ScalarMultiply(mat, matrix_data[1])

if __name__ == '__main__':
    main()
