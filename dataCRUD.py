# -*- coding: utf-8 -*-

"""
dataCRUD.py
Created on Sep 15, 2017

@author: lak
"""

import sqlite3 as sql

db = sql.connect('library_data.db')
c = db.cursor()

# level
def add_level(level):
    c.execute('INSERT OR IGNORE INTO levels(level) VALUES(?)', (level,))
    db.commit()

def get_level_id(level):
    c.execute('SELECT ID FROM levels WHERE level = ?', (level,))
    levelID = c.fetchall()[0]
    levelID = levelID[0]
    return levelID

def list_levels():

    c.execute('''SELECT level FROM levels ORDER BY level''')
    results = [i[0] for i in c.fetchall()]
    return results


# Languages C.R.U.D.
def add_language(language):
    language = language.title()

    c.execute('''INSERT OR IGNORE INTO languages(language) VALUES(?)''', (language,))
    db.commit()


def list_languages():
    """    return: all the languages from database     """

    c.execute('''SELECT language FROM languages ORDER BY language''')
    results = [i[0] for i in c.fetchall()]
    return results


def get_language_id(language):
    """ return: the ID (PK) of a given language    """
    language = language.title()

    c.execute('''SELECT ID FROM languages WHERE language = ? ''', (language,))

    lang_id = c.fetchall()[0]
    lang_id = lang_id[0]

    return lang_id


def get_language(lang_id):
    """ :param langID: return: language from ID    """

    c.execute('''SELECT language FROM languages WHERE ID = ?''', (lang_id,))
    lang_id = c.fetchall()[0]
    language_name = lang_id[0]
    return language_name


def update_language(language):
    language = language.title()
    lang_id = get_language_id(language)
    c.execute('''UPDATE languages SET language = ? WHERE ID =?''', (language, lang_id))
    db.commit()


def delete_language():
    language_id = get_language_id()
    c.execute('''DELETE FROM languages WHERE ID = ?''', (language_id,))
    db.commit()

# AUTHORS
    
def add_author(name):
    """    Adds author(s) to SQL database    """
    c.execute('''INSERT OR IGNORE INTO authors(name) VALUES(?)''', (name,))
    db.commit()

    """
   
    if ',' in nameslist:
        names = nameslist.title().split(',')
        for name in names:
            c.execute('''INSERT OR IGNORE INTO authors(name) VALUES(?)''', (name,))
    else:
        name = nameslist.title()
        c.execute('''INSERT OR IGNORE INTO authors(name) VALUES(?)''', (name,))

    db.commit()
    """


def list_authors():
    """    :return: all the author from database    """

    c.execute("SELECT name FROM authors")
    names = c.fetchall()
    results = [x for t in names for x in t]
    results = ' '.join(results)
    return results


def find_author(name):
    """ return: Searches for author based on partial match  """

    search = "%" + name + "%"
    c.execute("SELECT name FROM authors WHERE name LIKE ?", (search,))
    matches = c.fetchall()

    for i in matches:
        print(i)

    return matches


def get_author_id(author_name):
    """     :return: the ID of a given author    """

    c.execute('''SELECT ID FROM authors WHERE name = ? ''', (author_name,))

    author_id = c.fetchall()[0]
    author_id = author_id[0]

    return author_id


def get_author(author_id):
    """ return: author from ID    """

    c.execute('''SELECT name FROM authors WHERE ID = ?''', (author_id,))

    author_name = c.fetchall()[0]
    author_name = author_name[0]

    return author_name


def update_author(author_correction):
    author_correction = author_correction.title()
    author_id = get_author_id()

    c.execute('''UPDATE authors SET name = ? WHERE ID =?''', (author_correction, author_id))
    db.commit()


def delete_author(author_name):
    author_name = author_name.title()
    author_id = get_author_id(author_name)

    c.execute('''DELETE FROM authors WHERE ID = ?''', (author_id,))
    print("Deleting item: ", author_id)

    db.commit()

# PUBLISHER CRUD FUNCTIONS

def add_publisher(publisher_entry):
    """ Adds publisher to SQL database"""

    publisher = publisher_entry.title()

    c.execute('''INSERT OR IGNORE INTO publishers(publisher) VALUES(?)''', (publisher,))
    db.commit()


def list_publishers():
    """ Returns all the publisher from database"""

    c.execute('''SELECT publisher FROM publishers ORDER BY publisher''')
    results = [i[0] for i in c.fetchall()]
    return results

