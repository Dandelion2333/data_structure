import PrintShape
import Insert
import Search
import Delete


if __name__ == "__main__":
    BinaryTree = []
    GenerateData = []
    
    # Building a basic database
    for cnt in range(0,8):
        value = Insert.RandomVaule(1, 100)
        GenerateData.append(value)
        Insert.InsertElement(value, BinaryTree)

    # GenerateData = [2, 86, 68, 26, 57, 90, 41, 63]
    # for cnt in range (len(GenerateData)):
    #     Insert.InsertElement(GenerateData[cnt], BinaryTree)
    
    
    print(GenerateData)

    # Visual print binary tree
    PrintShape.BinaryTreePrinter(BinaryTree)

    # search value
    value = GenerateData[3]
    #result = Search.SearchData(value, 0, BinaryTree)

    # delete value
    value = GenerateData[2]
    print("Delete value:", value)
    DeleteElementRes = Delete.DeleteElement(value, 0, BinaryTree)
    print("Delete index:", DeleteElementRes)

    # Visual print binary tree
    PrintShape.BinaryTreePrinter(BinaryTree)

