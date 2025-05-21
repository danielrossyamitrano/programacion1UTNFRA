def calcular_primo(n):
    primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    if n <= 1:
        return False
    else:
        es_primo = True
        for primo in [i for i in primos if i < n]:
            if n % primo == 0:
                es_primo = False
                break
    return es_primo
