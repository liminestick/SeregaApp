from kivy.app import App
from kivy.config import Config
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
import time
import webbrowser


class MainWindow(Screen):

    def open_link(self, link):
        self.ids.my_image.source = 'komandir_button_press.png'
        webbrowser.open(link)
    def button_off(self):
        self.ids.my_image.source = 'komandir_button.png'



class WindowManager(ScreenManager):
    pass


# Настройки окна
Config.set('graphics', 'width', '540')
Config.set('graphics', 'height', '960')
Config.set('graphics', 'resizable', '0')

kv = Builder.load_file('interface.kv')


class MyApp(App):
    def build(self):
        return kv


if __name__ == '__main__':
    MyApp().run()
