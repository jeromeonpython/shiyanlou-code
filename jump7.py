for a in range(1,101):
    if a%7==0 or str(a).find('7')>=0:
        continue
    print(a)
