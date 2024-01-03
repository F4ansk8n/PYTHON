class Restaurante():

    def __init__(self, clientes, funcionarios,):
        self.pedido_anotado = False
        self.funcionario = None
        self.clientes = clientes 
        self.cliente_chegou = False 
        self.funcionarios = funcionarios
        self.pedido= None
    def reserva_cliente(self,mesa, horario_reserva,nome):
        print(f'O cliente {nome} reservou o horario: {horario_reserva} na mesa: {mesa}')

    def chegou(self):
        self.cliente_chegou = True

    def anotar_pedido(self):
        pedido_cliente = input('Faça o seu pedido: ')
        self.pedido = pedido_cliente
        return self.pedido

    def set_pedido_anotado(self):
        self.pedido_anotado = True
            
    def funcionario_atender(self):
        if self.cliente_chegou == True:
            # anotar_pedido()
            if self.pedido == 'arroz':
                print('Pedido anotado')
                self.set_pedido_anotado()

            if self.pedido_anotado == True:
                print('Preparar comida')
        # funcionario_atender()


restaurate = Restaurante(1, 10)

restaurate.chegou()
restaurate.reserva_cliente(1, '19:30', 'Mikael')
restaurate.anotar_pedido()
# restaurate.pedido_anotado()
restaurate.funcionario_atender()