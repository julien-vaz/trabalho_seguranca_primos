import random


class Fermat:
    def __init__(self, number, rounds):
        self.number = number
        self.rounds = rounds

    def primality_test(self):
        # Verifica se o número é um dos dois primeiros primos
        if self.number == 2 or self.number == 3:
            return f"{self.number}\n é primo!\n"
        # Verifica se o número é 0 ou 1, ou se é par 
        if self.number <= 1 or self.number % 2 == 0:
            return f"{self.number}\n é composto\n"

        # Como se trata de um teste probabilistico,
        # quanto mais vezes repetirmos mais o resultado é confiável
        for _ in range(self.rounds):
            a = random.randint(2, self.number - 2) # Devido ao Teorema de Fermat, para qualquer n
                                                   # primo e qualquer inteiro a não divisivel por n,
                                                   # a ** (n-1) sempre sera congruente a 1 (mod n),
                                                   # porém se n for composto existem a para os quais
                                                   # a ** (n-1) é congruente a 1 (mod n), sendo n 
                                                   # um pseudoprimo. Escolhemos a entre
                                                   # 2 e n-2 justamente para diminuir a possibilidade
                                                   # de selecionarmos um pseudoprimo
            
            # Verifica se a ** (n-1) é incongruente a 1 (mod n). Se sim, n é certamente composto
            if pow(a, (self.number - 1), self.number) != 1:
                return f"{self.number}\n é composto\n"

        # Se não,
        return f"{self.number}\n provavelmente é primo!\n"

        # Ainda assim existe a possibilidade de n ser um pseudoprimo e passar no teste,
        # porém com 40 rounds a probabilidade do pseudoprimo passar no teste
        # é de 1 em 2 ** 80, o que é considerado suficientemente seguro
