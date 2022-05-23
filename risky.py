def validate (_P, _Q):
    out = ""
    for cadena in _Q:
        validated = True
        k = 0
        for caracter in cadena:
            if caracter in _P[k:]:
                if _P[k:].index(caracter) == 0:
                    k += 1
                else:
                    k += _P[k:].index(caracter) + 1
            else:
                out += "N"
                validated = False
                break
        if validated:
            out += "Y"
    print(out)


def run ():

    while True:
        Q=[]
        N = int(input())
        if N == 0:
            break
        P = input()
        for i in range (N):
            Q.append(input())
        validate(P,Q)


if __name__=='__main__':
    run()