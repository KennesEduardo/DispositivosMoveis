from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Atividades(BoxLayout):
    def __init__(self, atividades):
        for ativ in atividades:
            super().__init__()
            self.add_widget(Label(text=ativ,font_size=30))
            
class Aula5_2(App):
    def build(self):
        return Atividades(['Andar', 'Correr', 'Camaninhar', 'Pular'])
    
if __name__ == "__main__":
    Aula5_2().run()    