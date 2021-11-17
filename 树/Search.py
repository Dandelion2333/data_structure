def SearchData(value, index, BinaryTree):
    left = index*2 + 1
    right = index*2 + 2
    if (index >= len(BinaryTree)) or (BinaryTree[index] == None):
        return None

    elif BinaryTree[index] == value:
        return index

    elif value <= BinaryTree[index]:
        result = SearchData(value, left, BinaryTree)

    elif value > BinaryTree[index]:
        result = SearchData(value, right, BinaryTree)

    return result