def get_publisher_id(publisher_entry):
    """ Returns the ID (PK) of a given publisher"""
    publisher = publisher_entry.title()

    c.execute('''SELECT ID FROM publishers WHERE publisher = ? ''', (publisher,))
    publisherID = c.fetchall()[0]
    publisherID = publisherID[0]

    return publisherID


def get_publisher(publisherID):
    """ Returns publisher from ID"""

    c.execute('''SELECT publisher FROM publishers WHERE ID = ?''', (publisherID,))
    return c.fetchall()[0]


def update_publisher(publisher_entry, publisher_correction_entry):
    publisher = publisher_entry.title()
    publisher_correction = publisher_correction_entry.title()

    publisherID = get_publisher_id(publisher)

    c.execute('''UPDATE publishers SET publisher = ? WHERE ID =?''', (publisher_correction, publisherID))
    db.commit()


def delete_publisher(publisher_entry):
    publisher = publisher_entry.title()
    publisherID = get_publisher_id(publisher)
    c.execute('''DELETE FROM publishers WHERE ID = ?''', (publisherID,))

    db.commit()


# RESOURCE medium CRUD
def add_resource_medium(medium_entry):
    medium = medium_entry.title()
    c.execute("INSERT OR IGNORE INTO resource_medium(medium) VALUES(?)", (medium,))
    db.commit()


def list_resource_medium():
    """ return: all the resource types from database    """

    c.execute('''SELECT medium FROM resource_medium ORDER BY medium''')
    results = [i[0] for i in c.fetchall()]
    return results


def get_resource_medium_id(medium_entry):
    """ Returns the ID (PK) of a given resource medium"""

    medium_entry = medium_entry.title()

    c.execute('''SELECT ID FROM resource_medium WHERE medium = ? ''', (medium_entry,))
    return c.fetchone()[0]


def get_resource_type(resource_medium_id):
    """ Returns resource medium from ID"""

    c.execute('''SELECT medium FROM resource_medium WHERE ID = ?''', (resource_medium_id,))

    return c.fetchall()[0]

def update_resource_medium(resource_medium_entry, media_correction_entry):
    resource_medium = resource_medium_entry.title()
    media_correction = media_correction_entry.title()

    resource_medium_id = get_resource_medium_id(resource_medium)

    c.execute('''UPDATE resource_medium SET medium = ? WHERE ID =?''', (media_correction, resource_medium_id))
    db.commit()


def delete_resource_medium(resource_medium_entry):
    resource_medium = resource_medium_entry.title()
    resource_medium_id = get_resource_medium_id(resource_medium)
    c.execute('''DELETE FROM resource_medium WHERE ID = ?''', (resource_medium_id,))
    db.commit()


# subject CRUD FUNCTIONS

def add_subject(subject_entry):
    subject = subject_entry.title()
    c.execute('''INSERT OR IGNORE INTO subjects(subject) VALUES(?)''', (subject,))
    db.commit()


def list_subjects():
    c.execute('''SELECT subject FROM subjects''')

    subjects = c.fetchall()
    results = [x for t in subjects for x in t]
    results = ' '.join(results)

    return results




def get_subject_id(subject):
    subject = subject.title()
    c.execute('''SELECT ID FROM subjects WHERE subject = ? ''', (subject,))
    return c.fetchone()[0]


def get_subject(subject_id):
    c.execute('''SELECT subject FROM subjects WHERE ID = ?''', (subject_id,))
    return c.fetchall()[0]


def update_subject(subject):
    subject = subject.title()
    subject_id = get_subject_id(subject)
    c.execute('''UPDATE subjects SET subject = ? WHERE ID =?''', (subject, subject_id))
    db.commit()


def delete_subject(subject_id):
    c.execute('''DELETE FROM subjects WHERE ID = ?''', (subject_id,))
    db.commit()


# RESOURCE
def get_text_id(text_title):
    #resource_title = resource_title_entry.title()
    c.execute('''SELECT ID FROM texts WHERE title = ?''', (text_title,))
    return c.fetchone()[0]


