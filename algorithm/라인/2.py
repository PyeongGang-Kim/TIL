'''
둘 같은데 오답이면 의심문항
의심문항 수 + 가장 긴 의심문항의 수^2
sheets중 두개 고르기 comb
두개 고르고 나면 비교하기

'''
result = 0
def chk(answer_sheet, sheet1, sheet2):
    lend = 0
    cnt = 0
    tmp = 0
    for i in range(len(answer_sheet)):
        if sheet1[i] == sheet2[i] and sheet2[i] != answer_sheet[i]:
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
    for i in range(len(sheets)-1):
        for j in range(i+1, len(sheets)):
            chk(answer_sheet, sheets[i], sheets[j])
    return result

answer_sheet, sheets = "4132315142", ["3241523133","4121314445","3243523133","4433325251","2412313253"]
print(solution(answer_sheet, sheets))