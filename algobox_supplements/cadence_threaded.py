import tkinter as tk
from multiprocessing import Process

class CounterApp:
    def __init__(self, root):
        self.counter = 0
        self.root = root
        self.root.geometry('500x200')
        self.root.title('CADENCE COUNTER')
        self.root.configure(bg='black')

        # counter display
        self.counter_disp = tk.Label(root, text=str(self.counter), bg='black', fg='white', font=("", 45))
        self.counter_disp.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # frame for buttons
        button_frame = tk.Frame(root, bg='black')
        button_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # increment button
        self.inc_button = tk.Button(button_frame, text='+', command=self.increment, fg='black', bg='white', font=("", 45))
        self.inc_button.pack(fill=tk.BOTH, expand=True)

        # clear button
        self.clear_button = tk.Button(button_frame, text='clear', command=self.clear, fg='black', bg='white', font=("", 45))
        self.clear_button.pack(fill=tk.BOTH, expand=True)

        # decrement button
        self.dec_button = tk.Button(button_frame, text='-', command=self.decrement, fg='black', bg='white', font=("", 45))
        self.dec_button.pack(fill=tk.BOTH, expand=True)

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

def run_app():
    root = tk.Tk()
    app = CounterApp(root)
    root.mainloop()

if __name__ == "__main__":
    # Create a list to hold the processes
    processes = []

    # Start 3 instances of the application
    for _ in range(3):
        # Create a new process that runs the run_app function
        proc = Process(target=run_app)
        # Start the process
        proc.start()
        # Add the process to the list
        processes.append(proc)

    # Wait for all processes to finish
    for proc in processes:
        proc.join()
