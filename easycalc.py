import tkinter as tk


class EasyCalc:
    def __init__(self):
        self.root = tk.Tk()
        self.result = ""
        self.title = "EasyCalc"
        self.width = 300
        self.height = 400
        self.expression = tk.StringVar()
        self.operations = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: x / y,
        }

    def set_title(self, title):
        self.title = title

    def set_size(self, width, height):
        self.width = width
        self.height = height

    def add_operation(self, operation, callback):
        self.operations[operation] = callback

    def on_calculate(self):
        try:
            expression = self.expression.get()
            for op, func in self.operations.items():
                if op in expression:
                    x, y = (float(i) for i in expression.split(op))
                    self.result = func(x, y)
                    break
            self.expression.set(str(self.result))
        except Exception as e:
            self.expression.set("Error")

    def create_calculator(self):
        self.root.title(self.title)
        self.root.geometry(f"{self.width}x{self.height}")

        entry = tk.Entry(self.root, textvariable=self.expression, font=("Arial", 14))
        entry.grid(row=0, column=0, columnspan=4)

        button_font = ("Arial", 12)
        buttons = [
            ("1", 1, 1), ("2", 1, 2), ("3", 1, 3),
            ("+", 1, 4), ("4", 2, 1), ("5", 2, 2),
            ("6", 2, 3), ("-", 2, 4), ("7", 3, 1),
            ("8", 3, 2), ("9", 3, 3), ("*", 3, 4),
            ("0", 4, 1), ("C", 4, 2), ("/", 4, 3),
            ("=", 4, 4)
        ]

        for button in buttons:
            button_label = button[0]
            if button_label == "C":
                tk.Button(self.root, text=button_label,
                          font=button_font, command=lambda: self.expression.set("")).grid(row=button[1], column=button[2])
            elif button_label == "=":
                tk.Button(self.root, text=button_label,
                          font=button_font, command=self.on_calculate).grid(row=button[1], column=button[2])
            else:
                tk.Button(self.root, text=button_label,
                          font=button_font, command=lambda button_label=button_label: self.expression.set(self.expression.get() + button_label)).grid(row=button[1], column=button[2])

        self.root.mainloop()


easycalc = EasyCalc()

if __name__ == "__main__":
    import sys

    sys.modules["easycalc"] = easycalc