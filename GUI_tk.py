import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter import ttk
import dataCRUD as data


class ProjectLibrary(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.main = tk.Frame()
        self.data = data

        topframe = ttk.LabelFrame(self, text="", padding='0.2i', borderwidth=0)
        topframe.pack()

        self.authors = data.list_authors()

        authors = ttk.Button(topframe, text = 'authors', command  = lambda: self.get_authors())
        authors.pack()

    def get_authors(self):
        for item in self.authors:
            print(item)



app = ProjectLibrary()
app.title('Project Library')
app.iconbitmap('project.ico')
app.mainloop()


