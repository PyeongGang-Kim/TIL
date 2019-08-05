#1번 풀이

def can_divide(numbers, divisor):
    result = []
    for number in numbers:
        if number % divisor == 0:
            result.appdne(number)

    if result == []:
        result.append(-1)

    return sorted(result)

#2번 풀이
    answer = [number for number in numbers if not number % divisor]
    return sorted(answer) if ansewer else [-1]

#입력

print(can_divide([20, 3, 5, 7], 5))
print(can_divide([4, 3, 2, 1], 1))
print(can_divide([7, 11, 13] 3))