def Adjust(list):
    for cnt in range(len(list)):
        if list[cnt] == None:
            list[cnt] = 0

    return list

def judgePosition(length):
    """
    根据位置判断此数据应该在二叉树的第几行、第几列
    :param length: 
    :return: 
    """
    rows = 0

    # get rows
    while True:
        if (2 ** (rows - 1)) <= length <= (2 ** rows - 1):
            break
        else:
            rows += 1

    # get cols
    cols = length - 2 ** (rows - 1) + 1

    return rows, cols


def BinaryTreePrinter(listOne=None):
    listTwo = listOne.copy()

    listTwo = Adjust(listTwo)
    # print(listTwo)

    """
    打印列表为二叉树形状
    :param listTwo: 传入的列表
    :return:
    """
    rows = judgePosition(len(listTwo))[0]  # rows为总行数
    count = 0
    pre_row, pre_col = 0, 0  # 记录上一个数的行与列

    for x in listTwo:
        count += 1  # 计数现在打印的是第几个数
        x_row, x_col = judgePosition(count)  # 计算出当前打印的数位于第几行，第几列
        if x_row != pre_row:  # 如果换行了，那么打印换行符
            print('\n')
        if x_col != 1:  # 如果当前打印的数字不是本行第一个，则打印步长为2**(rows-x_row+1)-1
            print('  ' * (2 ** (rows - x_row + 1) - 1), end='')
        else:
            print('  ' * ((2 ** (rows - x_row + 1) - 1) // 2), end='')
        print('{0:2}'.format(x), end='')
        pre_row, pre_col = x_row, x_col  # 位置记录更新

    print("\n")