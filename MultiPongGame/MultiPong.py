from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
#from kivy.core.window import Window


class MultiPong(App):
    def build(self):
        top = Widget()
        top.add_widget(Label(center=top.center, text='Hello there\nnanners city!'))
        #Window.size = top.children[0].size
        return top

if __name__ == "__main__":
    MultiPong().run()