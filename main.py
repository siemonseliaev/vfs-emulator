import tkinter as tk #сам GUI
import shlex #работа с командной строкой

First_string = "Начальная строка в ковычках (VFS)"

class Emulator(tk.Tk):
    def __init__(self): # инициализируем (объект)
        super().__init__()#вызов родительского класса

        self.title("Название файла")

        #вид текста
        self.output = tk.Text(self, height=20, width=80, bg="black", fg="white")
        self.output.pack(fill = tk.BOTH, expand = True)

        # Строка ввода
        self.entry = tk.Entry(self, bg="white", fg="black", insertbackground="white")
        self.entry.pack(fill =tk.X)
        self.entry.bind("<Return>", self.on_enter) #команда отработки ф-и при энтер

        # Первое приглашение
        self.show_first_str()

    def show_first_str(self):
        self.output.insert(tk.END, f"{First_string}")
        self.output.see(tk.END)

    def on_enter(self, event = None):
        my_text = self.entry.get() #получаем введенный текст
        self.entry.delete(0, tk.END)#удаляем все введенные символы

        self.output.insert(tk.END, my_text + "\n")#работа с несколькими словами

        try:
            args = shlex.split(my_text) #разделение текста
        except: #иначе
            self.output.insert(tk.END, f"Ошибка работы программы \n")
            self.show_first_str()
            return

        if not args:
            self.show_first_str()
            return

        command = args[0]
        command_args = args[1:]

        self.parser(command, command_args)
        self.show_first_str()

    def parser(self, command, args): # 3
        if command == "help": # список
            self.output.insert(tk.END,
                "Команды:\n"
                "help - показать эту справку\n"
                "cd - ввести 1 элемент через \ \n" #5
                "Is - ввести массив элементов через \ \n" #5
                "exit - выйти из программы\n" #6
            )

        elif (command == "cd"):
            if len(args) != 1:
                self.output.insert(tk.END, "Необходим один аргумент\n")
            else:
                self.output.insert(tk.END, f"cd {args}\n")
        elif command == "Is":
            self.output.insert(tk.END, f"ls {args}\n")
        elif command == "exit":
            self.destroy()
        else: #4
            self.output.insert(tk.END, "Ошибка, попробуйте ввести строку снова\n")


if __name__ == "__main__":
    app = Emulator()
    app.mainloop()

