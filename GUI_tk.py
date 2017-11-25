import tkinter as tk
import tkinter.messagebox as tkMessageBox
from tkinter import ttk
import dataCRUD as data
from blank_window import show_window


class ProjectLibrary(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        main=tk.Frame(self)
        main.pack(side='top', fill='both', expand=True)
        main.grid_rowconfigure(0, weight=1)
        main.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (HomePage, Projects, LinkResources, AddResource, AddText, AddAudioVideo, AddCourse,
                  AddInteractiveMedia, AddMedia, AddImages, SearchResource, EditProject):
            frame = F(main, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky ='nsew')

        self.show_frame(AddText)
        
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

        self.edit_project = tk.Button(self.firstframe, text='Edit Project',
                                      command=lambda: controller.show_frame(EditProject))
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

        self.edit_resource = tk.Button(self.secondframe, text='About')
        self.edit_resource.config(height=5, width=13)
        self.edit_resource.pack(pady=10)

        button1 = ttk.Button(self.middleframe, text = "", image=self.wordcloud, compound="center")
        button1.pack(anchor=tk.CENTER)

class AddResource(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.topframe = tk.LabelFrame(self, text='', borderwidth=0)
        self.topframe.pack(expand=tk.TRUE, fill=tk.BOTH)

        self.firstframe = tk.LabelFrame(self.topframe, text='', borderwidth=0)
        self.secondframe = tk.LabelFrame(self.topframe, text='', borderwidth=0)
        self.thirdframe = tk.LabelFrame(self.topframe, borderwidth=0, text='')
        self.fourthframe = tk.LabelFrame(self.topframe, borderwidth=0, text='')

        self.firstframe.pack(side=tk.LEFT, anchor=tk.CENTER, expand=tk.TRUE, ipadx=10, ipady=10, padx=10, pady=10)
        self.secondframe.pack(side=tk.LEFT, anchor=tk.CENTER, expand=tk.TRUE, ipadx=10, ipady=10, padx=10, pady=10)
        self.thirdframe.pack(side=tk.LEFT, anchor=tk.CENTER, expand=tk.TRUE, ipadx=10, ipady=10, padx=10, pady=20)
        self.fourthframe.pack(side=tk.LEFT, anchor=tk.CENTER, expand=tk.TRUE, ipadx=10, ipady=10, padx=10, pady=20)


        self.AddAudioVideoButton = tk.Button(self.firstframe, text='Audio\n and Video', width=20,height=5,
                                        command=lambda: controller.show_frame(AddAudioVideo))
        self.AddCourseButton = tk.Button(self.firstframe, text='Courses', width=20, height=5,
                                         command=lambda: controller.show_frame(AddCourse))

        self.AddImagesButton= tk.Button(self.secondframe, text='Clipart, Photos\nand Sprites', width=20,height=5,
                                        command=lambda: controller.show_frame(AddImages))
        self.AddInteractiveMediaButton= tk.Button(self.secondframe, text='Interactive\n Media',  width=20,height=5,
                                        command=lambda: controller.show_frame(AddInteractiveMedia))

        self.AddTextButton= tk.Button(self.thirdframe, text='Books\n and Texts', width=20,height=5,
                                        command=lambda: controller.show_frame(AddText))
        self.AddWebsitesbutton= tk.Button(self.thirdframe, text='Websites', width=20,height=5,
                                        command=lambda: controller.show_frame(AddMedia))


        self.go_projects = tk.Button( self.fourthframe, text='View\nProjects', width=20, height=5,
                                         command=lambda: controller.show_frame(Projects))

        self.go_home = tk.Button( self.fourthframe, text='Home', width=20, height=5,
                                         command=lambda: controller.show_frame(HomePage))

        self.AddAudioVideoButton.pack( pady=10)
        self.AddCourseButton.pack( pady=10)
        self.AddImagesButton.pack( pady=10)
        self.go_projects.pack( pady=10)

        self.AddInteractiveMediaButton.pack( pady=10)
        self.AddTextButton.pack( pady=10)
        self.AddWebsitesbutton.pack( pady=10)
        self.go_home.pack( pady=10)

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
        middleleftframe.grid(columnspan=5, column=0, row=2, sticky=tk.W)

        middleframe = tk.LabelFrame(mainframe, text="", borderwidth=0)
        middleframe.grid(columnspan=5, column=4, row=2, sticky=tk.W)

        middlerightframe = tk.LabelFrame(mainframe, text='', borderwidth=0)
        middlerightframe.grid(columnspan=3, column=6, row=2,  sticky=tk.E)

        bottomframe = tk.LabelFrame(self, text="", borderwidth=4)
        bottomframe.grid(column=0, row=3, pady=5)

        buttonsframe = tk.LabelFrame(self, text="", borderwidth=0)
        buttonsframe.grid(column=0, row=4)

        self.label = tk.Label(header_frame, text='New Text')
        self.label.grid(column=0, row=1)

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

        self.text_id = None
        self.current_author = ''
        self.current_media = ''

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
                                                *self.language_options)

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

        self.updateextresource = tk.Button(middlerightframe, text='Update', command=lambda: self.update_text())
        self.updateextresource.config(width=12, cursor='hand2')#
        self.updateextresource.grid(column=3, row=0, padx=2, sticky=tk.W)

        self.addtextresource = tk.Button(middlerightframe, text='Save', command=lambda: self.save_text())
        self.addtextresource.config(width=12, cursor='hand2')  #
        self.addtextresource.grid(column=4, row=0, padx=2, sticky=tk.E)

        self.level_label = tk.Label(middleframe, text='Level:')
        self.level_entry = tk.OptionMenu(middleframe, self.level,
                                         *self.level_options)
        self.level_entry.configure(width=15)

        self.level_label.grid(column=0, row=0, padx=10, sticky=tk.W)
        self.level_entry.grid(column=1, row=0, padx=5, sticky=tk.W)

        self.text_type_label = tk.Label(middleleftframe, text='Select text type:')

        self.text_type1 = tk.Radiobutton(middleleftframe, text='Book', variable=self.text_type, value=1)
        self.text_type2= tk.Radiobutton(middleleftframe, text='Short story', variable=self.text_type,
                                        value=2)
        self.text_type3= tk.Radiobutton(middleleftframe, text='Other text type', variable=self.text_type, value=3)

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
        self.resource_list.column('#0',minwidth=0, width=0)
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
        self.treeview.bind('<ButtonRelease-1>', self.select_text)

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

        self.delete_button = tk.Button(buttonsframe, text='Delete Text', bg='red', command=lambda: self.delete_text())
        self.delete_button.config(width=15, cursor='hand2')
        self.delete_button.grid(column=3, row=0, padx=10, sticky=tk.W)


    def list_resources(self):
        for i in self.resource_list.get_children():
            self.resource_list.delete(i)
        resources = data.list_text_resources()
        for item in resources:
            self.treeview.insert('', 'end', values=item)

    def show_updated_resources(self):
        updated = data.list_text_resources()
        for item in updated:
            self.treeview.insert('', 'end', values=item)

    def update_entry_widgets(self): # clears entry widgete

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
        elif self.text_type.get() == 3:
            media_name = 'Other text'
        return media_name

    def update_windows(self):
        self.list_resources()
        self.update_entry_widgets()

    def save_text(self):
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

        self.update_windows()

    def select_text(self, event):
        item = self.resource_list.focus()

        text = self.treeview.item(item)

        text_title = text['values'][0]
        self.text_id = data.get_text_id(text_title)

        text_info = data.get_full_text(self.text_id)

        self.current_author = text_info[0][1]
        self.current_media = text_info[0][8]

        self.title.set(text_info[0][0])
        self.author.set(text_info[0][1])
        self.year.set(text_info[0][2])
        self.pages.set(text_info[0][3])
        self.subject.set(text_info[0][7])
        self.notes.set(text_info[0][9])

        self.publisher.set(text_info[0][5])

        self.language.set(text_info[0][6])
        self.language_options = data.list_languages()

        self.level.set(text_info[0][4])
        self.level_options = data.list_levels()

        if text_info[0][8] == 'Book':
            self.text_type.set(1)
        elif text_info[0][8] == 'Short story':
            self.text_type.set(2)
        else:
            self.text_type.set(3)

        print(self.text_id)

        return self.text_id, self.current_author, self.current_media

    def update_text(self):
        media_name = self.get_media_name()
        author_name = self.author.get()

        if media_name != self.current_media or author_name != self.current_author:
            data. delete_resource_author(self.text_id, self.current_author, self.current_media)

            data.add_author(author_name)
            author_id = data.get_author_id(author_name)
            media_id = data.get_resource_medium_id(media_name)

            data.add_resource_author(self.text_id, author_id, media_id)

        if self.new_pub_flag.get() == 1:
            self.thepublisher = self.new_pub.get()
        else:
            self.thepublisher = self.publisher.get()

        if self.new_lang_flag.get() == 1:
            self.thelanguage = self.new_lang.get()
        else:
            self.thelanguage = self.language.get()

        data.update_text(self.text_id, self.title.get(), self.year.get(),
                          self.pages.get(), self.level.get(), self.thepublisher,
                          self.thelanguage, self.subject.get(), media_name, self.notes.get() )

        self.update_entry_widgets()
        self.clear_texts()
        self.show_updated_resources()

    def clear_texts(self):
        for i in self.resource_list.get_children():
            self.resource_list.delete(i)
        print('Text cleared')

    def show_updated_resource(self, text_id):
        text = data.get_text(self.text_id)
        self.treeview.insert('', 'end', values=text)

    def delete_text(self):
        media_name = self.title.get()
        message1 = "Delete " + self.current_media + " '" + media_name + "'?"
        message2 = "'" + media_name + "' deleted."

        print(self.current_media, self.current_author)

        result = tkMessageBox.askquestion("Delete?", message1)

        if result == 'yes':
            if tkMessageBox.askokcancel("Confirm", "Really?\nThis cannot be undone!", icon='warning'):
                data.delete_text(self.text_id, self.current_author, self.current_media)
                self.update_windows()
                tkMessageBox.showinfo('Deleted', message2)

class LinkResources(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.project_id = None
        self.resource_id = None
        self.media_id = None

        self.resources = set()

        self.project_title = tk.StringVar()
        self.project_type = tk.StringVar()
        self.resource_subject = tk.StringVar()

        self.media_type = tk.IntVar()
        self.media_type.set("?")

        self.searchheader = ttk.Label(self, text='Find Projects')
        self.searchheader.grid(column=0, row=0)

        self.mainframe = tk.LabelFrame(self, text='', borderwidth=4)
        self.mainframe.grid(column=0, row=1)

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

        self.clearbutton = ttk.Button(self.resultsframe, text='Clear project', command=lambda: self.clear_selection())
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
        self.project_list.column('#0', minwidth=0, width=0)
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
        self.project_list.column('4', width=120, anchor='w')
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

        self.audiovideo_rb = tk.Radiobutton(self.media_type_frame, text='Audio and Video',
                                            variable=self.media_type, value=1)
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

        show_window(self.resourceresults, 4)

    def show_results(self):
        results = self.create_table_values()
        column_names = results[0]
        resources = results[1]

        self.scollresources = ttk.Scrollbar(self.resourceresults)
        self.scollresources.grid(column=2, row=2, sticky=tk.N + tk.S + tk.W)

        self.resource_list = ttk.Treeview(self.resourceresults, height=4, selectmode='browse', #changed from 'extended'
                                          columns=column_names )

        self.scollresources.configure(orient="vertical", command=self.resource_list.yview)
        self.resource_list.configure(yscrollcommand=self.scollresources.set)

        self.resource_list['columns'] = column_names

        self.resource_list.column('#0', minwidth=0, width=0)
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

        self.search_resources(resources)

    def create_table_values(self):

        if self.media_type.get() == 1:
            column_names = ('Title', 'Artist', 'Year', 'Type', 'Program', 'Language')
            resources = data.find_av(self.resource_subject.get())

        if self.media_type.get() ==2:
            column_names = ('Title', 'Instructor', 'Start date', 'Duration', 'Platform', 'Subject')
            resources = data.find_courses(self.resource_subject.get())

        elif self.media_type.get() ==3:
            column_names = ('Title', 'Author', 'Website', 'Date', 'Access date', 'Subject')
            resources = data.find_web(self.resource_subject.get())

        elif self.media_type.get() ==4:
            column_names = ('Title', 'Creator', 'Type', 'Dimensions', 'Date', 'Location')
            resources = data.find_images(self.resource_subject.get())

        elif self.media_type.get() == 5:
            column_names = ('Title', 'Creator', 'Genre', 'Engine', 'Type', 'Comments')
            resources = data.find_interactive(self.resource_subject.get())

        elif self.media_type.get() ==6:
            column_names = ('Title', 'Author', 'Year', 'Pages', 'Language', 'Notes')
            resources = data.find_texts(self.resource_subject.get())


        return column_names, resources

    def select_resources(self, event):

        for item in self.treeview_resources.selection():
            item_text = self.treeview_resources.item(item)

            resource_name = item_text['values'][0]
            print(resource_name)

            if self.media_type.get() == 1:
                self.resource_id = data.get_audio_video_id(resource_name)
                self.media_id = data.get_av_mediaID(self.resource_id)
                print("AV ID =", self.resource_id)
                print("AV mediaID",self.media_id )

            if self.media_type.get() == 2:
                self.resource_id = data.get_course_id(resource_name)
                self.media_id = data.get_course_mediaID(self.resource_id)
                print('Courses:', self.resource_id, self.media_id)

            elif self.media_type.get() == 3:
                self.resource_id = data.get_website_id(resource_name)
                self.media_id = data.get_website_mediaID(self.resource_id)
                print("Website ID =", self.resource_id)
                print("Website mediaID", self.media_id)

            elif self.media_type.get() == 4:
                self.resource_id = data.get_image_id(resource_name)
                self.media_id = data.get_image_mediaID(self.resource_id)
                print("IMAGE ID =", self.resource_id)
                print("IMAGE mediaID =", self.media_id)

            elif self.media_type.get() == 5:
                self.resource_id = data.get_interactive_id(resource_name)
                self.media_id = data.get_media_interative_mediaID(self.resource_id)
                print("IF ID =", self.resource_id)
                print('IF mediaID = ', self.media_id)

            elif self.media_type.get() == 6:
                self.resource_id = data.get_text_id(resource_name)
                self.media_id = data.get_text_id(self.resource_id)
                print('Resource id =', self.resource_id)
                print('Text mediaID =', self.media_id)

            return self.resource_id, self.media_id

    def select_project(self, event):
        """ Takes item selected from listbox and stores it as a global variable to be used in
            Link resource window
        """
        self.project_id = None
        item = self.treeview_projects.selection()[0]
        project = self.treeview_projects.item(item)
        project_name = project['values'][0]
        print(project_name)

        project = data.get_projectID(project_name)
        self.project_id = project[0]
        print('Project ID =', self.project_id)
        return self.project_id

    def clear_selection(self):
        for i in self.treeview_projects.get_children():
            self.treeview_projects.delete(i)


    def link_project_resources(self):

        data.link_to_resources(self.project_id, self.resource_id, self.media_id)

        print("Added item(s)")


    def search_projects(self):
        for i in self.project_list.get_children():
            self.project_list.delete(i)
        projects = data.find_project(self.project_title.get())
        for item in projects:
            self.treeview_projects.insert('', 'end', values=item)
        self.titlebox.delete(0, 'end')

    def search_resources(self, resources):

        for i in self.resource_list.get_children():
            self.resource_list.delete(i)

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

        self.main_frame = tk.LabelFrame(self, text='',borderwidth=4)
        self.main_frame.grid(column=0, row=0, columnspan=10, sticky=tk.W+tk.E+tk.N+tk.S)

        self.label = tk.Label(self.main_frame, text='New Project')
        self.label.grid(column=0, row=0, columnspan=10)

        # FRAMES

        self.topleftframe = tk.LabelFrame(self.main_frame, text='', borderwidth=4)
        self.topleftframe.grid(column=0, row=1)

        self.toprightframe = tk.LabelFrame(self.main_frame, text='', borderwidth=4)
        self.toprightframe.grid(column=1, row=1)

        self.bottomframe = tk.LabelFrame(self, text='', borderwidth=4)
        self.bottomframe.grid(column=0, row=5, columnspan=4)

        self.button_frame = tk.LabelFrame(self, text='', borderwidth=0)
        self.button_frame.grid(column=0, row=6, columnspan=2, sticky=tk.W)

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
                                                *self.project_category_options)
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
        self.start_entry.grid(column=1, row=1,  columnspan=3, sticky=tk.W)
        self.finish_label.grid(column=0, row=2, sticky=tk.W)
        self.finish_entry.grid(column=1, row=2, columnspan=3, sticky=tk.W)

        self.refresh = tk.Button(self.toprightframe, text='Update list', width=12, command=lambda: self.list_projects())
        self.refresh.grid(column=1, row=6)

        self.add_project = tk.Button(self.toprightframe, text='Add Project',width=12, command=lambda: self.save_project())
        self.add_project.grid(column=2, row=6, pady=12, sticky=tk.E)

        # Bottom Frame

        self.scollprojects = tk.Scrollbar(self.bottomframe)
        self.scollprojects.grid(column=2, row=0, sticky=tk.N + tk.S)

        self.project_list = ttk.Treeview(self.bottomframe, height=12,
                                         columns=('Name', 'Type','Description', 'Start date', 'End date'))

        self.scollprojects.configure(orient="vertical", command=self.project_list.yview)
        self.project_list.configure(yscrollcommand=self.scollprojects.set)

        self.project_list['columns'] = ('Name', 'Type','Description', 'Start date', 'End date')
        self.project_list.column('#0',minwidth=0, width=0)
        self.project_list.grid(column=0, row=0, columnspan=2, sticky=tk.E)

        self.project_list.heading('0',  text='Name', anchor='w')
        self.project_list.heading('1',text='Type', anchor='w')
        self.project_list.heading('2', text='Description', anchor='w')
        self.project_list.heading('3',text='Start date', anchor='w')
        self.project_list.heading('4', text='End date', anchor='w')

        self.project_list.column('0', width=250, anchor='w')
        self.project_list.column('1', width=165, anchor='w' )
        self.project_list.column('2', width=250, anchor='w')
        self.project_list.column('3', width=100, anchor='w')
        self.project_list.column('4', width=100,anchor='w')
        self.treeview = self.project_list


        self.back = tk.Button(self.button_frame, text='Back', command=lambda: controller.show_frame(AddResource))
        self.back.config(width=10)
        self.back.grid(column=0, row=1, padx=20, pady=2, sticky=tk.W)

        self.home = tk.Button(self.button_frame, text='Home', command=lambda: controller.show_frame(HomePage))
        self.home.config(width=10)
        self.home.grid(column=1, row=1,sticky=tk.W)

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

        self.table = data.list_websites()

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

        self.document_id = tk.IntVar() # For id of resource
        self.current_author = ''
        self.current_media = ''

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
        self.center_frame.grid(column=1, row=2,columnspan=3, sticky=tk.E)

        self.bottomleft = tk.LabelFrame(self.mainframe, text="", borderwidth=3)
        self.bottomleft.grid(column=0, row=4, sticky=tk.W + tk.E)

        self.bottomright = tk.LabelFrame(self.mainframe, text="", borderwidth=3)
        self.bottomright.grid(column=1, row=4, sticky=tk.E)

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
        self.save_resource = tk.Button(self.center_frame, text='Save',width=8, command=lambda: self.save_data())
        self.save_resource.config(cursor='hand2')
        self.save_resource.grid(column=6, row=0,  sticky=tk.E)

        self.clear_boxes = tk.Button(self.center_frame, text='Clear',width=8,
                                        command=lambda: self.update_entry_widgets())
        self.clear_boxes.config(cursor='hand2')
        self.clear_boxes.grid(column=4, row=0,padx=10, sticky=tk.E)


        self.update_resource = tk.Button(self.center_frame, text='Update', bg='green', width=8,
                                        command=lambda: self.update())
        self.update_resource.config(cursor='hand2')
        self.update_resource.grid(column=5, row=0, padx=10, sticky=tk.E)

        self.delete_resource = tk.Button(self.bottomright, text='Delete', bg='red',width=15,
                                         command=lambda: self.delete())
        self.delete_resource.config(cursor='hand2')
        self.delete_resource.grid(column=6, row=1, sticky=tk.W)

        self.create_values()

        self.create_top_frame_widgets(self.window_header, self.b2L, self.b3L, self.b4L, self.b1R, self.b2R,
                                      self.b3R, self.b4R)

        self.place_widgets()

        self.add_radio_buttons(self.media_choice1, self.media_choice2, self.media_choice3)

        self.display_resources(self.c1, self.c2, self.c3, self.c4, self.c5, self.c6)

        self.list_resources(self.table)
        self.update_entry_widgets()


    def create_values(self):
        self.window_header = 'Websites'
        self.b2L = 'Author'
        self.b3L = 'Date Created'
        self.b4L = 'Subject'
        self.b1R = 'Website'
        self.b2R = 'URL'
        self.b3R = 'Access date'
        self.b4R = 'Notes'

        self.c1 = 'Title'
        self.c2 = 'Author'
        self.c3 = 'Website'
        self.c4 = 'Created'
        self.c5 = 'Access date'
        self.c6 = 'Subject'

        self.media_choice1 = 'Documentation'
        self.media_choice2 = 'Q&A Site'
        self.media_choice3 = 'Website'

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

        self.webdocs_list = ttk.Treeview(self.bottom_middleframe, height=12,
                                         columns= (col1, col2, col3, col4, col5, col6))

        scrollwebdocs.configure(orient="vertical", command=self.webdocs_list.yview)
        self.webdocs_list.configure(yscrollcommand=scrollwebdocs.set)

        self.webdocs_list['columns'] = (col1, col2, col3, col4, col5, col6)
        self.webdocs_list.column('#0', minwidth=0, width=0)
        self.webdocs_list.column('0', width=200, anchor='w')
        self.webdocs_list.column('1', width=160, anchor='w')
        self.webdocs_list.column('2', width=95, anchor='w')
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

        self.treeview_docs = self.webdocs_list
        self.treeview_docs.bind('<ButtonRelease-1>', self.select_document)

        return self.treeview_docs, self.webdocs_list


    def list_resources(self, data_table):
        for i in self.webdocs_list.get_children():
            self.webdocs_list.delete(i)
        resources = data_table
        for item in resources:
            self.treeview_docs.insert('', 'end', values=item)


    def get_media_name(self):
        if self.media_buttons.get() == 1:
            media_name = self.media_choice1
        elif self.media_buttons.get() == 2:
            media_name = self.media_choice2
        else:
            media_name = self.media_choice3
        return media_name

    def update_windows(self):
        search_table = data.list_websites()
        self.list_resources(search_table)
        self.update_entry_widgets()

    def save_data(self):
        media_name = self.get_media_name()

        data.add_website(self.box1L.get(), self.box2L.get(), self.box3L.get(), self.box4L.get(), self.box1R.get(),
                              self.box2R.get(), self.box3R.get(), self.box4R.get(), media_name)

        self.update_windows()


    def get_current_data(self):
        current_data = data.list_websites()
        return current_data

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

        # current_data = self.get_current_data()
        #
        # self.list_resources(current_data)

    def select_document(self, event):
        self.media_buttons.set('?')
        item = self.webdocs_list.focus()

        document = self.treeview_docs.item(item)

        document_name = document['values'][0]

        print(document, document_name)

        self.document_id = data.get_website_id(document_name)

        print(self.document_id)

        web_doc = data.get_website(self.document_id)
        self.current_author = web_doc[1]
        self.current_media = web_doc[8]

        self.box1L.set(web_doc[0])
        self.box2L.set(web_doc[1])
        self.box3L.set(web_doc[2])
        self.box4L.set(web_doc[3])
        self.box1R.set(web_doc[4])
        self.box2R.set(web_doc[5])
        self.box3R.set(web_doc[6])
        self.box4R.set(web_doc[7])

        media = web_doc[8].strip()

        if media == self.media_choice1.strip():
            self.media_buttons.set(1)
        elif media == self.media_choice2.strip():
            self.media_buttons.set(2)
        elif media == self.media_choice3.strip():
            self.media_buttons.set(3)

        return self.document_id, self.current_author, self.current_media

    def update(self):
        media_name = self.get_media_name()

        media_id = data.get_resource_medium_id(media_name)

        author_name = self.box2L.get()

        if self.current_author != author_name or self.current_media != media_name:
            data.delete_resource_author(self.document_id, self.current_author, self.current_media)

            data.add_author(author_name)

            author_id = data.get_author_id(author_name)

            data.add_resource_author(self.document_id, author_id, media_id)

        data.update_media(self.document_id, self.box1L.get(), self.box2L.get(), self.box3L.get(), self.box4L.get(),
                          self.box1R.get(), self.box2R.get(), self.box3R.get(), self.box4R.get(), media_id)

        search_table = data.list_websites()

        self.list_resources(search_table)
        self.update_entry_widgets()

    def clear_resource(self):
        for i in self.webdocs_list.get_children():
            self.webdocs_list.delete(i)

    def show_updated_resource(self):
        resource = data.get_website(self.document_id)
        self.treeview_docs.insert('', 'end', values=resource)

    def list_resource(self):
        self.clear_resource()
        resource_list = data.list_websites()

        for item in resource_list:
            self.treeview_docs.insert('', 'end', values=item)

    def delete(self):
        media_name = self.box1L.get()
        message1 = "Delete " + self.current_media + " '" + media_name + "'?"
        message2 = "'" + media_name + "' deleted."

        result = tkMessageBox.askquestion("Delete?", message1)
        if result == 'yes':
            if tkMessageBox.askokcancel("Confirm", "Really?\nThis cannot be undone!", icon='warning'):
                data.delete_website(self.document_id, self.current_author, self.current_media)
                self.update_windows()
                tkMessageBox.showinfo('Deleted', message2)

            else:
                print("Not deleted")

class AddCourse(AddMedia):
    def __init__(self, parent, controller):
        AddMedia.__init__(self, parent, controller)

        self.level = tk.StringVar()
        self.level_options = data.list_levels()
        self.level.set('Select one')
        self.document_id = None
        self.current_author = ''
        self.current_media = ''

        self.table = data.list_courses()

        self.level_label = tk.Label(self.center_frame, text='Level:')
        self.level_entry = tk.OptionMenu(self.center_frame, self.level,
                                            *self.level_options)
        self.level_entry.configure(width=15)
        self.level_label.grid(column=0, row=0, sticky=tk.W)
        self.level_entry.grid(column=1, row=0, padx=2, sticky=tk.W)

        self.create_values()

        self.display_resources(AddMedia.c1, AddMedia.c2, AddMedia.c3, AddMedia.c4,
                               AddMedia.c5, AddMedia.c6)

        self.update_entry_widgets()

        self.create_top_frame_widgets(AddMedia.window_header, AddMedia.b2L, AddMedia.b3L, AddMedia.b4L, \
                                      AddMedia.b1R, AddMedia.b2R, AddMedia.b3R, AddMedia.b4R)

        self.list_resources(self.table)

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
        AddMedia.c2 = 'Instructor'
        AddMedia.c3 = 'Start date'
        AddMedia.c4 = 'Duration'
        AddMedia.c5 = 'Platform'
        AddMedia.c6 = 'Comments'

        AddMedia.media_choice1 = 'Audio only class'
        AddMedia.media_choice2 = 'Web based class'
        AddMedia.media_choice3 = 'Blended Class'


        return AddMedia.c1, AddMedia.c2, AddMedia.c3, AddMedia.c4, AddMedia.c5, AddMedia.c6, AddMedia.window_header, \
               AddMedia.b2L, AddMedia.b3L, AddMedia.b4L, AddMedia.b1R, AddMedia.b2R, AddMedia.b3R, AddMedia.b4R, \
               AddMedia.media_choice1, AddMedia.media_choice2, AddMedia.media_choice3

    def get_media_name(self):
        if self.media_buttons.get() == 1:
            media_name = 'Audio only class'
        elif self.media_buttons.get() == 2:
            media_name = 'Web based class'
        elif self.media_buttons.get() == 3:
            media_name = 'Blended Class'
        print('Media name = ', media_name)
        return media_name

    def get_current_data(self):
        current_data = data.list_courses()
        return current_data

    def select_document(self, event):
        self.media_buttons.set('?')
        item = self.webdocs_list.focus()

        document = self.treeview_docs.item(item)

        document_name = document['values'][0]

        print('Document: ', document)
        print('Doc name: ', document_name)

        self.document_id = data.get_course_id(document_name)
        print('course_id = ', self.document_id)

        course = data.get_course_info(self.document_id)
        print(course)

        self.current_author = course[1]
        self.current_media = course[8]
        print('Author =', self.current_author)
        print('Current media= ', self.current_media)

        self.box1L.set(course[0])
        self.box2L.set(course[1])
        self.box3L.set(course[2])
        self.box4L.set(course[3])
        self.box1R.set(course[4])
        self.box2R.set(course[5])
        self.box3R.set(course[6])
        self.box4R.set(course[7])
        self.level.set(course[9])

        media = course[8].strip()
        print(media)


        if media == 'Audio only class':
            self.media_buttons.set(1)
        elif media == 'Web based class':
            self.media_buttons.set(2)
        elif media == 'Blended Class':
            self.media_buttons.set(3)

        return self.document_id, self.current_author, self.current_media

    def update_windows(self):

        search_table = data.list_courses()
        self.list_resources(search_table)
        self.update_entry_widgets()

    def save_data(self):
        media_name = self.get_media_name()
        print('Media name = ', media_name)

            # add_course(title, instructor, start_date, duration, url, comments, level, platform, media, subject)
        data.add_course(self.box1L.get(), self.box2L.get(), self.box3L.get(),
                        self.box3R.get(), self.box2R.get(), self.box4R.get(),
                        self.level.get(), self.box1R.get(), media_name,
                        self.box4L.get())

        self.update_windows()

        # search_table = data.list_courses()
        #
        # self.list_resources(search_table)
        # self.update_entry_widgets()

    def update(self):

        media_name = self.get_media_name()
        print('Media name = ', media_name)

        old_author_id = data.get_author_id(self.current_author)
        print('Old author id= ', old_author_id)
        old_media_id = data.get_resource_medium_id(self.current_media)
        print('old media id', old_media_id)

        author_name = self.box2L.get()

        if self.current_author != author_name or self.current_media != media_name:
            data.delete_resource_author(self.document_id, self.current_author, self.current_media)
            print('Deleted resource author for ID', self.document_id)

            data.add_author(author_name)

            author_id = data.get_author_id(author_name)
            print('Author ID', author_id)

            media_id = data.get_resource_medium_id(media_name)
            print('MediaID =', media_id)

            data.add_resource_author(self.document_id, author_id, media_id)


        data.update_course(self.document_id, self.box1L.get(), self.box3L.get(),
                        self.box3R.get(), self.box2R.get(), self.box4R.get(),
                        self.level.get(), self.box1R.get(), media_name,
                        self.box4L.get())

        self.update_windows()

        # search_table = data.list_courses()
        #
        # self.list_resources(search_table)
        # self.update_entry_widgets()

    def delete(self):
        media_name = self.box1L.get()
        message1 = "Delete " + self.current_media + " '" + media_name + "'?"
        message2 = "'" + media_name + "' deleted."

        result = tkMessageBox.askquestion("Delete?", message1)
        if result == 'yes':
            if tkMessageBox.askokcancel("Confirm", "Really?\nThis cannot be undone!", icon='warning'):
                data.delete_course(self.document_id, self.current_author, self.current_media)
                self.update_windows()
                tkMessageBox.showinfo('Deleted', message2)

            else:
                print("Not deleted")

class AddAudioVideo(AddMedia):
    def __init__(self, parent, controller):
        AddMedia.__init__(self, parent, controller)

        self.table = data.list_av()
        self.document_id = None
        self.current_author = ''
        self.current_media = ''

        self.language = tk.StringVar()
        self.language_options = data.list_languages()
        self.language.set('Select one')

        self.language_label = tk.Label(self.center_frame, text='Language:')
        self.language_entry = tk.OptionMenu(self.center_frame, self.language,
                                            *self.language_options)#  if self.language_options else '0')
        self.language_entry.configure(width=8)
        self.language_label.grid(column=0, row=0, sticky=tk.W)
        self.language_entry.grid(column=1, row=0,padx=5, sticky=tk.W)

        self.table = data.list_av()


        self.create_values()

        self.display_resources(AddMedia.c1, AddMedia.c2, AddMedia.c3, AddMedia.c4,
                               AddMedia.c5, AddMedia.c6)

        self.create_top_frame_widgets(AddMedia.window_header, AddMedia.b2L, AddMedia.b3L, AddMedia.b4L, \
                                      AddMedia.b1R, AddMedia.b2R, AddMedia.b3R, AddMedia.b4R)

        self.list_resources(self.table)


    def create_values(self):
        AddMedia.window_header = 'Audio and Video'
        AddMedia.b2L = 'Artist'
        AddMedia.b3L = 'Duration (mins)'
        AddMedia.b4L = 'Subject'
        AddMedia.b1R = 'Producer'
        AddMedia.b2R = 'Date'
        AddMedia.b3R = 'Program'
        AddMedia.b4R = 'URL'

        AddMedia.c1 = 'Title'
        AddMedia.c2 = 'Artist'
        AddMedia.c3 = 'Date'
        AddMedia.c4 = 'Type'
        AddMedia.c5 = 'Program'
        AddMedia.c6 = 'Language'
        AddMedia.media_choice1 = 'Music or Sound'
        AddMedia.media_choice2 = 'Podcast'
        AddMedia.media_choice3 = 'Video'

        return AddMedia.c1, AddMedia.c2, AddMedia.c3, AddMedia.c4, AddMedia.c5, AddMedia.c6, AddMedia.window_header, \
               AddMedia.b2L, AddMedia.b3L, AddMedia.b4L, AddMedia.b1R, AddMedia.b2R, AddMedia.b3R, AddMedia.b4R, \
               AddMedia.media_choice1, AddMedia.media_choice2, AddMedia.media_choice3


    def get_media_name(self):
        if self.media_buttons.get() == 1:
            media_name = 'Music/Sound'
        elif self.media_buttons.get() == 2:
            media_name = 'Podcast'
        else:
            media_name = 'Video'
        return media_name

    def update_windows(self):
        search_table = data.list_av()

        self.update_entry_widgets()
        self.list_resources(search_table)

    def save_data(self):
        media_name = self.get_media_name()

        data.add_audio_video(self.box1L.get(), self.box2L.get(), self.box3L.get(),
                             self.box2R.get(), self.box3R.get(), self.box4R.get(),
                             self.language.get(), media_name, self.box4L.get(),
                             self.box1R.get())

        self.update_windows()

    def select_document(self, event):
        self.media_buttons.set('?')

        item = self.webdocs_list.focus()

        document = self.treeview_docs.item(item)

        document_name = document['values'][0]

        print('Document: ', document)
        print('Doc name: ', document_name)

        self.document_id = data.get_audio_video_id(document_name)
        print('Doc_id = ', self.document_id)

        av = data.get_av_info(self.document_id)
        print(av)

        self.current_author = av[1]
        self.current_media = av[9]
        print('Author =', self.current_author)
        print('Current media= ', self.current_media)

        self.box1L.set(av[0])
        self.box2L.set(av[1])
        self.box3L.set(av[2])
        self.box4L.set(av[3])
        self.box1R.set(av[4])
        self.box2R.set(av[5])
        self.box3R.set(av[6])
        self.box4R.set(av[7])
        self.language.set(av[8])

        if self.current_media == 'Music or Sound':
            self.media_buttons.set(1)
        elif self.current_media == 'Podcast':
            self.media_buttons.set(2)
        elif self.current_media == 'Video':
            self.media_buttons.set(3)

        return self.document_id, self.current_author, self.current_media

    def update(self):

        media_name = self.get_media_name()
        print('Media name = ', media_name)

        old_author_id = data.get_author_id(self.current_author)
        print('Old author id= ', old_author_id)

        old_media_id = data.get_resource_medium_id(self.current_media)
        print('old media id', old_media_id)

        author_name = self.box2L.get()

        if self.current_author != author_name or self.current_media != media_name:
            print('Difference found!')
            data.delete_resource_author(self.document_id, self.current_author, self.current_media)
            print('Deleted resource author for ID', self.document_id)

            data.add_author(author_name)

            author_id = data.get_author_id(author_name)
            print('Author ID', author_id)

            media_id = data.get_resource_medium_id(media_name)
            print('MediaID =', media_id)

            data.add_resource_author(self.document_id, author_id, media_id)

        # update_av(av_id, title, duration,  year, program, url, language, media, subject, publisher)
        data.update_av(self.document_id, self.box1L.get(), self.box3L.get(),
                        self.box2R.get(), self.box3R.get(), self.box4R.get(),
                        self.language.get(), media_id, self.box4L.get(),
                        self.box1R.get())

        search_table = data.list_av()

        self.list_resources(search_table)
        self.update_entry_widgets()


    def delete(self):
        media_name = self.box1L.get()

        message1 = "Delete " + self.current_media + " '" + media_name + "'?"
        message2 = "'" + media_name + "' deleted."

        result = tkMessageBox.askquestion("Delete?", message1)
        if result == 'yes':
            if tkMessageBox.askokcancel("Confirm", "Really?\nThis cannot be undone!", icon='warning'):
                data.delete_av(self.document_id, self.current_author, self.current_media)
                self.update_windows()
                tkMessageBox.showinfo('Deleted', message2)

            else:
                print("Not deleted")

class AddInteractiveMedia(AddMedia):
    def __init__(self, parent, controller):
        AddMedia.__init__(self, parent, controller)

        self.table = data.list_interactive()
        self.document_id = None
        self.current_author = ''
        self.current_media = ''

        self.create_values()

        self.display_resources(AddMedia.c1, AddMedia.c2, AddMedia.c3, AddMedia.c4,
                               AddMedia.c5, AddMedia.c6)

        self.create_top_frame_widgets(AddMedia.window_header, AddMedia.b2L, AddMedia.b3L, AddMedia.b4L, \
                                      AddMedia.b1R, AddMedia.b2R, AddMedia.b3R, AddMedia.b4R)

        self.list_resources(self.table)

    def create_values(self):
        AddMedia.window_header = 'Interactive Media'
        AddMedia.b2L = 'Creator'
        AddMedia.b3L = 'Year created'
        AddMedia.b4L = 'Genre'
        AddMedia.b1R = 'Platform'
        AddMedia.b2R = 'Engine'
        AddMedia.b3R = 'Version'
        AddMedia.b4R = 'Comments'

        AddMedia.c1 = 'Title'
        AddMedia.c2 = 'Creator'
        AddMedia.c3 = 'Year'
        AddMedia.c4 = 'Engine'
        AddMedia.c5 = 'Type'
        AddMedia.c6 = 'Comments'
        AddMedia.media_choice1 = 'Interactive Fiction'
        AddMedia.media_choice2 = 'Video game'
        AddMedia.media_choice3 = 'Other'


        return AddMedia.c1, AddMedia.c2, AddMedia.c3, AddMedia.c4, AddMedia.c5, AddMedia.c6, AddMedia.window_header, \
               AddMedia.b2L, AddMedia.b3L, AddMedia.b4L, AddMedia.b1R, AddMedia.b2R, AddMedia.b3R, AddMedia.b4R, \
               AddMedia.media_choice1, AddMedia.media_choice2, AddMedia.media_choice3

    def get_media_name(self):
        if self.media_buttons.get() == 1:
            media_name = 'Interactive Fiction'
        elif self.media_buttons.get() == 2:
            media_name = 'Video game'
        else:
            media_name = 'Other interactive'
        return media_name

    def update_windows(self):
        search_table = data.list_interactive()
        self.list_resources(search_table)
        self.update_entry_widgets()

    def save_data(self):
        media_name = self.get_media_name()

        data.add_interactive_media(self.box1L.get(), self.box2L.get(), self.box3L.get(),
                                   self.box1R.get(), self.box3R.get(), self.box4R.get(),
                                   self.box2R.get(), media_name, self.box4L.get())

        self.update_windows()

    def select_document(self, event):
        item = self.webdocs_list.focus()

        document = self.treeview_docs.item(item)

        document_name = document['values'][0]

        print('Document: ', document)
        print('Doc name: ', document_name)

        self.document_id = data.get_interactive_id(document_name)
        print('Doc_id = ', self.document_id)

        interactive = data.get_interactive_info(self.document_id)
        print(interactive)

        self.current_author = interactive[1]
        self.current_media = interactive[8]
        print('Author =', self.current_author)
        print('Current media= ', self.current_media)

        self.box1L.set(interactive[0])
        self.box2L.set(interactive[1])
        self.box3L.set(interactive[2])
        self.box4L.set(interactive[3])
        self.box1R.set(interactive[4])
        self.box2R.set(interactive[5])
        self.box3R.set(interactive[6])
        self.box4R.set(interactive[7])

        if self.current_media == 'Interactive Fiction':
            self.media_buttons.set(1)
        elif self.current_media == 'Video game':
            self.media_buttons.set(2)
        elif self.current_media == 'Other interactive':
            self.media_buttons.set(3)

        return self.document_id, self.current_author, self.current_media

    def update(self):

        media_name = self.get_media_name()
        print('Media name = ', media_name)

        old_author_id = data.get_author_id(self.current_author)
        print('Old author id= ', old_author_id)

        old_media_id = data.get_resource_medium_id(self.current_media)
        print('old media id', old_media_id)

        author_name = self.box2L.get()

        author_id = data.get_author_id(author_name)
        print('Author ID', author_id)

        media_id = data.get_resource_medium_id(media_name)
        print('MediaID =', media_id)

        if self.current_author != author_name or self.current_media != media_name:
            print('Difference found!')
            data.delete_resource_author(self.document_id, self.current_author, self.current_media)
            print('Deleted resource author for ID', self.document_id)

            data.add_author(author_name)

            data.add_resource_author(self.document_id, author_id, media_id)

        data.update_interactive(self.document_id, self.box1L.get(), self.box3L.get(), self.box1R.get(),
                                self.box3R.get(), self.box4R.get(), self.box1R.get(), media_id, self.box4L.get())

        self.update_windows()

    def delete(self):
        media_name = self.box1L.get()
        message1 = "Delete " + self.current_media + " '" + media_name + "'?"
        message2 = "'" + media_name + "' deleted."

        result = tkMessageBox.askquestion("Delete?", message1)
        if result == 'yes':
            if tkMessageBox.askokcancel("Confirm", "Really?\nThis cannot be undone!", icon='warning'):
                data.delete_interactive(self.document_id, self.current_author, self.current_media)
                self.update_windows()
                tkMessageBox.showinfo('Deleted', message2)

            else:
                print("Not deleted")

class AddImages(AddMedia):
    def __init__(self, parent, controller):
        AddMedia.__init__(self, parent, controller)

        self.search_table = data.list_images()
        self.document_id = None
        self.current_author = ''
        self.current_media = ''


        self.create_values()

        self.display_resources(AddMedia.c1, AddMedia.c2, AddMedia.c3, AddMedia.c4,
                               AddMedia.c5, AddMedia.c6)

        self.create_top_frame_widgets(AddMedia.window_header, AddMedia.b2L, AddMedia.b3L, AddMedia.b4L, \
                                      AddMedia.b1R, AddMedia.b2R, AddMedia.b3R, AddMedia.b4R)

        self.list_resources(self.search_table)

    def create_values(self):
        AddMedia.window_header = 'Images'
        AddMedia.b2L = 'Creator'
        AddMedia.b3L = 'Date Created'
        AddMedia.b4L = 'Copywrite'
        AddMedia.b1R = 'Dimensions'
        AddMedia.b2R = 'Website'
        AddMedia.b3R = 'URL'
        AddMedia.b4R = 'Comments'

        AddMedia.c1 = 'Title'
        AddMedia.c2 = 'Creator'
        AddMedia.c3 = 'Type'
        AddMedia.c4 = 'Dimensions'
        AddMedia.c5 = 'Date'
        AddMedia.c6 = 'Comments'
        AddMedia.media_choice1 = 'Photo'
        AddMedia.media_choice2 = 'Clip art'
        AddMedia.media_choice3 = 'Sprite'

        return AddMedia.c1, AddMedia.c2, AddMedia.c3, AddMedia.c4, AddMedia.c5, AddMedia.c6, AddMedia.window_header, \
               AddMedia.b2L, AddMedia.b3L, AddMedia.b4L, AddMedia.b1R, AddMedia.b2R, AddMedia.b3R, AddMedia.b4R, \
               AddMedia.media_choice1, AddMedia.media_choice2, AddMedia.media_choice3


    def get_media_name(self):
        if self.media_buttons.get() == 1:
            media_name = 'Photo'
        elif self.media_buttons.get() == 2:
            media_name = 'Clip art'
        else:
            media_name = 'Sprite'
        return media_name

    def update_windows(self):
        search_table = data.list_images()

        self.update_entry_widgets()
        self.list_resources(search_table)

    def save_data(self):
        media_name = self.get_media_name()

        data.add_images(self.box1L.get(), self.box2L.get(), self.box3L.get(),
                        self.box4L.get(), self.box2R.get(), self.box1R.get(),
                        self.box3R.get(), self.box4R.get(), media_name)

        self.update_windows()

    def select_document(self, event):
        item = self.webdocs_list.focus()

        document = self.treeview_docs.item(item)

        document_name = document['values'][0]

        print('Document: ', document)
        print('Doc name: ', document_name)

        self.document_id = data.get_image_id(document_name)
        print('Doc_id = ', self.document_id)

        image = data.get_image_info(self.document_id)
        print(image)

        self.current_author = image[1]
        self.current_media = image[8]
        print('Author =', self.current_author)
        print('Current media= ', self.current_media)

        self.box1L.set(image[0])
        self.box2L.set(image[1])
        self.box3L.set(image[2])
        self.box4L.set(image[3])
        self.box1R.set(image[4])
        self.box2R.set(image[5])
        self.box3R.set(image[6])
        self.box4R.set(image[7])

        if self.current_media == 'Photo':
            self.media_buttons.set(1)
        elif self.current_media == 'Clip art':
            self.media_buttons.set(2)
        elif self.current_media == 'Sprite':
            self.media_buttons.set(3)

        return self.document_id, self.current_author, self.current_media

    def update(self):

        media_name = self.get_media_name()
        print('Media name = ', media_name)

        old_author_id = data.get_author_id(self.current_author)
        print('Old author id= ', old_author_id)

        old_media_id = data.get_resource_medium_id(self.current_media)
        print('old media id', old_media_id)

        author_name = self.box2L.get()

        if self.current_author != author_name or self.current_media != media_name:
            print('Difference found!')
            data.delete_resource_author(self.document_id, self.current_author, self.current_media)
            print('Deleted resource author for ID', self.document_id)

            data.add_author(author_name)

            author_id = data.get_author_id(author_name)
            print('Author ID', author_id)

            media_id = data.get_resource_medium_id(media_name)
            print('MediaID =', media_id)

            data.add_resource_author(self.document_id, author_id, media_id)

        data.update_image(self.document_id, self.box1L.get(),  self.box3L.get(),
                        self.box4L.get(), self.box2R.get(), self.box1R.get(),
                        self.box3R.get(), self.box4R.get(), media_name)

        self.update_windows()

    def delete(self):
        media_name = self.box1L.get()
        message1 = "Delete " + self.current_media + " '" + media_name + "'?"
        message2 = "'" + media_name + "' deleted."

        result = tkMessageBox.askquestion("Delete?", message1)
        if result == 'yes':
            if tkMessageBox.askokcancel("Confirm", "Really?\nThis cannot be undone!", icon='warning'):
                data.delete_image(self.document_id, self.current_author, self.current_media)
                self.update_windows()
                tkMessageBox.showinfo('Deleted', message2)

            else:
                print("Not deleted")

class SearchResource(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.search_bar = tk.StringVar()
        self.media_type = tk.IntVar()
        self.media_type.set('?')
        self.column_names = ()
        self.resources = None

        self.mainframe = tk.LabelFrame(self, text='', borderwidth=4)
        self.mainframe.grid(column=0, row=1)

        self.top = tk.LabelFrame(self.mainframe, text="", borderwidth=0)
        self.topmiddle = tk.LabelFrame(self.mainframe, text="", borderwidth=3)
        self.topright = tk.LabelFrame(self.mainframe, text='', borderwidth=0)

        self.top.grid(column=0, row=2, sticky=tk.N + tk.S + tk.W + tk.E)
        self.topmiddle.grid(column=1, row=2)
        self.topright.grid(column=2, row=2, sticky=tk.E)

        self.bottom = tk.LabelFrame(self.mainframe, text='', borderwidth=3)
        self.bottom.grid(column=0, row=5, columnspan=20)

        self.title = tk.Label(self, text='Find Resources')
        self.title.grid(column=0, row=0)

        self.search_bar_label = tk.Label(self.top, text='Enter search term')
        self.search_bar_entry = tk.Entry(self.top, width=40, textvariable=self.search_bar)

        self.search_button = ttk.Button(self.topright, text='Search', command=lambda : self.show_results())

        # SEARCH
        self.sort_label = tk.Label(self.top, text='Resource type:')

        self.audiovideo_rb = tk.Radiobutton(self.topmiddle, text='Audio and Video',
                                            variable=self.media_type, value=1)
        self.courses_rb = tk.Radiobutton(self.topmiddle, text='Courses', variable=self.media_type, value=2)
        self.websites_rb = tk.Radiobutton(self.topmiddle, text='Websites', variable=self.media_type, value=3)
        self.images_rb = tk.Radiobutton(self.topmiddle, text='Images', variable=self.media_type, value=4)
        self.interactive_rb = tk.Radiobutton(self.topmiddle, text='Interactive Media',
                                             variable=self.media_type, value=5)
        self.texts_rb = tk.Radiobutton(self.topmiddle, text='Books and Texts', variable=self.media_type, value=6)

        self.search_bar_label.grid(column=0, row=1)
        self.search_bar_entry.grid(column=1, row=1)
        self.sort_label.grid(column=2, row=1, padx=5, sticky=tk.E)

        self.audiovideo_rb.grid(column=3, row=1, sticky=tk.W)
        self.texts_rb.grid(column=4, row=1, sticky=tk.W)
        self.courses_rb.grid(column=5, row=1, sticky=tk.W)
        self.websites_rb.grid(column=3, row=2, sticky=tk.W)
        self.images_rb.grid(column=4, row=2, sticky=tk.W)
        self.interactive_rb.grid(column=5, row=2, sticky=tk.W)

        self.search_button.grid(column=4, row=1, sticky=tk.W)

        self.home = ttk.Button(self.bottom, text='Back', command=lambda: controller.show_frame(HomePage))
        self.home.config(width=10, cursor='hand2')
        self.home.grid(column=0, row=10, padx=20, sticky=tk.E)

        show_window(self.bottom, 12) # opens an empty window as a placeholder

    def show_results(self):
        results = self.create_table_values()
        column_names = results[0]
        resources = results[1]

        self.scollresources = ttk.Scrollbar(self.bottom)
        self.scollresources.grid(column=2, row=2, sticky=tk.N + tk.S + tk.W)

        self.resource_list = ttk.Treeview(self.bottom, height=12, selectmode='extended',
                                              columns=column_names)
        self.resource_list.bind()

        self.scollresources.configure(orient="vertical", command=self.resource_list.yview)
        self.resource_list.configure(yscrollcommand=self.scollresources.set)

        self.resource_list['columns'] = column_names

        self.resource_list.column('#0', minwidth=0, width=0)
        self.resource_list.column('0', width=240, anchor='w')
        self.resource_list.column('1', width=150, anchor='w')
        self.resource_list.column('2', width=75, anchor='w')
        self.resource_list.column('3', width=75, anchor='w')
        self.resource_list.column('4', width=100, anchor='w')
        self.resource_list.column('5', width=220, anchor='w')
        self.resource_list.grid(column=0, row=2, sticky=tk.W + tk.N + tk.E)

        self.resource_list.heading('0', anchor='w', text=column_names[0])
        self.resource_list.heading('1', anchor='w', text=column_names[1])
        self.resource_list.heading('2', anchor='w', text=column_names[2])
        self.resource_list.heading('3', anchor='w', text=column_names[3])
        self.resource_list.heading('4', anchor='w', text=column_names[4])
        self.resource_list.heading('5', anchor='w', text=column_names[5])
        self.treeview_resources = self.resource_list
        #self.treeview_resources.bind('<ButtonRelease-1>', self.select_resources)

        self.search_resources(resources)



    def create_table_values(self):

        if self.media_type.get() == 1:
            column_names = ('Title', 'Artist', 'Year', 'Type', 'Program', 'Language')
            resources = data.find_av(self.search_bar.get())

        if self.media_type.get() == 2:
            column_names = ('Title', 'Instructor', 'Start date', 'Duration', 'Platform', 'Subject')
            resources = data.find_courses(self.search_bar.get())

        elif self.media_type.get() == 3:
            column_names = ('Title', 'Author', 'Date', 'Website', 'Access date', 'Subject')
            resources = data.find_web(self.search_bar.get())

        elif self.media_type.get() == 4:
            column_names = ('Title', 'Creator', 'Type', 'Dimensions', 'Date', 'Comments')
            resources = data.find_images(self.search_bar.get())

        elif self.media_type.get() == 5:
            column_names = ('Title', 'Creator', 'Genre', 'Engine', 'Type', 'Comments')
            resources = data.find_interactive(self.search_bar.get())

        elif self.media_type.get() == 6:
            column_names = ('Title', 'Author', 'Year', 'Pages', 'Language', 'Notes')
            resources = data.find_texts(self.search_bar.get())

        return column_names, resources


    def search_resources(self, resources):

        for i in self.resource_list.get_children():
            self.resource_list.delete(i)

        for item in resources:
            self.treeview_resources.insert('', 'end', values=item)
        self.search_bar_entry.delete(0, 'end')

class EditProject(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # VARIABLES
        self.search_bar = tk.StringVar()

        self.project_name = tk.StringVar()
        self.project_type = tk.StringVar()
        self.description = tk.StringVar()
        self.start_date = tk.StringVar()
        self.end_date = tk.StringVar()
        self.new_type = tk.IntVar(self, value=0)
        self.add_projecttype = tk.StringVar()
        self.choices = tk.StringVar()
        self.project_category_options = data.list_project_category()

        self.project_id = tk.IntVar()

        self.choices.set('Choose project type:')

        # FRAMES
        self.main_frame = tk.LabelFrame(self, text='', borderwidth=4)
        self.main_frame.grid(column=0, row=0, columnspan=10, sticky=tk.W + tk.E + tk.N + tk.S)

        self.label = tk.Label(self.main_frame, text='Edit Project')
        self.label.grid(column=0, row=0, columnspan=10)

        self.topleftframe = tk.LabelFrame(self.main_frame, text='', borderwidth=4)
        self.topleftframe.grid(column=0, row=2)

        self.toprightframe = tk.LabelFrame(self.main_frame, text='', borderwidth=4)
        self.toprightframe.grid(column=1, row=2)

        self.bottomframe = tk.LabelFrame(self, text='', borderwidth=4)
        self.bottomframe.grid(column=0, row=5, columnspan=4)

        # SEARCH
        self.projectframe = tk.LabelFrame(self.main_frame, text='', borderwidth=4)
        self.projectframe.grid(column=0, row=1, columnspan=3, sticky=tk.N + tk.W + tk.E)

        self.titlebox_label = tk.Label(self.projectframe, text='Enter search keyword')
        self.titlebox_label.grid(column=0, row=0, sticky=tk.W)
        self.titlebox = tk.Entry(self.projectframe, width=32, textvariable=self.search_bar)
        self.titlebox.grid(column=1, row=0, sticky=tk.W)

        self.searchbutton = ttk.Button(self.projectframe, text='Search', command=lambda: self.search_projects())
        self.searchbutton.config(width=10, cursor='hand2')
        self.searchbutton.grid(column=2, row=0, padx=5, pady=5, sticky=tk.E)

        # Top Left frame

        self.project_name_label = tk.Label(self.topleftframe, text='Project Name')
        self.project_name_entry = ttk.Entry(self.topleftframe, width=61, textvariable=self.project_name)

        self.description_label = tk.Label(self.topleftframe, text='Description')
        self.description_entry = ttk.Entry(self.topleftframe, width=61, textvariable=self.description)

        self.project_type_label = tk.Label(self.topleftframe, text='Project Type')
        self.project_type_entry = tk.OptionMenu(self.topleftframe, self.choices,
                                                *self.project_category_options)
        self.project_type_entry.configure(width=20)

        self.new_projecttype_label = tk.Label(self.topleftframe, text='New Project Type')
        self.new_projecttype = ttk.Entry(self.topleftframe, width=61, textvariable=self.add_projecttype)

        self.project_name_label.grid(column=0, row=1, sticky=tk.W)
        self.project_name_entry.grid(column=1, row=1, columnspan=3, sticky=tk.W)

        self.description_label.grid(column=0, row=2, sticky=tk.W)
        self.description_entry.grid(column=1, row=2, columnspan=3, sticky=tk.W)

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
        self.start_entry.grid(column=1, row=1, columnspan=2,sticky=tk.W)
        self.finish_label.grid(column=0, row=2, sticky=tk.W)
        self.finish_entry.grid(column=1, row=2, columnspan=2, sticky=tk.W)

        self.update_project = tk.Button(self.toprightframe, width= 10, text='Update', command=lambda: self.update())
        self.update_project.grid(column=1, row=6, pady=12)

        self.delete_project = tk.Button(self.toprightframe, width= 10, text='Delete', bg='red',
                                        command=lambda:self.delete())
        self.delete_project.grid(column=2, row=6)

        # Bottom Frame

        self.scollprojects = tk.Scrollbar(self.bottomframe)
        self.scollprojects.grid(column=1, row=0, sticky=tk.N + tk.S)

        self.project_list = ttk.Treeview(self.bottomframe, height=10, selectmode='browse',
                                         columns=('Name', 'Type', 'Description', 'Start date', 'End date'))

        self.scollprojects.configure(orient="vertical", command=self.project_list.yview)
        self.project_list.configure(yscrollcommand=self.scollprojects.set)

        self.project_list['columns'] = ('Name', 'Type', 'Description', 'Start date', 'End date')
        self.project_list.column('#0', minwidth=0, width=0)
        self.project_list.grid(column=0, row=0, sticky=tk.E)

        self.project_list.heading('0', text='Name', anchor='w')
        self.project_list.heading('1', text='Type', anchor='w')
        self.project_list.heading('2', text='Description', anchor='w')
        self.project_list.heading('3', text='Start date', anchor='w')
        self.project_list.heading('4', text='End date', anchor='w')

        self.project_list.column('0', width=250, anchor='w')
        self.project_list.column('1', width=165, anchor='w')
        self.project_list.column('2', width=250, anchor='w')
        self.project_list.column('3', width=98, anchor='w')
        self.project_list.column('4', width=95, anchor='w')
        self.treeview_projects = self.project_list
        self.treeview_projects.bind('<ButtonRelease-1>', self.select_project)

        self.home = tk.Button(self.bottomframe, text='Home', command=lambda: controller.show_frame(HomePage))
        self.home.config(width=10)
        self.home.grid(column=0, row=1, padx=10, sticky=tk.W)

        self.list_projects()
        self.update_widgets()


    def select_project(self,event):
        item = self.project_list.focus()

        project = self.treeview_projects.item(item)

        project_name = project['values'][0]
        self.project_id = data.get_projectID(project_name)
        self.project_name.set(project['values'][0])
        self.choices.set(project['values'][1])
        self.description.set(project['values'][2])
        self.start_date.set(project['values'][3])
        self.end_date.set(project['values'][4])
        self.project_id = self.project_id[0]

        return self.project_id

    def update(self):

        data.update_project(self.project_id, self.project_name.get(), self.choices.get(),
                            self.description.get(), self.start_date.get(), self.end_date.get())

        self.clear_projects()
        self.show_updated_project()
        self.update_widgets()

    def clear_projects(self):
        for i in self.project_list.get_children():
            self.project_list.delete(i)

    def show_updated_project(self):
        project = data.get_project(self.project_id)
        self.treeview_projects.insert('', 'end', values=project)


    def list_projects(self):
        self.clear_projects()
        projects_list = data.list_projects()

        for item in projects_list:
            self.treeview_projects.insert('', 'end', values=item)

    def search_projects(self):
        self.clear_projects()

        projects = data.find_project(self.search_bar.get())

        for item in projects:
            self.treeview_projects.insert('', 'end', values=item)
        self.titlebox.delete(0, 'end')

    def update_widgets(self):
        self.project_name_entry.delete(0, 'end')
        self.description_entry.delete(0, 'end')
        self.start_entry.delete(0, 'end')
        self.finish_entry.delete(0, 'end')
        self.new_projecttype.delete(0, 'end')
        self.new_type.set(0)
        self.choices.set('Choose project type:')
        self.project_category_options = data.list_project_category()

    def delete(self):

        result = tkMessageBox.askquestion("Delete?", "Delete project?")
        if result == 'yes':
            if tkMessageBox.askokcancel("Confirm", "Really?\nThis cannot be undone!", icon='warning'):
                data.delete_project(self.project_id)
                print("Deleted")
                tkMessageBox.showinfo('Deleted', "Project deleted.")
                self.update_widgets()
                self.clear_projects()




if __name__ == "__main__":
    app = ProjectLibrary()
    app.title('Project Library')
    app.iconbitmap('project.ico')
    app.maxsize(890,750)
    app.mainloop()



