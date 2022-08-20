from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from playsound import playsound

Window.size = (320, 240)


class HondaButton(Widget):
    def button_pressed(self):
        print("VTEC kicked in, yo!")
        # playsound error 260 workaround
        done = False
        while not done:
            try:
                playsound("vtec.mp3")
                done = True
            except:
                pass


class HondaScreen(Widget):
    pass


class VTECButtonApp(App):
    def build(self):
        return HondaScreen()


if __name__ == '__main__':
    VTECButtonApp().run()
