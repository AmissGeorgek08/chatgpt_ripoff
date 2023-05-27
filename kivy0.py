#imports
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.popup import Popup

#main screen class
class MainScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        vl = BoxLayout(orientation='vertical')
        self.txt = Label(text= '')
        vl.add_widget(self.txt)
        hl_0 = BoxLayout(size_hint=(0.8, None), height='30sp')
        lbl1 = Label(text='Chat:', halign='right')
        self.input = TextInput(multiline=False)
        hl_0.add_widget(lbl1)
        hl_0.add_widget(self.input)
        vl.add_widget(hl_0)
        hl = BoxLayout(size_hint=(0.5, 0.2), pos_hint={'center_x': 0.5})
        btn_false = Button(text="Send")
        hl.add_widget(btn_false)
        vl.add_widget(hl)
        premium_btn = Button(text='Premium', size_hint=(None, None), size=('150sp', '50sp'), pos_hint={'x': 0.8, 'y': 0})
        premium_btn.bind(on_press=self.goto_premium)
        vl.add_widget(premium_btn)
        self.add_widget(vl)
        btn_false.bind(on_press=self.change_text)
    def change_text(self, *args):
        self.txt.text = "I am sorry I cannot talk with you right now, I am on high demand.\nPay 20$/mo for full access."
    def goto_premium(self, *args):
        self.manager.current = 'premium'

#2nd screen class
class PremiumScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        vl = BoxLayout(orientation='vertical')
        pay_btn = Button(text='Pay 20$', size_hint=(None, None), size=('150sp', '50sp'), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        pay_btn.bind(on_press=self.show_purchase_message)
        vl.add_widget(pay_btn)
        back_btn = Button(text='Back', size_hint=(None, None), size=('150sp', '50sp'), pos_hint={'center_x': 0.5, 'y': 0})
        back_btn.bind(on_press=self.goto_main)
        vl.add_widget(back_btn)
        self.add_widget(vl)
    def show_purchase_message(self, *args):
        vl = BoxLayout(orientation='vertical')
        lbl = Label(text='Thank you for your purchase', font_size=24)
        vl.add_widget(lbl)
        popup = Popup(title='Purchase', content=vl, size_hint=(0.6, 0.3))
        popup.open()
    def goto_main(self, *args):
        self.manager.current = 'main'

#app class
class ChatNotGPT(App):
    def build(self):
        sm = ScreenManager(transition=SlideTransition(direction='left'))
        sm.add_widget(MainScr(name='main'))
        sm.add_widget(PremiumScr(name='premium'))
        return sm
    def back(self, instance):
        self.root.transition.direction = 'right'
        self.root.current = self.root.previous()

#run command
ChatNotGPT().run()
