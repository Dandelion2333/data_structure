DeleteElementRes = None

def DeleteElement(value, cnt, BinaryTree):
    # delete the value
    Delete(value, cnt, BinaryTree)
    # Adjust the structure of the tree to meet the binary search tree
    AdjustTree(DeleteElementRes, BinaryTree)
    
    return DeleteElementRes

def Delete(value, cnt, BinaryTree):
    global DeleteElementRes

    leftCnt = cnt*2 + 1
    rightCnt = cnt*2 + 2

    if (cnt >= len(BinaryTree)) or (BinaryTree[cnt] == None):
        return 

    elif BinaryTree[cnt] == value:
        # delete the value
        BinaryTree[cnt] = None
        DeleteElementRes = cnt

    elif value <= BinaryTree[cnt]:
        # enter left child
        Delete(value, leftCnt, BinaryTree)   

    elif BinaryTree[cnt] < value:
        # enter right child
        Delete(value, rightCnt, BinaryTree)


def AdjustTree(cnt, BinaryTree):
    leftCnt = cnt*2 + 1
    rightCnt = cnt*2 + 2

    if rightCnt >= len(BinaryTree):
        return
    
    elif (BinaryTree[rightCnt] == None) and (BinaryTree[leftCnt] == None):
        return

    else: 
        if BinaryTree[rightCnt] != None:
            BinaryTree[cnt] = BinaryTree[rightCnt]
            BinaryTree[rightCnt] = None
            AdjustTree(rightCnt, BinaryTree)

        else: # At this point, the left child must not be empty
            # 把cnt点作为父结点，然后把它的左子树的全部一起，一一对应的移到cnt这个点上，用伪代码表示的话
            # cnt = cnt的左孩子， cnt的右孩子 = cnt的左孩子的右孩子， 用这种方式一一对应
            SwapTree(cnt, leftCnt, BinaryTree)

def SwapTree(node, value,  BinaryTree):
    # 用层次遍历的方式把cnt的左孩子全部记录，然后再复制到对应cnt的位置
    valueList = []
    cnt = 0
    valLeft = value*2 + 1
    valRight = value*2 + 2

    nodeLeft = node*2 + 1
    nodeRight = node*2 + 2

    if value < len(BinaryTree):
        BinaryTree[node] = BinaryTree[value]
        BinaryTree[value] = None

        # 因为左子树为空，所以根据递归的特性，先把右边的数据移走，然后再移动左边的数据
        SwapTree(nodeRight, valRight, BinaryTree)
        SwapTree(nodeLeft, valLeft, BinaryTree)        

    else:
        return
