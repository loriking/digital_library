import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter import ttk
import dataCRUD as data

smalllabelsfont = ('times', 10, 'bold')
labelsfont = ('times', 12, 'bold')
headerfont = ('times', 14, 'bold')
smallheaderfont = ('times', 12, 'italic')


class ProjectLibrary(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        main=tk.Frame(self)
        main.pack(side='top', fill='both', expand=True)
        main.grid_rowconfigure(0, weight=1)
        main.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (HomePage, Projects, LinkResources, AddResource, AddText, AddAudioVideo, AddCourse,
                  AddInteractiveMedia, AddOnlineMedia, AddImages, SearchResource, EditResource):
            frame = F(main, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky ='nsew')

        self.show_frame(AddCourse)
        
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
                
        self.label = tk.Label(self, text ='', font=headerfont)
        self.label.grid(row= 0, column = 0, columnspan=20)
          
        self.topframe = tk.LabelFrame(self, text='', borderwidth=0)
        self.topframe.grid(row=1, column=0, padx=200, columnspan=20)

        self.firstframe =tk.LabelFrame(self.topframe, text='Project Menu', borderwidth=0, font=labelsfont)
        self.secondframe = tk.LabelFrame(self.topframe, text='Resource Menu', borderwidth=0, font=labelsfont)
        self.middleframe = tk.LabelFrame(self.topframe, borderwidth=0, text='')

        self.firstframe.grid(column= 0, row=0, padx=10)
        self.middleframe.grid(column=1, row=0, padx=10)
        self.secondframe.grid(column=2, row=0, padx=10)

        self.wordcloud = tk.PhotoImage(file="smallwhitewordcloud.png")

        self.new_projects = tk.Button(self.firstframe, text='Add Project',
                                      command=lambda: controller.show_frame(Projects))
        self.new_projects.config(height=5, width=13)
        self.new_projects.grid(column = 0, row= 0, pady=5)

        self.view_project = tk.Button(self.firstframe, text='Link Resources\n to Projects',
                                      command=lambda: controller.show_frame(LinkResources))
        self.view_project.config(height=5,width=13)
        self.view_project.grid(column=0, row=1, pady=5)

        self.edit_project = tk.Button(self.firstframe, text='Edit Project')
        self.edit_project.config(height=5, width=13)
        self.edit_project.grid(column=0, row=2, pady=5)

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

        button1 = ttk.Button(self.middleframe, text = "", image=self.wordcloud, compound="center")
        button1.grid(column=2, row=1, rowspan=5,padx=10,sticky=tk.E)

class AddResource(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.button_window = tk.LabelFrame(self, text='Resource Type')
        self.button_window.grid(column=0, row=0, columnspan=4, padx=250, pady=100, sticky=tk.N+tk.S+tk.E+tk.W)

        self.AddAudioVideoButton = tk.Button(self.button_window, text='Audio\n and Video', width=20,height=5,
                                        command=lambda: controller.show_frame(AddAudioVideo))
        self.AddTextButton= tk.Button(self.button_window, text='Add Text', width=20,height=5,
                                        command=lambda: controller.show_frame(AddText))
        self.AddCourseButton= tk.Button(self.button_window, text='Courses', width=20,height=5,
                                        command=lambda: controller.show_frame(AddCourse))
        self.AddInteractiveMediaButton= tk.Button(self.button_window, text='Interactive\n Media',  width=20,height=5,
                                        command=lambda: controller.show_frame(AddInteractiveMedia))
        self.AddOnlineMediaButton= tk.Button(self.button_window, text='Online Media', width=20,height=5,
                                        command=lambda: controller.show_frame(AddOnlineMedia))
        self.AddImagesButton= tk.Button(self.button_window, text='Images', width=20,height=5,
                                        command=lambda: controller.show_frame(AddImages))



        self.AddTextButton.grid(column=0, row=0)
        self.AddOnlineMediaButton.grid(column=1, row=0)
        self.AddAudioVideoButton.grid(column=2, row=0)
        self.AddCourseButton.grid(column=1, row=1)
        self.AddInteractiveMediaButton.grid(column=0, row=1)
        self.AddImagesButton.grid(column=2, row=1)


class AddText(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        mainframe = tk.LabelFrame(self, text='Books/Texts', borderwidth=0)
        mainframe.grid(column=0, row=0, sticky=tk.N+tk.S+tk.W+tk.E)

        header_frame = tk.LabelFrame(mainframe, text='', borderwidth=0)
        header_frame.grid(column=0, row=0, columnspan=20,padx=10)

        topleftframe = tk.LabelFrame(mainframe, text="", borderwidth=0)
        topleftframe.grid(column=0, row=1, padx=10, pady=5)

        topcenterframe = tk.LabelFrame(mainframe, text="", borderwidth=0)
        topcenterframe.grid(column=1, row=1, pady=5)

        toprightframe = tk.LabelFrame(mainframe, text="", borderwidth=0)
        toprightframe.grid(column=2, row=1, pady=5)

        bottomframe = tk.LabelFrame(self, text="", borderwidth=0)
        bottomframe.grid(column=0, row=3, padx=10, sticky=tk.W)

        self.label = tk.Label(header_frame, text='New Text', font=smallheaderfont)
        self.label.grid(column=0, row=1, pady=5)

        self.title = tk.StringVar()
        self.author = tk.StringVar()
        self.year = tk.IntVar()
        self.pages = tk.IntVar()
        self.subject = tk.StringVar()
        self.notes = tk.StringVar()

        self.publisher = tk.StringVar()
        self.publisher_options = data.list_publishers()
        self.publisher.set('Choose one:')

        self.language = tk.StringVar()
        self.language_options = data.list_languages()
        self.language.set('Choose one:')

        self.new_lang = tk.StringVar()
        self.new_pub = tk.StringVar()

        self.new_lang_flag = tk.IntVar(self, value=0)
        self.new_pub_flag = tk.IntVar(self, value=0)

        # Top left frame

        self.title_label=tk.Label(topleftframe, text='Title')
        self.title_entry=ttk.Entry(topleftframe, width=50, textvariable =self.title)

        self.author_label=tk.Label(topleftframe, text ='Author(s)')
        self.author_entry = ttk.Entry(topleftframe, width=50, textvariable=self.author)

        self.year_label=tk.Label(topleftframe, text ='Year')
        self.year_entry = ttk.Entry(topleftframe, width=50, textvariable=self.year)

        self.pages_label=tk.Label(topleftframe, text ='Pages')
        self.pages_entry = ttk.Entry(topleftframe, width=50, textvariable=self.pages)

        self.title_label.grid(column=0, row=0, pady=2, sticky=tk.W)
        self.title_entry.grid(column=1, row=0, pady=2)

        self.author_label.grid(column=0, row=1, pady=2, sticky=tk.W)
        self.author_entry.grid(column=1, row=1, pady=2)

        self.year_label.grid(column=0, row=2, pady=2, sticky=tk.W)
        self.year_entry.grid(column=1, row=2, pady=2)

        self.pages_label.grid(column=0, row=3,  pady=2, sticky=tk.W)
        self.pages_entry.grid(column=1, row=3, pady=2)


        # Top center frame
        self.publisher_label = tk.Label(topcenterframe, text='Publisher')
        self.publisher_entry = tk.OptionMenu(topcenterframe, self.publisher,
                                                *self.publisher_options)
        self.publisher_entry.configure(width=20)

        self.add_publisher_entry = ttk.Entry(topcenterframe, textvariable =self.new_pub)
        self.add_publisher_entry.configure(width=20)

        self.language_label = tk.Label(topcenterframe, text='Language')
        self.language_entry= tk.OptionMenu(topcenterframe, self.language,
                                                *self.language_options)
        self.language_entry.configure(width=20)

        self.add_language_entry=ttk.Entry(topcenterframe, width=20, textvariable =self.new_lang)

        self.notes_label = tk.Label(topcenterframe, text='Notes')
        self.notes_entry = ttk.Entry(topcenterframe, width=50, textvariable =self.notes)

        self.subject_label = tk.Label(topcenterframe, text='Subject')
        self.subject_entry = ttk.Entry(topcenterframe, width=50, textvariable=self.subject)


        self.publisher_label.grid(column=0, row=0)
        self.publisher_entry.grid(column=1, row=0)
        self.add_publisher_entry.grid(column=2, row=0)


        self.language_label.grid(column=0, row=2)
        self.language_entry.grid(column=1, row=2)
        self.add_language_entry.grid(column=2, row=2)

        self.notes_label.grid(column=0, row=3, sticky=tk.W)
        self.notes_entry.grid(column=1, row=3, columnspan=2, sticky=tk.W)

        self.subject_label.grid(column=0, row=4, sticky=tk.W)
        self.subject_entry.grid(column=1, row=4, columnspan=2, sticky=tk.W)

        # Top right frame

        self.add_pub_flag = tk.Checkbutton(toprightframe, text='Add new publisher',
                                           variable=self.new_pub_flag)
        self.add_lang_flag = tk.Checkbutton(toprightframe, text='Add new language',
                                            variable=self.new_lang_flag)

        self.add_pub_flag.grid(column=0, row=0, sticky=tk.E)
        self.add_lang_flag.grid(column=0, row=1, sticky=tk.E)

        self.addtextresource = tk.Button(toprightframe, text='Save', command=lambda: self.new_textresource())
        self.addtextresource.config(width=12, cursor='hand2')
        self.addtextresource.grid(column=0, row=2, padx=10, pady=12)


        # Bottom frame

        self.scrollresources = tk.Scrollbar(bottomframe)
        self.scrollresources.grid(column=1,row=1, sticky=tk.N+tk.S+tk.W)

        self.resource_list = ttk.Treeview(bottomframe,
                                         columns=('Title', 'Author','Year',
                                                  'Pages','Publisher',
                                                  'Language', 'Notes'))

        self.scrollresources.configure(orient="vertical", command=self.resource_list.yview)
        self.resource_list.configure(yscrollcommand=self.scrollresources.set)

        self.resource_list['columns'] = ('Title', 'Author', 'Year', 'Pages',
                          'Publisher', 'Language', 'Notes')
        self.resource_list.column('#0', width=1)
        self.resource_list.column('0', width=200, anchor='w')
        self.resource_list.column('1', width=150, anchor='w')
        self.resource_list.column('2', width=75, anchor='w')
        self.resource_list.column('3', width=60, anchor='w')
        self.resource_list.column('4', width=100, anchor='w')
        self.resource_list.column('5', width=100, anchor='w')
        self.resource_list.column('6', width=200, anchor='w')
        self.resource_list.grid(column=0, row=1)

        self.resource_list.heading('0', text='Title', anchor='w')
        self.resource_list.heading('1', text='Author(s)', anchor='w')
        self.resource_list.heading('2', text='Year', anchor='w')
        self.resource_list.heading('3', text='Pages', anchor='w')
        self.resource_list.heading('4', text='Publisher', anchor='w')
        self.resource_list.heading('5', text='Language', anchor='w')
        self.resource_list.heading('6', text='Notes', anchor='w')

        self.treeview = self.resource_list
        self.list_resources()
        self.update_entry_widgets()

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
        resources = data.list_text_resources()
        for item in resources:
            self.treeview.insert('', 'end', values=item)

    def update_entry_widgets(self):

        self.title_entry.delete(0, 'end')
        self.author_entry.delete(0, 'end')
        self.year_entry.delete(0, 'end')
        self.pages_entry.delete(0, 'end')
        self.subject_entry.delete(0, 'end')
        self.notes_entry.delete(0, 'end')
        self.add_language_entry.delete(0, 'end')
        self.add_publisher_entry.delete(0, 'end')
        self.new_lang_flag.set(0)
        self.new_pub_flag.set(0)
        self.publisher.set('Choose publisher:')
        self.language.set('Choose language:')


    def new_textresource(self):

        if self.new_pub_flag.get() == 1:
            self.thepublisher = self.new_pub.get()
        else:
            self.thepublisher = self.publisher.get()

        if self.new_lang_flag.get() == 1:
            self.thelanguage = self.new_lang.get()
        else:
            self.thelanguage = self.language.get()

        data.add_text(self.title.get(), self.author.get(), self.year.get(),
                          self.pages.get(), self.thepublisher,
                          self.thelanguage, self.subject.get(), self.notes.get())

        self.list_resources()
        self.update_entry_widgets()








class AddInteractiveMedia(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.home = tk.Button(self, text='Home', command=lambda: controller.show_frame(HomePage))
        self.home.config(width=15, cursor='hand2')
        self.home.grid(column=0, row=2, padx=10, sticky=tk.W)



class AddImages(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.home = tk.Button(self, text='Home', command=lambda: controller.show_frame(HomePage))
        self.home.config(width=15, cursor='hand2')
        self.home.grid(column=0, row=2, padx=10, sticky=tk.W)

class LinkResources(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.project_id = None
        self.resources = set()

        self.project_title = tk.StringVar()
        self.project_type = tk.StringVar()
        self.resource_subject = tk.StringVar()

        self.media_type = tk.StringVar()
        self.media_type.set("?")

        self.searchheader = ttk.Label(self, text='Search by project title', font=headerfont)
        self.searchheader.grid(column=0, row=0)

        self.mainframe = tk.LabelFrame(self, text='', borderwidth=0)
        self.mainframe.grid(column=0, row=1, sticky=tk.W + tk.E + tk.N)

        # TOP LEFT FRAME
        self.searchframe = tk.LabelFrame(self.mainframe, text='', borderwidth=0)
        self.searchframe.grid(column=0, row=0, sticky=tk.N+tk.W+tk.E)

        self.titlebox_label = tk.Label(self.searchframe, text='Title', font=labelsfont)
        self.titlebox_label.grid(column=0, row=0, sticky=tk.W)
        self.titlebox = tk.Entry(self.searchframe, width=32, textvariable=self.project_title)
        self.titlebox.grid(column=1, row=0, padx=5, sticky=tk.E)

        self.searchbutton = ttk.Button(self.searchframe, text='Search', command=lambda: self.search_projects())
        self.searchbutton.config(width=10, cursor='hand2')
        self.searchbutton.grid(column=1, row=2, padx=5, pady=5, sticky=tk.E)

        # TOP RIGHT FRAME PROJECT SEARCH RESULTS:

        self.resultsframe = tk.LabelFrame(self.mainframe, text='', borderwidth=0)
        self.resultsframe.grid(column=3, row=0, sticky=tk.E)

        self.scrollresults = tk.Scrollbar(self.resultsframe)
        self.scrollresults.grid(column=4, row=0, sticky=tk.N +tk.S + tk.W)

        self.project_list = ttk.Treeview(self.resultsframe, height=4, selectmode='browse',
                                         columns=('Name', 'Type', 'Description', 'Start date', 'End date'))

        self.scrollresults.configure(orient="vertical", command=self.project_list.yview)
        self.project_list.configure(yscrollcommand=self.scrollresults.set)

        self.project_list['columns'] = ('Name', 'Type', 'Description', 'Start date', 'End date')
        self.project_list.column('#0', width=5)
        self.project_list.grid(column=3, row=0, sticky=tk.W+tk.E)

        self.project_list.heading('0', text='Name', anchor='w')
        self.project_list.heading('1', text='Type', anchor='w')
        self.project_list.heading('2', text='Description', anchor='w')
        self.project_list.heading('3', text='Start date', anchor='w')
        self.project_list.heading('4', text='End date', anchor='w')

        self.project_list.column('0', width=200, anchor='w')
        self.project_list.column('1',  width=100, anchor='w')
        self.project_list.column('2', width=200, anchor='w')
        self.project_list.column('3', width=75, anchor='w')
        self.project_list.column('4', width=75, anchor='w')
        self.treeview_projects = self.project_list
        self.treeview_projects.bind('<ButtonRelease-1>', self.select_project)

        # MIDDLE FRAME
        self.middleframe = tk.LabelFrame(self.mainframe, text='', borderwidth=0)
        self.middleframe.grid(columnspan=40, pady=10, column=0, row=3)

        self.resourceresults_label = ttk.Label(self.middleframe, text='Available Resources', font=smallheaderfont)
        self.resourceresults_label.grid(columnspan=4, column=2, row=0, pady=5)

        # BOTTOM LEFT FRAME SORT FRAME

        self.searchresourceframe = tk.LabelFrame(self.mainframe, text='', borderwidth=0)
        self.searchresourceframe.grid(column=0, row=4,  sticky=tk.N)

        self.sortframe = tk.LabelFrame(self.searchresourceframe, text='', borderwidth=4)
        self.sortframe.grid(columnspan=2, column=0, row=2, padx=5, pady=5, sticky=tk.W+tk.E)

        self.subjectbox_label = tk.Label(self.searchresourceframe, text='Subject', font=labelsfont)
        self.subjectbox_label.grid(column=0, row=0, sticky=tk.W)
        self.subjectbox = tk.Entry(self.searchresourceframe, width=28, textvariable=self.resource_subject)
        self.subjectbox.grid(column=1, row=0,  sticky=tk.W)

        self.searchbutton = ttk.Button(self.searchresourceframe, text='Search',command=lambda:self.search_resources())
        self.searchbutton.config(width=10, cursor='hand2')
        self.searchbutton.grid(column=1, row=1, pady=5, sticky=tk.E)

        self.sort_label = tk.Label(self.sortframe, text='Limit by type', font=smallheaderfont)
        self.sort_label.grid(column=0, row=0, sticky=tk.W)

        self.audio_rb = tk.Radiobutton(self.sortframe, text='Audio and Video', variable=self.media_type,
                                       value='Audio and Video', command= self.limit_resources)
        self.book_rb = tk.Radiobutton(self.sortframe, text='Texts', variable=self.media_type, value='Texts',
                                       command= self.limit_resources)
        self.course_rb = tk.Radiobutton(self.sortframe, text='Courses', variable=self.media_type, value='Courses',
                                       command= self.limit_resources)
        self.interactive_rb = tk.Radiobutton(self.sortframe, text='Interactive Media', variable=self.media_type,
                                             value='Interactive Media', command= self.limit_resources)
        self.webdocs_rb = tk.Radiobutton(self.sortframe, text='Web docs', variable=self.media_type,
                                         value='Web docs', command= self.limit_resources)

        self.audio_rb.grid(column=1, row=0, sticky=tk.W)
        self.book_rb.grid(column=1, row=1, sticky=tk.W)
        self.course_rb.grid(column=1, row=2, sticky=tk.W)
        self.interactive_rb.grid(column=1, row=3, sticky=tk.W)
        self.webdocs_rb.grid( column=1, row=4, sticky=tk.W)

        self.showall = ttk.Button(self.sortframe, text='Show All')
        self.showall.config(width=10, cursor='hand2')
        self.showall.grid(column=1, row=7)

        # BOTTOM RIGHT FRAME
        self.resourceresults = tk.LabelFrame(self.mainframe, text='', borderwidth=0)
        self.resourceresults.grid(column=3, row=4, columnspan=40, sticky=tk.E)

        self.scollresources = tk.Scrollbar(self.resourceresults)
        self.scollresources.grid(column=2, row=0, sticky=tk.N + tk.S + tk.W)

        self.resource_list = ttk.Treeview(self.resourceresults, height=10, selectmode='extended',
                                          columns=('Title', 'Author', 'Year',
                                                   'Pages', 'Language', 'Format',
                                                   'Abstract'))

        self.scollresources.configure(orient="vertical", command=self.resource_list.yview)
        self.resource_list.configure(yscrollcommand=self.scollresources.set)

        self.resource_list['columns'] = ('Title', 'Author', 'Year', 'Pages', 'Language', 'Format')
        self.resource_list.column('#0', width=1)
        self.resource_list.column('0', width=250, anchor='w')
        self.resource_list.column('1', width=150, anchor='w')
        self.resource_list.column('2', width=75, anchor='w')
        self.resource_list.column('3', width=60, anchor='w')
        self.resource_list.column('4', width=100, anchor='w')
        self.resource_list.column('5', width=100, anchor='w')
        self.resource_list.grid(column=0, row=0, sticky=tk.W + tk.N + tk.E)

        self.resource_list.heading('0', text='Title', anchor='w')
        self.resource_list.heading('1', text='Author(s)', anchor='w')
        self.resource_list.heading('2', text='Year', anchor='w')
        self.resource_list.heading('3', text='Pages', anchor='w')
        self.resource_list.heading('4', text='Language', anchor='w')
        self.resource_list.heading('5', text='Format', anchor='w')
        self.treeview_resources = self.resource_list
        self.treeview_resources.bind('<ButtonRelease-1>', self.select_resources)

        self.go_to_resources = ttk.Button(self.resourceresults, text='Link resource(s)',
                                          command=lambda: self.link_project_resources())
        self.go_to_resources.config(cursor='hand2')
        self.go_to_resources.grid(column=0, row=4, sticky=tk.E)

        self.home = ttk.Button(self.mainframe, text='Home', command=lambda: controller.show_frame(HomePage))
        self.home.config(width=10, cursor='hand2')
        self.home.grid(column=0, row=5, sticky=tk.N)

    def select_resources(self, event):
        self.resources.clear()

        for item in self.treeview_resources.selection():
            item_text = self.treeview_resources.item(item)

            resource_name = item_text['values'][0]

            resource_ids = data.get_resource_id(resource_name)
            resourceID = resource_ids[0][0]
            mediaID = resource_ids[0][1]
            print('Resource ID = ', resourceID)
            print('Media ID = ', mediaID)

            self.resources.add((resourceID, mediaID))

        return self.resources

    def select_project(self, event):
        """ Takes item selected from listbox and stores it as a global variable to be used in
            Link resource window
        """
        self.project_id = None
        item = self.treeview_projects.selection()[0]
        project = self.treeview_projects.item(item)
        project_name = project['values'][0]

        project = data.get_projectID(project_name)
        self.project_id = project[0]
        return self.project_id

    def clear_selection(self):
        item = self.treeview_projects.selection()[0]
        self.project_list.selection_remove(item)

        items = self.treeview_resources.selection()[0]
        self.resource_list.selection_remove(items)

    def link_project_resources(self):

        for resource_item, media_type in self.resources:
            data.link_to_resources(self.project_id, resource_item, media_type)

        self.clear_selection()

        print("Added item(s)")


    def search_projects(self):
        for i in self.project_list.get_children():
            self.project_list.delete(i)
        projects = data.find_project(self.project_title.get())
        for item in projects:
            self.treeview_projects.insert('', 'end', values=item)
        self.titlebox.delete(0, 'end')


    def search_resources(self):
        for i in self.resource_list.get_children():
            self.resource_list.delete(i)

        resources = data.find_resource_by_subject(self.resource_subject.get())

        for item in resources:
            self.treeview_resources.insert('', 'end', values=item)
        self.subjectbox.delete(0, 'end')

    def limit_resources(self):
        for i in self.resource_list.get_children():
            self.resource_list.delete(i)

        resources_sorted = data.resources_by_type(self.media_type.get())

        for item in resources_sorted:
            self.treeview_resources.insert('', 'end', values=item)
        self.subjectbox.delete(0, 'end')

class Projects(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        main_frame = tk.LabelFrame(self, text='',borderwidth=4)
        main_frame.grid(column=0, row=0, columnspan=10, sticky=tk.W+tk.E+tk.N+tk.S)

        self.label = tk.Label(main_frame, text='Project Details', font=labelsfont)
        self.label.grid(column=0, row=0, columnspan=10)

        # FRAMES

        self.topleftframe = tk.LabelFrame(main_frame, text='', borderwidth=4)
        self.topleftframe.grid(column=0, row=1)

        self.toprightframe = tk.LabelFrame(main_frame, text='', borderwidth=4)
        self.toprightframe.grid(column=1, row=1)

        self.bottomframe = tk.LabelFrame(self, text='', borderwidth=4)
        self.bottomframe.grid(column=0, row=5, columnspan=4)

        # VARIABLES

        self.project_name = tk.StringVar()
        self.project_type = tk.StringVar()
        self.description = tk.StringVar()
        self.start_date = tk.StringVar()
        self.end_date = tk.StringVar()
        self.new_type = tk.IntVar(self, value=0)
        self.add_projecttype = tk.StringVar()
        self.choices = tk.StringVar()
        self.project_category_options = data.list_project_category()
        self.choices.set('Choose project type:')

        # Top Left frame

        self.project_name_label = tk.Label(self.topleftframe, text='Project Name')
        self.project_name_entry = ttk.Entry(self.topleftframe, width=60, textvariable=self.project_name)

        self.description_label = tk.Label(self.topleftframe, text='Description')
        self.description_entry = ttk.Entry(self.topleftframe, width=60, textvariable=self.description)

        self.project_type_label = tk.Label(self.topleftframe, text='Project Type')
        self.project_type_entry = tk.OptionMenu(self.topleftframe, self.choices, *self.project_category_options)
        self.project_type_entry.configure(width=20)

        self.new_projecttype_label = tk.Label(self.topleftframe, text='New Project Type')
        self.new_projecttype = ttk.Entry(self.topleftframe, width=60, textvariable=self.add_projecttype)

        self.project_name_label.grid(column=0, row=1, sticky=tk.W)
        self.project_name_entry.grid(column=1, row=1, columnspan=3, sticky=tk.W)

        self.description_label.grid(column=0, row=2, sticky=tk.W)
        self.description_entry.grid(column=1, row=2,  columnspan=3, sticky=tk.W)

        self.project_type_label.grid(column=0, row=4, sticky=tk.W)
        self.project_type_entry.grid(column=1, row=4, sticky=tk.W)
        self.new_projecttype_label.grid(column=0, row=5)
        self.new_projecttype.grid(column=1, row=5, columnspan=3,)

        self.new_type_flag = tk.Checkbutton(self.topleftframe, text="Add new project type", variable=self.new_type)
        self.new_type_flag.grid(column=2, row=4, padx=6, sticky=tk.W)


        # Top right frame
        self.start_label = tk.Label(self.toprightframe, text='Start Date')
        self.start_entry = ttk.Entry(self.toprightframe, width=50, textvariable=self.start_date)

        self.finish_label = tk.Label(self.toprightframe, text='End Date')
        self.finish_entry = ttk.Entry(self.toprightframe, width=50, textvariable=self.end_date)

        self.start_label.grid(column=0, row=1, sticky=tk.W)
        self.start_entry.grid(column=1, row=1,  sticky=tk.W)
        self.finish_label.grid(column=0, row=2, sticky=tk.W)
        self.finish_entry.grid(column=1, row=2, sticky=tk.W)

        self.add_project = tk.Button(self.toprightframe, text='Add Project', command=lambda: self.save_project())
        self.add_project.grid(column=1, row=6, padx=10,pady=12, sticky=tk.E)

        # Bottom Frame

        self.scollprojects = tk.Scrollbar(self.bottomframe)
        self.scollprojects.grid(column=1, row=0, sticky=tk.N + tk.S)

        self.project_list = ttk.Treeview(self.bottomframe, columns=('Name', 'Type','Description', 'Start date', 'End date'))

        self.scollprojects.configure(orient="vertical", command=self.project_list.yview)
        self.project_list.configure(yscrollcommand=self.scollprojects.set)

        self.project_list['columns'] = ('Name', 'Type','Description', 'Start date', 'End date')
        self.project_list.column('#0', width=5)
        self.project_list.grid(column=0, row=0,sticky=tk.E)

        self.project_list.heading('0',  text='Name', anchor='w')
        self.project_list.heading('1',text='Type', anchor='w')
        self.project_list.heading('2', text='Description', anchor='w')
        self.project_list.heading('3',text='Start date', anchor='w')
        self.project_list.heading('4', text='End date', anchor='w')

        self.project_list.column('0', width=250, anchor='w')
        self.project_list.column('1', width=150, anchor='w' )
        self.project_list.column('2', width=250, anchor='w')
        self.project_list.column('3', width=100, anchor='w')
        self.project_list.column('4', width=100,anchor='w')
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
        self.finish_entry.delete(0, 'end')
        self.new_projecttype.delete(0, 'end')
        self.new_type.set(0)
        self.choices.set('Choose project type:')
        self.project_category_options = data.list_project_category()


    def save_project(self):

        if self.new_type.get() == 1:
            self.category = self.add_projecttype.get()
        else:
            self.category = self.choices.get()


        data.add_project(self.project_name.get(), self.category, self.description.get(),
                         self.start_date.get(), self.end_date.get())

        self.list_projects()
        self.update_widgets()


class AddOnlineMedia(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.author = tk.StringVar()
        self.title = tk.StringVar()
        self.date = tk.StringVar()
        self.host = tk.StringVar()
        self.access_date = tk.StringVar()
        self.url = tk.StringVar()
        self.subject = tk.StringVar()
        self.comments = tk.StringVar()
        self.audio_video = tk.IntVar()
        self.audio_video.set('?')

        # Frames

        self.mainframe = tk.LabelFrame(self, text='', borderwidth=4)
        self.mainframe.grid(column=0, row=1, sticky=tk.N + tk.S + tk.W + tk.E)

        self.topleft = tk.LabelFrame(self.mainframe, text="", borderwidth=3)
        self.topleft.grid(column=0, row=1, sticky=tk.W + tk.E)

        self.topright = tk.LabelFrame(self.mainframe, text="", borderwidth=3)
        self.topright.grid(column=1, row=1, sticky=tk.W + tk.E)

        self.bottomleft = tk.LabelFrame(self.mainframe, text="", borderwidth=3)
        self.bottomleft.grid(column=0, row=4, sticky=tk.W + tk.E)

        self.bottomright = tk.LabelFrame(self.mainframe, text="", borderwidth=3)
        self.bottomright.grid(column=1, row=5, sticky=tk.W + tk.E)

        self.bottom_middleframe = tk.LabelFrame(self.mainframe, text='', borderwidth=3)
        self.bottom_middleframe.grid(column=0, row=3, columnspan=2, sticky=tk.W + tk.E)

        # Bottom left frame
        self.home = tk.Button(self.bottomleft, text='Home', command=lambda: controller.show_frame(HomePage))
        self.home.config(width=15, cursor='hand2')
        self.home.grid(column=0, row=2, padx=10, sticky=tk.W)

        self.create_values()

        self.create_top_frame_widgets(self.A, self.B, self.C, self.D, self.E)

        self.add_radio_buttons()

        self.display_resources(self.c1, self.c2, self.c3, self.c4, self.c5, self.c6)

    def create_values(self):
        self.A = 'Online Media'
        self.B = 'Author'
        self.C = 'Date'
        self.D = 'Access date'
        self.E = 'Domain'

        self.c1 = 'Title'
        self.c2 ='Author'
        self.c3 = 'Date'
        self.c4 = 'Host'
        self.c5 = 'Access date'
        self.c6 = 'URL'

    def create_top_frame_widgets(self, a, b, c, d, e):

        # Title Frame
        window_title = tk.Label(self.mainframe, text=a)
        window_title.grid(column=0, row=0, columnspan=2)

        # Top left frame

        author_label = tk.Label(self.topleft, text=b)
        author_entry = tk.Entry(self.topleft, width=50, textvariable=self.author)

        title_label = tk.Label(self.topleft, text='Title')
        title_entry = tk.Entry(self.topleft, width=50, textvariable=self.title)

        date_label = tk.Label(self.topleft, text=c)
        date_entry = tk.Entry(self.topleft, width=50, textvariable=self.date)

        subject_label = tk.Label(self.topleft, text='Subject')
        subject_entry = tk.Entry(self.topleft, width=50, textvariable=self.subject)

        host_label = tk.Label(self.topright, text=d)
        host_entry = tk.Entry(self.topright, width=50, textvariable=self.host)

        access_date_label = tk.Label(self.topright, text=e)
        access_date_entry = tk.Entry(self.topright, width=50, textvariable=self.access_date)

        url_label = tk.Label(self.topright, text='URL')
        url_entry = tk.Entry(self.topright, width=50, textvariable=self.url)

        comment_label = tk.Label(self.topright, text='Notes')
        comment_entry = tk.Entry(self.topright, width=50, textvariable=self.comments)

        author_label.grid(column=0, row=0)
        author_entry.grid(column=1, row=0)
        title_label.grid(column=0, row=1)
        title_entry.grid(column=1, row=1)
        date_label.grid(column=0, row=2)
        date_entry.grid(column=1, row=2)
        subject_label.grid(column=0, row=3)
        subject_entry.grid(column=1, row=3)

        host_label.grid(column=0, row=0)
        host_entry.grid(column=1, row=0)
        url_label.grid(column=0, row=1)
        url_entry.grid(column=1, row=1)
        access_date_label.grid(column=0, row=2)
        access_date_entry.grid(column=1, row=2)
        comment_label.grid(column=0, row=3)
        comment_entry.grid(column=1, row=3)



    def add_radio_buttons(self):
        self.center_leftframe = tk.LabelFrame(self.mainframe, text='', borderwidth=3)
        self.center_leftframe.grid(column=0, row=2)

        self.media_audio = tk.Radiobutton(self.center_leftframe, text='Audio', variable=self.audio_video)
        self.media_audio.grid(column=1, row=0)

        self.media_video = tk.Radiobutton(self.center_leftframe, text='Video', variable=self.audio_video)
        self.media_video.grid(column=2, row=0)

        self.media_other = tk.Radiobutton(self.center_leftframe, text='Other', variable=self.audio_video)
        self.media_other.grid(column=3, row=0)


    def display_resources(self, c1, c2, c3, c4, c5, c6):
        scrollwebdocs = tk.Scrollbar(self.bottom_middleframe)
        scrollwebdocs.grid(column=1, row=1, sticky=tk.N + tk.S + tk.W)

        webdocs_list = ttk.Treeview(self.bottom_middleframe,
                                         columns= (c1, c2, c3, c4, c5, c6))

        scrollwebdocs.configure(orient="vertical", command=webdocs_list.yview)
        webdocs_list.configure(yscrollcommand=scrollwebdocs.set)

        webdocs_list['columns'] = ('Title', 'Author', 'Date',
                                        'Host', 'Access date', 'URL')
        webdocs_list.column('#0', width=1)
        webdocs_list.column('0', width=150, anchor='w')
        webdocs_list.column('1', width=100, anchor='w')
        webdocs_list.column('2', width=75, anchor='w')
        webdocs_list.column('3', width=75, anchor='w')
        webdocs_list.column('4', width=75, anchor='w')
        webdocs_list.column('5', width=250, anchor='w')
        webdocs_list.grid(column=0, row=1)

        webdocs_list.heading('0', text=c1, anchor='w')
        webdocs_list.heading('1', text=c2, anchor='w')
        webdocs_list.heading('2', text=c3, anchor='w')
        webdocs_list.heading('3', text=c4, anchor='w')
        webdocs_list.heading('4', text=c5, anchor='w')
        webdocs_list.heading('5', text='URL', anchor='w')

        treeview = webdocs_list


    def saveonlinemedia(self):
        data.add_online_media(self.title.get(), self.author.get(), self.date.get(), self.subject.get(),
                              self.host.get(), self.url.get(), self.access_date.get(), self.comments.get(),
                              self.audio_video.get())
        pass

class AddCourse(AddOnlineMedia):
    def __init__(self, parent, controller):
        AddOnlineMedia.__init__(self, parent, controller)

        self.create_values()

        self.display_resources(AddOnlineMedia.c1, AddOnlineMedia.c2, AddOnlineMedia.c3, AddOnlineMedia.c4,
                               AddOnlineMedia.c5, AddOnlineMedia.c6)


        self.create_top_frame_widgets(AddOnlineMedia.A, AddOnlineMedia.B, AddOnlineMedia.C,
                                      AddOnlineMedia.D, AddOnlineMedia.E)

    def create_values(self):

        AddOnlineMedia.A = 'Courses'
        AddOnlineMedia.B = 'Teacher'
        AddOnlineMedia.C = 'Start date'
        AddOnlineMedia.D = 'End date'
        AddOnlineMedia.E = 'Platform'

        AddOnlineMedia.c1 = 'Title'
        AddOnlineMedia.c2 = 'Teacher'
        AddOnlineMedia.c3 = 'Start date'
        AddOnlineMedia.c4 = 'End date'
        AddOnlineMedia.c5 = 'Platform'
        AddOnlineMedia.c6 = 'URL'



        #self.create_top_frame_widgets('Courses', 'Teacher', 'Start date', 'End date', 'Platform')




class AddAudioVideo(AddOnlineMedia):
    def __init__(self, parent, controller):
        AddOnlineMedia.__init__(self, parent, controller)

        self.display_resources(AddOnlineMedia.c1, AddOnlineMedia.c2, AddOnlineMedia.c3, AddOnlineMedia.c4,
                               AddOnlineMedia.c5, AddOnlineMedia.c6)

        self.create_top_frame_widgets(AddOnlineMedia.A, AddOnlineMedia.B, AddOnlineMedia.C,
                                      AddOnlineMedia.D, AddOnlineMedia.E)

    def create_values(self):
        AddOnlineMedia.A = 'Audio and Video'
        AddOnlineMedia.B = 'Creator'
        AddOnlineMedia.C = 'Duration'
        AddOnlineMedia.D = 'Format'
        AddOnlineMedia.E = 'Type'

        AddOnlineMedia.c1 = 'Title'
        AddOnlineMedia.c2 ='Creator'
        AddOnlineMedia.c3 = 'Duration'
        AddOnlineMedia.c4 = 'Format'
        AddOnlineMedia.c5 = 'Type'
        AddOnlineMedia.c6 = 'URL'


class SearchResource(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.resource_title = tk.StringVar()
        self.resource_author = tk.StringVar()
        self.resource_subject = tk.StringVar()

        self.searchframe = tk.LabelFrame(self, text='Search parameters', borderwidth=0)
        self.searchframe.grid(column=0, row=0)

        self.searchbar = tk.LabelFrame(self.searchframe, text='', borderwidth=0)
        self.searchbar.grid(column=0, row=0, sticky =tk.W+tk.E)

        self.middleframe = tk.LabelFrame(self.searchframe, text='',borderwidth=0)
        self.middleframe.grid(column=0, row=1, sticky=tk.W+tk.E)

        self.bottomframe = tk.LabelFrame(self.searchframe, text='', borderwidth=0)
        self.bottomframe.grid(column=0, row=2, sticky=tk.W+tk.E)

        self.r_title_label = tk.Label(self.searchbar, text='Title: ')
        self.r_entry = tk.Entry(self.searchbar,  width=48, textvariable=self.resource_title)

        self.r_author_label = tk.Label(self.searchbar, text='Author: ')
        self.r_author_entry= tk.Entry(self.searchbar,  width=48, textvariable=self.resource_author)

        self.r_subject_label = tk.Label(self.searchbar, text='Subject: ')
        self.r_subject_entry= tk.Entry(self.searchbar,  width=48, textvariable=self.resource_subject)

        self.r_title_label.grid(column=0, row=0, padx=5)
        self.r_entry.grid(column=1, row=0, padx=5)

        self.r_author_label.grid(column=0, row=1, padx=5)
        self.r_author_entry.grid(column=1, row=1, padx=5)

        self.r_subject_label.grid(column=0, row=2, padx=5)
        self.r_subject_entry.grid(column=1, row=2, padx=5)

        self.searchbutton = tk.Button(self.searchbar, text='Search')
        self.searchbutton.config(width=12, cursor='hand2')
        self.searchbutton.grid(column=1, row=3, padx= 10, pady=10, sticky=tk.E)

        self.homebutton = tk.Button(self.bottomframe, text='Home', command=lambda: controller.show_frame(HomePage))
        self.homebutton.config(width=12, cursor='hand2')
        self.homebutton.grid(column=0, row=1, padx=10, pady=2, sticky=tk.W)

        self.addresource = tk.Button(self.bottomframe, text='Add Resource',
                                     command=lambda: controller.show_frame(AddResource))
        self.addresource.config(width=12, cursor='hand2')
        self.addresource.grid(column=0, row=2, padx=10,pady=2, sticky=tk.W)

        self.resource_list = ttk.Treeview(self.middleframe,
                                          columns=('Title', 'Author', 'Year',
                                                   'Pages', 'Publisher',
                                                   'Language', 'Notes'))
        self.resource_list['columns'] = ('Title', 'Author', 'Year', 'Pages',
                                         'Publisher', 'Language', 'Notes')
        self.resource_list.column('#0', width=1)
        self.resource_list.column('0', width=250, anchor='w')
        self.resource_list.column('1', width=150, anchor='w')
        self.resource_list.column('2', width=75, anchor='w')
        self.resource_list.column('3', width=60, anchor='w')
        self.resource_list.column('4', width=100, anchor='w')
        self.resource_list.column('5', width=90, anchor='w')
        self.resource_list.column('6', width=200, anchor='w')
        self.resource_list.grid(column=0, row=1, padx=10)

        self.resource_list.heading('0', text='Title', anchor='w')
        self.resource_list.heading('1', text='Author(s)', anchor='w')
        self.resource_list.heading('2', text='Year', anchor='w')
        self.resource_list.heading('3', text='Pages', anchor='w')
        self.resource_list.heading('4', text='Publisher', anchor='w')
        self.resource_list.heading('5', text='Language', anchor='w')
        self.resource_list.heading('6', text='Notes', anchor='w')

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



