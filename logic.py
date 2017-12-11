import sqlite3 as sql
import dataCRUD as data


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
    

# BOOKS
def add_text(title, author, year, pages, level, publisher, language, subject, media):

    data.add_author(author)
    data.add_publisher(publisher)
    data.add_language(language)
    data.add_subject(subject)

    level_id = data.get_level_id(level)
    publisher_id = data.get_publisher_id(publisher)
    language_id = data.get_language_id(language)
    media_id = data.get_resource_medium_id(media)
    subject_id = data.get_subject_id(subject)

    data.add_text_to_db(title, year, pages, level_id, publisher_id, language_id, subject_id, media_id)

    resource_id = data.get_text_id(title)
    author_id = data.get_author_id(author)

    data.add_resource_author(resource_id, author_id, media_id)


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


def add_image(title, author, date_created, date_accessed, subject, url, copyright, media):

    data.add_author(author)
    data.add_subject(subject)
    image_name = get_image_name(media)
    copyright_status = get_image_type(copyright)

    author_id = data.get_author_id(author)
    subject_id = data.get_subject_id(subject)
    copyright_id = data.get_copyright_id(copyright_status)
    media_id = data.get_resource_medium_id(image_name)

    data.add_images_to_database(title, date_created, date_accessed, subject_id, url, copyright_id, media_id)

    image_id = data.get_image_id(title)

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


def remove_website(title):
    resource =  data.get_website_details(title)
    resource_id = resource[0]
    data.delete_website(resource_id)

    #data.delete_resource_author(resource_id, author, media)
    pass

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