import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter import ttk
import dataCRUD as data

labelsfont = ('times', 12, 'bold')
headerfont = ('times', 14, 'bold')

class ProjectLibrary(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        main = tk.Frame(self)
        main.pack(side="top", fill="both", expand=True)
        main.grid_rowconfigure(0, weight=1)
        main.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (HomePage, AddResource, AddProject, SearchProjects, LinkResources, ViewProjects):
            frame = F(main, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(AddResource)

    def show_frame(self, cont):
        ''' raises this frame in the stacking order'''
        frame = self.frames[cont]
        frame.tkraise()


class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
                
        self.label = tk.Label(self, text ='Home')
        self.label.grid(row= 0, column = 0, columnspan=4)
          
        self.topframe = ttk.LabelFrame(self, text='Menu', padding='0.05i', borderwidth = 0)
        self.topframe.grid(row=1, column=0, columnspan=20)
         
        self.firstframe =ttk.LabelFrame(self.topframe, text='Project Menu', padding='0.5i', borderwidth = 0)
        self.secondframe = ttk.LabelFrame(self.topframe, text='Resource Menu', padding='0.5i', borderwidth=0)
        self.firstframe.grid(column= 0, row=0)
        self.secondframe.grid(column=1, row=0)
         
        self.new_projects = tk.Button(self.firstframe, text='New Project', command=lambda: controller.show_frame(AddProject))
        self.new_projects.config(height=3, width=13)
        self.new_projects.grid(column = 0, row= 0)

        self.view_project = tk.Button(self.firstframe, text='Find Projects',
                                      command=lambda: controller.show_frame(SearchProjects))
        self.view_project.config(height=3,width=13)
        self.view_project.grid(column=0, row=1)

        self.edit_project = tk.Button(self.firstframe, text='Edit Project')
        self.edit_project.config(height=3, width=13)
        self.edit_project.grid(column=0, row=2)

        self.link_projects = tk.Button(self.firstframe, text='View All',
                                       command=lambda: controller.show_frame(ViewProjects))
        self.link_projects.config(height=3, width=13)
        self.link_projects.grid(column=0, row=3)

        self.new_resources = tk.Button(self.secondframe, text='New Resource',
                                   command=lambda: controller.show_frame(AddResource))
        self.new_resources.config(height=3, width=13)
        self.new_resources.grid(column=1, row=0)

        self.view_resources = tk.Button(self.secondframe, text='View Resources')
        self.view_resources.config(height=3, width=13)
        self.view_resources.grid(column=1, row=1)

        self.edit_resource = tk.Button(self.secondframe, text='Edit Resource')
        self.edit_resource.config(height=3, width=13)
        self.edit_resource.grid(column=1, row=2)

        self.search_resources = tk.Button(self.secondframe, text='Search Resources')
        self.search_resources.config(height=3, width=13)
        self.search_resources.grid(column=1,row=3)

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
        
      
class EditResource(AddResource):
    def __init__(self, parent, controller):
        Addresource.__init__(self, parent, controller)

        label = tk.Label(self, text="Edit Resource", font=self.headlabelfont)
        label.grid(row=0, column=0, columnspan=4, pady=10, padx=10)


class AddProject(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.header_frame = ttk.LabelFrame(self, text='', borderwidth=0)
        self.header_frame.grid(column=0, row=0, columnspan=20)

        self.topframe = ttk.LabelFrame(self, text='', padding='0.05i', borderwidth=0)
        self.topframe.grid(row=1, column=0)

        self.bottomframe = ttk.LabelFrame(self, text='', borderwidth=0)
        self.bottomframe.grid(row=2, column=0)

        self.label = tk.Label(self.header_frame, text='New Project', font=headerfont)
        self.label.grid(column=0, row=1)

        self.project_name = tk.StringVar(self, value='')
        self.project_type = tk.StringVar(self, value='')
        self.description = tk.StringVar(self, value='')
        self.start_date = tk.StringVar(self, value='')
        self.end_date = tk.StringVar(self, value='')

        self.title_label = tk.Label(self.topframe, text='Project Name', font=labelsfont)
        self.project_type_label = tk.Label(self.topframe, text='Project Type', font=labelsfont)
        self.description_label = tk.Label(self.topframe, text='Description', font=labelsfont)
        self.start_label = tk.Label(self.topframe, text='Start Date', font=labelsfont)
        self.finish_label = tk.Label(self.topframe, text='End Date', font=labelsfont)

        self.title_label.grid(column=0, row=0, sticky=tk.W)
        self.project_type_label.grid(column=0, row=1, sticky=tk.W)
        self.description_label.grid(column=0, row=2, sticky=tk.W)
        self.start_label.grid(column=0, row=3, sticky=tk.W)
        self.finish_label.grid(column=0, row=4, sticky=tk.W)

        self.project_name_entry = ttk.Entry(self.topframe, width=40, textvariable=self.project_name)
        self.project_type_entry = ttk.Combobox(self.topframe, width=37, textvariable=self.project_type)
        self.description_entry= ttk.Entry(self.topframe, width=40, textvariable=self.description)
        self.start_entry= ttk.Entry(self.topframe, width=40, textvariable=self.start_date)
        self.end_entry= ttk.Entry(self.topframe, width=40, textvariable=self.end_date)

        self.project_type_entry['values'] = data.list_project_category()

        self.project_name_entry.grid(column=1, row=0, sticky=tk.W)
        self.project_type_entry.grid(column=1, row=1, sticky=tk.W)
        self.description_entry.grid(column=1, row=2, sticky=tk.W)
        self.start_entry.grid(column=1, row=3, sticky=tk.W)
        self.end_entry.grid(column=1, row=4, sticky=tk.W)

        self.home = tk.Button(self.bottomframe, text='Home', command=lambda: controller.show_frame(Home))
        self.home.grid(column=0, row=1, padx=10, sticky=tk.W)

        self.add_project = tk.Button(self.bottomframe, text = 'Save', command=lambda: self.save_project())
        self.add_project.grid(column=1, row=1,  padx=10, sticky=tk.E)

    def save_project(self):
        """ Adds project to SQL database """

        data.add_project(self.project_name.get(), self.project_type.get(), self.description.get(),
                         self.start_date.get(),self.end_date.get())

        self.project_name_entry.delete(0, "end")
        self.project_type_entry.delete(0, "end")
        self.description_entry.delete(0, "end")
        self.start_entry.delete(0, "end")
        self.end_entry.delete(0, "end")

        self.project_type_entry['values'] = data.list_project_category()

class SearchProjects(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.project_title = tk.StringVar(self, value='')

        self.searchheader = ttk.Label(self, text='Search by project title', font=headerfont)
        self.searchheader.grid(column=0, row=0)

        self.searchframe = ttk.LabelFrame(self, text='')
        self.searchframe.grid(column=0, row=1, columnspan=40, sticky=tk.W)

        self.resultsframe = ttk.LabelFrame(self, text='')
        self.resultsframe.grid(column=0, row=2, columnspan=40, sticky=tk.W)

        self.choiceframe = ttk.LabelFrame(self, text='')
        self.choiceframe.grid(column=0, row=3, columnspan=40, sticky=tk.W)

        self.search_label = tk.Label(self.searchframe, text='Title: ', font=labelsfont)
        self.search_label.grid(column=0, row=0, sticky=tk.W)

        self.searchbox = tk.Entry(self.searchframe, width=60, textvariable=self.project_title)
        self.searchbox.grid(column=1, row=0)

        self.searchbutton = ttk.Button(self.searchframe, text='Search')
        self.searchbutton.config(width=10)
        self.searchbutton.grid(column=1, row=1, sticky=tk.E)

        self.projects_box = tk.Listbox(self.resultsframe, height=5, width=68)
        self.projects_box.grid(column=0, row=0, sticky=tk.W)

        self.select_project = tk.Button(self.resultsframe, text='Select', command=lambda:self.select_project())
        self.select_project.config(width=10)
        self.select_project.grid(column=0, row=1,sticky=tk.E)

        self.resource_selected = tk.Label(self.choiceframe, textvariable='test title')
        self.resource_selected.config(width=46)
        self.resource_selected.grid(column=0, row=2, padx=0.5, sticky=tk.W)

        self.go_to_resources = tk.Button(self.choiceframe, text='Link resource',
                                         command=lambda: controller.show_frame(LinkResources))
        self.go_to_resources.config(width=10)
        self.go_to_resources.grid(column=1, row=2,sticky=tk.E)

        self.home = tk.Button(self.choiceframe, text='Home', command=lambda: controller.show_frame(HomePage))
        self.home.config(width=10)
        self.home.grid(column=1, row=3, sticky=tk.E)

    def select_project(self):
        """ Takes item selected from listbox and stores it as a global variable to be used in
            Link resource window
        """
        pass



app = ProjectLibrary()
app.title('Project Library')
app.iconbitmap('project.ico')
app.mainloop()


