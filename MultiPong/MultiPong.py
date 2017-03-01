from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget


class MultiPong(App):
    def build(self):
        top = Widget()
        top.add_widget(Label(text='Hello there'))
        return top

if __name__ == "__main__":
    MultiPong().run()