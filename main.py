from collections import deque
import time

num=0
vis=set()

def print_puzzle(arr):
    for i in range(3):
        for j in range(3):
            print(arr[i * 3 + j], end=' ')
        print()


def check(start, goal):
    for i in range(len(start)):
        if start[i] != goal[i]:
            return False
    return True


def get_count(l1, goal):
    count = 0
    for i in range(len(goal)):
        if l1[i] == goal[i]:
            count = count + 1
    return count


def in_stack2_dfs(i, j, start, goal, zero_pos, new_puzzles_collection):
    first_move = []
    second_move = []
    first_move = start.copy()
    second_move = start.copy()
    first_move[zero_pos], first_move[zero_pos + i] = first_move[zero_pos + i], first_move[zero_pos]
    second_move[zero_pos], second_move[zero_pos + j] = second_move[zero_pos + j], second_move[zero_pos]

    x = get_count(first_move, goal)
    y = get_count(second_move, goal)

    if x >= y:
        new_puzzles_collection.append(second_move)
        new_puzzles_collection.append(first_move)

    else:
        new_puzzles_collection.append(first_move)
        new_puzzles_collection.append(second_move)


def sortTuple(tupleSort):
    return (sorted(tupleSort, key=lambda x: x[1]))


def in_stack3_dfs(i, j, k, start, goal, zero_pos, new_puzzles_collection):
    first_move = []
    second_move = []
    third = []

    first_move = start.copy()
    second_move = start.copy()
    third = start.copy()
    first_move[zero_pos], first_move[zero_pos + i] = first_move[zero_pos + i], first_move[zero_pos]

    second_move[zero_pos], second_move[zero_pos + j] = second_move[zero_pos + j], second_move[zero_pos]

    third[zero_pos], third[zero_pos + k] = third[zero_pos + k], third[zero_pos]

    x = get_count(first_move, goal)
    y = get_count(second_move, goal)
    z = get_count(third, goal)

    arr = [(first_move, x), (second_move, y), (third, z)]
    arr = sortTuple(arr)

    for i in range(len(arr)):
        new_puzzles_collection.append(arr[i][0])


def in_stack4_dfs(i, j, k, l, start, goal, zero_pos, new_puzzles_collection):
    first = []
    second = []
    third = []
    fourth = []

    first = start.copy()
    second = start.copy()
    third = start.copy()
    fourth = start.copy()
    first[zero_pos], first[zero_pos + i] = first[zero_pos + i], first[zero_pos]

    second[zero_pos], second[zero_pos + j] = second[zero_pos + j], second[zero_pos]

    third[zero_pos], third[zero_pos + k] = third[zero_pos + k], third[zero_pos]
    fourth[zero_pos], fourth[zero_pos + l] = fourth[zero_pos + l], fourth[zero_pos]
    w = get_count(first, goal)
    x = get_count(second, goal)
    y = get_count(third, goal)
    z = get_count(fourth, goal)

    arr = [(first, w), (second, x), (third, y), (fourth, z)]
    arr = sortTuple(arr)
    for i in range(len(arr)):
        new_puzzles_collection.append(arr[i][0])


def future_moves_dfs(start, goal):
    next_moves = []
    zero_pos = start.index(0)
    new_puzzles_collection = []

    if zero_pos == 0:

        in_stack2_dfs(1, 3, start, goal, zero_pos, new_puzzles_collection)

    elif zero_pos == 1:

        in_stack3_dfs(-1, 1, 3, start, goal, zero_pos, new_puzzles_collection)

    elif zero_pos == 2:

        in_stack2_dfs(-1, 3, start, goal, zero_pos, new_puzzles_collection)

    elif zero_pos == 3:

        in_stack3_dfs(-3, 1, 3, start, goal, zero_pos, new_puzzles_collection)

    elif zero_pos == 4:

        in_stack4_dfs(3, 1, -1, -3, start, goal, zero_pos, new_puzzles_collection)

    elif zero_pos == 5:

        in_stack3_dfs(-3, -1, 3, start, goal, zero_pos, new_puzzles_collection)

    elif zero_pos == 6:

        in_stack2_dfs(1, -3, start, goal, zero_pos, new_puzzles_collection)


    elif zero_pos == 7:

        in_stack3_dfs(-1, 1, -3, start, goal, zero_pos, new_puzzles_collection)

    elif zero_pos == 8:

        in_stack2_dfs(-1, -3, start, goal, zero_pos, new_puzzles_collection)

    return new_puzzles_collection






