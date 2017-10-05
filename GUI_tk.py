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

        for F in (Homepage, Addproject, Addresource, Editresource):
            frame = F(main, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Addresource)

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

        newproject = tk.Button(topframe, text = "Add Project",
                                command=lambda: controller.show_frame(Addproject))
        newproject.grid(column = 1, row = 0)

        newresource = tk.Button(topframe, text = "Add Resource",
                                 command = lambda: controller.show_frame(Addresource))
        newresource.grid(column = 2, row = 0)

        editresource = tk.Button(topframe, text = "Edit Resource",
                                 command = lambda: controller.show_frame(Editresource))
        editresource.grid(column = 3, row = 0)

class Addresource(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.headlabelfont = ('times', 20, 'bold')
        self.labelsfont = ('times', 12, 'bold')

        label = tk.Label(self, text = "New Resource", font = self.headlabelfont)
        label.grid(row = 0, column = 0, columnspan = 4, pady = 10, padx  =10)

        topframe = ttk.LabelFrame(self, text = "", padding='0.2i', borderwidth=0)
        topframe.grid(column = 0, row = 2)

        title_label = ttk.Label(topframe, text="Title", font = self.labelsfont)
        title_label.grid(column=0, row=1, padx=5, pady=5,  sticky=tk.W)

        author_label = ttk.Label(topframe, text="Author(s)", font = self.labelsfont)
        author_label.grid(column=0, row=2, padx=5, pady=5,  sticky=tk.W)

        publisher_label = ttk.Label(topframe, text="Publisher", font = self.labelsfont)
        publisher_label.grid(column = 0, row = 3, padx = 5, pady = 5,  sticky = tk.W)

        year_label = ttk.Label(topframe, text="Year", font = self.labelsfont)
        year_label.grid(column=0, row=4, padx=5, pady=5,   sticky=tk.W)

        page_label = ttk.Label(topframe, text="Pages", font = self.labelsfont)
        page_label.grid(column=2, row=4, padx=5, pady=5, sticky=tk.W)

        resource_type_label = ttk.Label(topframe, text="Resource Type", font = self.labelsfont)
        resource_type_label.grid(column = 0, row = 5, padx = 5, pady = 5,sticky = tk.W)

        language_label = ttk.Label(topframe, text = "Language", font = self.labelsfont)
        language_label.grid(column = 0, row = 6, padx = 5, pady = 5,sticky = tk.W)

        new_language = tk.Button(topframe, text="Add Language")
        # command = lambda: )
        new_language.config(cursor='hand2')
        new_language.grid(column=3, row=6, sticky=tk.E)

        abstract_label = ttk.Label(topframe, text="Abstract", font = self.labelsfont)
        abstract_label.grid(column=0, row=8, padx=5, pady=5, sticky=tk.W)

        self.title = tk.StringVar()
        self.author_name = tk.StringVar()
        self.publisher = tk.StringVar()
        self.year = tk.IntVar()
        self.pages = tk.IntVar()
        self.resource_type = tk.StringVar()
        self.language = tk.StringVar()
        self.abstract = tk.StringVar()


        self.title_entry = ttk.Entry(topframe, width = 40, textvariable = self.title)
        self.title_entry.focus()

        self.author_entry = ttk.Entry(topframe, width=40, textvariable=self.author_name)
        self.publisher_entry = ttk.Entry(topframe, width = 40, textvariable = self.publisher)
        self.year_entry = ttk.Entry(topframe, width = 15, textvariable = self.year)
        self.pages_entry = ttk.Entry(topframe, width = 15, textvariable = self.pages)
        self.resource_type_entry = ttk.Entry(topframe, width = 40, textvariable = self.resource_type)
        self.language_entry = ttk.Entry(topframe, width = 25, textvariable = self.language)
        self.abstract_entry = ttk.Entry(topframe, width=40, textvariable=self.abstract)

        self.title_entry.grid(column=1, row=1, columnspan = 3, sticky=tk.W)
        self.author_entry.grid(column = 1, row = 2, columnspan = 3, sticky=tk.W)
        self.publisher_entry.grid(column = 1, row = 3, columnspan = 3, sticky=tk.W)
        self.year_entry.grid(column= 1, row=4, columnspan = 1, sticky=tk.W)
        self.pages_entry.grid(column=3, row=4, columnspan = 1, sticky=tk.W)
        self.resource_type_entry.grid(column=1, row=5, columnspan = 3, sticky=tk.W)
        self.language_entry.grid(column=1, row=6, columnspan= 3, sticky=tk.W)
        self.abstract_entry.grid(column=1, row=8, columnspan=3, sticky=tk.W + tk.E)

        self.save_button = tk.Button(topframe, text = 'Save',
                                     command=lambda : self.addresource())

        self.save_button.grid(column=0, row=10, columnspan = 4, sticky=tk.E)

    def addauthor(self):
        data.add_author(name)
        pass

    def addresource(self):
        data.add_resource(self.title.get(), self.author_name.get(), self.publisher.get(), self.year.get(),
                              self.pages.get(), self.resource_type.get(), self.language.get(), self.abstract.get())


class Editresource(Addresource):
    def __init__(self, parent, controller):
        Addresource.__init__(self, parent, controller)

        label = tk.Label(self, text="Edit Resource", font=self.headlabelfont)
        label.grid(row=0, column=0, columnspan=4, pady=10, padx=10)


class Addproject(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.label = tk.Label(self, text="Menus")
        self.label.grid(row=0, column=0, columnspan=4)



app = ProjectLibrary()
app.title('Project Library')
app.iconbitmap('project.ico')
app.mainloop()


