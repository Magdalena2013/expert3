from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image

class Main_App(App):
    def build(self):
        label = Image(source='C:/Users/Impact/Desktop/test.jpg',
                     size_hint=(1, 0.5),
                     pos_hint={'center_y': 0.5, 'center_x': 0.5})
        return label

Main_App().run()