def in_stack2_bfs(i, j, start, goal, zero_pos, new_puzzles_collection):
    first_move = []
    second_move = []
    first_move = start.copy()
    second_move = start.copy()
    first_move[zero_pos], first_move[zero_pos + i] = first_move[zero_pos + i], first_move[zero_pos]
    second_move[zero_pos], second_move[zero_pos + j] = second_move[zero_pos + j], second_move[zero_pos]

    x = get_count(first_move, goal)
    y = get_count(second_move, goal)

    if x <= y:
        new_puzzles_collection.append(second_move)
        new_puzzles_collection.append(first_move)

    else:
        new_puzzles_collection.append(first_move)
        new_puzzles_collection.append(second_move)



def in_stack3_bfs(i, j, k, start, goal, zero_pos, new_puzzles_collection):
    first_move = []
    second_move = []
    third = []

    first_move = start.copy()
    second_move = start.copy()
    third = start.copy()
    first_move[zero_pos], first_move[zero_pos + i] = first_move[zero_pos + i], first_move[zero_pos]

    second_move[zero_pos], second_move[zero_pos + j] = second_move[zero_pos + j], second_move[zero_pos]

    third[zero_pos], third[zero_pos + k] = third[zero_pos + k], third[zero_pos]

    x = get_count(first_move, goal)
    y = get_count(second_move, goal)
    z = get_count(third, goal)

    arr = [(first_move, x), (second_move, y), (third, z)]
    arr = sortTuple(arr)


    new_puzzles_collection.append(arr[2][0])
    new_puzzles_collection.append(arr[1][0])
    new_puzzles_collection.append(arr[0][0])



def in_stack4_bfs(i, j, k, l, start, goal, zero_pos, new_puzzles_collection):
    first = []
    second = []
    third = []
    fourth = []

    first = start.copy()
    second = start.copy()
    third = start.copy()
    fourth = start.copy()
    first[zero_pos], first[zero_pos + i] = first[zero_pos + i], first[zero_pos]

    second[zero_pos], second[zero_pos + j] = second[zero_pos + j], second[zero_pos]

    third[zero_pos], third[zero_pos + k] = third[zero_pos + k], third[zero_pos]
    fourth[zero_pos], fourth[zero_pos + l] = fourth[zero_pos + l], fourth[zero_pos]
    w = get_count(first, goal)
    x = get_count(second, goal)
    y = get_count(third, goal)
    z = get_count(fourth, goal)

    arr = [(first, w), (second, x), (third, y), (fourth, z)]
    arr = sortTuple(arr)

    new_puzzles_collection.append(arr[3][0])
    new_puzzles_collection.append(arr[2][0])
    new_puzzles_collection.append(arr[1][0])
    new_puzzles_collection.append(arr[0][0])



def future_moves_bfs(start, goal):
    next_moves = []
    zero_pos = start.index(0)
    new_puzzles_collection = []

    if zero_pos == 0:

        in_stack2_bfs(1, 3, start, goal, zero_pos, new_puzzles_collection)

    elif zero_pos == 1:

        in_stack3_bfs(-1, 1, 3, start, goal, zero_pos, new_puzzles_collection)

    elif zero_pos == 2:

        in_stack2_bfs(-1, 3, start, goal, zero_pos, new_puzzles_collection)

    elif zero_pos == 3:

        in_stack3_bfs(-3, 1, 3, start, goal, zero_pos, new_puzzles_collection)

    elif zero_pos == 4:

        in_stack4_bfs(3, 1, -1, -3, start, goal, zero_pos, new_puzzles_collection)

    elif zero_pos == 5:

        in_stack3_bfs(-3, -1, 3, start, goal, zero_pos, new_puzzles_collection)


    elif zero_pos == 6:

        in_stack2_bfs(1, -3, start, goal, zero_pos, new_puzzles_collection)


    elif zero_pos == 7:

        in_stack3_bfs(-1, 1, -3, start, goal, zero_pos, new_puzzles_collection)


    elif zero_pos == 8:
        in_stack2_bfs(-1, -3, start, goal, zero_pos, new_puzzles_collection)


    return new_puzzles_collection


