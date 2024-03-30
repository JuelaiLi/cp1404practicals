from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder


class DynamicLabelsApp(App):
    def build(self):

        return Builder.load_file('dynamic_labels.kv')

    def on_start(self):

        main_layout = self.root.ids['main']

        names_list = ['Alice', 'Bob', 'Charlie', 'Diana']

        for name in names_list:
            label = Label(text=name)
            main_layout.add_widget(label)


if __name__ == '__main__':
    DynamicLabelsApp().run()