def add_text(title, author, year, pages, level, publisher, language, subject, medium, notes):

    levelID = get_level_id(level)
    print('Level ID is ', levelID)

    add_publisher(publisher)
    publisherID = get_publisher_id(publisher)
    print('Pub ID =', publisherID)

    add_language(language)
    languageID = get_language_id(language)
    print('Lang ID = ', languageID)

    add_subject(subject)
    subjectID = get_subject_id(subject)
    print('Subject ID =', subjectID)

    add_resource_medium(medium)
    medium = medium.title()
    mediaID = get_resource_medium_id(medium)
    print('Text media ID = ', mediaID)

    title = title.title()
    print('Title = ', title)

    c.execute('''INSERT OR IGNORE INTO texts(title, year, pages, levelID, publisherID, languageID, subjectID, 
                    mediaID, notes) 
                 VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)''',
              (title, year, pages, levelID, publisherID, languageID, subjectID, mediaID, notes))

    resourceID = get_text_id(title)
    print('ResourceID = ', resourceID)

    add_author(author)
    authorID = get_author_id(author)
    print('Author ID = ', authorID)


    c.execute('''INSERT OR IGNORE INTO resource_author(resourceID, authorID, mediaID) VALUES(?,?, ?)''',
              (resourceID, authorID, mediaID))
    db.commit()


def list_text_resources():
    """ Returns all the resources from database"""

    c.execute('''SELECT texts.title, authors.name, texts.year, texts.pages, 
                publishers.publisher, languages.language, texts.notes
                FROM texts JOIN languages JOIN publishers JOIN authors JOIN resource_author
                ON texts.languageID = languages.ID
                AND texts.publisherID = publishers.ID AND authors.ID = resource_author.authorID 
                AND texts.ID = resource_author.resourceID
                ''')

    return c.fetchall()

def find_resource_by_subject(subject):
    subject = subject.title()

    c.execute('''SELECT texts.title, authors.name, texts.year, texts.pages, subjects.name,
                languages.language,  resource_medium.medium
                FROM texts JOIN languages JOIN publishers JOIN resource_medium JOIN authors
                JOIN resource_author JOIN subjects 
                ON texts.languageID = languages.ID AND texts.mediaID = resource_medium.ID 
                AND texts.publisherID = publishers.ID AND authors.ID = resource_author.authorID 
                AND texts.ID = resource_author.resourceID
                AND texts.subjectID = subjects.ID
                WHERE subjects.subject = ?''', (subject,))
    return c.fetchall()

def resources_by_language(language):
    ' Returns all the resources from database of a given language'
    
    c.execute('''SELECT DISTINCT texts.title, texts.year, languages.language
              FROM texts JOIN languages
              ON texts.languageID = languages.ID 
              WHERE texts.languageID = ?''', (language,))
    
def resources_by_type(media_type):
    c.execute('''SELECT texts.title, texts.year, texts.mediaID
                FROM texts JOIN resource_medium
                ON texts.mediaID = resource_medium.ID 
                WHERE texts.mediaID = ?''', (media_type,))


# Web doc
def get_website_id(title):
    c.execute('''SELECT ID FROM websites WHERE title = ?''', (title,))
    return c.fetchone()[0]

def add_website(title, author, creation_date, subject, website_name, url, access_date, notes, medium):

    add_author(author)

    add_publisher(website_name)
    website_nameID = get_publisher_id(website_name)
    print('Website name ID =', website_nameID)

    add_resource_medium(medium)
    medium = medium.title()
    mediaID = get_resource_medium_id(medium)
    print('Website type = ', mediaID)

    add_subject(subject)
    subjectID = get_subject_id(subject)
    print('Subject ID =', subjectID)


    c.execute('''INSERT OR IGNORE INTO websites (title, creation_date, website_nameID, url, access_date, 
                notes, mediaID, subjectID) VALUES(?,?,?,?,?,?,?,?)''',
              (title, creation_date, website_nameID, url, access_date, notes, mediaID, subjectID))
    db.commit()


    authorID = get_author_id(author)
    print('Author ID = ', authorID)

    website_id= get_website_id(title)
    print('Website ID', website_id)

    c.execute('''INSERT OR IGNORE INTO resource_author(resourceID, authorID, mediaID ) 
              VALUES(?, ?, ?)''', (website_id, authorID, mediaID ))
    db.commit()

def list_websites():
    """ Returns all the resources from database"""

    c.execute('''SELECT websites.title, authors.name, websites.creation_date, 
                publishers.publisher, websites.url
                FROM websites JOIN publishers JOIN authors JOIN resource_author
                ON websites.website_nameID = publishers.ID 
				AND authors.ID = resource_author.authorID 
                AND websites.ID = resource_author.resourceID
				AND websites.mediaID = resource_author.mediaID
                ''')




def link_website():
    pass


