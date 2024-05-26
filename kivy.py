from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import boxlayout

class MyApp(App):
    def build(self):
        layout = boxloyaaout()
        label1 = Label(text='Hello world')
        label2 = Label(text='Button 2')
        layout.add_widget(label1)
        layout.add_widget(label2)
        
        return Label(text='Hello World')

if __name__ == '__main__':
    MyApp().run()
