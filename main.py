from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text="CSV_App initial test")

if __name__ == "__main__":
    MyApp().run()    
