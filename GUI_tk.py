import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter import ttk
import dataCRUD as data


class ProjectLibrary(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        main = tk.Frame(self)
        main.pack(side="top", fill="both", expand=True)
        main.grid_rowconfigure(0, weight=1)
        main.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Homepage, Addproject, Addresource):
            frame = F(main, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Homepage)

    def show_frame(self, cont):
        ''' raises this frame in the stacking order'''
        frame = self.frames[cont]
        frame.tkraise()


class Homepage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.authors = data.list_authors()

        topframe = ttk.LabelFrame(self, text="", padding='0.2i', borderwidth=0)
        topframe.grid(column = 0, row = 0)

        newproject = ttk.Button(topframe, text = "Add Project",
                                command=lambda: controller.show_frame(Addproject))
        newproject.grid(column = 1, row = 0)

        newresource = ttk.Button(topframe, text = "Add Resource",
                                 command = lambda: controller.show_frame(Addresource))
        newresource.grid(column = 2, row = 0)

class Addresource(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text = "Resources")
        label.grid(row = 0, column = 0, columnspan = 4, pady = 10, padx  =10)

        topframe = ttk.LabelFrame(self, text = "", padding='0.2i', borderwidth=0)
        topframe.grid(column = 0, row = 2)



class Addproject(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.label = tk.Label(self, text="Menus")
        self.label.grid(row=0, column=0, columnspan=4)



app = ProjectLibrary()
app.title('Project Library')
app.iconbitmap('project.ico')
app.mainloop()


