import tkinter as tk
import shlex 

First_string = "Начальная строка в ковычках (VFS)"

class Emulator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Название файла")

        #вид текста
        self.output = tk.Text(self, height=20, width=80, bg="black", fg="white")
        self.output.pack(fill = tk.BOTH, expand = True)

        # Строка ввода
        self.entry = tk.Entry(self, bg="white", fg="black", insertbackground="white")
        self.entry.pack(fill =tk.X)
        self.entry.bind("<Return>", self.on_enter) 

        # Первое приглашение
        self.show_first_str()

    def show_first_str(self):
        self.output.insert(tk.END, f"{First_string}")
        self.output.see(tk.END)

    def on_enter(self, event = None):
        my_text = self.entry.get() 
        self.entry.delete(0, tk.END)
        self.output.insert(tk.END, my_text + "\n")

        try:
            args = shlex.split(my_text)
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

    def parser(self, command, args):
        if command == "help": # список
            self.output.insert(tk.END,
                "Команды:\n"
                "help - показать эту справку\n"
                "cd - ввести 1 элемент через \ \n" 
                "Is - ввести массив элементов через \ \n"
                "exit - выйти из программы\n" 
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
        else: 
            self.output.insert(tk.END, "Ошибка, попробуйте ввести строку снова\n")


if __name__ == "__main__":
    app = Emulator()
    app.mainloop()

