lunch={
    '양자강': '02-556-3241',
    '김밥카페': '02-5351-123',
    '순남시레기': '234-12-52'}

with open('lunch.csv','w',encoding="utf-8") as f:
    for item in lunch.items():
        f.write(f'{item[0]}, {item[1]}\n')