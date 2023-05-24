class MaquinaMealy:
    def __init__(self):
        self.estados = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5']  
        self.alfabeto = [25, 50, 100]
        self.transicoes = {
            'q0': {25: ('q1', 0), 50: ('q2', 0), 100: ('q4', 1)}, 
            'q1': {25: ('q3', 0), 50: ('q2', 0), 100: ('q4', 1)},
            'q2': {25: ('q1', 0), 50: ('q2', 0), 100: ('q3', 1)},
            'q3': {25: ('q5', 0), 50: ('q2', 0), 100: ('q4', 1)},
            'q4': {25: ('q1', 0), 50: ('q2', 0), 100: ('q3', 1)},
            'q5': {25: ('q1', 0), 50: ('q2', 0), 100: ('q3', 1)}
        }
        self.estado_inicial = 'q0'
        self.estados_finais = ['q3', 'q4'] 

    def processar_entrada(self, sequencia_entrada):
        estado = self.estado_inicial
        sequencia_saida = []
        soma_cumulativa = 0

        for simbolo in sequencia_entrada:

            proximo_estado, saida = self.transicoes[estado][simbolo]
            soma_cumulativa += simbolo

            if soma_cumulativa >= 100:
                proximo_estado = 'q4'
                saida = 1
                soma_cumulativa -= 100

            print(f"({estado}, {simbolo}) -> {proximo_estado}")
            print(f"({estado}, {simbolo}) -> {saida}")
            print("")
            sequencia_saida.append(saida)
           
            estado = proximo_estado

        return sequencia_saida

sequencia_entrada = [25, 25, 50, 50, 25, 25, 50, 25, 50, 100, 25, 50]
# [25, 25, 50, 50, 50, 25, 25, 25, 25, 50, 25, 50, 100, 25, 50, 100]
#  [50, 25, 50, 100, 25, 50, 100]
maquina = MaquinaMealy()
sequencia_saida = maquina.processar_entrada(sequencia_entrada)

print(f"Sequencia de entrada: {sequencia_entrada}")
print(f"Sequencia de saida:   {sequencia_saida}")

