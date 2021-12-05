import threading

import kivy
kivy.require('2.0.0')
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from threading import Timer
import time

#Window.clearcolor = get_color_from_hex("ffffff")

lugar = 0

class Raiz(FloatLayout):

# variável lugar para saber momento do programa (lugar: 1 (raiz), 2(telainst), 3 (iet))

    def on_press_btinst(self):
        janela.root_window.remove_widget(janela.root)
        janela.root_window.add_widget(TelaInst())


class TelaInst(FloatLayout):

    def on_press_btini(self):
        janela.root_window.remove_widget(janela.root)
        janela.root_window.add_widget(TelaEst())
        self.remove_widget(self.ids.instru)
        self.remove_widget(self.ids.btini)

class TelaEst(FloatLayout):


    ### definir qual etapa do treino (1 a 5)

    fase = [1, 2, 3, 4, 5]

    ### definir se tentativa FF1 (1) ou FF2 (2)

    tentype = [1, 1, 2, 2]

    ### se tentype = 1 e fase = 1, então:

    estfase11 = ['ff1', '1v1', 'ec', '2v3']

    ### se tentype = 1 e fase = 2, então:

    estfase21 = ['ff1', '1v2', 'ec', '2v3']

    ### se tentype = 1 e fase = 3, então:

    estfase31 = ['ff1', '1v3', 'ec', '2v3']

    ### se tentype = 1 e fase = 4, então:

    estfase41 = ['ff1', '1v4', 'ec', '2v3']

    ### se tentype = 1 e fase = 5, então:

    estfase51 = ['ff1', '1v5', 'ec', '2v3']

    ### se tentype = 2 e fase = 2, então:

    estfase12 = ['ff2', '2v1', 'ec', '1v3']

    ### se tentype = 2 e fase = 2, então:

    estfase22 = ['ff2', '2v2', 'ec', '1v3']

    ### se tentype = 2 e fase = 2, então:

    estfase32 = ['ff2', '2v3', 'ec', '1v3']

    ### se tentype = 2 e fase = 2, então:

    estfase42 = ['ff2', '2v4', 'ec', '1v3']

    ### se tentype = 2 e fase = 2, então:

    estfase52 = ['ff2', '2v5', 'ec', '1v3']


    def on_press_bt1(self):
        janela.root_window.remove_widget(janela.root)
        janela.root_window.add_widget(TelaIET())
        self.remove_widget(self.ids.est1)
        self.remove_widget(self.ids.est2)
        self.remove_widget(self.ids.est3)
        self.remove_widget(self.ids.est4)
        time.sleep(1)

    def on_press_bt2(self):
        pass
    def on_press_bt3(self):
        pass
    def on_press_bt4(self):
        pass


class TelaIET(FloatLayout):

### função para retornar a tela de estímulos

    def reiniciar(self):
        janela.root_window.remove_widget(janela.root)
        janela.root_window.add_widget(TelaEst())


    #def reiniciar(self):
    #    time.sleep(4)
    #    return TelaEst()

#    if lugar(1):
#        reiniciar()
#    else:
#        pass

    # if telaest.lugar == 1(True):
    #    time.sleep(6)
    #else:
    #    time.sleep(6)
    #    reiniciar()



#  if a.lugar == 3:
   #     def novatentativa(self):
   #         return TelaInst()


        #iet_start = time.time()
        #iet_end = time.time()
        #iet_duration = iet_end - iet_start


class ExpApp(App):

    def build(self):
        return Raiz()



lugar = ExpApp()
janela = ExpApp()

janela.run()