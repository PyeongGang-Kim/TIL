# 1번 방법

def alphabet_count(word):
    result = {}

    for char in word:
        if result.get(char):
            result[char] += 1
        else:
            result[char] = 1
    return result

# 2번 방법

def alphabet_count(word):
    return {char: word.count(char) for char in word}


print(alphabet_count('hello'))
print(alphabet_count('internationaliziation'))
print(alphabet_count('haha'))