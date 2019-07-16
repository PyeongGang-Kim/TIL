a=['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
b={'A': 0, 'O': 0, 'B': 0, 'AB': 0}
for B in a:
    b[B]+=1
print(b)