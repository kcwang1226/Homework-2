liquidity = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}

class Queue:
    def __init__(self):
        self.list = []

    def push(self,item):
        self.list.insert(0,item)

    def pop(self):
        return self.list.pop()

    def isEmpty(self):
        return len(self.list) == 0
    
def create_circle():
    queue = Queue()
    queue.push(("tokenB", liquidity, []))
    circles = []
    while not queue.isEmpty():
        token, remain, path = queue.pop()
        path = path + [token]
        # print(token, remain, path)
        if token == "tokenB" and len(path)>2:
            # print(path)
            # input()
            circles.append(path)
        for pair, value in (remain.items()):
            token0, token1 = pair[0], pair[1]
            re = remain.copy()
            # print(pair)
            if token == token0:
                del re[pair]
                # print(re)
                # input()
                queue.push((token1, re, path))
            if token == token1:
                del re[pair]
                # print(re)
                queue.push((token0, re, path))
            # re = remain.copy()
            # new_insert = re.pop(id)
            # # print(re)
            # queue.push((new_insert, re, path))
    return circles

def calculate(path):
    prev_token = path[0]
    number = 5
    for i in range(len(path)-1):
        cur_token = path[i+1]
        # print(path[i+1])
        # num = liquidity[prev_token, cur_token]
        # print(prev_token, cur_token)
        if prev_token[5] < cur_token[5]:
            num = liquidity[(prev_token, cur_token)]
            Rx, Ry = num[0], num[1]
        else:
            num = liquidity[(cur_token, prev_token)]
            Rx, Ry = num[1], num[0]
        
        number = (Ry * 0.997 * number) / (Rx + 0.997 * number)
        prev_token = cur_token

    return number


circles = create_circle()
# print(circles)
maximum = 0
max_path = []
for path in circles:
    # print(path)
    temp = calculate(path)
    if temp > maximum:
        maximum = temp
        max_path = path

# print(maximum, max_path)
def calculate_each_step(path):
    prev_token = path[0]
    print_path = path[0]
    number = 5
    for i in range(len(path)-1):
        cur_token = path[i+1]
        print_path = print_path + f"->{cur_token}"
        # print(f" -> {cur_token}")
        # print(path[i+1])
        # num = liquidity[prev_token, cur_token]
        # print(prev_token, cur_token)
        if prev_token[5] < cur_token[5]:
            num = liquidity[(prev_token, cur_token)]
            Rx, Ry = num[0], num[1]
        else:
            num = liquidity[(cur_token, prev_token)]
            Rx, Ry = num[1], num[0]
        
        number1 = (Ry * 0.997 * number) / (Rx + 0.997 * number)
        # print(f"{prev_token} -> {cur_token}: (amount in: {number}, amount out: {number1})")
        number = number1
        prev_token = cur_token

    print(f"path: {print_path}, total balance:{maximum}")

    return number


calculate_each_step(max_path)
