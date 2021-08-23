from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.core.text import LabelBase
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout

# -*- coding: utf-8 -*-


LabelBase.register(name='Font_Hanzi', fn_regular='./fonts/STKAITI.ttf')

global i
i = 0
Builder.load_string('''
<GridLayout>
    canvas.before:
        BorderImage:
            # BorderImage behaves like the CSS BorderImage
            border: 0, 0, 0, 0
            source: 'image/1.jpg'
            pos: self.pos
            size: self.size
<RootWidget>
    GridLayout:
        # size_hint: .9, .9
        pos_hint: {'center_x': .5, 'center_y': .5}
        rows:1
        Label:
            id:sa                                                   #设置id为sa
            canvas.before:
                Rectangle:
                    pos: [0,0]
                    size: self.width-20,100
                    source: 'image/1.png'
            text: "今天又一不小心看动漫到这么晚了，好想去二次元啊~"
            text_size: self.width-200, self.height-100
            valign: 'bottom'
            font_name: 'Font_Hanzi'
            on_touch_down: root.hulk_smash()                 
            #点击时调用根元素（RootWidget）的hulk_smash()方法
''')


class RootWidget(FloatLayout):
    def hulk_smash(self):
        global i
        i += 1
        switch = {
            1: "。。。。。。",
            2: "。。。",
            3: ""
        }

        self.ids.sa.text = switch.get(i, '000')  # 获取id为sa的元素并设置text为ss


class MainApp(App):
    def build(self):
        sound = SoundLoader.load('music/1.mp3')
        sound.play()
        return RootWidget()


if __name__ == '__main__':
    MainApp().run()
