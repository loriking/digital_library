import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter import ttk
import dataCRUD as data

smalllabelsfont = ('times', 10, 'bold')
labelsfont = ('times', 12, 'bold')
headerfont = ('times', 14, 'bold')

class ProjectLibrary(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        main=tk.Frame(self)
        main.pack(side='top', fill='both', expand=True)
        main.grid_rowconfigure(0, weight=1)
        main.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (HomePage, Projects, SearchProjects, AddResource, SearchResource, EditResource):
            frame = F(main, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky ='nsew')

        self.show_frame(SearchProjects)
        
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
                
        self.label = tk.Label(self, text ='', font=headerfont)
        self.label.grid(row= 0, column = 0, columnspan=20)
          
        self.topframe = tk.LabelFrame(self, text='')
        self.topframe.config(bd=0)
        self.topframe.grid(row=1, column=0, padx=200, columnspan=20)

        self.firstframe =tk.LabelFrame(self.topframe, text='Project Menu', font=labelsfont)
        self.firstframe.config(bd=0)

        self.secondframe = tk.LabelFrame(self.topframe, text='Resource Menu', font=labelsfont)
        self.secondframe.config(bd=0)

        self.middleframe = tk.LabelFrame(self.topframe, text='')
        self.middleframe.config(bd=0)

        self.firstframe.grid(column= 0, row=0, padx=40)
        self.middleframe.grid(column=1, row=0, padx=40)
        self.secondframe.grid(column=2, row=0, padx=40)

        self.wordcloud = tk.PhotoImage(file="smallwhitewordcloud.png")

        self.new_projects = tk.Button(self.firstframe, text='Add Project', command=lambda: controller.show_frame(Projects))
        self.new_projects.config(height=5, width=13)
        self.new_projects.grid(column = 0, row= 0, pady=5)

        self.view_project = tk.Button(self.firstframe, text='Search Projects',
                                      command=lambda: controller.show_frame(SearchProjects))
        self.view_project.config(height=5,width=13)
        self.view_project.grid(column=0, row=1, pady=5)

        self.edit_project = tk.Button(self.firstframe, text='Edit Project')
        self.edit_project.config(height=5, width=13)
        self.edit_project.grid(column=0, row=2, pady=5)
        """
        self.link_projects = tk.Button(self.firstframe, text='View All',
                                       command=lambda: controller.show_frame(AddProjects))
        self.link_projects.config(height=3, width=13)
        self.link_projects.grid(column=0, row=3)
        """

        self.new_resources = tk.Button(self.secondframe, text='Add Resource',
                                   command=lambda: controller.show_frame(AddResource))
        self.new_resources.config(height=5, width=13)
        self.new_resources.grid(column=1, row=0, pady=5)

        self.view_resources = tk.Button(self.secondframe, text='Search Resources',
                                        command=lambda: controller.show_frame(SearchResource))
        self.view_resources.config(height=5, width=13)
        self.view_resources.grid(column=1, row=1, pady=5)

        self.edit_resource = tk.Button(self.secondframe, text='Edit Resource')
        self.edit_resource.config(height=5, width=13)
        self.edit_resource.grid(column=1, row=2, pady=5)
        """
        self.search_resources = tk.Button(self.secondframe, text='Search Resources')
        self.search_resources.config(height=3, width=13)
        self.search_resources.grid(column=1,row=3)
        """

        button1 = ttk.Button(self.middleframe, text = "", image=self.wordcloud, compound="center")
        button1.grid(column=2, row=1, rowspan=5,padx=10,sticky=tk.E)



class AddResource(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        header_frame = tk.LabelFrame(self, text='', borderwidth=0)
        header_frame.grid(column=0, row=0, columnspan=20,padx=10)

        topframe = tk.LabelFrame(self, text="", borderwidth=0)
        topframe.grid(column=0, row=1, padx=10, sticky=tk.W)

        bottomframe = tk.LabelFrame(self, text="", borderwidth=0)
        bottomframe.grid(column=0, row=3, padx=10, sticky=tk.W)

        self.label = tk.Label(header_frame, text='New Resource', font=headerfont)
        self.label.grid(column=0, row=1)

        self.title = tk.StringVar()
        self.author = tk.StringVar()
        self.year = tk.IntVar()
        self.pages = tk.IntVar()
        self.abstract = tk.StringVar()
        self.subject = tk.StringVar()
        
        self.publisher = tk.StringVar()
        self.publisher_options = data.list_publishers()
        self.publisher.set('Choose publisher:')
        
        self.language = tk.StringVar()
        self.language_options = data.list_languages()
        self.language.set('Choose language:')
        
        self.medium = tk.StringVar()
        self.medium_options = data.list_resource_medium()
        self.medium.set('Choose format:')

        self.new_lang = tk.StringVar()
        self.new_pub = tk.StringVar()
        self.new_format =tk.StringVar()

        self.new_lang_flag = tk.IntVar(self, value=0)
        self.new_pub_flag = tk.IntVar(self, value=0)
        self.new_format_flag = tk.IntVar(self, value=0)

        self.title_label=tk.Label(topframe, text='Title', font=labelsfont)
        self.author_label=tk.Label(topframe, text ='Author(s)', font=labelsfont)
        self.year_label=tk.Label(topframe, text ='Year', font=labelsfont)
        self.pages_label=tk.Label(topframe, text ='Pages', font=labelsfont)
        self.publisher_label = tk.Label(topframe, text='Publisher', font=labelsfont)
        self.lan_label=tk.Label(topframe, text='Language',font=labelsfont)
        self.media_label=tk.Label(topframe, text='Fomat', font=labelsfont)
        self.subject_label = tk.Label(topframe, text='Subject', font=labelsfont)
        self.abstract_label=tk.Label(topframe, text='Abstract', font=labelsfont)
        self.add_publisher_label = tk.Label(topframe, text='New Publisher', font=smalllabelsfont)
        self.add_language_label = tk.Label(topframe, text='New Language', font=smalllabelsfont)
        self.add_format_label =  tk.Label(topframe, text='New Format', font=smalllabelsfont)

        self.title_entry=ttk.Entry(topframe, width=50, textvariable =self.title)
        self.author_entry=ttk.Entry(topframe, width=50, textvariable=self.author)
        self.year_entry=ttk.Entry(topframe, width=50, textvariable=self.year)
        self.pages_entry=ttk.Entry(topframe, width=50, textvariable=self.pages)
        self.publisher_entry = tk.OptionMenu(topframe, self.publisher, 
                                                *self.publisher_options)
        self.publisher_entry.configure(width=43)  
        self.add_publisher_entry = ttk.Entry(topframe, width=50, 
                                             textvariable =self.new_pub)
        self.language_entry= tk.OptionMenu(topframe, self.language, 
                                                *self.language_options)
        self.language_entry.configure(width=43)                
        self.add_language_entry=ttk.Entry(topframe, width=50, textvariable =self.new_lang)

        self.media_menu=tk.OptionMenu(topframe, self.medium, 
                                                *self.medium_options)
        self.media_menu.configure(width=43)                

        self.add_format_entry =ttk.Entry(topframe, width=53, textvariable =self.new_format)
        self.subject_entry = ttk.Entry(topframe, width = 53, textvariable=self.subject)
        self.abstract_entry=ttk.Entry(topframe, width=53, textvariable=self.abstract)

        self.add_pub_flag = tk.Checkbutton(topframe, text='Check if adding new publisher', 
                                           variable=self.new_pub_flag)
        self.add_lang_flag = tk.Checkbutton(topframe, text='Check if adding new language', 
                                            variable=self.new_lang_flag)
        self.add_format_flag = tk.Checkbutton(topframe, text='Check if adding new format', 
                                              variable=self.new_format_flag)


        self.title_label.grid(column=0, row=1,  padx=5, sticky=tk.W)
        self.title_entry.grid(column=1, row=1,  padx=5,sticky=tk.W)
        self.author_label.grid(column=2, row=1, padx=10, sticky=tk.W)
        self.author_entry.grid(column=3, row=1,padx=5, sticky=tk.W)
        self.subject_label.grid(column=4, row=1,  padx=10, sticky=tk.W)
        self.subject_entry.grid(column=5, row=1, padx=6,sticky=tk.E)

        self.year_label.grid(column=0, row=2, padx=5, sticky=tk.W)
        self.year_entry.grid(column=1, row=2,padx=5, sticky=tk.W)
        self.pages_label.grid(column=2, row=2, padx=10, sticky=tk.W)
        self.pages_entry.grid(column=3, row=2,padx=5, sticky=tk.W)
        self.abstract_label.grid(column=4, row=2, padx=10, sticky=tk.W)
        self.abstract_entry.grid(column=5, row=2, padx=5, sticky=tk.E)

        self.publisher_label.grid(column=0, row=3,  padx=5, sticky=tk.W)
        self.publisher_entry.grid(column=1, row=3, padx=5, sticky=tk.W)

        self.add_publisher_label.grid(column=0, row=4,  padx=5, sticky=tk.W)
        self.add_publisher_entry.grid(column=1, row=4,  padx=5, sticky=tk.W)
        
        self.lan_label.grid(column=2, row=3, padx=10, sticky=tk.W)
        self.language_entry.grid(column=3, row=3, padx=5, sticky=tk.W)

        self.add_language_label.grid(column=2, row=4, padx=10, sticky=tk.W)
        self.add_language_entry.grid(column=3, row=4, padx=5, sticky=tk.W)
        self.media_label.grid(column=4, row=3, padx=10,sticky=tk.W)
        self.media_menu.grid(column=5, row=3, padx=5, sticky=tk.E)

        self.add_format_label.grid(column=4, row=4, padx=10,sticky=tk.W)
        self.add_format_entry.grid(column=5, row=4, padx=5, sticky=tk.E)

        self.add_pub_flag.grid(column=1, row=5,  sticky=tk.E)
        self.add_lang_flag.grid(column=3, row=5,sticky=tk.E)
        self.add_format_flag.grid(column=5, row=5,sticky=tk.E)


        self.resource_list = ttk.Treeview(bottomframe,
                                         columns=('Title', 'Author','Year', 
                                                  'Pages','Publisher', 
                                                  'Language', 'Format', 
                                                  'Abstract'))
        self.resource_list['columns'] = ('Title', 'Author', 'Year', 'Pages', 
                          'Publisher', 'Language', 'Format', 'Abstract')
        self.resource_list.column('#0', width=1)
        self.resource_list.column('0', width=250, anchor='w')
        self.resource_list.column('1', width=150, anchor='w')
        self.resource_list.column('2', width=75, anchor='w')
        self.resource_list.column('3', width=60, anchor='w')
        self.resource_list.column('4', width=100, anchor='w')
        self.resource_list.column('5', width=100, anchor='w')
        self.resource_list.column('6', width=90, anchor='w')
        self.resource_list.column('7', width=400, anchor='w')
        self.resource_list.grid(column=0, row=1)

        self.resource_list.heading('0', text='Title', anchor='w')
        self.resource_list.heading('1', text='Author(s)', anchor='w')
        self.resource_list.heading('2', text='Year', anchor='w')
        self.resource_list.heading('3', text='Pages', anchor='w')
        self.resource_list.heading('4', text='Publisher', anchor='w')
        self.resource_list.heading('5', text='Language', anchor='w')
        self.resource_list.heading('6', text='Format', anchor='w')
        self.resource_list.heading('7', text='Abstract', anchor='w')

        self.treeview = self.resource_list       
        self.list_resources()
        self.update_entry_widgets()

        self.addresource=tk.Button(bottomframe, text='Save', command=lambda:self.new_resource())
        self.addresource.config(width=12, cursor='hand2')
        self.addresource.grid(column=0, row=0, padx=10, sticky=tk.E)

        self.home=tk.Button(bottomframe, text='Home', command=lambda: controller.show_frame(HomePage))
        self.home.config(width=15, cursor='hand2')
        self.home.grid(column=0, row=2, padx=10, sticky=tk.W)

        self.searchresource = tk.Button(bottomframe, text='Search Resources',
                                     command=lambda: controller.show_frame(SearchResource))
        self.searchresource.config(width=15, cursor='hand2')
        self.searchresource.grid(column=0, row=3, padx=10, sticky=tk.W)

    def list_resources(self):
        for i in self.resource_list.get_children():
            self.resource_list.delete(i)
        resources = data.list_resources()
        for item in resources:
            self.treeview.insert('', 'end', values=item)
            
    def update_entry_widgets(self):
       
        self.title_entry.delete(0, 'end')
        self.author_entry.delete(0, 'end')
        self.year_entry.delete(0, 'end')
        self.pages_entry.delete(0, 'end')
        self.subject_entry.delete(0, 'end')
        self.abstract_entry.delete(0, 'end')
        self.add_language_entry.delete(0, 'end')
        self.add_publisher_entry.delete(0, 'end')
        self.add_format_entry.delete(0, 'end')
        self.new_lang_flag.set(0)
        self.new_pub_flag.set(0)
        self.new_format_flag.set(0)
        self.publisher.set('Choose publisher:')
        self.language.set('Choose language:')
        self.medium.set('Choose format:')
        
    def new_resource(self):
        
        if self.new_pub_flag.get() == 1:
            self.thepublisher = self.new_pub.get()
        else:
            self.thepublisher = self.publisher.get()

        if self.new_lang_flag.get() == 1:
            self.thelanguage = self.new_lang.get()
        else:
            self.thelanguage = self.language.get()

        if  self.new_format_flag.get() == 1:
            self.theformat = self.new_format.get()
        else:
            self.theformat = self.medium.get()

        data.add_resource(self.title.get(), self.author.get(), self.year.get(), 
                          self.pages.get(), self.thepublisher,
                          self.thelanguage, self.theformat, self.subject.get(), 
                          self.abstract.get())

        self.list_resources()
        self.update_entry_widgets()



class SearchProjects(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.project_title = tk.StringVar()
        self.project_type = tk.StringVar()

        self.media_type = tk.StringVar()
        self.media_type.set("?")

        self.searchheader = ttk.Label(self, text='Search by project title', font=headerfont)
        self.searchheader.grid(column=0, row=0)

        self.searchframe = tk.LabelFrame(self, text='', borderwidth=0)
        self.searchframe.grid(column=0, row=1, columnspan=40, sticky=tk.W)

        self.resultsframe = tk.LabelFrame(self, text='', borderwidth=0)
        self.resultsframe.grid(column=1, row=2, columnspan=40, sticky=tk.W)

        self.sortframe = tk.LabelFrame(self, text='', borderwidth=1)
        self.sortframe.grid(column=0, row=4, columnspan=40, padx=10, sticky=tk.W)

        self.choiceframe = tk.LabelFrame(self, text='', borderwidth=0)
        self.choiceframe.grid(column=0, row=3, columnspan=40, sticky=tk.W)

        self.titlebox_label = tk.Label(self.searchframe, text='Title: ', font=labelsfont)
        self.titlebox_label.grid(column=0, row=0, sticky=tk.W)
        self.titlebox = tk.Entry(self.searchframe, width=40, textvariable=self.project_title)
        self.titlebox.grid(column=1, row=0)

        self.projecttype_label = tk.Label(self.searchframe,  text='Project type:', font=labelsfont)
        self.projecttype_label.grid(column=2, row=0, padx=5, sticky=tk.W)
        self.projecttype_entry = tk.Entry(self.searchframe,width=40, textvariable=self.project_type)
        self.projecttype_entry.grid(column=3, row=0, sticky=tk.W)

        self.searchbutton = ttk.Button(self.searchframe, text='Search', command=lambda: self.search_projects())
        self.searchbutton.config(width=10)
        self.searchbutton.grid(column=3, row=1, sticky=tk.E)

        self.audio_rb = tk.Radiobutton(self.sortframe, text='Audio', variable=self.media_type, value=1)
        self.book_rb = tk.Radiobutton(self.sortframe, text='Book/eBook', variable=self.media_type, value=2)
        self.course_rb = tk.Radiobutton(self.sortframe, text='Course', variable=self.media_type, value=3)
        self.interactive_rb = tk.Radiobutton(self.sortframe, text='Interactive Media', variable=self.media_type, value=4)
        self.multimedia_rb = tk.Radiobutton(self.sortframe, text='Multimedia', variable=self.media_type, value=5)
        self.video_rb = tk.Radiobutton(self.sortframe, text='Video', variable=self.media_type, value=6)
        self.webdocs_rb = tk.Radiobutton(self.sortframe, text='Web doc', variable=self.media_type, value=7)

        self.audio_rb.grid(column=0, row=0, sticky=tk.W)
        self.book_rb.grid(column=0, row=1, sticky=tk.W)
        self.course_rb.grid(column=0, row=2, sticky=tk.W)
        self.interactive_rb.grid(column=0, row=3, sticky=tk.W)
        self.multimedia_rb.grid(column=0, row=4, sticky=tk.W)
        self.video_rb.grid(column=0, row=5, sticky=tk.W)
        self.webdocs_rb.grid(column=0, row=6, sticky=tk.W)


        self.project_list = ttk.Treeview(self.resultsframe, height=4,
                                         columns=('Name', 'Type', 'Description', 'Start date', 'End date'))
        self.project_list['columns'] = ('Name', 'Type', 'Description', 'Start date', 'End date')
        self.project_list.column('#0', width=5)
        self.project_list.grid(column=0, row=0, pady=10)

        self.project_list.heading('0', text='Name', anchor='w')
        self.project_list.heading('1', text='Type', anchor='w')
        self.project_list.heading('2', text='Description', anchor='w')
        self.project_list.heading('3', text='Start date', anchor='w')
        self.project_list.heading('4', text='End date', anchor='w')

        self.project_list.column('0', anchor='w')
        self.project_list.column('1', anchor='w')
        self.project_list.column('2', anchor='w')
        self.project_list.column('3', anchor='w')
        self.project_list.column('4', anchor='w')
        self.treeview = self.project_list

        self.go_to_resources = tk.Button(self.choiceframe, text='Link resource')#,
                                         #command=lambda: controller.show_frame(LinkResources))
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

    def search_projects(self):
        for i in self.project_list.get_children():
            self.project_list.delete(i)
        projects = data.find_project(self.project_title.get())
        for item in projects:
            self.treeview.insert('', 'end', values=item)
        self.titlebox.delete(0, 'end')


class Projects(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.label = tk.Label(self, text='Project Details', font=labelsfont)
        self.label.grid(column=0, row=0, sticky=tk.W+tk.E)

        self.topframe = tk.LabelFrame(self, text='')
        self.topframe.config(bd=0)
        self.topframe.grid(column=0, row=1, sticky=tk.W+tk.E)

        self.bottomframe = tk.LabelFrame(self, text='', borderwidth=0)
        self.bottomframe.config(bd=0)
        self.bottomframe.grid(column=0, row=2)

        self.project_name = tk.StringVar()
        self.project_type = tk.StringVar()
        self.description = tk.StringVar()
        self.start_date = tk.StringVar()
        self.end_date = tk.StringVar()
        self.link = tk.IntVar(self, value=0)
        self.add_category = tk.StringVar()
        self.choices = tk.StringVar()
        self.project_category_options = data.list_project_category()
        self.choices.set('Choose project type:')

        self.title_label = tk.Label(self.topframe, text='Project Name', font=labelsfont)
        self.project_type_label = tk.Label(self.topframe, text='Project Type', font=labelsfont)
        self.description_label = tk.Label(self.topframe, text='Description', font=labelsfont)
        self.start_label = tk.Label(self.topframe, text='Start Date', font=labelsfont)
        self.finish_label = tk.Label(self.topframe, text='End Date', font=labelsfont)
        self.new_category_label = tk.Label(self.topframe, text='New Project Type', font=labelsfont)

        self.project_name_entry = ttk.Entry(self.topframe, width=60, textvariable=self.project_name)
        self.project_type_entry = tk.OptionMenu(self.topframe, self.choices, *self.project_category_options)
        self.project_type_entry.configure(width=54)
        self.description_entry = ttk.Entry(self.topframe, width=60, textvariable=self.description)
        self.start_entry = ttk.Entry(self.topframe, width=60, textvariable=self.start_date)
        self.end_entry = ttk.Entry(self.topframe, width=60, textvariable=self.end_date)
        self.new_category = ttk.Entry(self.topframe, width=60, textvariable=self.add_category)

        self.title_label.grid(column=0, row=1, padx=10, sticky=tk.W)
        self.project_name_entry.grid(column=1, row=1, padx=10, sticky=tk.W)
        self.description_label.grid(column=2, row=1, padx=10, sticky=tk.W)
        self.description_entry.grid(column=3, row=1, padx=10, sticky=tk.W)
        self.start_label.grid(column=0, row=3, padx=10, sticky=tk.W)
        self.start_entry.grid(column=1, row=3, padx=10, sticky=tk.W)
        self.finish_label.grid(column=2, row=3, padx=10, sticky=tk.W)
        self.end_entry.grid(column=3, row=3, padx=10, sticky=tk.W)

        self.project_type_label.grid(column=0, row=4, padx=10, sticky=tk.W)
        self.project_type_entry.grid(column=1, row=4, padx=8, sticky=tk.E)
        self.new_category_label.grid(column=2, row=4, padx=10, sticky=tk.W)
        self.new_category.grid(column=3, row=4, padx=10, sticky=tk.W)

        self.add_project = tk.Button(self.topframe, text='Add Project', command=lambda: self.save_project())
        self.add_project.grid(column=1, row=6, padx=10, sticky=tk.E)

        self.new_cat_flag = tk.Checkbutton(self.topframe, text="Check to add new project type", variable=self.link)
        self.new_cat_flag.grid(column=3, row=6, padx=6,sticky=tk.W)

        self.project_list = ttk.Treeview(self.bottomframe, columns=('Name', 'Type','Description', 'Start date', 'End date'))
        self.project_list['columns'] = ('Name', 'Type','Description', 'Start date', 'End date')
        self.project_list.column('#0', width=5)
        self.project_list.grid(column=0, row=0, padx=10)

        self.project_list.heading('0',  text='Name', anchor='w')
        self.project_list.heading('1',text='Type', anchor='w')
        self.project_list.heading('2', text='Description', anchor='w')
        self.project_list.heading('3',text='Start date', anchor='w')
        self.project_list.heading('4', text='End date', anchor='w')

        self.project_list.column('0', anchor='w')
        self.project_list.column('1', anchor='w' )
        self.project_list.column('2', anchor='w')
        self.project_list.column('3', anchor='w')
        self.project_list.column('4', anchor='w')
        self.treeview = self.project_list

        self.home = tk.Button(self.bottomframe, text='Home', command=lambda: controller.show_frame(HomePage))
        self.home.config(width=10)
        self.home.grid(column=0, row=1, padx=10, sticky=tk.W)
        self.list_projects()
        self.update_widgets()

    def list_projects(self):
        for i in self.project_list.get_children():
            self.project_list.delete(i)
        projects = data.list_projects()
        for item in projects:
            self.treeview.insert('', 'end', values=item)

    def link_to_resource(self):
        # will link project to resources:self.controller.show_frame(LinkResources)
        pass

    def update_widgets(self):
        self.project_name_entry.delete(0, 'end')
        self.description_entry.delete(0, 'end')
        self.start_entry.delete(0, 'end')
        self.end_entry.delete(0, 'end')
        self.new_category.delete(0, 'end')
        self.link.set(0)
        self.choices.set('Choose project type:')
        self.project_category_options = data.list_project_category()

    def save_project(self):
        """ Adds project to SQL database """

        if self.link.get() == 1:
            self.category = self.new_category.get()
        else:
            self.category = self.choices.get()


        data.add_project(self.project_name.get(), self.category, self.description.get(),
                         self.start_date.get(), self.end_date.get())

        self.list_projects()
        self.update_widgets()


class SearchResource(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.resource_title = tk.StringVar()
        self.resource_author = tk.StringVar()
        self.resource_subject = tk.StringVar()

        self.searchframe = tk.LabelFrame(self, text='Search parameters', borderwidth=0, font=headerfont)
        self.searchframe.grid(column=0, row=0)

        self.searchbar = tk.LabelFrame(self.searchframe, text='', borderwidth=0)
        self.searchbar.grid(column=0, row=0, sticky =tk.W+tk.E)

        self.middleframe = tk.LabelFrame(self.searchframe, text='',borderwidth=0)
        self.middleframe.grid(column=0, row=1, sticky=tk.W+tk.E)

        self.bottomframe = tk.LabelFrame(self.searchframe, text='', borderwidth=0)
        self.bottomframe.grid(column=0, row=2, sticky=tk.W+tk.E)

        self.r_title_label = tk.Label(self.searchbar, text='Title: ', font=labelsfont)
        self.r_entry = tk.Entry(self.searchbar,  width=48, textvariable=self.resource_title)

        self.r_author_label = tk.Label(self.searchbar, text='Author: ', font=labelsfont)
        self.r_author_entry= tk.Entry(self.searchbar,  width=48, textvariable=self.resource_author)

        self.r_subject_label = tk.Label(self.searchbar, text='Subject: ', font=labelsfont)
        self.r_subject_entry= tk.Entry(self.searchbar,  width=48, textvariable=self.resource_subject)

        self.r_title_label.grid(column=0, row=0, padx=5)
        self.r_entry.grid(column=1, row=0, padx=5)

        self.r_author_label.grid(column=2, row=0, padx=5)
        self.r_author_entry.grid(column=3, row=0, padx=5)

        self.r_subject_label.grid(column=4, row=0, padx=5)
        self.r_subject_entry.grid(column=5, row=0, padx=5)

        self.searchbutton = tk.Button(self.searchbar, text='Search')
        self.searchbutton.config(width=12, cursor='hand2')
        self.searchbutton.grid(column=6, row=0, padx= 10, pady=10, sticky=tk.E)

        self.homebutton = tk.Button(self.bottomframe, text='Home', command=lambda: controller.show_frame(HomePage))
        self.homebutton.config(width=12, cursor='hand2')
        self.homebutton.grid(column=0, row=1, padx=10, pady=2, sticky=tk.W)

        self.addresource = tk.Button(self.bottomframe, text='Add Resource', command=lambda: controller.show_frame(AddResource))
        self.addresource.config(width=12, cursor='hand2')
        self.addresource.grid(column=0, row=2, padx=10,pady=2, sticky=tk.W)

        self.resource_list = ttk.Treeview(self.middleframe,
                                          columns=('Title', 'Author', 'Year',
                                                   'Pages', 'Publisher',
                                                   'Language', 'Format',
                                                   'Abstract'))
        self.resource_list['columns'] = ('Title', 'Author', 'Year', 'Pages',
                                         'Publisher', 'Language', 'Format', 'Abstract')
        self.resource_list.column('#0', width=1)
        self.resource_list.column('0', width=250, anchor='w')
        self.resource_list.column('1', width=150, anchor='w')
        self.resource_list.column('2', width=75, anchor='w')
        self.resource_list.column('3', width=60, anchor='w')
        self.resource_list.column('4', width=100, anchor='w')
        self.resource_list.column('5', width=100, anchor='w')
        self.resource_list.column('6', width=90, anchor='w')
        self.resource_list.column('7', width=400, anchor='w')
        self.resource_list.grid(column=0, row=1, padx=10)

        self.resource_list.heading('0', text='Title', anchor='w')
        self.resource_list.heading('1', text='Author(s)', anchor='w')
        self.resource_list.heading('2', text='Year', anchor='w')
        self.resource_list.heading('3', text='Pages', anchor='w')
        self.resource_list.heading('4', text='Publisher', anchor='w')
        self.resource_list.heading('5', text='Language', anchor='w')
        self.resource_list.heading('6', text='Format', anchor='w')
        self.resource_list.heading('7', text='Abstract', anchor='w')

        self.treeview = self.resource_list



class EditResource(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        pass

if __name__ == "__main__":
    app = ProjectLibrary()
    app.title('Project Library')
    app.iconbitmap('project.ico')
    app.mainloop()



