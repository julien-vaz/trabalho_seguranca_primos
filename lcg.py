import time # Para calcular o tempo gasto e gerar a semente


class LCG:
    # Parametros
    def __init__(self, mult, incr, bits):
        self.a = mult
        self.c = incr
        self.m = 2 ** bits - 1 # Escolhi usar um Mersenne Prime como módulo
        self.state = int(time.time())
        # Parametro adicional para controlar o numero de bits
        self.bits = bits

    # Funcao geradora
    def generate(self):
        self.state = (self.a * self.state + self.c) % self.m
        return self.state & ((1 << self.bits) - 1)

# Funcao global para salvar os numeros gerados em um TXT
def save_as_txt(bits, lcg):
    numbers = open(f"lcg_numbers_{bits}.txt", "w")
    numbers.write("Number, Bits, Time required (s)\n")
    for _ in range(100):
        start_time = time.monotonic()
        number = lcg.generate()
        end_time = time.monotonic()

        # Calculo do tempo gasto
        time_taken = end_time - start_time

        numbers.write(f"{number}, {number.bit_length()}, {time_taken:.6f}\n")
    numbers.close()

# -----------------------------------------------------------

# Parametros para numeros de 40 bits
mult = 1664525
incr = 1013904223
bits = 40

# Gerador de 40 bits
lcg_40 = LCG(mult, incr, bits)

# Salvo os numeros gerados em um TXT, para analise posterior
save_as_txt(bits, lcg_40)

#-------------------------------------------------------------

# Parametros para numeros de 56 bits
mult = 1103515245
incr = 12345
bits = 56

# Gerador de 56 bits
lcg_56 = LCG(mult, incr, bits)

# Salvo os numeros gerados em um novo TXT, para analise posterior
save_as_txt(bits, lcg_56)

# --------------------------------------------------------------

# Parametros para numeros de 80 bits
mult = 6364136223846793005
incr = 1442695040888963407
bits = 80

# Gerador de 80 bits
lcg_80 = LCG(mult, incr, bits)

# Salvo os numeros gerados em um novo TXT, para analise posterior
save_as_txt(bits, lcg_80)

# ---------------------------------------------------------------

# Parametros para numeros de 128 bits
mult = 4294957665
incr = 1372765723
bits = 128

# Gerador de 128 bits
lcg_128 = LCG(mult, incr, bits)

# Salvo os numeros gerados em um novo TXT, para analise posterior
save_as_txt(bits, lcg_128)

# -----------------------------------------------------------------

# Parametros para numeros de 168 bits
mult = 103067
incr = 123456789
bits = 168

# Gerador de 168 bits
lcg_168 = LCG(mult, incr, bits)

# Salvo os numeros gerados em um novo TXT, para analise posterior
save_as_txt(bits, lcg_168)

# -----------------------------------------------------------------

# Parametros para numeros de 224 bits
mult = 1125899906842597
incr = 987654321
bits = 224

# Gerador de 224 bits
lcg_224 = LCG(mult, incr, bits)

# Salvo os numeros gerados em um novo TXT, para analise posterior
save_as_txt(bits, lcg_224)

# -----------------------------------------------------------------

# Parametros para numeros de 256 bits
mult = 1103515245
incr = 12345
bits = 256

# Gerador de 256 bits
lcg_256 = LCG(mult, incr, bits)

# Salvo os numeros gerados em um novo TXT, para analise posterior
save_as_txt(bits, lcg_256)

# -----------------------------------------------------------------

# Parametros para numeros de 512 bits
mult = 69069687767179458030604164730607065059
incr = 2531011
bits = 512

# Gerador de 512 bits
lcg_512 = LCG(mult, incr, bits)

# Salvo os numeros gerados em um novo TXT, para analise posterior
save_as_txt(bits, lcg_512)

# -----------------------------------------------------------------

# Parametros para numeros de 1024 bits
mult = 6193318378121905469
incr = 284470788008853
bits = 1024

# Gerador de 1024 bits
lcg_1024 = LCG(mult, incr, bits)

# Salvo os numeros gerados em um novo TXT, para analise posterior
save_as_txt(bits, lcg_1024)

# -----------------------------------------------------------------

# Parametros para numeros de 2048 bits
mult = 9949325612958798629
incr = 9949325612958798629
bits = 2048

# Gerador de 2048 bits
lcg_2048 = LCG(mult, incr, bits)

# Salvo os numeros gerados em um novo TXT, para analise posterior
save_as_txt(bits, lcg_2048)

# -----------------------------------------------------------------

# Parametros para numeros de 4096 bits
mult = 10509375158889068245
incr = 10509375158889068245
bits = 4096

# Gerador de 4096 bits
lcg_4096 = LCG(mult, incr, bits)

# Salvo os numeros gerados em um novo TXT, para analise posterior
save_as_txt(bits, lcg_4096)
