class Widget():
    def __init__(self, text, x, y,):
        self.text = text
        self.x = x
        self.y = y


    def print_info(self):
        print("Напис:", self.text)
        print("Росташування:", self.x, self.y)


class Button(Widget):
    def __init__(self, text, x, y, is_clicked):
        super().__init__(text, x, y)
        self.is_clicked = is_clicked


    def click(self):
        self.is_clicked = True
        print("Ви зареєстровані")



button1 = Button("Брати участь", 100, 100, False)
button1.print_info()


question = input("Хочете зареєструватися? (так / ні):") 
if question.lower() == "так":
   button1.click()
else:
    print("А шкода!")






        

        
