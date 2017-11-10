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
                  AddInteractiveMedia, AddMedia, AddImages, SearchResource, EditResource):
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

        self.topframe = tk.LabelFrame(self, text='', borderwidth=0)
        self.topframe.pack(expand=tk.TRUE, fill=tk.BOTH)

        self.firstframe =tk.LabelFrame(self.topframe, text='', borderwidth=0)
        self.secondframe = tk.LabelFrame(self.topframe, text='', borderwidth=0)
        self.middleframe = tk.LabelFrame(self.topframe, borderwidth=0, text='')

        self.firstframe.pack(side=tk.LEFT, anchor=tk.CENTER,expand=tk.TRUE, ipadx=10, ipady=10, padx=10,pady=10)
        self.middleframe.pack(side=tk.LEFT, anchor=tk.CENTER, expand=tk.TRUE, ipadx=10, ipady=10, padx=10,pady=20)
        self.secondframe.pack(side=tk.LEFT, anchor=tk.CENTER, expand=tk.TRUE, ipadx=10, ipady=10, padx=10,pady=10)



        self.wordcloud = tk.PhotoImage(file="smallwhitewordcloud.png")

        self.new_projects = tk.Button(self.firstframe, text='Add Project',
                                      command=lambda: controller.show_frame(Projects))
        self.new_projects.config(height=5, width=13)
        self.new_projects.pack( pady=10)

        self.view_project = tk.Button(self.firstframe, text='Link Resources\n to Projects',
                                      command=lambda: controller.show_frame(LinkResources))
        self.view_project.config(height=5,width=13)
        self.view_project.pack( pady=10)

        self.edit_project = tk.Button(self.firstframe, text='Edit Project')
        self.edit_project.config(height=5, width=13)
        self.edit_project.pack( pady=10)

        self.new_resources = tk.Button(self.secondframe, text='Add Resource',
                                   command=lambda: controller.show_frame(AddResource))
        self.new_resources.config(height=5, width=13)
        self.new_resources.pack( pady=10)

        self.view_resources = tk.Button(self.secondframe, text='Search Resources',
                                        command=lambda: controller.show_frame(SearchResource))
        self.view_resources.config(height=5, width=13)
        self.view_resources.pack(pady=10)

        self.edit_resource = tk.Button(self.secondframe, text='Edit Resource')
        self.edit_resource.config(height=5, width=13)
        self.edit_resource.pack(pady=10)

        button1 = ttk.Button(self.middleframe, text = "", image=self.wordcloud, compound="center")
        button1.pack(anchor=tk.CENTER)

