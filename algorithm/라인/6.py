'''
'''
result = []
class Dir():
    def __init__(self):
        child = dict()


def initialize(directory):
    global root
    root = Dir()
    root.child = dict()
    for directory_com in directory:
        dir_spl = directory_com.split('/')
        cur = root
        for i in range(1, len(dir_spl)):
            if i == len(dir_spl)-1:
                cur.child[dir_spl[i]] = Dir()
                cur.child[dir_spl[i]].child = dict()
            else:
                cur = cur.child.get(dir_spl[i])


def mkdir(dir):
    cur = root
    dir_spl = dir.split('/')
    for i in range(1, len(dir_spl)):
        if i == len(dir_spl)-1:
            cur.child[dir_spl[i]] = Dir()
            cur.child[dir_spl[i]].child = dict()
        else:
            cur=cur.child[dir_spl[i]]


def rm(dir):
    cur = root
    dir_spl = dir.split('/')
    for i in range(1, len(dir_spl)):
        if i == len(dir_spl)-1:
            del cur.child[dir_spl[i]]
        else:
            cur=cur.child[dir_spl[i]]


def cp(source, dest):
    cur1 = root
    cur2 = root
    source_spl = source.split('/')
    dest_spl = dest.split('/')
    for i in range(1, len(source_spl)-1):
        cur1 = cur1.child[source_spl[i]]
    for i in range(1, len(dest_spl)-1):
        cur2 = cur2.child[dest_spl[i]]
    # print("=====")
    # for k, v in cur1.child.items():
    #     print(k, v)
    # print("=====")
    # for k, v in cur2.child.items():
    #     print(k, v)
    cp_dir(cur1.child[source_spl[-1]], cur2.child[dest_spl[-1]])


def cp_dir(source, dest):
    for key, value in source.child.items():
        dest.child[key] = Dir()
        dest.child[key].child = dict()
        cp_dir(value, dest.child[key])



def print_dir(cur, dir=""):
    global result
    for key, val in cur.child.items():
        if key:
            dir += '/'
        dir += key
        result.append(dir)
        print_dir(val, dir)


def solution(directory, command):
    initialize(directory)
    for cur_command in command:
        list_command = cur_command.split(' ')

        if list_command[0] == 'mkdir':
            mkdir(list_command[1])
        elif list_command[0] == 'rm':
            rm(list_command[1])
        elif list_command[0] == 'cp':
            cp(list_command[1], list_command[2])
    print_dir(root)
    result[0] = '/'
    print(result)


    result.sort()

    answer = result
    return answer

directory = [
"/",
"/hello",
"/hello/tmp",
"/root",
"/root/abcd",
"/root/abcd/etc",
"/root/abcd/hello"
]
command = [
"mkdir /root/tmp",
"cp /hello /root/tmp",
"rm /hello"
]
solution(directory, command)

