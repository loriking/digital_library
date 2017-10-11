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

        for F in (HomePage, Addproject, AddResource, Editresource, New_language):
            frame = F(main, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Addresource)

    def show_frame(self, cont):
        ''' raises this frame in the stacking order'''
        frame = self.frames[cont]
        frame.tkraise()


class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

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

class AddResource(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.labelsfont = ('times', 12, 'bold')

        bottomframe = ttk.LabelFrame(self, text="", borderwidth=0)
        bottomframe.grid(column=1, row=9)

        self.title = tk.StringVar(parent, value="")
        self.author = tk.StringVar(parent, value="")
        self.year = tk.IntVar(parent, value=None)
        self.pages = tk.IntVar(parent, value=None)
        self.publisher = tk.StringVar(parent, value="")
        self.language = tk.StringVar(parent, value="")
        self.medium = tk.StringVar(parent, value="")
        self.abstract = tk.StringVar(parent, value="")

        self.title_label=tk.Label(self, text='Title', font=self.labelsfont)
        self.author_label=tk.Label(self, text ='Author', font=self.labelsfont)
        self.year_label=tk.Label(self, text ='Year', font=self.labelsfont)
        self.pages_label=tk.Label(self, text ='Pages', font=self.labelsfont)
        self.publisher_label = tk.Label(self, text='Publisher', font=self.labelsfont)
        self.lan_label=tk.Label(self, text='Language',font=self.labelsfont)
        self.media_label=tk.Label(self, text='Medium', font=self.labelsfont)
        self.abstract_label=tk.Label(self, text='Abstract', font=self.labelsfont)
        
        self.title_entry=ttk.Entry(self, width=40, textvariable =self.title)
        self.author_entry=ttk.Entry(self, width=40, textvariable=self.author)
        self.year_entry=ttk.Entry(self, width=40, textvariable=self.year)
        self.pages_entry=ttk.Entry(self, width=40, textvariable=self.pages)
        self.publisher_entry = ttk.Combobox(self, width=37, textvariable=self.publisher)
        self.language_entry=ttk.Combobox(self, width=37, textvariable=self.language)
        self.media_box=ttk.Combobox(self, width=37, textvariable=self.medium)
        self.abstract_entry=ttk.Entry(self, width=40, textvariable=self.abstract)

        self.publisher_entry['values'] = data.list_publishers()
        self.media_box['values'] = data.list_resource_medium()
        self.language_entry['values'] = data.list_languages()

        self.title_label.grid(column=0, row=1, sticky=tk.W)
        self.title_entry.grid(column=1, row=1, sticky=tk.E)
        self.author_label.grid(column=0, row=2, sticky=tk.W)
        self.author_entry.grid(column=1, row=2, sticky=tk.E)
        self.year_label.grid(column=0, row=3, sticky=tk.W)
        self.year_entry.grid(column=1, row=3, sticky=tk.E)
        self.pages_label.grid(column=0, row=4, sticky=tk.W)
        self.pages_entry.grid(column=1, row=4, sticky=tk.E)
        self.publisher_label.grid(column=0, row=5, sticky=tk.W)
        self.publisher_entry.grid(column=1, row=5, sticky=tk.E)
        self.lan_label.grid(column=0, row=6, sticky=tk.W)
        self.language_entry.grid(column=1, row=6, sticky=tk.E)
        self.media_label.grid(column=0, row=7, sticky=tk.W)
        self.media_box.grid(column=1, row=7, sticky=tk.E)
        self.abstract_label.grid(column=0, row=8, sticky=tk.W)
        self.abstract_entry.grid(column=1, row=8, sticky=tk.E)
        
        self.addresource=tk.Button(bottomframe, text='Save', command=lambda:self.new_resource())
        self.addresource.config(cursor='hand2')
        self.addresource.grid(column=2, row=1, padx=10, sticky=tk.E)

        self.home=tk.Button(bottomframe, text='Home', command=lambda: controller.show_frame(HomePage))
        self.home.config(cursor='hand2')
        self.home.grid(column=1, row=1, padx=10, sticky=tk.W)

    def new_resource(self):
        data.add_resource(self.title.get(), self.author.get(), self.year.get(), self.pages.get(), self.publisher.get(),
                          self.language.get(), self.medium.get(), self.abstract.get())

        self.title_entry.delete(0, "end")
        self.author_entry.delete(0, "end")
        self.year_entry.delete(0, "end")
        self.pages_entry.delete(0, "end")
        self.publisher_entry.delete(0, "end")
        self.language_entry.delete(0, "end")
        self.media_box.delete(0, "end")
        self.abstract_entry.delete(0, "end")

        self.publisher_entry['values'] = data.list_publishers()
        self.media_box['values'] = data.list_resource_medium()
        self.language_entry['values'] = data.list_languages()
        
        




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


class New_language(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.label = tk.Label(self, text="Add Language")
        self.label.grid(row=0, column=0, columnspan=4)

        self.languages = data.list_languages()
        self.language = tk.StringVar()

        language_label = ttk.Label(self, text="Language ")
        language_label.grid(column=0, row=0, padx=5, pady=5, sticky=tk.W)
        language_entry = ttk.Entry(self, width=25, textvariable=self.language)
        language_entry.grid(column=1, row=0, columnspan=3, sticky=tk.W)

        newlanguage = tk.Button(self, text="Add Language", command=lambda:self.newlanguage())
        newlanguage.grid(column=1, row=1, sticky=tk.E)

    def newlanguage(self, event=None):
        language_text = self.language.get(1.0, tk.END).strip()

        if len(language_text) > 0:
            data.add_language(language_text)




app = ProjectLibrary()
app.title('Project Library')
app.iconbitmap('project.ico')
app.mainloop()


