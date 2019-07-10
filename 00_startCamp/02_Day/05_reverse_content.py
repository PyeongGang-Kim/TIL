#1. 각각의 라인을 리스트의 요소로 불러오기
with open('writelines_ssafy.txt','r') as f:
    lines=f.read()

#2. 뒤집기
reverse_lines=reversed(lines)

#3. 뒤집은 라인을 작성하기
with open('reverse_ssafy.txt','w') as f:
    f.writelines(reverse_lines)