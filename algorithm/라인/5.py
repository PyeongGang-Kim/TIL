'''
태그 딕셔너리에 문서 추가하기
태그들에서 있는 문서들 딕셔너리에 추가하기
    있는놈이면 +1
    없는놈이면 1

 제한 사항에  동일한 문서가 여러번 들어올 수가 있는지 궁금합니다.
 예)
[
    ["문서1", "태그1", "태그2", "태그3", ...],
    ["문서2", "태그2", "태그3", "태그5", ...],
    ["문서3", "태그99", "태그100", ..],
    ["문서1", "태그1", "태그2", "태그3", ...],
    ["문서1", "태그1", "태그2", "태그3", ...],
    ...
]
'''

def solution(dataSource, tags):
    tagdict = dict()
    for i in range(len(dataSource)):
        for j in range(1, len(dataSource[i])):
            if tagdict.get(dataSource[i][j]):
                tagdict[dataSource[i][j]].add(dataSource[i][0])
            else:
                tagdict[dataSource[i][j]] = set()
                tagdict[dataSource[i][j]].add(dataSource[i][0])

            # print(dataSource[i][j])
    answer = []
    # print(tagdict)
    docdict = dict()
    for tag in tags:
        # print(tagdict[tag])
        for doc in tagdict[tag]:
            if docdict.get(doc):
                docdict[doc] += 1
            else:
                docdict[doc] = 1
    tmp = [[b, a] for a, b in docdict.items()]
    tmp.sort(key=lambda x:(-x[0], x[1]))
    answer = []
    for i in range(min(10, len(tmp))):
        answer.append(tmp[i][1])
    return answer

dataSource = [
    ["doc1", "t1", "t2", "t3"],
    ["doc2", "t0", "t2", "t3"],
    ["doc3", "t1", "t6", "t7"],
    ["doc4", "t1", "t2", "t4"],
    ["doc5", "t6", "t100", "t8"]
]
tags = ["t1", "t2", "t3"]
solution(dataSource, tags)

