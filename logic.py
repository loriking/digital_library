import operator
import dataCRUD as data
import csv


# AUDIO
def add_audio(title, author, duration, subject,  program, url, date, media_id, language):

    # if language != 'Select one':
    #     data.add_language(language)
    # else:
    #     language = 'Unknown'
    #     data.add_language(language)
    # if new_lang:
    #     data.add_language(language)

    language_id = data.get_language_id(language)

    data.add_subject(subject)
    subject_id = data.get_subject_id(subject)
        #add_audio_to_db(title,  duration, subjectID, program, url, date, mediaID, languageID)
    data.add_audio_to_db(title, duration, subject_id, program, url, date, media_id, language_id)

    audio_id = data.get_audio_id(title)
    data.add_author(author)
    author_id = data.get_author_id(author)

    data.add_resource_author(audio_id, author_id, media_id)
    
def edit_audio(audio_id, title, author, duration, subject, program, date, url, media, language):
    data.add_author(author)
    data.add_subject(subject)
    data.add_language(language)

    author_id = data.get_author_id(author)
    subject_id = data.get_subject_id(subject)
    language_id = data.get_language_id(language)
    media_id = data.get_resource_medium_id(media)

    data.update_audio_data(audio_id, title, duration, subject_id, program, date, url, media_id, language_id)

    data.add_resource_author(audio_id, author_id, media_id)

def delete_audio(audio_id, author, media):
    data.delete_audio_from_db(audio_id)
    data.delete_resource_author(audio_id, author, media)

# BOOKS
def add_text(title, author, year, pages, level, publisher, language, subject, medium):

    data.add_author(author)
    data.add_publisher(publisher)
    data.add_language(language)
    data.add_subject(subject)

    level_id = data.get_level_id(level)
    publisher_id = data.get_publisher_id(publisher)
    language_id = data.get_language_id(language)
    media_id = data.get_resource_medium_id(medium)
    subject_id = data.get_subject_id(subject)

    data.add_text_to_db(title, year, pages, level_id, publisher_id, language_id, subject_id, media_id)

    resource_id = data.get_text_id(title)
    author_id = data.get_author_id(author)

    data.add_resource_author(resource_id, author_id, media_id)

def edit_text(text_id, title, author, year, pages, level, publisher, language, subject, medium):

    data.add_author(author)
    data.add_publisher(publisher)
    data.add_language(language)
    data.add_subject(subject)

    author_id = data.get_author_id(author)
    publisher_id = data.get_publisher_id(publisher)
    language_id = data.get_language_id(language)
    subject_id = data.get_subject_id(subject)
    level_id = data.get_level_id(level)
    media_id = data.get_resource_medium_id(medium)

    data.update_text(text_id, title, year, pages, subject_id, publisher_id, language_id, media_id, level_id)
    data.add_resource_author(text_id, author_id, media_id)

# COURSES

def add_course(title, instructor, subject, duration, provider, url, notes, medium, level):
    data.add_author(instructor)
    data.add_subject(subject)
    data.add_provider(provider)

    subject_id = data.get_subject_id(subject)
    provider_id = data.get_provider_id(provider)
    media_id = data.get_resource_medium_id(medium)
    level_id = data.get_level_id(level)

    data.add_course_to_db(title, subject_id, duration, provider_id, url, notes, media_id, level_id)

    resource_id = data.get_course_id(title)
    author_id = data.get_author_id(instructor)

    data.add_resource_author(resource_id, author_id, media_id)

def edit_course(course_id, title, instructor, subject, duration_weeks, provider, url, notes, media, level):
    data.add_author(instructor)
    data.add_subject(subject)
    data.add_provider(provider)

    author_id = data.get_author_id(instructor)
    subject_id = data.get_subject_id(subject)
    provider_id = data.get_provider_id(provider)
    media_id = data.get_resource_medium_id(media)
    level_id = data.get_level_id(level)

    # update_course(course_id, title, subject_id, duration_weeks, provider_id, url, notes, media_id, level_id)
    data.update_course(course_id, title, subject_id, duration_weeks, provider_id, url, notes, media_id, level_id)

    data.add_resource_author(course_id, author_id, media_id)

# IMAGES
def get_image_type(status):
    if status == 1:
        image_status = 'Public Domain'
    elif status == 2:
        image_status = 'Creative Commons'
    elif status == 3:
        image_status = 'Copyrighted'
    return image_status

def get_image_name(media_button_value):
    if media_button_value == 1:
        image_name = 'Photo'
    elif media_button_value == 2:
        image_name = 'Clipart/Sprite'
    elif media_button_value == 3:
        image_name = 'Other image'
    return image_name


def add_image(title, author, date_created, date_accessed, subject, url, copyright_id, media):

    data.add_author(author)
    data.add_subject(subject)
    image_name = get_image_name(media)

    author_id = data.get_author_id(author)
    subject_id = data.get_subject_id(subject)
    media_id = data.get_resource_medium_id(image_name)

    data.add_images_to_database(title, date_created, date_accessed, subject_id, url, copyright_id, media_id)

    image_id = data.get_image_id(title)

    data.add_resource_author(image_id, author_id, media_id)

def edit_image_entry(image_id, title, author, date_created, date_accessed, subject, url, copyright_id, media):
    data.add_author(author)
    data.add_subject(subject)
    image_name = get_image_name(media)

    author_id = data.get_author_id(author)
    subject_id = data.get_subject_id(subject)
    media_id = data.get_resource_medium_id(image_name)

    data.update_image(image_id, title, date_created, date_accessed, url,  subject_id, copyright_id, media_id)
    data.add_resource_author(image_id, author_id, media_id)

