import webbrowser

a=['bts', '레드벨벳']
for i in range(len(a)):
    print(type(a[i]))
    webbrowser.open('https://search.naver.com/search.naver?query='+a[i])
