from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image

labelStr = '''
[b]Kivy Logo[/b]
    test test test
'''


class TestApp(App):
    def build(self):
        self.title = 'Kivy Logo'
        # title窗口标题

        layout = GridLayout(cols=1)
        # gridLayout网格布局,cols列数

        lab = Label(text=labelStr, markup=True,
                    font_size='30sp', size_hint_y=None, height=100)
        # 开启markup语法支持.字体大小:30sp.高度:100

        img = Image(source='image/1.jpg')

        layout.add_widget(lab)
        layout.add_widget(img)
        return layout


if __name__ == '__main__':
    TestApp().run()
