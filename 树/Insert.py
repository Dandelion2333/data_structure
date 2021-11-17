import random

TreeDepth = 0

def RandomVaule(start, end):
    value = random.randint(start, end)

    return value

def InsertElement(value, BinaryTree):
    # if the binary tree is null, so, we are create it
    if len(BinaryTree) == 0:
        BinaryTree.append(value)
        TreeDepth = 0
    else:
        FindPosition(0, value, BinaryTree)

def FindPosition(cnt, value, BinaryTree):
    leftCnt = cnt*2 + 1
    rightCnt = cnt*2 + 2
    
    if value <= BinaryTree[cnt]:
        if leftCnt > (len(BinaryTree)-1):
            FillBinaryTree(BinaryTree)
            BinaryTree[leftCnt] = value    
        elif BinaryTree[leftCnt] == None:
            BinaryTree[leftCnt] = value   
        else:
            FindPosition(leftCnt, value, BinaryTree)

    if value > BinaryTree[cnt]:
        if rightCnt > (len(BinaryTree)-1):
            FillBinaryTree(BinaryTree)
            BinaryTree[rightCnt] = value        
        elif BinaryTree[rightCnt] == None:
            BinaryTree[rightCnt] = value  
        else:
            FindPosition(rightCnt, value, BinaryTree)

def FillBinaryTree(BinaryTree):
    global TreeDepth

    TreeDepth = TreeDepth + 1
    
    for cnt in range(0, 2**TreeDepth):
        BinaryTree.append(None)

    #print(TreeDepth, 2**TreeDepth, BinaryTree)