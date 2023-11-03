def naughty_or_nice(data):
    num = 0
    Num = 0
    naughty_or_nice = data
    for yue, ri in naughty_or_nice.items():
        for s ,value in ri.items():
            if(value == "Naughty"):
                num += 1
            elif(value == "Nice"):
                Num += 1
    if num>Num:
        return 'Naughty!'
    else:
        return 'Nice!'