# INTERACTIVE
def get_interactive_name(media_button_value):
    if media_button_value == 1:
        interactive_name = 'Interactive Fiction'
    elif media_button_value == 2:
        interactive_name = 'Video game'
    elif media_button_value == 3:
        interactive_name =  'Other interactive'
    return interactive_name

def add_interactive_media(title, author, year, subject, platform, engine, version, medium):
    data.add_author(author)
    data.add_subject(subject)
    data.add_platform(platform)
    data.add_engine(engine)

    media_name = get_interactive_name(medium)

    author_id = data.get_author_id(author)
    subject_id = data.get_subject_id(subject)
    platform_id = data.get_platform_id(platform)
    engine_id = data.get_engine_id(engine)
    media_id = data.get_resource_medium_id(media_name)

    data.add_interactive_media_to_db(title, year, subject_id, platform_id, engine_id, version, media_id)

    resource_id = data.get_interactive_id(title)

    data.add_resource_author(resource_id, author_id, media_id)

def edit_interactive_media(im_id,title, author, year, subject, platform, engine, version, medium ):
    data.add_author(author)
    data.add_subject(subject)
    data.add_platform(platform)
    data.add_engine(engine)

    media_name = get_interactive_name(medium)

    author_id = data.get_author_id(author)
    subject_id = data.get_subject_id(subject)
    platform_id = data.get_platform_id(platform)
    engine_id = data.get_engine_id(engine)
    media_id = data.get_resource_medium_id(media_name)

    data.update_interactive(im_id, title, year, subject_id, platform_id, engine_id, version, media_id)
    data.add_resource_author(im_id, author_id, media_id)


# VIDEO

def add_video(title, author, duration,  subject, producer, year, url, medium, language):

    data.add_author(author)
    data.add_subject(subject)
    data.add_language(language)

    language_id = data.get_language_id(language)
    media_id = data.get_resource_medium_id(medium)
    subject_id = data.get_subject_id(subject)
    author_id = data.get_author_id(author)

    data.add_video_to_db(title, duration, subject_id, producer, year, url, media_id, language_id)

    video_id = data.get_video_id(title)

    data.add_resource_author(video_id, author_id, media_id)


def edit_video(video_id, title, author, duration, subject, producer, year, url, medium, language):
    data.add_author(author)
    data.add_subject(subject)

    author_id = data.get_author_id(author)
    subject_id = data.get_subject_id(subject)
    media_id = data.get_resource_medium_id(medium)
    language_id = data.get_language_id(language)

    data.update_video(video_id, title, duration, subject_id,  producer, year, url, media_id, language_id)
    data.add_resource_author(video_id, author_id, media_id)

# WEBSITES
def add_website(title, author, subject, url, date_created, date_accessed, notes, medium):

    data.add_author(author)
    data.add_subject(subject)

    media_id = data.get_resource_medium_id(medium)
    subject_id = data.get_subject_id(subject)

    data.add_website_to_db(title, subject_id, url, date_created, date_accessed, notes, media_id)

    author_id = data.get_author_id(author)
    resource_id = data.get_website_id(title)

    data.add_resource_author(resource_id, author_id, media_id)

def edit_website(website_id, title, author, subject, url, date_created, date_accessed, notes, medium):
    data.add_author(author)
    data.add_subject(subject)

    author_id = data.get_author_id(author)
    subject_id = data.get_subject_id(subject)
    media_id = data.get_resource_medium_id(medium)

    data.update_website(website_id, title, subject_id, url, date_created, date_accessed, notes, media_id)
    data.add_resource_author(website_id, author_id, media_id)

def remove_website(title):
    resource =  data.get_website_details(title)
    resource_id = resource[0]
    data.delete_website(resource_id)

    #data.delete_resource_author(resource_id, author, media)
    pass


# Project references
def view_project_references(project_id):
    items = []
    references = data.get_project_references(project_id)
    for item in references:
        results = data.get_reference_details(item[0], item[1] )

        for reference in results:
            items.append(reference)

    items = sorted(items, key=operator.itemgetter(0))

    if len(items) == 0:
        items.append('None')

    return items


def remove_project_reference(project_id, resource_name, media_name):
    media_id = data.get_resource_medium_id(media_name)
    resource_id = data.get_id(resource_name, media_name)

    data.delete_resources_reference(project_id, resource_id, media_id)


def export_to_txt(project_id):
    project = data.get_project(project_id)

    save_as = project[0]

    save_as = save_as + ' references' + '.txt'

    items = view_project_references(project_id)

    with open(save_as, 'w') as out_file:
        out_file.write('Type'.ljust(10))
        out_file.write('Title'.ljust(20))
        out_file.write('Author'.ljust(20))
        out_file.write('Subject'.ljust(10))
        for i in items:
            i = '\t'.join(i)
            out_file.write('\n')
            out_file.write(i)


def export_to_csv(project_id):
    project = data.get_project(project_id)
    save_as = project[0]

    save_as = save_as + ' references' + '.csv'
    items = view_project_references(project_id)

    myFile = open(save_as, 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerow(['Project Details'])
        writer.writerow(['Project Title', 'Project Type', 'Description', 'Start Date', 'Deadline'])
        writer.writerow(project)
        writer.writerow('')
        writer.writerow(['References'])
        writer.writerow(['Type', 'Title', 'Author', 'Topic'])
        writer.writerows(items)