# audio/video
def get_audio_video_id(title):
    c.execute('SELECT ID FROM audio_video WHERE title =?', (title,))
    return c.fetchone()[0]


def add_audio_video(title, author, duration, format, year, source, comments, media, subject, publisher):
    add_author(author)

    mediaID = get_resource_medium_id(media)
    print('Audio/Video ID = ', mediaID)

    add_subject(subject)
    subjectID = get_subject_id(subject)
    print('Subject ID =', subjectID)

    add_publisher(publisher)
    publisherID = get_publisher_id(publisher)

    c.execute('''INSERT OR IGNORE INTO audio_video(title, duration_mins, format, year, location,
                comments, mediaID, subjectID, publisherID)
                VALUES (?,?,?,?,?,?,?,?,?)''', (title, duration, format, year, source, mediaID, subjectID, publisherID ))
    db.commit()

    authorID = get_author_id(author)
    print('Author ID = ', authorID)

    audio_video_id = get_audio_video_id(title)
    print('Audio/video ID', audio_video_id)

    c.execute('''INSERT OR IGNORE INTO resource_author(resourceID, authorID, mediaID ) 
                  VALUES(?, ?, ?)''', (audio_video_id, authorID, mediaID))
    db.commit()

# courses
def get_course_id(title):
    c.execute('SELECT ID FROM courses WHERE title =?', (title,))
    return c.fetchone()[0]

def add_course(title, instructor, start_date, duration, url, level, platform, media, subject):

    levelID = get_level_id(level)
    print('Level ID is ', levelID)

    mediaID = get_resource_medium_id(media)
    print('Course ID = ', mediaID)

    add_subject(subject)
    subjectID = get_subject_id(subject)
    print('Subject ID =', subjectID)

    add_publisher(platform)
    publisherID = get_publisher_id(platform)

    c.execute('''INSERT OR IGNORE INTO courses(title, start_date, duration, url, levelID, platform,
                    mediaID, subjectID)
                VALUES(?,?,?,?,?,?,?,?)''', (title, start_date, duration, url, levelID, platform, publisherID, subjectID))

    db.commit()

    courseID = get_course_id(title)

    add_author(instructor)
    authorID = get_author_id(instructor)

    c.execute('''INSERT OR IGNORE INTO resource_author(resourceID, authorID, mediaID ) 
                      VALUES(?, ?, ?)''', (courseID, authorID, mediaID))
    db.commit()


# interactive media

def get_interactive_id(title):
    c.execute('SELECT ID FROM interactive_media WHERE title =?', (title,))
    return c.fetchone()[0]

def add_interactive_media(title, creator, year, platform, version, comments, engine, medium, genre):
    add_subject(genre)
    genreID = get_subject_id(genre)

    add_publisher(engine)
    engineID = get_publisher_id(engine)

    add_resource_medium(medium)
    typeID = get_resource_medium_id(medium)

    c.execute('''INSERT INTO interactive_media(title, year, platform, version, comments, engineID,
                typeID, genreID
                VALUES(?,?,?,?,?,?,?,?)''', (title, year, platform, version, comments, engineID, typeID, genreID))
    db.commit()

    interactiveID = get_interactive_id(title)

    add_author(creator)
    authorID = get_author_id(creator)

    c.execute('''INSERT OR IGNORE INTO resource_author(resourceID, authorID, mediaID ) 
                      VALUES(?, ?, ?)''', (interactiveID, authorID, typeID))
    db.commit()




# images
def get_image_id(title):
    c.execute('SELECT ID FROM images WHERE title =?', (title,))
    return c.fetchone()[0]

def add_images(title, creator, format, date, material, dimensions, location, comments, image_type):

    add_resource_medium(image_type)
    imagetypeID = get_resource_medium_id(image_type)

    c.execute('''INSERT OR IGNORE INTO images(title, format, date, material, dimensions, location, comments,
                imagetypeID) VALUES(?,?,?,?,?,?,?,?)''', (title, format, date, material, dimensions, location, comments,
                imagetypeID))
    db.commit()

    db.commit()

    imageID = get_image_id(title)
    add_author(creator)
    authorID = get_author_id(creator)

    c.execute('''INSERT OR IGNORE INTO resource_author(resourceID, authorID, mediaID ) 
                      VALUES(?, ?, ?)''', (imageID, authorID, imagetypeID))
    db.commit()



# PROJECT Category CRUD

