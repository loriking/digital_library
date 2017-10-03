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

        topframe = ttk.LabelFrame(self, text="", padding='0.2i', borderwidth=0)
        topframe.grid(column=0, row=2)

        title_label = ttk.Label(topframe, text="Title:")
        title_label.grid(column=0, row=1, padx=5, pady=5, sticky=tk.W)

        author_label = ttk.Label(topframe, text="Author:")
        author_label.grid(column=0, row=2, padx=5, pady=5, sticky=tk.W)

        publisher_label = ttk.Label(topframe, text="Publisher:")
        publisher_label.grid(column = 0, row = 3, padx = 5, pady = 5, sticky = tk.W)

        year_label = ttk.Label(topframe, text="Year: ")
        year_label.grid(column = 0, row=4, padx = 5, pady = 5, sticky=tk.W)

        page_label = ttk.Label(topframe, text="Pages: ")
        page_label.grid(column = 2, row = 4, padx = 5, pady = 5, sticky = tk.W)

        resource_type_label = ttk.Label(topframe, text="Resource Type: ")
        resource_type_label.grid(column = 0, row = 5, padx = 5, pady = 5,sticky = tk.W)

        language_label = ttk.Label(topframe, text = "Language: ")
        language_label.grid(column = 0, row = 6, padx = 5, pady = 5,sticky = tk.W)

        new_language = ttk.Button(topframe, text="Add Language")
        # command = lambda: )
        new_language.grid(column=1, row=7, sticky=tk.W)

        author_name = tk.StringVar()
        title = tk.StringVar()
        publisher = tk.StringVar()
        year = tk.IntVar()
        pages = tk.IntVar()
        resource_type = tk.StringVar()
        language = tk.StringVar()

        author_entry = ttk.Entry(topframe, width = 40, textvariable = author_name)
        title_entry = ttk.Entry(topframe, width = 40, textvariable = title)
        publisher_entry = ttk.Entry(topframe, width = 40, textvariable = publisher)
        year_entry = ttk.Entry(topframe, width = 40, textvariable = year)
        pages_entry = ttk.Entry(topframe, width = 40, textvariable = pages)
        resource_type_entry = ttk.Entry(topframe, width = 40, textvariable = resource_type)
        language_entry = ttk.Entry(topframe, width = 40, textvariable = language)

        author_entry.grid(column = 1, row = 1, sticky=tk.W)
        title_entry.grid(column = 1, row = 2, sticky=tk.W)
        publisher_entry.grid(column = 1, row = 3, sticky=tk.W)
        year_entry.grid(column= 1, row=4, sticky=tk.W)
        pages_entry.grid(column=3, row=4, sticky=tk.W)
        resource_type_entry.grid(column=1, row=5, sticky=tk.W)
        language_entry.grid(column=1, row=6, sticky=tk.W)



class Addproject(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.label = tk.Label(self, text="Menus")
        self.label.grid(row=0, column=0, columnspan=4)



app = ProjectLibrary()
app.title('Project Library')
app.iconbitmap('project.ico')
app.mainloop()


