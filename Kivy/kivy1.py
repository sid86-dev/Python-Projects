import kivy
from kivy.app import App
from kivy.uix.label import Label

class Sid_app(App):
    def build(self):
        # display a text
        return Label(text="This is Sid's App")
if __name__ == '__main__':
        Sid_app().run()