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

        headlabelfont = ('times', 20, 'bold')
        labelsfont = ('times', 12, 'bold')

        label = tk.Label(self, text = "New Resource", font = headlabelfont)
        label.grid(row = 0, column = 0, columnspan = 4, pady = 10, padx  =10)

        topframe = ttk.LabelFrame(self, text = "", padding='0.2i', borderwidth=0)
        topframe.grid(column = 0, row = 2)

        title_label = ttk.Label(topframe, text="Title", font = labelsfont)
        title_label.grid(column=0, row=1, padx=5, pady=5,  sticky=tk.W)

        author_label = ttk.Label(topframe, text="Author(s)", font = labelsfont)
        author_label.grid(column=0, row=2, padx=5, pady=5,  sticky=tk.W)

        publisher_label = ttk.Label(topframe, text="Publisher", font = labelsfont)
        publisher_label.grid(column = 0, row = 3, padx = 5, pady = 5,  sticky = tk.W)

        year_label = ttk.Label(topframe, text="Year", font = labelsfont)
        year_label.grid(column=0, row=4, padx=5, pady=5,   sticky=tk.W)

        page_label = ttk.Label(topframe, text="Pages", font = labelsfont)
        page_label.grid(column=2, row=4, padx=5, pady=5, sticky=tk.W)

        resource_type_label = ttk.Label(topframe, text="Resource Type", font = labelsfont)
        resource_type_label.grid(column = 0, row = 5, padx = 5, pady = 5,sticky = tk.W)

        language_label = ttk.Label(topframe, text = "Language", font = labelsfont)
        language_label.grid(column = 0, row = 6, padx = 5, pady = 5,sticky = tk.W)

        new_language = tk.Button(topframe, text="Add Language")
        # command = lambda: )
        new_language.config(cursor='hand2')
        new_language.grid(column=3, row=6, sticky=tk.E)

        abstract_label = ttk.Label(topframe, text="Abstract", font = labelsfont)
        abstract_label.grid(column=0, row=8, padx=5, pady=5, sticky=tk.W)

        title = tk.StringVar()
        author_name = tk.StringVar()
        publisher = tk.StringVar()
        year = tk.IntVar()
        pages = tk.IntVar()
        resource_type = tk.StringVar()
        language = tk.StringVar()
        abstract = tk.StringVar()

        title_entry = ttk.Entry(topframe, width = 40, textvariable = title)
        author_entry = ttk.Entry(topframe, width=40, textvariable=author_name)
        publisher_entry = ttk.Entry(topframe, width = 40, textvariable = publisher)
        year_entry = ttk.Entry(topframe, width = 15, textvariable = year)
        pages_entry = ttk.Entry(topframe, width = 15, textvariable = pages)
        resource_type_entry = ttk.Entry(topframe, width = 40, textvariable = resource_type)
        language_entry = ttk.Entry(topframe, width = 25, textvariable = language)
        abstract_entry = ttk.Entry(topframe, width=40, textvariable=abstract)

        title_entry.grid(column=1, row=2, columnspan = 3, sticky=tk.W)
        author_entry.grid(column = 1, row = 1, columnspan = 3, sticky=tk.W)
        publisher_entry.grid(column = 1, row = 3, columnspan = 3, sticky=tk.W)
        year_entry.grid(column= 1, row=4, columnspan = 1, sticky=tk.W)
        pages_entry.grid(column=3, row=4, columnspan = 1, sticky=tk.W)
        resource_type_entry.grid(column=1, row=5, columnspan = 3, sticky=tk.W)
        language_entry.grid(column=1, row=6, columnspan= 3, sticky=tk.W)
        abstract_entry.grid(column=1, row=8, columnspan=3, sticky=tk.W + tk.E)



class Addproject(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.label = tk.Label(self, text="Menus")
        self.label.grid(row=0, column=0, columnspan=4)



app = ProjectLibrary()
app.title('Project Library')
app.iconbitmap('project.ico')
app.mainloop()


