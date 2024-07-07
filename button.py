class Button():
    def __init__(self, title_text, x, y):
        self.title = title_text
        self.x = x
        self.y = y
        self.appearance = True
    def hide(self):
        self.appearance = False
    def show(self):
        self.appearance = True
    def print_info(self):
        print("Дані про віджет:")
        print(self.title, self.x, self.y, self.appearance)




button1 = Button("ok", 100, 100)
button1.print_info()
button1.hide()
button1.print_info()



