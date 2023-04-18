import time
from lcg import LCG
from miller_rabin import MillerRabin
from fermat import Fermat

# Instancia um LCG para gerar números com comprimento de bits especificado
mult = 10509375158889068245 # Altere aqui os parametros
incr = 10509375158889068245
bits = 4096 # e o numero de bits desejado
lcg = LCG(mult, incr, bits)

# Inicia a contagem do tempo
start_time = time.monotonic()

# Gera e testa os numeros, até achar um primo
while True:
    # Gera um candidato
    candidate = lcg.generate() | (1 << (bits - 1)) | 1 # Garante o número de bits
    print(f"Candidato: {candidate}\n")

    # Verifica se o candidato é par
    if candidate % 2 == 0:
        print(f"Candidato par. Gerando outro...")
        continue
    
    '''
    # Executa o teste de Miller-Rabin no candidato
    miller_rabin = MillerRabin(candidate, 40)
    result = miller_rabin.primality_test()
    '''

    # Executa o teste de Fermat no candidato
    fermat = Fermat(candidate, 40)
    result = fermat.primality_test()

    # Verifica se candidato passou no teste
    if "provavelmente é primo" in result:
        print(f"{candidate} é primo!\n")
        break

end_time = time.monotonic()
time_taken = end_time - start_time

print(f"Tempo gasto para gerar: {time_taken} s\n")
