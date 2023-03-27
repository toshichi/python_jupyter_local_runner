import ipywidgets as widgets
from IPython.display import display, HTML, FileLink
from io import BytesIO

class App:
    def __init__(self):
        self.button = widgets.Button(
            description='Your UI'
        )
        self.button.on_click(self.on_button)

        display(self.button)
        
    def on_button(self, button):
        print("Button clicked")

if __name__ == '__main__':
    app = App()
