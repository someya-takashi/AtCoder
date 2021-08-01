def CC(A: list) -> list:
    "座標圧縮"
    B = {j: i for i, j in enumerate(A)}
    return B