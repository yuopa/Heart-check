# Создание и запуск приложения, программирование интерфейса экранов и действий на них

# Здесь должен быть твой код
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView

from instructions import *
from scrollLabel import ScrollLabel
from ruffier import *
from seconds import Seconds

p1, p2, p3 = 0, 0, 0


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        instr = ScrollLabel(ltext=txt_instruction)

        l1 = Label(text='Введите имя')
        self.user_name = TextInput()
        self.button = Button(text='Начать')
        self.button.background_color = (0, 1, 0, 1)
        self.button.on_press = self.next
        l2 = Label(text='Введите Ваш возраст')
        self.user_age = TextInput()


        line1 = BoxLayout(orientation='vertical', size_hint=(1, None), height='60sp')
        line2 = BoxLayout(orientation='vertical', size_hint=(1, None), height='60sp')

        line1.add_widget(l1)
        line1.add_widget(self.user_name)

        line2.add_widget(l2)
        line2.add_widget(self.user_age)

        


        main_line = BoxLayout(orientation='vertical', padding=8, spacing=8)

        main_line.add_widget(instr)
        main_line.add_widget(line1)
        main_line.add_widget(line2)
        main_line.add_widget(self.button)
        

        self.add_widget(main_line)

    def next(self):
        self.manager.current = 'test'



class TestScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


        instr = ScrollLabel(ltext=txt_test1)
        self.ltimer = Seconds(15)
        self.ltimer.bind(done=self.timer_end)
        
        self.start_button = Button(text='Начать')
        self.start_button.on_press = self.start_timer
        self.start_button.background_color = (0,0,1,1)

        l1 = Label(text='Запишите релузьтат')
        self.test1_input = TextInput()
        self.test1_input.set_disabled(True)



        line1 = BoxLayout(orientation='vertical', size_hint=(1, None), height='60sp')
        line1.add_widget(l1)
        line1.add_widget(self.test1_input)

        self.button = Button(text='Далее')
        self.button.background_color = (1, 0, 0, 1)
        self.button.set_disabled(True)
        self.button.on_press = self.next

        main_line = BoxLayout(orientation='vertical', padding=8, spacing=8)
        main_line.add_widget(instr)
        main_line.add_widget(self.ltimer)
        main_line.add_widget(self.start_button)
        main_line.add_widget(line1)
        main_line.add_widget(self.button)

        self.add_widget(main_line)

    def start_timer(self):
        self.ltimer.start()
        self.start_button.set_disabled(True)

    def timer_end(self, *args):
        self.test1_input.set_disabled(False)
        self.button.set_disabled(False)


    def next(self):
        global p1
        p1 = int(self.test1_input.text)
        self.manager.current = 'sitting'


class SitScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        instr = ScrollLabel(ltext=txt_sitting)

        self.button = Button(text='Далее')
        self.button.background_color = (1, 0, 0, 1)
        self.button.on_press = self.next

        main_line = BoxLayout(orientation='vertical', padding=8, spacing=8)
        main_line.add_widget(instr)
        main_line.add_widget(self.button)

        self.add_widget(main_line)

    def next(self):
        self.manager.current = 'test_result'


class Test2Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        instr = ScrollLabel(ltext=txt_test2)

        l1 = Label(text='Результат после приседаний:')
        self.test2_input = TextInput()
        
        l2 = Label(text='Результат после отдыха:')
        self.test3_input = TextInput()

        self.button = Button(text='Показать результат')
        self.button.background_color = (1, 0, 0, 1)
        self.button.on_press = self.next


        line1 = BoxLayout(orientation='vertical', size_hint=(1, None), height='60sp')
        line2 = BoxLayout(orientation='vertical', size_hint=(1, None), height='60sp')

        line1.add_widget(l1)
        line1.add_widget(self.test2_input)

        line2.add_widget(l2)
        line2.add_widget(self.test3_input)

        


        main_line = BoxLayout(orientation='vertical', padding=8, spacing=8)

        main_line.add_widget(instr)
        main_line.add_widget(line1)
        main_line.add_widget(line2)
        main_line.add_widget(self.button)
        

        self.add_widget(main_line)

    def next(self):
        global p2, p3
        p2 = int(self.test2_input.text)
        p3 = int(self.test3_input.text)
        self.manager.current = 'result'
        


class ResultScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.l = ScrollLabel(ltext='')

        self.add_widget(self.l)
        self.on_enter = self.before

    def before(self):
        index = ruffier_index(p1,p2,p3)
        self.l.label.text = '\nВаш индекс Руфье равен ' + str(index)

    




class RuffierTest(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(TestScreen(name='test'))
        sm.add_widget(SitScreen(name='sitting'))
        sm.add_widget(Test2Screen(name='test_result'))
        sm.add_widget(ResultScreen(name='result'))
        return sm






RuffierTest().run()