def ids_search(start_state, goal_state):

    for depth in range(20):
        visited = set()
        path = dls_search(start_state, goal_state, depth, visited)

        if path is not None:

            return path, visited, sum

    return None, None


def dls_search(start, goal, depth, visited):
    global num
    stack = deque([(start, 0)])


    count = 0
    #print("the depth is : ", depth)
    while stack:

        puzzle, current_depth = stack.pop()
        print_puzzle(puzzle)
        print("\n")
        num += 1
        count=count+1
        if current_depth > depth:
            continue

        if check(puzzle, goal):
            print('-----------------')
            print('IDS Algorithm')

            print('Path Cost:', count - 1)
            vis.add(str(puzzle))
            return puzzle

        if str(puzzle) in visited:
            continue
        visited.add(str(puzzle))
        vis.add(str(puzzle))
        for move in future_moves_dfs(puzzle, goal):
            stack.append((move, current_depth + 1))
    return None




def DFS(start, goal):
    stack = deque([start])
    visited = set()
    start_time = time.time()
    count = 0

    while stack:

        puzzle = stack.pop()
        print_puzzle(puzzle)
        print("\n")

        count = count + 1
        if check(puzzle, goal):
            print('-----------------')
            print('DFS Algorithm')
            print('-----------------')
            print('Time taken:', time.time() - start_time, 'seconds')
            print('Path Cost:', count - 1)
            print('No of Node Visited:', len(visited) + 1)
            print('-----------------')
            return puzzle

        # print(puzzle)
        if str(puzzle) in visited:
            continue

        # print(puzzle)
        visited.add(str(puzzle))
        #print(visited)

        for move in future_moves_dfs(puzzle, goal):
            stack.append(move)


    return None


def bfs(start, goal):

    #queue = deque([start])
    queue = deque([(start, [])])
    visited = set()
    start_time = time.time()
    count = 0

    while queue:

        puzzle,path = queue.popleft()
       #state, path = queue.popleft()
        print_puzzle(puzzle)
        print("\n")
        count = count + 1
        if check(puzzle, goal):
            print('-----------------')
            print('BFS Algorithm')
            print('-----------------')
            print('Time taken:', time.time() - start_time, 'seconds')
            #print('Path Cost:', count-1)
            print('No of Node Visited:', len(visited) + 1)
            print('-----------------')
            return path



        if str(puzzle) in visited:
            continue
        visited.add(str(puzzle))


        for move in future_moves_bfs(puzzle, goal):
            if str(move) not in visited:
                queue.append((move, path+[move] ))


    return None



def main():
    start_puzzle = [1, 2, 0, 3, 4, 5, 6, 7, 8]
    goal_state = [0,1,2,3,4,5,6,7,8]


    # start_puzzle = [3,1,2,0,4,5,6,7,8]
    # goal_state = [0,1,2,3,4,5,6,7,8]
    #
    # start_puzzle = [1,3,4,8,6,2,7,0,5]
    # goal_state = [1, 2, 3, 8,0,4,7,6,5]
    #
    # start_puzzle = [8, 3, 5, 4, 1, 6, 2, 7, 0]
    # goal_state = [1, 2, 3, 8,0,4,7,6,5]

    result = DFS(start_puzzle, goal_state)
    if result:
        print("The solution is found:", result)
    else:
        print("No solution is found")

    result = bfs(start_puzzle, goal_state)
    print("the path cost is : ", len(result))



    start_time = time.time()
    sum = 0
    path, visited, sum = ids_search(start_puzzle, goal_state)
    end_time = time.time()

    if path is not None:


        print('-----------------')
        print('Time taken:', time.time() - start_time, 'seconds')
        print('No of Node Visited:',len(vis))
        print("the visited nodes", vis)
        print('-----------------')

    else:
        print("IDS search failed to find a solution :(")


main()