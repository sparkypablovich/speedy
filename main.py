import tkinter as ttk
from timeit import default_timer as timer 
import random
import codecs

class SpeedTypingTest:
    
    def __init__(self, root: ttk.Tk):
         # настройка темы
        self.darkmode = '#161a1e'
        self.textcolor = '#e6e6e6'
        self.errcolor = '#cb2821'
        self.start_timer = 0
         # создание окна
        self.root = root
        self.root.title('Speed Typing Test')
        self.root.geometry("1000x600")

        icon = ttk.PhotoImage(file="icon.png")
        self.root.iconphoto(False, icon)

        self.root.configure(background=self.darkmode)
        
        self.setup_ui()

    def setup_ui(self):
        """Set up the UI components."""

         # рамка для вывода времени
        self.timelabel = ttk.Label(self.root, foreground=self.textcolor, background=self.darkmode, text='Приготовься!', font=10, height=5, )
        self.timelabel.pack()
         # вывод текста
        self.label = ttk.Label(self.root, foreground=self.textcolor, background=self.darkmode, text='Для запуска теста нажимайте кнопку "Начать тест".\nПосле написания нажмите клавишу Enter\nНе забудте нажать на строку ввода ;)', borderwidth=50, font=30)
        self.label.pack()
         # поле ввода
        self.entry = ttk.Entry(self.root)
        self.entry.configure(width=100, justify='center')
        self.entry.pack(anchor='center', padx=8, pady= 8)
         # кнопка start
        self.start_button = ttk.Button(self.root, background=self.textcolor, text="Начать тест", font=5, width=10, height=2, border=15, command=self.reset_test)
        self.start_button.pack(anchor='center', padx=10, pady=20)
         # поле ввода
        self.label_ent = ttk.Label(self.root, foreground=self.textcolor, background=self.darkmode, text='', borderwidth=30, font=15)
        self.label_ent.pack()
        self.root.bind('<Return>', self.write_text)
         # вывод результата
        self.mistakes = ttk.Label(self.root, foreground=self.textcolor, background=self.darkmode, text='', font=15)
        self.mistakes.pack()

    def check_result(self, timer):
        """Check if the typed sentence matches the displayed one and show the result."""

        if self.label['text'] != self.label_ent['text']:
            self.mistakes.config(text='В предложении есть ошибки. Попробуйте еще раз.', foreground=self.errcolor)
        else:
            wpm = round((len(self.label_ent['text']) / 5) / (timer / 60), 2)
            self.mistakes.config(text='Слов в минуту: ' + str(wpm))

    def reset_test(self):
        """Reset the test with a new sentence and restart the timer."""
        
        self.label.config(text=self.random_sentense())
        self.timelabel.config(text='...')
        self.label_ent.config(text='')
        self.mistakes.config(text='')
        self.entry.delete('0', 'end')
        self.entry.config(text='')
        self.start_timer = timer()

    # вывод результата после нажатия Enter
    def write_text(self, event):
        self.label_ent.config(text=self.entry.get())
        self.entry.delete('0', 'end')
        result_timer = round(timer() - self.start_timer, 2)
        self.check_result(result_timer)
        
        self.timelabel.config(text='Время: ' + str(result_timer))
        self.start_timer = 0

    # выбор случайного предложения
    def random_sentense(self):
        n = random.randint(0, 520)
        path = 'database\\' + str(n) + '_sentence.txt'
        with codecs.open(path, 'r', 'utf-8') as sentense:
            text = sentense.readline().strip('\n')
            return text

if __name__ == "__main__":
    root = ttk.Tk()
    app = SpeedTypingTest(root)
    root.mainloop()