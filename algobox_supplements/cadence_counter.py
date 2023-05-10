import tkinter as tk

class CounterApp:
    def __init__(self, root):
        self.counter = 0
        self.root = root
        self.root.geometry('200x100')
        self.root.title('CADENCE COUNTER')
        self.root.configure(bg='black')
        self.root.resizable(0, 0)

        # counter display
        self.counter_disp = tk.Label(root, text=str(self.counter), bg='black', fg='white')
        self.counter_disp.pack(side=tk.LEFT)

        # frame for buttons
        button_frame = tk.Frame(root, bg='black')
        button_frame.pack(side=tk.RIGHT)

        # increment button
        self.inc_button = tk.Button(button_frame, text='+', command=self.increment, fg='black', bg='white')
        self.inc_button.pack()

        # clear button
        self.clear_button = tk.Button(button_frame, text='clear', command=self.clear, fg='black', bg='white')
        self.clear_button.pack()

        # decrement button
        self.dec_button = tk.Button(button_frame, text='-', command=self.decrement, fg='black', bg='white')
        self.dec_button.pack()

    def increment(self):
        self.counter += 1
        self.update_counter()

    def clear(self):
        self.counter = 0
        self.update_counter()

    def decrement(self):
        self.counter -= 1
        self.update_counter()

    def update_counter(self):
        self.counter_disp['text'] = str(self.counter)

if __name__ == "__main__":
    root = tk.Tk()
    app = CounterApp(root)
    root.mainloop()
