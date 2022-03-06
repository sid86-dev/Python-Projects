import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class Sid_grid(GridLayout):
    def __init__(self, **kwargs):
        super(Sid_grid, self).__init__()
        self.cols = 2

        self.add_widget(Label(text="Your name: "))
        self.s_name = TextInput(multiline=True)
        self.add_widget(self.s_name)

        self.add_widget(Label(text="Your Role: "))
        self.s_role = TextInput(multiline=True)
        self.add_widget(self.s_role)


        self.add_widget(Label(text="Your Address: "))
        self.s_adress = TextInput(multiline=True)
        self.add_widget(self.s_adress)

class Sid_App(App):
    def build(self):
        return Sid_grid()


if __name__ == '__main__':
    Sid_App().run()
