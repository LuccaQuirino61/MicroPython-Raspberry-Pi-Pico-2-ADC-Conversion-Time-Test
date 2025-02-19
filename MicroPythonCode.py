#The comments made in this code are in Portugues. So you can translate them if necessary.

# O algorítmo está programado para executar 100 períodos de ciclo do PWM. Se quiser alterar, mude a variável "MAX_MEDIDAS"
import machine
import utime

# Configuração dos ADCs
adc1 = machine.ADC(1)  # Canal ADC1
adc2 = machine.ADC(2)  # Canal ADC2

# Configuração do PWM no pino 21
pwm = machine.PWM(machine.Pin(21))
pwm.freq(50_000)  # Frequência de 50 kHz
pwm.duty_u16(32768)  # 50% de duty cycle

# Buffers para armazenar leituras do ADC
buffer_adc1 = []
buffer_adc2 = []
buffer_tempos = []

contador = 0
MAX_MEDIDAS = 100

# Interrupção acionada pelo PWM no início de cada ciclo 
def pwm_isr(timer):
    global contador

    if contador >= MAX_MEDIDAS:
        pwm.deinit()  # Desativa o PWM após 100 períodos
        return

    t_inicio = utime.ticks_us()  # Marca o tempo antes da leitura do ADC

    # Leitura simultânea dos 2 ADCs
    valor_adc1 = adc1.read_u16()
    valor_adc2 = adc2.read_u16()

    t_fim = utime.ticks_us()  # Marca o tempo após a leitura
    tempo_conversao = t_fim - t_inicio

    # Armazena as leituras e tempo de conversão
    buffer_adc1.append(valor_adc1)
    buffer_adc2.append(valor_adc2)
    buffer_tempos.append(tempo_conversao)

    contador += 1

# Configurar um Timer para chamar a interrupção no início de cada ciclo PWM
timer = machine.Timer()
timer.init(freq=50_000, mode=machine.Timer.PERIODIC, callback=pwm_isr)

# Esperar as medições terminarem antes de exibir os resultados
while contador < MAX_MEDIDAS:
    utime.sleep_us(1)  # Pequeno delay para evitar uso excessivo da CPU

# Calcular média do tempo de conversão
tempo_medio = sum(buffer_tempos) / len(buffer_tempos)
print(buffer_tempos)
print(f"Tempo médio de conversão: {tempo_medio:.2f} us")
