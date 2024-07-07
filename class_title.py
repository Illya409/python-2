class Title():
    def __init__(self, title_text, x, y):
        self.title = title_text
        self.x = x
        self.y = y
        self.appearance = appearance
    def hide(self):
        self.appearance = False
        print(self.title, "- приховано")
    def show(self):
        self.appearance = True
        print(self.title, "- відображається")
    def print_info(self):
        print("Кнопка:",self.title)
        print("Розташування:", "(" + str(self.x) + "," + str(self.y) + ")" )
        print("Видимість:", self.appearance)





main = ("Дізнатися переможця прямо зараз", 150, 50)
rules =("Переможець соже бути тільки один", 150, -100)

main.print_info()
rules.print_info()
rules.hide()

