def solution(inputString):
    cl = [0, 0, 0, 0]
    cnt = 0
    D = {
            "(": (0, 1), ")": (0, -1),
            "{": (1, 1), "}": (1, -1),
            "[": (2, 1), "]": (2, -1),
            "<": (3, 1), ">": (3, -1),
         }
    for char in inputString:
        tmp = D.get(char)
        if tmp:
            cl[tmp[0]] += tmp[1]
            if cl[tmp[0]] < 0:
                return -1
            if tmp[1] == -1:
                cnt += 1
    if sum(cl):
        return -1
    answer = cnt
    return answer
inputString = "<[>]"
print(solution(inputString))