# 项目目的：加深对图遍历方式的理解，如使用DFS或者BFS的理解与运用
# 题目介绍：007站在水池的中央，周围有很多鳄鱼，他要通过踩在鳄鱼的头上的方式最终跳到岸上。
#            已知007的跳跃半径为Jump，鳄鱼坐标存在list中，问题为，007是否能够跳到岸上？输出yes or no

def Save007_DFS(list, start, jump):
    # 设置递归出口
    if IsOutput(start) == True:
        print("start",start)
        return True

    answer = False
    start[2] = 1    # 标记此点被访问过
    print("start",start)
    # 循环遍历list中所有的顶点
    for cnt in range(len(list)):
        # 获取以顶点为圆心，跳跃距离为半径，落在圆内的点
        if (IsJump(start, list[cnt], jump) == True) and (list[cnt][2] == 0):   
            #print("list", cnt, list[cnt])         
            answer = Save007_DFS(list, list[cnt], jump)
            if answer == True:
                break
            else:
                print("start",start)
    
    return answer

def IsJump(start, list, jump):
    num = (start[0] - list[0]) * (start[0] - list[0]) + ((start[1] - list[1]) * (start[1] - list[1]))
    num_sqrt = num ** 0.5
    #print("IsJump",start,list,num,num_sqrt)
    # 判断是否能调到鳄鱼身上
    if num_sqrt <= jump:
        return True
    else:
        return False

def IsOutput(start):
    if (start[0] - jump <= 0) or (start[0] + jump >= 10) or (start[1] - jump <= 0) or (start[1] + jump >= 10):
        return True
    else:
        return False

if __name__ == "__main__":
    list = [[1,2,0],[3,4,0],[9,5,0],[6,4,0],[7,7,0],[3,5,0],[1,4,0],[4,4,0],[2,3,0]]
    start = [5,5,0]
    jump = 2

    answer_dfs = Save007_DFS(list, start, jump)

    if answer_dfs == True:
        print("yes")
    else:
        print("no")