def add_project_category(project_category):
    """  Adds project_type to database    """
    project_category = project_category.title()

    c.execute('''INSERT OR IGNORE INTO project_category(category) VALUES(?)''', (project_category,))
    db.commit()


def list_project_category():
    """    :return: all the project categories from database    """

    c.execute('''SELECT category FROM project_category ORDER BY category''')
    results = [i[0] for i in c.fetchall()]
    return results


def get_project_categoryID(project_category):
    project_category = project_category.title()

    try:
        c.execute('''SELECT ID FROM project_category WHERE category = ? ''', (project_category,))
        project_categoryID = c.fetchone()[0]

    except TypeError:
        add_project_category(project_category)

        c.execute('''SELECT ID FROM project_category WHERE category = ? ''', (project_category,))
        project_categoryID = c.fetchone()[0]

    return project_categoryID


def get_project_category(project_categoryID):
    c.execute('''SELECT category FROM project_category WHERE ID = ?''', (project_categoryID,))

    return c.fetchall()[0]


def update_project_category(project_category, project_category_correction):

    project_categoryID = get_project_categoryID(project_category)

    c.execute('''UPDATE project_category SET category = ? WHERE ID =?''',
              (project_category_correction, project_categoryID))
    db.commit()


def delete_project_category(project_category):
    project_categoryID = get_project_categoryID(project_category)
    c.execute('''DELETE FROM project_category WHERE ID = ?''', (project_categoryID,))

    db.commit()


# Project CRUD functions

def add_project(project_name, project_category, description, date_start, date_end):

    project_categoryID = get_project_categoryID(project_category)

    c.execute(
        '''INSERT INTO projects(project_name, project_category, description, date_start, date_end ) VALUES(?,?,?,?,?)''',
        (project_name, project_categoryID, description, date_start, date_end))
    db.commit()


def get_projectID(project_name):
    """ Returns the ID of a given project """

    c.execute('''SELECT ID FROM projects WHERE project_name = ?''', (project_name,))
    results = [i[0] for i in c.fetchall()]
    return results

def find_project(project_name):
    search = "%" + project_name + "%"
    c.execute('''SELECT project_name, category, description, date_start, date_end
                FROM projects JOIN project_category 
                ON projects.project_category = project_category.ID
                WHERE project_name LIKE ?''', (search,))
    return c.fetchall()


def list_projects():
    """ :return list of projects """
    c.execute('''SELECT project_name, category, description, date_start, date_end
            FROM projects JOIN project_category 
            ON projects.project_category = project_category.ID 
            ORDER BY project_name          
            ''')
    return c.fetchall()


def get_project(projectID):
    c.execute('''SELECT project_name, category, description, date_start, date_end 
                FROM projects JOIN project_category 
                ON projects.project_category = project_category.ID 
                WHERE projects.ID = ? ''', (projectID,))
    project =  c.fetchall()
    results = [x for t in project for x in t]
    results = ','.join(results)
    return results


"""
def update_project(projectID=None, project_name=None, project_category=None, description=None, date_start=None, date_end=None):
    fields = get_project(projectID)

    if not project_name:
        project_name = fields[0]
    if not project_category:
        project_category = fields[1]
    if not description:
        description = fields[2]
    if not date_start:
        date_start = fields[3]
    if not date_end:
        date_end = fields[4]

    c.execute(''' UPDATE project SET project_name = ?, project_category = ?,  description = ?, date_start = ?, date_end = ?, 
            publisherID = ?, abstract = ?
            WHERE ID = ? ''', (project_name, project_category, description, date_start, date_end, ID))

    db.commit()
"""

def delete_project(projectID):
    c.execute(''' DELETE from projects WHERE projects.ID = ?''', (projectID,))
    db.commit()


def link_to_resources(projectID, resourceID, mediaID):
    c.execute('''INSERT OR IGNORE INTO project_references(projectID, resourceID, mediaID) VALUES(?,?, ?)''',
              (projectID, resourceID, mediaID))

    db.commit()



"""
def init_db(filename=None):
    global db, c
    if not filename:
        filename = 'small_data.db'
    try:
        db = sql.connect(filename)
        c = db.cursor()
        #c.execute('PRAGMA Foreign_Keys=True')
    except:
        print('Error connecting to', filename)
        c = None
        raise

def close_db():
    try:
        c.close()
        db.commit()
        db.close()
    except:
        print('Problem closing database')
        raise

if __name__ == '__main__':
    init_db()
"""
