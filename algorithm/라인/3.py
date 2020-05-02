'''
0으로 스플릿 한다
길이를 리스트로 만든다.

'''
def chk(answer_sheet, arr):
    lend = 0
    cnt = 0
    tmp = 0
    for i in range(len(answer_sheet)):
        if arr[0][i] == arr[1][i] and arr[0][i] != answer_sheet[i]:
            cnt += 1
            tmp += 1
            lend = max(tmp, lend)
        else:
            tmp = 0
    global result
    result = max(result, cnt + lend**2)


def comb(answer_sheet, sheets, dep=0, arr=[]):
    if len(arr) == 2:
        chk(answer_sheet, arr)
        return
    if dep == len(sheets):
        return
    arr.append(sheets[dep])
    comb(answer_sheet, sheets, dep+1, arr)
    arr.pop()
    comb(answer_sheet, sheets, dep+1, arr)


def solution(answer_sheet, sheets):
    comb(answer_sheet, sheets)
    return result