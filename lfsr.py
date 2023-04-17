import time


class LFSR:
    def __init__(self, bits, taps):
        self.state = 1 << bits | 1
        self.taps = taps
        # Parametro adicional para controlar o numero de bits
        self.bits = bits
    
    def generate(self):
        # Calcula o XOR dos bits tocados
        xor = 0
        for tap in self.taps:
            xor ^= (self.state >> tap) & 1
        
        # Desloca state e adiciona o resultado de XOR ao bit menos significativo
        self.state = (self.state >> 1) | (xor << (self.bits - 1))
        
        return self.state

# Funcao global para salvar os numeros gerados em um TXT
def save_as_txt(bits, lfsr):
    numbers = open(f"lfsr_numbers_{bits}.txt", "w")
    numbers.write("Number, Bits, Time required (s)\n")
    for _ in range(100):
        start_time = time.monotonic()
        number = lfsr.generate()
        end_time = time.monotonic()

        # Calculo do tempo gasto
        time_taken = end_time - start_time

        numbers.write(f"{number}, {number.bit_length()}, {time_taken:.6f}\n")
    numbers.close()

# -----------------------------------------------------------

# REFERENCE: Xilinx Application Note by Peter Alfke XAPP 052 July 7,1996 (Version 1.1)

# Parametros para numeros de 40 bits
bits = 40
taps = [40,38,21,19]

# Gerador de 40 bits
lfsr_40 = LFSR(bits, taps)

# Salvo os numeros gerados em um TXT, para analise posterior
save_as_txt(bits, lfsr_40)

#-------------------------------------------------------------

# Parametros para numeros de 56 bits
bits = 56
taps = [56,55,35,34]

# Gerador de 56 bits
lfsr_56 = LFSR(bits, taps)

# Salvo os numeros gerados em um novo TXT, para analise posterior
save_as_txt(bits, lfsr_56)

# --------------------------------------------------------------

# Parametros para numeros de 80 bits
bits = 80
taps = [80,79,43,42]

# Gerador de 80 bits
lfsr_80 = LFSR(bits, taps)

# Salvo os numeros gerados em um novo TXT, para analise posterior
save_as_txt(bits, lfsr_80)

# ---------------------------------------------------------------

# Parametros para numeros de 128 bits
bits = 128
taps = [128,126,101,99]

# Gerador de 128 bits
lfsr_128 = LFSR(bits, taps)

# Salvo os numeros gerados em um novo TXT, para analise posterior
save_as_txt(bits, lfsr_128)

# -----------------------------------------------------------------

# Parametros para numeros de 168 bits
bits = 168
taps = [168,166,153,151]

# Gerador de 168 bits
lfsr_168 = LFSR(bits, taps)

# Salvo os numeros gerados em um novo TXT, para analise posterior
save_as_txt(bits, lfsr_168)

# -----------------------------------------------------------------

# Parametros para numeros de 224 bits
bits = 224
taps = [223,220,210,209]

# Gerador de 224 bits
lfsr_224 = LFSR(bits, taps)

# Salvo os numeros gerados em um novo TXT, para analise posterior
save_as_txt(bits, lfsr_224)

# -----------------------------------------------------------------

# Parametros para numeros de 256 bits
bits = 256
taps = [255,251,247,246]

# Gerador de 256 bits
lfsr_256 = LFSR(bits, taps)

# Salvo os numeros gerados em um novo TXT, para analise posterior
save_as_txt(bits, lfsr_256)

# -----------------------------------------------------------------

# Parametros para numeros de 512 bits
bits = 512
taps = [511,507,503,499]

# Gerador de 512 bits
lfsr_512 = LFSR(bits, taps)

# Salvo os numeros gerados em um novo TXT, para analise posterior
save_as_txt(bits, lfsr_512)

# -----------------------------------------------------------------

# Parametros para numeros de 1024 bits
bits = 1024
taps = [1023,1019,1013,1009]

# Gerador de 1024 bits
lfsr_1024 = LFSR(bits, taps)

# Salvo os numeros gerados em um novo TXT, para analise posterior
save_as_txt(bits, lfsr_1024)

# -----------------------------------------------------------------

# Parametros para numeros de 2048 bits
bits = 2048
taps = [2047,2039,2035,2029]

# Gerador de 2048 bits
lfsr_2048 = LFSR(bits, taps)

# Salvo os numeros gerados em um novo TXT, para analise posterior
save_as_txt(bits, lfsr_2048)

# -----------------------------------------------------------------

# Parametros para numeros de 4096 bits
bits = 4096
taps = [4095,4079,4073,4057]

# Gerador de 4096 bits
lfsr_4096 = LFSR(bits, taps)

# Salvo os numeros gerados em um novo TXT, para analise posterior
save_as_txt(bits, lfsr_4096)