class AddResource(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.button_window = tk.LabelFrame(self, text='Resource Type')
        self.button_window.grid(column=0, row=0, columnspan=4, sticky=tk.N+tk.S+tk.E+tk.W) # padx=250, pady=100,

        self.AddAudioVideoButton = tk.Button(self.button_window, text='Audio\n and Video', width=20,height=5,
                                        command=lambda: controller.show_frame(AddAudioVideo))
        self.AddTextButton= tk.Button(self.button_window, text='Add Text', width=20,height=5,
                                        command=lambda: controller.show_frame(AddText))
        self.AddCourseButton= tk.Button(self.button_window, text='Courses', width=20,height=5,
                                        command=lambda: controller.show_frame(AddCourse))
        self.AddInteractiveMediaButton= tk.Button(self.button_window, text='Interactive\n Media',  width=20,height=5,
                                        command=lambda: controller.show_frame(AddInteractiveMedia))
        self.AddOnlineMediaButton= tk.Button(self.button_window, text='Websites', width=20,height=5,
                                        command=lambda: controller.show_frame(AddMedia))
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

        mainframe = tk.LabelFrame(self, text='', borderwidth=0)
        mainframe.grid(columnspan=20, column=0, row=0, sticky=tk.N+tk.S+tk.W+tk.E)

        header_frame = tk.LabelFrame(mainframe, text='', borderwidth=0)
        header_frame.grid(column=0, row=0, columnspan=20,padx=10)

        topleftframe = tk.LabelFrame(mainframe, text="", borderwidth=4)
        topleftframe.grid(columnspan=4, column=0, row=1)

        topcenterframe = tk.LabelFrame(mainframe, text="", borderwidth=4)
        topcenterframe.grid(columnspan=4,column=5, row=1)

        middleleftframe = tk.LabelFrame(mainframe, text="", borderwidth=4)
        middleleftframe.grid(columnspan=5, column=0, row=2, sticky=tk.W)  #

        middleframe = tk.LabelFrame(mainframe, text="", borderwidth=0)
        middleframe.grid(columnspan=5, column=4, row=2, sticky=tk.W)

        middlerightframe = tk.LabelFrame(mainframe, text='', borderwidth=0)
        middlerightframe.grid(columnspan=3, column=6, row=2,  sticky=tk.E)

        bottomframe = tk.LabelFrame(self, text="", borderwidth=4)
        bottomframe.grid(column=0, row=3, pady=5)

        buttonsframe = tk.LabelFrame(self, text="", borderwidth=0)
        buttonsframe.grid(column=0, row=4)#, sticky=tk.W+tk.E+tk.N)

        self.label = tk.Label(header_frame, text='New Text')
        self.label.grid(column=0, row=1, pady=5)

        self.title = tk.StringVar()
        self.author = tk.StringVar()
        self.year = tk.IntVar()
        self.pages = tk.IntVar()
        self.subject = tk.StringVar()
        self.notes = tk.StringVar()

        self.publisher = tk.StringVar()
        self.publisher_options = data.list_publishers()
        self.publisher.set('Select:')

        self.language = tk.StringVar()
        self.language_options = data.list_languages()
        self.language.set('Select:')

        self.new_lang = tk.StringVar()
        self.new_pub = tk.StringVar()

        self.new_lang_flag = tk.IntVar(self, value=0)
        self.new_pub_flag = tk.IntVar(self, value=0)

        self.text_type = tk.IntVar()
        self.text_type.set('?')

        self.level = tk.StringVar()
        self.level_options = data.list_levels()
        self.level.set('Select')

        # Top left frame

        self.title_label=tk.Label(topleftframe, text='Title')
        self.title_entry=ttk.Entry(topleftframe, width=61, textvariable =self.title)

        self.author_label=tk.Label(topleftframe, text ='Author(s)')
        self.author_entry = ttk.Entry(topleftframe,  width=61, textvariable=self.author)

        self.year_label=tk.Label(topleftframe, text ='Year')
        self.year_entry = ttk.Entry(topleftframe, width=25, textvariable=self.year)

        self.pages_label=tk.Label(topleftframe, width=5, text ='Pages')
        self.pages_entry = ttk.Entry(topleftframe, width=25, textvariable=self.pages)

        # Top center frame
        self.publisher_label = tk.Label(topcenterframe, text='Publisher')
        self.publisher_entry = tk.OptionMenu(topcenterframe, self.publisher,
                                                *self.publisher_options)
        self.publisher_entry.configure(width=15)

        self.add_publisher_entry = ttk.Entry(topcenterframe, width=25, textvariable =self.new_pub)

        self.language_label = tk.Label(topcenterframe, text='Language')
        self.language_entry= tk.OptionMenu(topcenterframe, self.language,
                                                *self.language_options)# if self.language_options else '0')

        self.language_entry.configure(width=15)

        self.add_language_entry=ttk.Entry(topcenterframe, width=25, textvariable =self.new_lang)

        self.notes_label = tk.Label(topcenterframe, text='Notes')
        self.notes_entry = ttk.Entry(topcenterframe, width=63, textvariable =self.notes)

        self.subject_label = tk.Label(topleftframe, text='Subject')
        self.subject_entry = ttk.Entry(topleftframe, width=61, textvariable=self.subject)


        # Place widgets
        self.title_label.grid(column=0, row=0, sticky=tk.W)
        self.title_entry.grid(columnspan=3, column=1, row=0, sticky=tk.E)

        self.author_label.grid(column=0, row=1, sticky=tk.W)
        self.author_entry.grid(columnspan=3, column=1, row=1)

        self.year_label.grid(columnspan=1, column=0, row=2, sticky=tk.W)
        self.year_entry.grid(columnspan=1, column=1, row=2, sticky=tk.W)
        self.pages_label.grid(columnspan=1, column=2, row=2)
        self.pages_entry.grid(columnspan=1,column=3, row=2, sticky=tk.E)

        #self.select_label.grid(column=0, row=3, sticky=tk.W)


        self.notes_label.grid(columnspan=1, column=0, row=1, sticky=tk.W)
        self.notes_entry.grid(columnspan=3, column=1, row=1, sticky=tk.W)

        self.subject_label.grid(column=0, row=3, sticky=tk.W)
        self.subject_entry.grid(columnspan=3, column=1, row=3, sticky=tk.W)


        # Top right frame

        self.add_pub_flag = tk.Checkbutton(topcenterframe,  text='Add new',
                                           variable=self.new_pub_flag)
        self.add_lang_flag = tk.Checkbutton(topcenterframe, text='Add new',
                                            variable=self.new_lang_flag)

        self.publisher_label.grid(column=0, row=3)
        self.publisher_entry.grid(columnspan=1, column=1, row=3, sticky=tk.W)
        self.add_pub_flag.grid(column=2, row=3,  sticky=tk.W)
        self.add_publisher_entry.grid(column=3, row=3,  sticky=tk.E)

        self.language_label.grid(column=0, row=4, sticky=tk.W)
        self.language_entry.grid(columnspan=1, column=1, row=4, sticky=tk.W)
        self.add_lang_flag.grid(column=2, row=4, sticky=tk.W)
        self.add_language_entry.grid(column=3, row=4, sticky=tk.N+tk.E)

        self.addtextresource = tk.Button(middlerightframe, text='Save', command=lambda: self.new_textresource())
        self.addtextresource.config(width=12, cursor='hand2')#
        self.addtextresource.grid(column=4, row=0, padx=2, sticky=tk.E)

        self.level_label = tk.Label(middleframe, text='Level:')
        self.level_entry = tk.OptionMenu(middleframe, self.level,
                                         *self.level_options)# if self.level_options else '0')
        self.level_entry.configure(width=15)

        self.level_label.grid(column=0, row=0, padx=10, sticky=tk.W)
        self.level_entry.grid(column=1, row=0, padx=5, sticky=tk.W)

        self.text_type_label = tk.Label(middleleftframe, text='Text type:')
        self.text_type1 = tk.Radiobutton(middleleftframe, text='Book', variable=self.text_type, value=1)
        self.text_type2= tk.Radiobutton(middleleftframe, text='Short story', variable=self.text_type,
                                        value=2)
        self.text_type3= tk.Radiobutton(middleleftframe, text='Other', variable=self.text_type, value=3)
        self.text_type_label.grid(column=0, row=0, sticky=tk.W)
        self.text_type1.grid(column=1, row = 0, sticky= tk.W)
        self.text_type2.grid(column=2, row=0, sticky=tk.W)
        self.text_type3.grid(column=3, row=0, sticky=tk.W)


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
        self.resource_list.column('0', width=180, anchor='w')
        self.resource_list.column('1', width=150, anchor='w')
        self.resource_list.column('2', width=75, anchor='w')
        self.resource_list.column('3', width=60, anchor='w')
        self.resource_list.column('4', width=100, anchor='w')
        self.resource_list.column('5', width=90, anchor='w')
        self.resource_list.column('6', width=200, anchor='w')
        self.resource_list.grid(column=0, row=1, sticky=tk.E)

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

        self.home=tk.Button(buttonsframe, text='Home', command=lambda: controller.show_frame(HomePage))
        self.home.config(width=15, cursor='hand2')
        self.home.grid(column=1, row=0, padx=10, sticky=tk.W+tk.E)

        self.back_button = tk.Button(buttonsframe, text='Back', command=lambda: controller.show_frame(AddResource))
        self.back_button.config(width=15, cursor='hand2')
        self.back_button.grid(column=0, row=0, padx=10, sticky=tk.W)

        self.searchresource = tk.Button(buttonsframe, text='Search Resources',
                                     command=lambda: controller.show_frame(SearchResource))
        self.searchresource.config(width=15, cursor='hand2')
        self.searchresource.grid(column=2, row=0, padx=10, sticky=tk.E)

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
        self.publisher.set('Select:')
        self.language.set('Select:')
        self.level.set('Select: ')
        self.text_type.set('?')


    def get_media_name(self):
        if self.text_type.get() == 1:
            media_name = 'Book'
        elif self.text_type.get() == 2:
            media_name = 'Short story'
        else:
            media_name = 'Other'
        return media_name


    def new_textresource(self):
        media_name = self.get_media_name()

        if self.new_pub_flag.get() == 1:
            self.thepublisher = self.new_pub.get()
        else:
            self.thepublisher = self.publisher.get()

        if self.new_lang_flag.get() == 1:
            self.thelanguage = self.new_lang.get()
        else:
            self.thelanguage = self.language.get()


        data.add_text(self.title.get(), self.author.get(), self.year.get(),
                          self.pages.get(), self.level.get(), self.thepublisher,
                          self.thelanguage, self.subject.get(), media_name, self.notes.get())

        self.list_resources()
        self.update_entry_widgets()


class LinkResources(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.project_id = None
        self.resources = set()

        self.project_title = tk.StringVar()
        self.project_type = tk.StringVar()
        self.resource_subject = tk.StringVar()

        self.media_type = tk.IntVar()
        self.media_type.set("?")

        self.columns = ()

        self.searchheader = ttk.Label(self, text='Find Projects')
        self.searchheader.grid(column=0, row=0)

        self.mainframe = tk.LabelFrame(self, text='', borderwidth=4)
        self.mainframe.grid(column=0, row=1, sticky=tk.W + tk.E + tk.N)

        self.home = ttk.Button(self.mainframe, text='Home', command=lambda: controller.show_frame(HomePage))
        self.home.config(width=10, cursor='hand2')
        self.home.grid(column=0, row=10, padx=20, sticky=tk.E)

        # TOP LEFT FRAME
        self.projectframe = tk.LabelFrame(self.mainframe, text='', borderwidth=4)
        self.projectframe.grid(column=0, row=0, columnspan=3, sticky=tk.N+tk.W+tk.E)

        self.titlebox_label = tk.Label(self.projectframe, text='Enter search keyword')
        self.titlebox_label.grid(column=0, row=0, sticky=tk.W)
        self.titlebox = tk.Entry(self.projectframe, width=32, textvariable=self.project_title)
        self.titlebox.grid(column=1, row=0, sticky=tk.W)

        self.searchbutton = ttk.Button(self.projectframe, text='Search', command=lambda: self.search_projects())
        self.searchbutton.config(width=10, cursor='hand2')
        self.searchbutton.grid(column=2, row=0, padx=5, pady=5, sticky=tk.E)

        # TOP RIGHT FRAME PROJECT SEARCH RESULTS:

        self.resultsframe = tk.LabelFrame(self.mainframe, text='', borderwidth=4)
        self.resultsframe.grid(column=0, row=2, sticky=tk.E)

        self.clearbutton = ttk.Button(self.resultsframe, text='Clear project')
        self.clearbutton.config( cursor='hand2')
        self.clearbutton.grid(column=0, row=10, pady=5, sticky=tk.E)

        # Project results
        self.scrollresults = tk.Scrollbar(self.resultsframe)
        self.scrollresults.grid(column=1, row=4, sticky=tk.N +tk.S + tk.W)

        self.project_list = ttk.Treeview(self.resultsframe, height=2, selectmode='browse',
                                         columns=('Name', 'Type', 'Description', 'Start date', 'End date'))

        self.scrollresults.configure(orient="vertical", command=self.project_list.yview)
        self.project_list.configure(yscrollcommand=self.scrollresults.set)

        self.project_list['columns'] = ('Name', 'Type', 'Description', 'Start date', 'End date')
        self.project_list.column('#0', width=5)
        self.project_list.grid(column=0, row=4, sticky=tk.W+tk.E)

        self.project_list.heading('0', text='Name', anchor='w')
        self.project_list.heading('1', text='Type', anchor='w')
        self.project_list.heading('2', text='Description', anchor='w')
        self.project_list.heading('3', text='Start date', anchor='w')
        self.project_list.heading('4', text='End date', anchor='w')

        self.project_list.column('0', width=250, anchor='w')
        self.project_list.column('1',  width=110, anchor='w')
        self.project_list.column('2', width=280, anchor='w')
        self.project_list.column('3', width=100, anchor='w')
        self.project_list.column('4', width=100, anchor='w')
        self.treeview_projects = self.project_list
        self.treeview_projects.bind('<ButtonRelease-1>', self.select_project)

        # MIDDLE FRAME
        self.middleframe = tk.LabelFrame(self.mainframe, text='', borderwidth=0)
        self.middleframe.grid(columnspan=40, pady=5, column=0, row=3)

        self.resourceresults_label = ttk.Label(self.middleframe, text='Available Resources')
        self.resourceresults_label.grid(columnspan=4, column=2, row=0, pady=5)

        # BOTTOM FRAME SORT FRAME

        self.searchresourceframe = tk.LabelFrame(self.mainframe, text='', borderwidth=4)
        self.searchresourceframe.grid( column=0, row=4, columnspan=3, sticky=tk.N+tk.W+tk.E)

        self.media_type_frame = tk.LabelFrame(self.searchresourceframe, text='', borderwidth=3)
        self.media_type_frame.grid(rowspan=2, column=4, row=0, padx=10, sticky=tk.E)

        self.media_button_frame = tk.LabelFrame(self.searchresourceframe, text='', borderwidth=0)
        self.media_button_frame.grid(rowspan=2, column=6, row=0, sticky=tk.E)

        self.subjectbox_label = tk.Label(self.searchresourceframe, text='Enter search keyword')
        self.subjectbox_label.grid(column=0, row=0, sticky=tk.W)
        self.subjectbox = tk.Entry(self.searchresourceframe, width=32, textvariable=self.resource_subject)
        self.subjectbox.grid(column=1, row=0, sticky=tk.W)

        self.searchbutton = ttk.Button(self.media_button_frame, text='Search',
                                       command=lambda:self.show_results())
        self.searchbutton.config(width=10, cursor='hand2')
        self.searchbutton.grid(column=0, row=2, padx=5, pady=5, sticky=tk.E)

        self.sort_label = tk.Label(self.searchresourceframe, text='Resource type:')
        self.sort_label.grid(column=3, row=0, padx=5, sticky=tk.W)

        self.audiovideo_rb = tk.Radiobutton(self.media_type_frame, text='Audio and Video', variable=self.media_type,
                                       value=1)
        self.courses_rb = tk.Radiobutton(self.media_type_frame, text='Courses', variable=self.media_type, value=2)

        self.websites_rb = tk.Radiobutton(self.media_type_frame, text='Websites', variable=self.media_type,
                                             value=3)
        self.images_rb = tk.Radiobutton(self.media_type_frame, text='Images', variable=self.media_type,
                                             value=4)
        self.interactive_rb = tk.Radiobutton(self.media_type_frame, text='Interactive Media',
                                             variable=self.media_type, value=5)
        self.texts_rb = tk.Radiobutton(self.media_type_frame, text='Books and Texts', variable=self.media_type,
                                         value=6)

        self.audiovideo_rb.grid(column=0, row=0, sticky=tk.W)
        self.texts_rb.grid(column=1, row=0, sticky=tk.W)
        self.courses_rb.grid(column=2, row=0, sticky=tk.W)
        self.websites_rb.grid(column=2, row=1, sticky=tk.W)
        self.images_rb.grid(column=0, row=1, sticky=tk.W)
        self.interactive_rb.grid(column=1, row=1, sticky=tk.W)

        # BOTTOM RIGHT FRAME
        self.resourceresults = tk.LabelFrame(self.mainframe, text='', borderwidth=4)
        self.resourceresults.grid(column=0, row=5, columnspan=40, sticky=tk.W)


    def show_results(self):
        column_names = self.create_table_values()

        self.scollresources = tk.Scrollbar(self.resourceresults)
        self.scollresources.grid(column=2, row=2, sticky=tk.N + tk.S + tk.W)

        self.resource_list = ttk.Treeview(self.resourceresults, height=4, selectmode='extended',
                                          columns=column_names )

        self.scollresources.configure(orient="vertical", command=self.resource_list.yview)
        self.resource_list.configure(yscrollcommand=self.scollresources.set)

        self.resource_list['columns'] = column_names
        self.resource_list.column('#0', width=5)
        self.resource_list.column('0', width=240, anchor='w')
        self.resource_list.column('1', width=150, anchor='w')
        self.resource_list.column('2', width=75, anchor='w')
        self.resource_list.column('3', width=75, anchor='w')
        self.resource_list.column('4', width=100, anchor='w')
        self.resource_list.column('5', width=200, anchor='w')
        self.resource_list.grid(column=0, row=2, sticky=tk.W + tk.N + tk.E)

        self.resource_list.heading('0', anchor='w', text=column_names[0])
        self.resource_list.heading('1', anchor='w', text=column_names[1])
        self.resource_list.heading('2', anchor='w', text=column_names[2])
        self.resource_list.heading('3', anchor='w', text=column_names[3])
        self.resource_list.heading('4', anchor='w', text=column_names[4])
        self.resource_list.heading('5', anchor='w', text=column_names[5])
        self.treeview_resources = self.resource_list
        self.treeview_resources.bind('<ButtonRelease-1>', self.select_resources)

        self.go_to_resources = ttk.Button(self.resourceresults, text='Link resource(s)',
                                          command=lambda: self.link_project_resources())
        self.go_to_resources.config(cursor='hand2')
        self.go_to_resources.grid(column=0, row=4, sticky=tk.E)

        self.search_resources()


    def create_table_values(self):
        if self.media_type.get() == 1:
            column_names = ('Title', 'Creator', 'Duration', 'Format', 'Type', 'URL')
            print('Audio/Video')
        elif self.media_type.get() ==2:
            column_names = ('Title', 'Instructor', 'Start date', 'Duration', 'Platform', 'URL')
            print('Courses')
        elif self.media_type.get() ==3:
            column_names = ('Title', 'Author', 'Date', 'Website', 'Access date', 'URL')
            print('Websites')
        elif self.media_type.get() ==4:
            column_names = ('Title', 'Creator', 'Format', 'Dimensions', 'Date', 'Location')
            print('Images')
        elif self.media_type.get() == 5:
            column_names = ('Title', 'Creator', 'Genre', 'Engine', 'Type', 'Comments')
            print('Interactive Media')
        elif self.media_type.get() ==6:
            column_names = ('Title', 'Author', 'Year', 'Pages', 'Language', 'Format')
            print('Books/texts')
        else:
            print('Not working')

        return column_names


    def select_resources(self, event):
        self.resources.clear()

        for item in self.treeview_resources.selection():
            item_text = self.treeview_resources.item(item)

            resource_name = item_text['values'][0]

            resource_ids = data.get_text_id(resource_name)
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

        self.label = tk.Label(main_frame, text='New Project')
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
        self.project_name_entry = ttk.Entry(self.topleftframe, width=61, textvariable=self.project_name)

        self.description_label = tk.Label(self.topleftframe, text='Description')
        self.description_entry = ttk.Entry(self.topleftframe, width=61, textvariable=self.description)

        self.project_type_label = tk.Label(self.topleftframe, text='Project Type')
        self.project_type_entry = tk.OptionMenu(self.topleftframe, self.choices,
                                                *self.project_category_options)# if self.project_category_options else '0')
        self.project_type_entry.configure(width=20)

        self.new_projecttype_label = tk.Label(self.topleftframe, text='New Project Type')
        self.new_projecttype = ttk.Entry(self.topleftframe, width=61, textvariable=self.add_projecttype)

        self.project_name_label.grid(column=0, row=1, sticky=tk.W)
        self.project_name_entry.grid(column=1, row=1, columnspan=3, sticky=tk.W)

        self.description_label.grid(column=0, row=2, sticky=tk.W)
        self.description_entry.grid(column=1, row=2,  columnspan=3, sticky=tk.W)

        self.project_type_label.grid(column=0, row=4, sticky=tk.W)
        self.project_type_entry.grid(column=1, row=4, sticky=tk.W)
        self.new_projecttype_label.grid(column=0, row=5)
        self.new_projecttype.grid(column=1, row=5, columnspan=3, sticky=tk.W)

        self.new_type_flag = tk.Checkbutton(self.topleftframe, text="Add type", variable=self.new_type)
        self.new_type_flag.grid(column=2, row=4, padx=6, sticky=tk.W)


        # Top right frame
        self.start_label = tk.Label(self.toprightframe, text='Start Date')
        self.start_entry = ttk.Entry(self.toprightframe, width=55, textvariable=self.start_date)

        self.finish_label = tk.Label(self.toprightframe, text='End Date')
        self.finish_entry = ttk.Entry(self.toprightframe, width=55, textvariable=self.end_date)

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


class AddMedia(tk.Frame):
    def __init__(self, parent, controller, *args):
        tk.Frame.__init__(self, parent)

        self.box1L = tk.StringVar()
        self.box2L = tk.StringVar()
        self.box3L = tk.StringVar()
        self.box4L = tk.StringVar()

        self.box1R = tk.StringVar()
        self.box2R = tk.StringVar()
        self.box3R = tk.StringVar()
        self.box4R = tk.StringVar()

        self.media_buttons = tk.IntVar()
        self.media_buttons.set('?')

        self.treeview = None
        self.webdocs_list = None

        # Frames

        self.mainframe = tk.LabelFrame(self, text='', borderwidth=4)
        self.mainframe.grid(column=0, row=1, columnspan=40, sticky=tk.N + tk.S + tk.W + tk.E)

        self.topleft = tk.LabelFrame(self.mainframe, text="", borderwidth=3)
        self.topleft.grid(column=0, row=1, sticky=tk.W + tk.E)

        self.topright = tk.LabelFrame(self.mainframe, text="", borderwidth=3)
        self.topright.grid(column=1, row=1, sticky=tk.W + tk.E)

        self.center_leftframe = tk.LabelFrame(self.mainframe, text='', borderwidth=0)
        self.center_leftframe.grid(column=0, row=2, columnspan=2,sticky=tk.W)

        self.center_frame = tk.LabelFrame(self.mainframe, text='', borderwidth=0)
        self.center_frame.grid(column=1, row=2,columnspan=3, sticky=tk.W)

        self.bottomleft = tk.LabelFrame(self.mainframe, text="", borderwidth=3)
        self.bottomleft.grid(column=0, row=4, sticky=tk.W + tk.E)

        self.bottomright = tk.LabelFrame(self.mainframe, text="", borderwidth=3)
        self.bottomright.grid(column=1, row=5, sticky=tk.W + tk.E)

        self.bottom_middleframe = tk.LabelFrame(self.mainframe, text='', borderwidth=3)
        self.bottom_middleframe.grid(column=0, row=3, columnspan=2, sticky=tk.W + tk.E)

        # Home button
        self.home = tk.Button(self.bottomleft, text='Home', command=lambda: controller.show_frame(HomePage))
        self.home.config(width=15, cursor='hand2')
        self.home.grid(column=0, row=2, padx=10, sticky=tk.W)

        self.back_button = tk.Button(self.bottomleft, text='Back', command=lambda:controller.show_frame(AddResource))
        self.back_button.config(width=15, cursor='hand2')
        self.back_button.grid(column=1, row=2, padx=10, sticky=tk.W)

        # Save resource button
        self.save_resource = ttk.Button(self.center_frame, text='Save', command=lambda: self.save_data())
        self.save_resource.config(cursor='hand2')
        self.save_resource.grid(column=4, row=0, sticky=tk.E)

        self.create_values()

        self.create_top_frame_widgets(self.window_header, self.b2L, self.b3L, self.b4L, self.b1R, self.b2R,
                                      self.b3R, self.b4R)

        self.place_widgets()

        self.add_radio_buttons(self.media_choice1, self.media_choice2, self.media_choice3)

        self.display_resources(self.c1, self.c2, self.c3, self.c4, self.c5, self.c6)

        self.list_resources()
        self.update_entry_widgets()


    def create_values(self):
        self.window_header = 'Websites'
        self.b2L = 'Author'
        self.b3L = 'Date'
        self.b4L = 'Subject'
        self.b1R = 'Website'
        self.b2R = 'URL'
        self.b3R = 'Access date'
        self.b4R = 'Notes'

        self.c1 = 'Title'
        self.c2 = 'Author'
        self.c3 = 'Date'
        self.c4 = 'Website'
        self.c5 = 'Access date'
        self.c6 = 'URL'

        self.media_choice1 = 'Documention'
        self.media_choice2 = 'Q&A site'
        self.media_choice3 = 'Other'

        return self.window_header, self.b2L, self.b3L, self.b4L, self.b1R, self.b2R, self.b3R, \
               self.b4R, self.c1, self.c2, self.c3, self.c4, self.c5, self.c6, self.media_choice1, \
               self.media_choice2

    def create_top_frame_widgets(self, window_header, box2L, box3L, box4L, box1R, box2R, box3R, box4R):

        # Title Frame
        self.window_title = tk.Label(self.mainframe, text=window_header)

        # Top left frame

        self.title_label = tk.Label(self.topleft, text='Title')
        self.title_entry = tk.Entry(self.topleft, width=60, textvariable=self.box1L)

        self.box_2_L = tk.Label(self.topleft, text=box2L)
        self.box_2_L_entry = tk.Entry(self.topleft, width=60, textvariable=self.box2L)

        self.box_3_L = tk.Label(self.topleft, text=box3L)
        self.box_3_L_entry = tk.Entry(self.topleft, width=60, textvariable=self.box3L)

        self.box_4_L = tk.Label(self.topleft, text=box4L)
        self.box_4_L_entry = tk.Entry(self.topleft, width=60, textvariable=self.box4L)

        self.box_1_R = tk.Label(self.topright, text=box1R)
        self.box_1_R_entry = tk.Entry(self.topright, width=60, textvariable=self.box1R)

        self.box_2_R = tk.Label(self.topright, text=box2R)
        self.box_2_R_entry = tk.Entry(self.topright, width=60, textvariable=self.box2R)

        self.box_3_R = tk.Label(self.topright, text=box3R)
        self.box_3_R_entry = tk.Entry(self.topright, width=60, textvariable=self.box3R)

        self.box_4_R = tk.Label(self.topright, text=box4R)
        self.box_4_R_entry = tk.Entry(self.topright, width=60, textvariable=self.box4R)

        return self.title_entry, self.box_2_L_entry, self.box_3_L_entry, self.box_4_L_entry, self.box_1_R_entry,\
                self.box_2_R_entry, self.box_3_R_entry, self.box_4_R_entry

    def place_widgets(self):
        self.window_title.grid(column=0, row=0, columnspan=2)

        self.title_label.grid(column=0, row=0, sticky=tk.W)
        self.title_entry.grid(column=1, row=0, sticky=tk.W)

        self.box_2_L.grid(column=0, row=1, sticky=tk.W)
        self.box_2_L_entry.grid(column=1, row=1, sticky=tk.W)

        self.box_3_L.grid(column=0, row=2, sticky=tk.W)
        self.box_3_L_entry.grid(column=1, row=2, sticky=tk.W)

        self.box_4_L.grid(column=0, row=3, sticky=tk.W)
        self.box_4_L_entry.grid(column=1, row=3, sticky=tk.W)

        self.box_1_R.grid(column=0, row=0, sticky=tk.W)
        self.box_1_R_entry.grid(column=1, row=0, sticky=tk.W)

        self.box_2_R.grid(column=0, row=1, sticky=tk.W)
        self.box_2_R_entry.grid(column=1, row=1, sticky=tk.W)

        self.box_3_R.grid(column=0, row=2, sticky=tk.W)
        self.box_3_R_entry.grid(column=1, row=2, sticky=tk.W)

        self.box_4_R.grid(column=0, row=3, sticky=tk.W)
        self.box_4_R_entry.grid(column=1, row=3, sticky=tk.W)


    def add_radio_buttons(self, media_type1, media_type2, media_type3 ):

        self.media_label = tk.Label(self.center_leftframe, text='Select type: ')
        self.media_label.grid(column=0, row=0, sticky=tk.W)

        self.media_1 = tk.Radiobutton(self.center_leftframe, text=media_type1, variable=self.media_buttons,
                                      value=1)
        self.media_1.grid(column=1, row=0)

        self.media_2 = tk.Radiobutton(self.center_leftframe, text=media_type2, variable=self.media_buttons,
                                      value=2)
        self.media_2.grid(column=2, row=0)

        self.media_other = tk.Radiobutton(self.center_leftframe, text=media_type3, variable=self.media_buttons,
                                          value=3)
        self.media_other.grid(column=3, row=0)


    def display_resources(self, col1, col2, col3, col4, col5, col6):
        scrollwebdocs = tk.Scrollbar(self.bottom_middleframe)
        scrollwebdocs.grid(column=1, row=1, sticky=tk.N + tk.S + tk.W)

        self.webdocs_list = ttk.Treeview(self.bottom_middleframe,
                                         columns= (col1, col2, col3, col4, col5, col6))

        scrollwebdocs.configure(orient="vertical", command=self.webdocs_list.yview)
        self.webdocs_list.configure(yscrollcommand=scrollwebdocs.set)

        self.webdocs_list['columns'] = (col1, col2, col3, col4, col5, col6)
        self.webdocs_list.column('#0', width=1)
        self.webdocs_list.column('0', width=200, anchor='w')
        self.webdocs_list.column('1', width=180, anchor='w')
        self.webdocs_list.column('2', width=75, anchor='w')
        self.webdocs_list.column('3', width=75, anchor='w')
        self.webdocs_list.column('4', width=75, anchor='w')
        self.webdocs_list.column('5', width=250, anchor='w')
        self.webdocs_list.grid(column=0, row=1)

        self.webdocs_list.heading('0', text=col1, anchor='w')
        self.webdocs_list.heading('1', text=col2, anchor='w')
        self.webdocs_list.heading('2', text=col3, anchor='w')
        self.webdocs_list.heading('3', text=col4, anchor='w')
        self.webdocs_list.heading('4', text=col5, anchor='w')
        self.webdocs_list.heading('5', text=col6, anchor='w')

        self.treeview = self.webdocs_list
        return self.treeview, self.webdocs_list


    def list_resources(self):
        for i in self.webdocs_list.get_children():
            self.webdocs_list.delete(i)
        resources = data.list_websites()
        for item in resources:
            self.treeview.insert('', 'end', values=item)


    def get_media_name(self):
        if self.media_buttons.get() == 1:
            media_name = self.media_choice1
        elif self.media_buttons.get() == 2:
            media_name = self.media_choice2
        else:
            media_name = self.media_choice3
        return media_name

    def save_data(self):
        media_name = self.get_media_name()


        data.add_website(self.box1L.get(), self.box2L.get(), self.box3L.get(), self.box4L.get(), self.box1R.get(),
                              self.box2R.get(), self.box3R.get(), self.box4R.get(), media_name)
        self.update_entry_widgets()

    def update_entry_widgets(self):

        self.title_entry.delete(0, 'end')
        self.box_2_L_entry.delete(0, 'end')
        self.box_3_L_entry.delete(0, 'end')
        self.box_4_L_entry.delete(0, 'end')

        self.box_1_R_entry.delete(0, 'end')
        self.box_2_R_entry.delete(0, 'end')
        self.box_3_R_entry.delete(0, 'end')
        self.box_4_R_entry.delete(0, 'end')

        self.media_buttons.set('?')
        self.list_resources()


class AddCourse(AddMedia):
    def __init__(self, parent, controller):
        AddMedia.__init__(self, parent, controller)

        self.level = tk.StringVar()
        self.level_options = data.list_levels()
        self.level.set('Select one')

        self.level_label = tk.Label(self.center_frame, text='Level:')
        self.level_entry = tk.OptionMenu(self.center_frame, self.level,
                                            *self.level_options)
        self.level_entry.configure(width=15)
        self.level_label.grid(column=0, row=0, sticky=tk.W)
        self.level_entry.grid(column=1, row=0, padx=10, sticky=tk.W)

        self.create_values()

        self.display_resources(AddMedia.c1, AddMedia.c2, AddMedia.c3, AddMedia.c4,
                               AddMedia.c5, AddMedia.c6)

        self.update_entry_widgets()

        self.create_top_frame_widgets(AddMedia.window_header, AddMedia.b2L, AddMedia.b3L, AddMedia.b4L, \
                                      AddMedia.b1R, AddMedia.b2R, AddMedia.b3R, AddMedia.b4R)

    def create_values(self):
        AddMedia.window_header = 'Online Courses'
        AddMedia.b2L = 'Instructor'
        AddMedia.b3L = 'Start date'
        AddMedia.b4L = 'Subject'

        AddMedia.b1R = 'Platform'
        AddMedia.b2R = 'URL'
        AddMedia.b3R = 'Length (hrs)'
        AddMedia.b4R = 'Comments'

        AddMedia.c1 = 'Title'
        AddMedia.c2 = 'Teacher'
        AddMedia.c3 = 'Start date'
        AddMedia.c4 = 'Duration'
        AddMedia.c5 = 'Platform'
        AddMedia.c6 = 'URL'

        AddMedia.media_choice1 = 'Audio'
        AddMedia.media_choice2 = 'Video'
        AddMedia.media_choice3 = 'Blended Classroom'

        return AddMedia.c1, AddMedia.c2, AddMedia.c3, AddMedia.c4, AddMedia.c5, AddMedia.c6, AddMedia.window_header, \
               AddMedia.b2L, AddMedia.b3L, AddMedia.b4L, AddMedia.b1R, AddMedia.b2R, AddMedia.b3R, AddMedia.b4R, \
               AddMedia.media_choice1, AddMedia.media_choice2, AddMedia.media_choice3

    def list_resources(self):
        for i in self.webdocs_list.get_children():
            self.webdocs_list.delete(i)
        resources = data.list_courses()
        for item in resources:
            self.treeview.insert('', 'end', values=item)
        pass

    def get_media_name(self):
        if self.media_buttons.get() == 1:
            media_name = 'Audio'
        elif self.media_buttons.get() == 2:
            media_name = 'Video'
        else:
            media_name = 'Blended'
        return media_name

    def save_data(self):
        media_name = self.get_media_name()

        data.add_course(self.box1L.get(), self.box2L.get(), self.box3L.get(),
                        self.box3R.get(), self.box2R.get(), self.box4R.get(),
                        self.level.get(), self.box1R.get(), self.box4L.get(),
                        media_name)
        self.update_entry_widgets()

class AddAudioVideo(AddMedia):
    def __init__(self, parent, controller):
        AddMedia.__init__(self, parent, controller)

        self.language = tk.StringVar()
        self.language_options = data.list_languages()
        self.language.set('Select one')

        self.language_label = tk.Label(self.center_frame, text='Language:')
        self.language_entry = tk.OptionMenu(self.center_frame, self.language,
                                            *self.language_options  if self.language_options else '0')
        self.language_entry.configure(width=15)
        self.language_label.grid(column=0, row=0, sticky=tk.W)
        self.language_entry.grid(column=1, row=0,padx=10, sticky=tk.W)


        self.create_values()

        self.display_resources(AddMedia.c1, AddMedia.c2, AddMedia.c3, AddMedia.c4,
                               AddMedia.c5, AddMedia.c6)

        self.create_top_frame_widgets(AddMedia.window_header, AddMedia.b2L, AddMedia.b3L, AddMedia.b4L, \
                                      AddMedia.b1R, AddMedia.b2R, AddMedia.b3R, AddMedia.b4R)


    def create_values(self):
        AddMedia.window_header = 'Audio and Video'
        AddMedia.b2L = 'Creator'
        AddMedia.b3L = 'Duration'
        AddMedia.b4L = 'Subject'
        AddMedia.b1R = 'Format'
        AddMedia.b2R = 'Date'
        AddMedia.b3R = 'Location'
        AddMedia.b4R = 'Comments'

        AddMedia.c1 = 'Title'
        AddMedia.c2 = 'Creator'
        AddMedia.c3 = 'Duration'
        AddMedia.c4 = 'Format'
        AddMedia.c5 = 'Type'
        AddMedia.c6 = 'URL'
        AddMedia.media_choice1 = 'Music or Sound'
        AddMedia.media_choice2 = 'Podcast'
        AddMedia.media_choice3 = 'Video'

        return AddMedia.c1, AddMedia.c2, AddMedia.c3, AddMedia.c4, AddMedia.c5, AddMedia.c6, AddMedia.window_header, \
               AddMedia.b2L, AddMedia.b3L, AddMedia.b4L, AddMedia.b1R, AddMedia.b2R, AddMedia.b3R, AddMedia.b4R, \
               AddMedia.media_choice1, AddMedia.media_choice2, AddMedia.media_choice3

    def save_data(self):
        data.add_audio_video(self.box1L.get(), self.box2L.get(), self.box3L.get(), self.box4L.get(), self.box1R.get(),
                              self.box2R.get(), self.box3R.get(), self.box4R.get(), self.media_buttons.get())
        pass


class AddInteractiveMedia(AddMedia):
    def __init__(self, parent, controller):
        AddMedia.__init__(self, parent, controller)

        self.create_values()

        self.display_resources(AddMedia.c1, AddMedia.c2, AddMedia.c3, AddMedia.c4,
                               AddMedia.c5, AddMedia.c6)

        self.create_top_frame_widgets(AddMedia.window_header, AddMedia.b2L, AddMedia.b3L, AddMedia.b4L, \
                                      AddMedia.b1R, AddMedia.b2R, AddMedia.b3R, AddMedia.b4R)

    def create_values(self):
        AddMedia.window_header = 'Interactive Media'
        AddMedia.b2L = 'Creator'
        AddMedia.b3L = 'Year'
        AddMedia.b4L = 'Genre'
        AddMedia.b1R = 'Platform'
        AddMedia.b2R = 'Engine'
        AddMedia.b3R = 'Version'
        AddMedia.b4R = 'Comments'

        AddMedia.c1 = 'Title'
        AddMedia.c2 = 'Creator'
        AddMedia.c3 = 'Genre'
        AddMedia.c4 = 'Engine'
        AddMedia.c5 = 'Type'
        AddMedia.c6 = 'Comments'
        AddMedia.media_choice1 = 'Interactive Fiction'
        AddMedia.media_choice2 = 'Video game'
        AddMedia.media_choice3 = 'Other'

        return AddMedia.c1, AddMedia.c2, AddMedia.c3, AddMedia.c4, AddMedia.c5, AddMedia.c6, AddMedia.window_header, \
               AddMedia.b2L, AddMedia.b3L, AddMedia.b4L, AddMedia.b1R, AddMedia.b2R, AddMedia.b3R, AddMedia.b4R, \
               AddMedia.media_choice1, AddMedia.media_choice2, AddMedia.media_choice3
    def save_data(self):
        data.add_interactive_media(self.box1L.get(), self.box2L.get(), self.box3L.get(), self.box4L.get(), self.box1R.get(),
                              self.box2R.get(), self.box3R.get(), self.box4R.get(), self.media_buttons.get())
        pass


class AddImages(AddMedia):
    def __init__(self, parent, controller):
        AddMedia.__init__(self, parent, controller)

        self.create_values()

        self.display_resources(AddMedia.c1, AddMedia.c2, AddMedia.c3, AddMedia.c4,
                               AddMedia.c5, AddMedia.c6)

        self.create_top_frame_widgets(AddMedia.window_header, AddMedia.b2L, AddMedia.b3L, AddMedia.b4L, \
                                      AddMedia.b1R, AddMedia.b2R, AddMedia.b3R, AddMedia.b4R)

    def create_values(self):
        AddMedia.window_header = 'Images'
        AddMedia.b2L = 'Creator'
        AddMedia.b3L = 'Format'
        AddMedia.b4L = 'Date Created'
        AddMedia.b1R = 'Material'
        AddMedia.b2R = 'Dimensions'
        AddMedia.b3R = 'Location'
        AddMedia.b4R = 'Comments'


        AddMedia.c1 = 'Title'
        AddMedia.c2 = 'Creator'
        AddMedia.c3 = 'Format'
        AddMedia.c4 = 'Dimensions'
        AddMedia.c5 = 'Date'
        AddMedia.c6 = 'Location'
        AddMedia.media_choice1 = 'Photo'
        AddMedia.media_choice2 = 'Clip art'
        AddMedia.media_choice3 = 'Sprite'

        return AddMedia.c1, AddMedia.c2, AddMedia.c3, AddMedia.c4, AddMedia.c5, AddMedia.c6, AddMedia.window_header, \
               AddMedia.b2L, AddMedia.b3L, AddMedia.b4L, AddMedia.b1R, AddMedia.b2R, AddMedia.b3R, AddMedia.b4R, \
               AddMedia.media_choice1, AddMedia.media_choice2, AddMedia.media_choice3

    def save_data(self):
        data.add_images(self.box1L.get(), self.box2L.get(), self.box3L.get(), self.box4L.get(), self.box1R.get(),
                              self.box2R.get(), self.box3R.get(), self.box4R.get(), self.media_buttons.get())
        pass

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
                                         'Publisher', 'Language')#, 'Notes')
        self.resource_list.column('#0', width=1)
        self.resource_list.column('0', width=250, anchor='w')
        self.resource_list.column('1', width=150, anchor='w')
        self.resource_list.column('2', width=75, anchor='w')
        self.resource_list.column('3', width=60, anchor='w')
        self.resource_list.column('4', width=100, anchor='w')
        self.resource_list.column('5', width=90, anchor='w')
        #self.resource_list.column('6', width=200, anchor='w')
        self.resource_list.grid(column=0, row=1, padx=10)

        self.resource_list.heading('0', text='Title', anchor='w')
        self.resource_list.heading('1', text='Author(s)', anchor='w')
        self.resource_list.heading('2', text='Year', anchor='w')
        self.resource_list.heading('3', text='Pages', anchor='w')
        self.resource_list.heading('4', text='Publisher', anchor='w')
        self.resource_list.heading('5', text='Language', anchor='w')
        #self.resource_list.heading('6', text='Notes', anchor='w')

        self.treeview = self.resource_list



class EditResource(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        pass

if __name__ == "__main__":
    app = ProjectLibrary()
    app.title('Project Library')
    app.iconbitmap('project.ico')
    app.maxsize(890,750)
    app.mainloop()



