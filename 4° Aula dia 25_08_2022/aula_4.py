import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget

class MyWidget(Widget):
    pass

class aula_4(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    aula_4().run()