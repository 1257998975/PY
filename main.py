from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.core.audio import SoundLoader
from kivy.core.text import LabelBase
from kivy.core.image import Image as CoreImage

# -*- coding: utf-8 -*-


LabelBase.register(name='Font_Hanzi', fn_regular='./fonts/STKAITI.ttf')

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
        # Label:
        #     text: "I don't suffer from insanity, I enjoy every minute of it"
        #     text_size: self.width-20, self.height-20
        #     valign: 'top'
        # Label:
        #     text: "When I was born I was so surprised; I didn't speak for a year and a half."
        #     text_size: self.width-20, self.height-20
        #     valign: 'middle'
        #     # halign: 'center'
        Label:
            canvas.before:
                Rectangle:
                    pos: [0,0]
                    size: self.width-20,100
                    source: 'image/1.png'
            text: "今天又一不小心看动漫到这么晚了，好想去二次元啊~"
            text_size: self.width-200, self.height-100
            valign: 'bottom'
            font_name: 'Font_Hanzi'
''')


class RootWidget(FloatLayout):
    pass


class MainApp(App):
    def build(self):
        sound = SoundLoader.load('music/1.mp3')
        sound.play()
        return RootWidget()


if __name__ == '__main__':
    MainApp().run()
