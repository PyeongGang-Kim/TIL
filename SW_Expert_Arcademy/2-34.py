beer = {'하이트': 2000, '카스': 2100, '칭따오': 2500, '하이네켄': 4000, '버드와이저': 500}
beer_after={x:y*1.05 for x,y in beer.items()}
print(beer, end="\t")
print("# 인상 전")
print(beer_after, end="\t")
print("# 인상 후")