import random


class MillerRabin:
    def __init__(self, number, rounds):
        self.number = number
        self.rounds = rounds

    def primality_test(self):
        # Precisamos de um numero d > 0 impar e um s > 0 que satisfaçam: n - 1 = 2 ** s * d
        d = int(self.number - 1)
        s = 0
        while (d % 2 == 0):
            d //= 2
            s += 1
        
        # Como se trata de um teste probabilistico,
        # quanto mais vezes repetirmos mais o resultado é confiável
        for _ in range(self.rounds):
            a = random.randint(2, self.number - 2) # Devido ao Teorema de Fermat, para qualquer n
                                                   # primo e qualquer inteiro a não divisivel por n
                                                   # a ** (n-1) sempre sera congruente a 1 (mod n),
                                                   # porém se n for composto existem a para os quais
                                                   # a ** (n-1) não é congruente a 1 (mod n),
                                                   # os chamados pseudoprimos. Escolhemos a entre
                                                   # 2 e n-2 justamente para diminuir a possibilidade
                                                   # de selecionarmos um pseudoprimo
                                         

            # Selecionada a base para testar a primalidade de n, verifica-se se a é testemunha
            # da composição de n. Se n for composto, haverá pelo menos um valor de (a ** i) mod n
            # que não é congruente a i (mod n), para algum i no intervalo [0, n-1]
            x = pow(a, d, self.number)
            for _ in range(s):
                # Mais um passo necessário para encontrar testemunhas da composição de n, iterativamente.
                # Busca-se por raízes quadradas não triviais de 1 (mod n)
                y = pow(x, 2, self.number)
                # Se x não é congruente a 1 (mod n) ou -1 (mod n),
                # então x é uma raiz quadrada não trivial de 1 (mod n) e a é testemunha da composição de n
                if y == 1 and x != 1 and x != (self.number - 1):
                    return f"{self.number}\n é composto\n"
                x = y
            # Verifica o mesmo para o último valor de y calculado
            if y != 1:
                return f"{self.number}\n é composto\n"
        return f"{self.number}\n provavelmente é primo\n"

        # Apesar de mais robusto do que o Teste de Primalidade de Fermat,
        # ainda assim existe a possibilidade de n ser um pseudoprimo e passar no teste,
        # porém com 40 rounds a probabilidade do pseudoprimo passar no teste
        # é de 1 em 2 ** 80, o que é considerado suficientemente seguro