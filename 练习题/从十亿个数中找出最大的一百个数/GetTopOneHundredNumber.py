import random
import time 
import datetime

########################################################################
# Quickly sorted method calls
def QuickSortMathod(left, right, QuMatrix):
    begin = left
    end = right

    if left > right:
        return

    while left != right:
        if QuMatrix[right] <= QuMatrix[begin]:
            if QuMatrix[left] > QuMatrix[begin]:
                quickTemp = QuMatrix[left]
                QuMatrix[left] = QuMatrix[right]
                QuMatrix[right] = quickTemp

                right = right - 1
            else:
                left = left + 1
        else:
            right = right - 1
    
    quickTemp = QuMatrix[begin]
    QuMatrix[begin] = QuMatrix[right]
    QuMatrix[right] = quickTemp

    QuickSortMathod(begin, (left - 1), QuMatrix)
    QuickSortMathod((right + 1), end, QuMatrix)

# Quickly sorted method
def QuickSort(QuMatrix):
    QuickSortMathod(0, (len(QuMatrix) - 1), QuMatrix)

    return QuMatrix

########################################################################

########################################################################
# Get an array whose elements are unordered integers
def RandomInitList(start, end, length):
    randomList = []
    for i in range(length):
        randomList.append(random.randint(start, end))
    
    # print("The automatically generated unordered array data is:")
    # print(randomList)
    
    return randomList

#######################################################################
def GetMinValue(Matrix):
    if len(Matrix) == 0:
        return

    minValue = Matrix[0]

    for cnt in range (len(Matrix)):
        if minValue > Matrix[cnt]:
            minValue = Matrix[cnt]

    return minValue

def GetMaxValue(Matrix):
    if len(Matrix) == 0:
        return

    maxValue = Matrix[0]
    for cnt in range (len(Matrix)):
        if maxValue < Matrix[cnt]:
            maxValue = Matrix[cnt]

    return maxValue

########################################################################
def TopOneHundredNumber(Matrix, topCount):
    maxValue = GetMaxValue(Matrix)
    minValue = GetMinValue(Matrix)
    interval = int((maxValue - minValue)/10)
    NewMatrix = []

    # ??????????????????????????????
    for cnt in range (len(Matrix)):
        if Matrix[cnt] > (maxValue - interval):
            NewMatrix.append(Matrix[cnt])

    if len(NewMatrix) > topCount:        
        Matrix = TopOneHundredNumber(NewMatrix, topCount)

    elif len(NewMatrix) == topCount:
        return NewMatrix

    else:
        # ????????????????????????????????????topCount?????????
        # Quick Sort
        Matrix = QuickSort(Matrix)
        
        # while len(Matrix) > topCount:
        #     del Matrix[0]
        del Matrix[0:(len(Matrix) - topCount)]

    return Matrix

def WriteFile(WtMatrix, path):
    f = open(path, "w")

    for cnt in range (len(WtMatrix)):
        f.write(str(WtMatrix[cnt]) + '\t')
        if cnt%10 == 9:
            f.write('\n')

    f.close


########################################################################

if __name__ == "__main__":
    GeneratePath = "file_generate.txt"
    QuickPath = "file_quick.txt"
    TopNumber = "file_topNumber.txt"

    Matrix = []
    OneHundreNumber = []
    min = 1
    max = 5010000
    number = 1010000
    topNum = 100

    ##################### ?????????????????? #####################
    print("?????????????????????...")

    timeStart = time.time()
    Matrix = RandomInitList(min, max, number)

    timeEnd = time.time()
    timeStart = int(round(timeStart * 1000))
    timeEnd = int(round(timeEnd * 1000))
    timeGap = timeEnd - timeStart
    
    print("????????????????????????:", timeGap,"ms")

    print("??????????????????????????????...")
    WriteFile(Matrix, GeneratePath)

    ###################### ?????????????????? ########################
    print("\n?????????????????????...")

    timeStart = time.time()
    QuMatrix = Matrix.copy()
    QuMatrix = QuickSort(QuMatrix)
    # print(QuMatrix)

    timeEnd = time.time()
    timeStart = int(round(timeStart * 1000))
    timeEnd = int(round(timeEnd * 1000))
    timeGap = timeEnd - timeStart
    
    print("??????????????????:", timeGap,"ms")

    print("??????????????????  \n??????????????????????????????...")
    WriteFile(QuMatrix, QuickPath)
    
    #################### ?????????????????????????????? ##################

    print("\n????????????????????????????????????...")

    timeStart = time.time()

    Matrix = TopOneHundredNumber(Matrix, topNum)
    #print(Matrix)

    timeEnd = time.time()
    timeStart = int(round(timeStart * 1000))
    timeEnd = int(round(timeEnd * 1000))
    timeGap = timeEnd - timeStart
    
    print("?????????????????????????????????:", timeGap,"ms")

    print("???????????????????????? \n?????????????????????...")
    WriteFile(Matrix, TopNumber)

    print("?????????????????????")
 
