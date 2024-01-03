class FoneDeOuvido:

    def get_volume(self):
        print('Entrei no get')
        return self.__volume
    
    def set_volume(self, novo_volume):
        self.__volume = novo_volume
        print('Entrei no set')

    # Para o property funcionar e preciso que a variavel tenha '__', tanto, no get como no set 
    volume = property(get_volume, set_volume) 

fone = FoneDeOuvido() # get

fone.volume = 200 # set

print(fone.volume) # get