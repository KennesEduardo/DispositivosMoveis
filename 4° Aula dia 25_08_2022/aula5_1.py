from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Incrementar(BoxLayout):
    pass

class Aula5_1(App):
    def build(self):
        return Incrementar()
    
if __name__ == "__main__":
    Aula5_1().run()    