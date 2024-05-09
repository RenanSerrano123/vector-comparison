def verifica_multiplicacao(vetor1, vetor2):
    n = len(vetor1)
    multiplicador = None
    for i in range(n):
        if vetor1[i] == 0:
            if vetor2[i] != 0:
                return False
        else:
            if vetor2[i] % vetor1[i] != 0:
                return False
            if multiplicador is None:
                multiplicador = vetor2[i] // vetor1[i]
            else:
                if vetor2[i] // vetor1[i] != multiplicador:
                    return False
    return True
def main():
    n = int(input())
    vetor1 = list(map(int, input().split()))
    vetor2 = list(map(int, input().split()))
    if verifica_multiplicacao(vetor1, vetor2):
        print("SIM")
    else:
        print("NAO")
main()