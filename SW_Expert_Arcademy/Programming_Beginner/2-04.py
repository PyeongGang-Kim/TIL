a = "aeiou"
b = "Pythn s pwrfl... nd fst; plys wll wth thrs; rns vrywhr; s frndly & sy t lrn; s Opn."
result = [char for char in b if char not in a]
print("".join(result))