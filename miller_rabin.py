import random


class MillerRabin:
    def __init__(self, number, rounds):
        self.number = number
        self.rounds = rounds

    def primality_test(self):
        # Precisamos de um numero d > 0 impar e um s > 0 que satisfaçam: n - 1 = 2 ** s * d
        d = number - 1
        s = 0
        while (d % 2 == 0):
            d /= 2
            s += 1
        
        # Como se trata de um teste probabilistico,
        # quanto mais vezes repetirmos mais o resultado é confiável
        for _ in range(self.rounds):
            a = random.randint(2, n - 2) # Devido ao Teorema de Fermat,
                                         # a ** (n-1) sempre sera congruente a 1 (mod n),
                                         # independente de n ser primo ou composto. Isso fara
                                         # com que n seja identificado como possivelmente primo,
                                         # o que nao é desejavel

            # Selecionada a base para testar a primalidade de n, verifica-se se a é testemunha
            # da composição de n. Se n for composto, haverá pelo menos um valor de (a ** i) mod n
            # que não é congruente a i (mod n), para algum i no intervalo [0, n-1]
            x = (a ** d) % n
            for _ in range(s):
                # Mais um passo necessário para encontrar testemunhas da composição de n, iterativamente.
                # Busca-se por raízes quadradas não triviais de 1 (mod n)
                y = (x ** 2) % n
                # Se x não é congruente a 1 (mod n) ou -1 (mod n),
                # então x é uma raiz quadrada não trivial de 1 (mod n) e a é testemunha da composição de n
                if y == 1 and x != 1 and x != (n - 1):
                    return f"{self.number}\n é composto"
                x = y
            if y != 1:
                return f"{self.number}\n é composto"
        return f"{self.number}\n provavelmente é primo"