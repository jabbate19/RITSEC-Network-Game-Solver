import socket
import statistics as stat
from time import sleep

TCP_IP='129.21.125.199'
TCP_PORT=10000
BUFFER_SIZE=4096
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def init():
    s.connect((TCP_IP, TCP_PORT))
    #s.send(MESSAGE)
    data = s.recv(BUFFER_SIZE)
    #print(repr(data))
    s.send("".encode())

def get_problem():
    data = s.recv(BUFFER_SIZE)
    data_string = repr(data)
    print(data_string)
    #print(data_string.find("problem"))
    problem = ''
    for x in range( data_string.find("problem:")+8, len(data_string) ):
        char = data_string[x]
        if char == ' ':
            break
        else:
            problem += char
    #for x in range( data_string.find("size:")+5, len(data_string)-1 ):
    #    char = data_string[x]
    #    items += char
    pos1 = data_string.find('\\n')
    pos2 = (data_string.find('\\n',pos1+1))
    items = data_string[pos2:]
    items = items.split('\\n')
    items.insert(0, problem)
    items.remove('')
    items.remove("'")
    return items

def solve_problem():
    problem = get_problem()
    type = problem.pop(0)
    nums = [int(x) for x in problem ]
    if type == 'mean':
        return stat.mean(nums)
    elif type == 'median':
        return stat.median(nums)
    elif type == 'range':
        return max(nums) - min(nums)
    elif type == 'minimum':
        return min(nums)
    elif type == 'maximum':
        return max(nums)
    else:
        raise Exception("Invalid Type")

def main():
    init()
    #print(get_problem())
    #print(solve_problem())
    for x in range(0,100):
        print( x + 1 )
        s.send(str(round(solve_problem())).encode())
        sleep(0.5)
    data = s.recv(BUFFER_SIZE)
    data_string = repr(data)
    print(data_string)
    s.close()
main()