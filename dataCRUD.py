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

    return c.fetchone()[0]

def list_levels():

    c.execute('''SELECT level FROM levels''')
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

    return c.fetchone()[0]


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

    return c.fetchone()[0]


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
    # medium = medium_entry.title()
    c.execute("INSERT OR IGNORE INTO resource_medium(medium) VALUES(?)", (medium_entry,))
    db.commit()


def list_resource_medium():
    """ return: all the resource types from database    """

    c.execute('''SELECT medium FROM resource_medium ORDER BY medium''')
    results = [i[0] for i in c.fetchall()]
    return results


def get_resource_medium_id(medium_entry):
    """ Returns the ID (PK) of a given resource medium"""
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


# Resource author media functions

def add_resource_author(resourceID, authorID, mediaID):
    c.execute('''INSERT OR IGNORE INTO resource_author(resourceID, authorID, mediaID) VALUES(?,?, ?)''',
              (resourceID, authorID, mediaID))
    db.commit()

def delete_resource_author(resource_id, author, media):

    author_id = get_author_id(author)
    media_id = get_resource_medium_id(media)


    c.execute("""DELETE FROM resource_author WHERE resourceID = ?
                 AND authorID = ? AND mediaID = ?""",
              (resource_id, author_id, media_id))
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


# TEXTS
def get_text_id(text_title):
    #resource_title = resource_title_entry.title()
    c.execute('''SELECT ID FROM texts WHERE title = ?''', (text_title,))
    return c.fetchone()[0]


def add_text(title, author, year, pages, level, publisher, language, subject, medium, notes):

    levelID = get_level_id(level)

    add_publisher(publisher)
    publisherID = get_publisher_id(publisher)

    add_language(language)
    languageID = get_language_id(language)

    add_subject(subject)
    subjectID = get_subject_id(subject)

    mediaID = get_resource_medium_id(medium)

    c.execute('''INSERT OR IGNORE INTO texts(title, year, pages, levelID, publisherID, languageID, subjectID, 
                    mediaID, notes) 
                 VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)''',
              (title, year, pages, levelID, publisherID, languageID, subjectID, mediaID, notes))

    db.commit()

    resourceID = get_text_id(title)
    print('ResourceID = ', resourceID)

    add_author(author)
    db.commit()

    authorID = get_author_id(author)
    print('Author ID = ', authorID)

    add_resource_author(resourceID, authorID, mediaID)


def update_text(textID, title, year, pages, level, publisher, language, subject, medium, notes):
    levelID = get_level_id(level)
    # print('Level ID is ', levelID)

    add_publisher(publisher)
    publisherID = get_publisher_id(publisher)
    # print('Pub ID =', publisherID)

    add_language(language)
    languageID = get_language_id(language)
    # print('Lang ID = ', languageID)

    add_subject(subject)
    subjectID = get_subject_id(subject)
    # print('Subject ID =', subjectID)

    mediaID = get_resource_medium_id(medium)
    # print('Text media ID = ', mediaID)

    c.execute('''UPDATE texts
                            SET title = ?, year= ?, pages = ?,  levelID = ?, publisherID = ?, 
                                languageID = ?, subjectID = ?, mediaID = ?,notes = ? 
                     WHERE ID  = ?''',
                  (title, year, pages, levelID, publisherID, languageID, subjectID, mediaID, notes, textID))
    db.commit()

def list_text_resources():
    """ Returns all the resources from database"""

    c.execute('''SELECT texts.title, authors.name, texts.year, texts.pages, 
                publishers.publisher, languages.language, texts.notes
                FROM texts JOIN languages JOIN publishers JOIN authors JOIN resource_author
                ON texts.languageID = languages.ID
                AND texts.publisherID = publishers.ID AND authors.ID = resource_author.authorID 
                AND texts.ID = resource_author.resourceID
                AND texts.mediaID = resource_author.mediaID
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
    
    c.execute('''SELECT texts.title, texts.year, languages.language
              FROM texts JOIN languages
              ON texts.languageID = languages.ID 
              WHERE language = ?''', (language,))
    return c. fetchall()
    
def resources_by_type(media_type):
    c.execute('''SELECT texts.title, texts.year, texts.mediaID
                FROM texts JOIN resource_medium
                ON texts.mediaID = resource_medium.ID 
                WHERE texts.mediaID = ?''', (media_type,))
    return c.fetchall()

def delete_text(resource_id, author, media):
    c.execute('''DELETE FROM texts WHERE texts.ID = ?''', (resource_id,))

    delete_resource_author(resource_id, author, media)
    db.commit()

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

def get_website_mediaID(resourceID):
    c.execute('''SELECT mediaID FROM websites WHERE websites.ID = ?''', (resourceID,))
    return c.fetchone()[0]

def list_websites():
    """ Returns all the resources from database"""

    c.execute('''SELECT websites.title, authors.name, publishers.publisher, 
                websites.creation_date, websites.access_date, subjects.subject
                FROM websites JOIN publishers JOIN authors JOIN resource_author JOIN subjects
                ON websites.website_nameID = publishers.ID 
				AND authors.ID = resource_author.authorID 
                AND websites.ID = resource_author.resourceID
				AND websites.mediaID = resource_author.mediaID
				AND websites.subjectID = subjects.ID
                ''')
    return c.fetchall()

def link_website():
    pass

def delete_website(resource_id, author, media):
    c.execute('''DELETE FROM websites WHERE websites.ID = ?''', (resource_id,))

    delete_resource_author(resource_id, author, media)
    db.commit()

# audio/video
def get_audio_video_id(title):
    c.execute('SELECT ID FROM audio_video WHERE title =?', (title,))
    return c.fetchone()[0]

def add_audio_video(title, author, duration,  year, program, url, language, media, subject, publisher):
    add_author(author)

    add_language(language)
    languageID = get_language_id(language)
    print('Language ID is ', languageID)

    add_resource_medium(media)
    media = media.title()
    mediaID = get_resource_medium_id(media)
    print('Audio/Video ID = ', mediaID)

    add_subject(subject)
    subjectID = get_subject_id(subject)
    print('Subject ID =', subjectID)

    add_publisher(publisher)
    publisherID = get_publisher_id(publisher)

    c.execute('''INSERT OR IGNORE INTO audio_video(title, duration_mins, year, 
                program, url, languageID, mediaID, subjectID, publisherID)
                VALUES (?,?,?,?,?,?,?,?,?)''',
              (title, duration, year, program, url, languageID, mediaID, subjectID, publisherID ))
    db.commit()

    authorID = get_author_id(author)
    print('Author ID = ', authorID)

    audio_video_id = get_audio_video_id(title)
    print('Audio/video ID', audio_video_id)

    c.execute('''INSERT OR IGNORE INTO resource_author(resourceID, authorID, mediaID ) 
                  VALUES(?, ?, ?)''', (audio_video_id, authorID, mediaID))
    db.commit()

def get_av_mediaID(resourceID):
    c.execute('''SELECT mediaID FROM audio_video WHERE audio_video.ID = ?''', (resourceID,))
    return c.fetchone()[0]

def get_av_info(resourceID):
    c.execute('''SELECT title, authors.name, duration_mins, subjects.subject, publishers.publisher,
                    year, program, url, languages.language, resource_medium.medium                    
                FROM audio_video JOIN authors JOIN languages JOIN resource_medium 
                JOIN resource_author JOIN subjects JOIN publishers
                ON audio_video.ID = resource_author.resourceID 
                AND audio_video.publisherID = publishers.ID
                AND audio_video.mediaID = resource_medium.ID
                AND audio_video.mediaID = resource_author.mediaID
                AND authors.ID = resource_author.authorID
                AND audio_video.subjectID = subjects.ID
                AND authors.ID = resource_author.authorID
                AND resource_author.mediaID = resource_medium.ID
                AND audio_video.languageID = languages.ID 
                WHERE audio_video.ID = ?''', (resourceID,))
    return c.fetchone()

def list_av():
    c.execute('''SELECT audio_video.title, authors.name, audio_video.year, resource_medium.medium, 
	                audio_video.program, languages.language
                FROM audio_video JOIN publishers JOIN authors JOIN resource_author 
                JOIN resource_medium JOIN languages
                ON audio_video.publisherID = publishers.ID 
                AND authors.ID = resource_author.authorID 
                AND audio_video.ID = resource_author.resourceID
                AND audio_video.mediaID = resource_author.mediaID
                AND audio_video.mediaID = resource_medium.ID
                AND audio_video.languageID = languages.ID''')
    return c.fetchall()

def update_av(av_id, title, duration,  year, program, url, language, media, subject, publisher):

    language_id = get_language_id(language)
    add_subject(subject)
    subject_id = get_subject_id(subject)

    add_publisher(publisher)
    publisher_id = get_publisher_id(publisher)

    c.execute('''UPDATE audio_video SET title = ?, duration_mins = ?,  year = ?, program  = ?,
                    url = ?, languageID = ?, mediaID = ?, subjectID = ?, publisherID = ?
                WHERE ID = ?''',
              (title, duration, year, program, url, language_id, media, subject_id, publisher_id, av_id))
    db.commit()

def delete_av(resource_id, author, media):

    c.execute('''DELETE FROM audio_video  WHERE audio_video.ID = ?''', (resource_id,))

    delete_resource_author(resource_id, author, media)

    db.commit()

# courses
def get_course_id(title):
    c.execute('SELECT ID FROM courses WHERE title =?', (title,))
    return c.fetchone()[0]

def add_course(title, instructor, start_date, duration, url, comments, level, platform, media, subject):

    levelID = get_level_id(level)
    print('Level ID is ', levelID)

    # add_resource_medium(media)
    # media = media.title()
    mediaID = get_resource_medium_id(media)
    print('Course ID = ', mediaID)

    add_subject(subject)
    subjectID = get_subject_id(subject)
    print('Subject ID =', subjectID)

    add_publisher(platform)
    publisherID = get_publisher_id(platform)
    print('Platform ID', publisherID)

    c.execute('''INSERT OR IGNORE INTO courses(title, start_date, duration_hours, url, comments, levelID, platformID,
                    mediaID, subjectID)
                VALUES(?,?,?,?,?,?,?,?, ?)''', (title, start_date, duration, url, comments,
                                             levelID, publisherID, mediaID, subjectID))

    db.commit()

    courseID = get_course_id(title)

    add_author(instructor)
    authorID = get_author_id(instructor)

    add_resource_author(courseID, authorID, mediaID)

    # c.execute('''INSERT OR IGNORE INTO resource_author(resourceID, authorID, mediaID )
    #                   VALUES(?, ?, ?)''', (courseID, authorID, mediaID))
    db.commit()

def get_course_mediaID(resourceID):
    c.execute('''SELECT mediaID FROM courses WHERE courses.ID = ?''', (resourceID,))
    return c.fetchone()[0]

def get_course_info(course_id):
    c.execute('''SELECT courses.title, authors.name, courses.start_date, subjects.subject,
                    publishers.publisher, courses.url, courses.duration_hours, courses.comments,
                    resource_medium.medium, levels.level
                FROM courses JOIN authors JOIN publishers JOIN resource_author 
                JOIN resource_medium JOIN levels JOIN subjects
                ON courses.ID = resource_author.resourceID 
                AND courses.platformID = publishers.ID
                AND courses.mediaID = resource_medium.ID
                AND courses.mediaID = resource_author.mediaID
                AND authors.ID = resource_author.authorID
                AND courses.subjectID = subjects.ID
                AND authors.ID = resource_author.authorID
                AND resource_author.mediaID = resource_medium.ID
                AND courses.levelID = levels.ID 
                WHERE courses.ID = ?''', (course_id,))
    return c.fetchone()

def list_courses():
    c.execute('''SELECT courses.title, authors.name, courses.start_date, courses.duration_hours, 
                    publishers.publisher, courses.comments
                FROM courses JOIN publishers JOIN authors JOIN resource_author JOIN resource_medium
                ON courses.platformID = publishers.ID 
                AND authors.ID = resource_author.authorID 
                AND courses.ID = resource_author.resourceID
                AND courses.mediaID = resource_author.mediaID
                AND courses.mediaID = resource_medium.ID''')
    return c.fetchall()

def update_course(courseID = None, title= None, start_date= None, duration= None, url=None,
                  comments= None, level= None, platform= None, media = None, subject= None):


    add_publisher(platform)
    platform_id = get_publisher_id(platform)

    add_level(level)
    level_id = get_level_id(level)

    add_subject(subject)
    subject_id = get_subject_id(subject)

    media_id = get_resource_medium_id(media)

    c.execute('''UPDATE courses SET title = ?, start_date= ?, duration_hours = ?, url = ?, 
                    comments = ?, levelID = ?, platformID = ?, mediaID = ?, subjectID = ? 
                  WHERE ID = ?''',(title, start_date, duration, url, comments, level_id,
                                   platform_id, media_id, subject_id, courseID))


    db.commit()

def delete_course(resource_id, author, media):
    c.execute('''DELETE FROM courses WHERE courses.ID = ?''', (resource_id,))

    delete_resource_author(resource_id, author, media)
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
                typeID, genreID)
                VALUES(?,?,?,?,?,?,?,?)''',
              (title, year, platform, version, comments, engineID, typeID, genreID))
    db.commit()

    interactiveID = get_interactive_id(title)

    add_author(creator)
    authorID = get_author_id(creator)

    c.execute('''INSERT OR IGNORE INTO resource_author(resourceID, authorID, mediaID ) 
                      VALUES(?, ?, ?)''', (interactiveID, authorID, typeID))
    db.commit()


def get_media_interactive_mediaID(resourceID):
    c.execute('''SELECT typeID FROM interactive_media WHERE interactive_media.ID = ?''', (resourceID,))
    return c.fetchone()[0]

def list_interactive():
    c.execute('''SELECT interactive_media.title, authors.name, interactive_media.year, 
                    publishers.publisher, resource_medium.medium, interactive_media.comments
                FROM interactive_media JOIN publishers JOIN authors JOIN resource_author
                JOIN resource_medium
                ON interactive_media.engineID = publishers.ID 
                AND authors.ID = resource_author.authorID 
                AND interactive_media.ID = resource_author.resourceID
                AND interactive_media.typeID = resource_medium.ID
                AND interactive_media.typeID = resource_author.mediaID
                ''')
    return c.fetchall()

def get_interactive_info(resourceID):
    c.execute('''SELECT interactive_media.title, authors.name, interactive_media.year, subjects.subject,
                    interactive_media.platform, publishers.publisher, interactive_media.version,
                    interactive_media.comments, resource_medium.medium
                    
                FROM interactive_media JOIN authors JOIN resource_medium 
                JOIN resource_author JOIN subjects JOIN publishers
                ON interactive_media.ID = resource_author.resourceID 
                AND interactive_media.engineID = publishers.ID
                AND interactive_media.typeID = resource_medium.ID
                AND interactive_media.typeID = resource_author.mediaID
                AND authors.ID = resource_author.authorID
                AND interactive_media.genreID = subjects.ID
                AND authors.ID = resource_author.authorID
                AND resource_author.mediaID = resource_medium.ID
                WHERE interactive_media.ID = ?''', (resourceID,))
    return c.fetchone()


def update_interactive(interactiveID, title, year, platform, version, comments, engine, media_id, genre):

    genre_id = get_subject_id(genre)
    print("Genre ID= ", genre_id)

    add_publisher(engine)

    engine_id = get_publisher_id(engine)
    print('EngineID = ', engine_id)

    c.execute('''UPDATE interactive_media SET title = ?, year = ?, platform = ?, version = ?, comments = ?, 
                    engineID = ?, typeID = ?, genreID = ?  WHERE interactive_media.ID =?''',
              (title, year, platform, version, comments, engine_id, media_id, genre_id, interactiveID))

    db.commit()

def delete_interactive(resource_id, author, media):
    c.execute('''DELETE FROM interactive_media WHERE interactive_media.ID = ?''', (resource_id,))

    delete_resource_author(resource_id, author, media)
    db.commit()

# images
def get_image_id(title):
    c.execute('SELECT ID FROM images WHERE title =?', (title,))
    return c.fetchone()[0]

def add_images(title, creator, date, copywrite, website, dimensions, url, comments, image_type):

    add_resource_medium(image_type)
    imagetypeID = get_resource_medium_id(image_type)

    c.execute('''INSERT OR IGNORE INTO images(title, date, copywrite, website_name, dimensions, url, comments,
                imagetypeID) VALUES(?,?,?,?,?,?,?,?)''',
              (title, date, copywrite, website, dimensions, url, comments,imagetypeID))
    db.commit()

    imageID = get_image_id(title)
    add_author(creator)
    authorID = get_author_id(creator)

    c.execute('''INSERT OR IGNORE INTO resource_author(resourceID, authorID, mediaID ) 
                      VALUES(?, ?, ?)''', (imageID, authorID, imagetypeID))
    db.commit()

def get_image_mediaID(resourceID):
    c.execute('''SELECT imagetypeID FROM images WHERE images.ID = ?''', (resourceID,))
    return c.fetchone()[0]

def list_images():
    c.execute('''SELECT images.title, authors.name, resource_medium.medium, images.dimensions, images.date, 
                        images.comments
                    FROM images JOIN  authors JOIN resource_author JOIN resource_medium
                    ON authors.ID = resource_author.authorID 
                    AND images.ID = resource_author.resourceID
                    AND images.imagetypeID = resource_author.mediaID
                    AND images.imagetypeID = resource_medium.ID''')
    return c.fetchall()

def get_image_info(resource_id):
    c.execute('''SELECT title, authors.name, date, copywrite, dimensions, website_name, url, 
                    comments, resource_medium.medium 
                FROM images JOIN authors JOIN resource_author JOIN resource_medium
                ON images.ID = resource_author.resourceID 
                AND authors.ID = resource_author.authorID
                AND images.imagetypeID = resource_medium.ID
                AND images.imagetypeID = resource_author.mediaID
                WHERE images.ID = ?''', (resource_id,))
    return c.fetchone()

def update_image(resource_id, title, date, copywrite, website, dimensions, url, comments, image_type):
    imagetypeID = get_resource_medium_id(image_type)

    c.execute('''UPDATE images SET title = ?, date  = ?, copywrite = ?, website_name = ?, dimensions = ?, 
                    url = ?, comments = ?, imagetypeID = ? WHERE images.ID  = ?''',
              (title, date, copywrite, website, dimensions, url, comments, imagetypeID, resource_id))
    db.commit()

def delete_image(resource_id, author, media):
    c.execute('''DELETE FROM images WHERE images.ID = ?''', (resource_id,))

    delete_resource_author(resource_id, author, media)
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
    return c.fetchone()

def list_projects():
    """ :return list of projects """
    c.execute('''SELECT project_name, category, description, date_start, date_end
            FROM projects JOIN project_category 
            ON projects.project_category = project_category.ID 
            ORDER BY projects.project_name          
            ''')
    return c.fetchall()


def get_project(projectID):

    c.execute('''SELECT project_name, category, description, date_start, date_end
                FROM projects JOIN project_category
                ON projects.project_category = project_category.ID
                WHERE projects.ID = ? ''', (projectID,))
    project =  c.fetchall()
    results = [x for t in project for x in t]
    return results


def update_project(projectID=None, project_name=None, project_category=None, description=None,
                   date_start=None, date_end=None):

    project_categoryID = get_project_categoryID(project_category)

    c.execute(''' UPDATE projects SET project_name = ?, project_category = ?,  description = ?, 
                    date_start = ?, date_end = ?
                WHERE ID = ? ''', (project_name, project_categoryID, description, date_start, date_end, projectID,))

    db.commit()


def delete_project(projectID):
    c.execute(''' DELETE from projects WHERE projects.ID = ?''', (projectID,))
    db.commit()


def link_to_resources(projectID, resourceID, mediaID):
    c.execute('''INSERT OR IGNORE INTO project_references(projectID, resourceID, mediaID) VALUES(?,?, ?)''',
              (projectID, resourceID, mediaID))

    db.commit()


# SEARCHES
def find_project(project_name):
 
    
    search = "%" + project_name + "%"
    c.execute('''SELECT project_name, category, description, date_start, date_end
                FROM projects JOIN project_category 
                ON projects.project_category = project_category.ID
                WHERE project_name LIKE ? OR description LIKE ?''', (search, search))
    return c.fetchall()

# RESOURCES

def find_texts(search_term):
    search_term =  "%" + search_term + "%"
    c.execute('''SELECT texts.title, authors.name, texts.year, texts.pages, languages.language, texts.notes
                FROM texts JOIN languages JOIN resource_medium JOIN authors
                JOIN resource_author JOIN subjects 
                ON texts.mediaID = resource_medium.ID
                AND authors.ID = resource_author.authorID
                AND texts.ID = resource_author.resourceID
                AND texts.mediaID = resource_author.mediaID
                AND texts.subjectID = subjects.ID
                AND texts.languageID = languages.ID
                WHERE texts.title LIKE ?
                OR subjects.subject LIKE ? 
                OR authors.name LIKE ? 
                OR texts.notes LIKE ?''',
              (search_term, search_term, search_term, search_term))

    # c.execute('''
    # ''')

    return c.fetchall()

def find_courses(search_term):
    search_term = "%" + search_term + "%"

    c.execute('''SELECT courses.title, authors.name, courses.start_date, courses.duration_hours, 
                    publishers.publisher, subjects.subject
                FROM courses JOIN  resource_medium JOIN authors JOIN resource_author JOIN subjects JOIN publishers
                ON courses.mediaID = resource_medium.ID 
                AND authors.ID = resource_author.authorID 
                AND courses.ID = resource_author.resourceID
                AND courses.mediaID = resource_author.mediaID
                AND courses.subjectID = subjects.ID
                AND courses.platformID = publishers.ID
                WHERE courses.title LIKE ?
                OR subjects.subject LIKE ?
                OR courses.comments LIKE ?''',
              (search_term, search_term, search_term))

    return c.fetchall()


def find_av(search_term):
    search_term = "%" + search_term + "%"
    # RESULTS WANTED: 'Title', 'Artist', 'Year', 'Type', 'Program' 'Language'

    c.execute('''SELECT audio_video.title, authors.name, audio_video.year, resource_medium.medium, 
                        audio_video.program, languages.language
                    FROM audio_video JOIN  resource_medium JOIN authors 
                    JOIN resource_author JOIN publishers JOIN languages
                    ON audio_video.mediaID = resource_medium.ID 
                    AND authors.ID = resource_author.authorID 
                    AND audio_video.ID = resource_author.resourceID
                    AND audio_video.mediaID = resource_author.mediaID
                    AND audio_video.publisherID = publishers.ID
                    AND audio_video.languageID = languages.ID
                    WHERE audio_video.title LIKE ?
                    OR authors.name LIKE ?''',
              (search_term, search_term))

    return c.fetchall()

def find_interactive(search_term):
    # Wanted 'Title', 'Creator', 'Genre', 'Engine', 'Type', 'Comments'
    search_term = "%" + search_term + "%"

    c.execute('''SELECT interactive_media.title, authors.name, subjects.subject,
                        publishers.publisher, resource_medium.medium, 
                        interactive_media.comments
                        FROM interactive_media JOIN resource_medium JOIN authors 
                        JOIN resource_author JOIN publishers JOIN subjects
                        ON interactive_media.typeID = resource_medium.ID 
                        AND authors.ID = resource_author.authorID 
                        AND interactive_media.ID = resource_author.resourceID
                        AND interactive_media.typeID = resource_author.mediaID
                        AND interactive_media.engineID = publishers.ID
                        AND interactive_media.genreID = subjects.ID
                        WHERE interactive_media.title LIKE ?
                        OR authors.name LIKE ?
                        OR subjects.subject LIKE ?
                        OR interactive_media.comments LIKE ?
                        OR publishers.publisher LIKE ? ''',
              (search_term, search_term, search_term, search_term, search_term))

    return c.fetchall()


def find_images(search_term):
    #'Title', 'Creator', 'Type', 'Dimensions', 'Date', 'Comments'
    search_term = "%" + search_term + "%"
    c.execute('''SELECT images.title, authors.name, resource_medium.medium,
                        images.dimensions, images.date, images.comments
                    FROM images JOIN resource_medium JOIN authors JOIN resource_author
                    ON images.imagetypeID = resource_medium.ID 
                    AND authors.ID = resource_author.authorID 
                    AND images.ID = resource_author.resourceID
                    AND images.imagetypeID = resource_author.mediaID
                    WHERE images.title LIKE ?
                    OR authors.name LIKE ? 
                    OR resource_medium.medium LIKE ?
                    OR images.comments LIKE ?''',
              (search_term, search_term, search_term, search_term))
    return c.fetchall()

def find_web(search_term):
    # RESULTS DESIRED 'Title', 'Author', 'Website', 'Date', 'Access date', 'URL'
    search_term = "%" + search_term + "%"
    c.execute('''SELECT websites.title, authors.name, publishers.publisher, websites.creation_date,
                            websites.access_date, subjects.subject
                    FROM websites JOIN resource_medium JOIN authors JOIN resource_author 
                    JOIN publishers JOIN subjects
                    ON websites.website_nameID = publishers.ID
                    AND websites.mediaID = resource_medium.ID 
                    AND authors.ID = resource_author.authorID 
                    AND websites.ID = resource_author.resourceID
                    AND websites.mediaID = resource_author.mediaID
                    AND websites.subjectID = subjects.ID
                    WHERE websites.title LIKE ?
                    OR authors.name LIKE ? 
                    OR publishers.publisher LIKE ? 
                    OR websites.notes LIKE ?''',
              (search_term, search_term, search_term, search_term))

    return c.fetchall()

# Retrieve item
def get_text(textID):
    c.execute('''SELECT texts.title, authors.name, texts.year, texts.pages, languages.language, texts.notes
                FROM texts JOIN languages JOIN resource_medium JOIN authors
                JOIN resource_author JOIN subjects 
                ON texts.mediaID = resource_medium.ID
                AND texts.languageID =  languages.ID
                AND authors.ID = resource_author.authorID
                AND texts.ID = resource_author.resourceID
                AND texts.mediaID = resource_author.mediaID
                AND texts.subjectID = subjects.ID
                WHERE texts.ID = ?''',(textID,))

    return c.fetchall()

def get_full_text(textID):
    c.execute('''SELECT texts.title, authors.name,  texts.year, texts.pages, 
                    levels.level, publishers.publisher, languages.language, subjects.subject, 
                    resource_medium.medium, texts.notes

                FROM texts JOIN levels JOIN publishers JOIN languages JOIN authors
                JOIN subjects JOIN resource_medium JOIN resource_author

                ON texts.mediaID = resource_medium.ID
                AND texts.levelID = levels.ID
                AND texts.publisherID = publishers.ID
                AND texts.languageID = languages.ID
                AND texts.subjectID = subjects.ID
                AND texts.ID = resource_author.resourceID
                AND texts.mediaID = resource_author.mediaID
                AND authors.ID = resource_author.authorID
                WHERE texts.ID = ?''',(textID,))

    return c.fetchall()

def get_course(courseID):
    c.execute('''SELECT courses.title, authors.name, courses.start_date, courses.duration_hours, 
                    publishers.publisher, subjects.subject
                FROM courses JOIN  resource_medium JOIN authors JOIN resource_author JOIN subjects JOIN publishers
                ON courses.mediaID = resource_medium.ID 
                AND authors.ID = resource_author.authorID 
                AND courses.ID = resource_author.resourceID
                AND courses.mediaID = resource_author.mediaID
                AND courses.subjectID = subjects.ID
                AND courses.platformID = publishers.ID
                WHERE courses.ID = ?''',(courseID,))

    return c.fetchall()


def get_av(avID):
    c.execute('''SELECT audio_video.title, authors.name, audio_video.year, resource_medium.medium, 
                        audio_video.program, languages.language
                    FROM audio_video JOIN  resource_medium JOIN authors 
                    JOIN resource_author JOIN publishers JOIN languages
                    ON audio_video.mediaID = resource_medium.ID 
                    AND authors.ID = resource_author.authorID 
                    AND audio_video.ID = resource_author.resourceID
                    AND audio_video.mediaID = resource_author.mediaID
                    AND audio_video.publisherID = publishers.ID
                    AND audio_video.languageID = languages.ID
                    WHERE audio_video.ID = ?''', (avID,))

    return c.fetchall()

def get_interactive(interactiveID):
    c.execute('''SELECT interactive_media.title, authors.name, subjects.subject,
                        publishers.publisher, resource_medium.medium, 
                        interactive_media.comments
                        FROM interactive_media JOIN resource_medium JOIN authors 
                        JOIN resource_author JOIN publishers JOIN subjects
                        ON interactive_media.typeID = resource_medium.ID 
                        AND authors.ID = resource_author.authorID 
                        AND interactive_media.ID = resource_author.resourceID
                        AND interactive_media.typeID = resource_author.mediaID
                        AND interactive_media.engineID = publishers.ID
                        AND interactive_media.genreID = subjects.ID
                        WHERE interactive_media.ID = ?''', (interactiveID,))

    return c.fetchall()


def get_image(imageID):
    c.execute('''SELECT images.title, authors.name, resource_medium.medium,
                        images.dimensions, images.date, images.comments
                    FROM images JOIN resource_medium JOIN authors JOIN resource_author
                    ON images.imagetypeID = resource_medium.ID 
                    AND authors.ID = resource_author.authorID 
                    AND images.ID = resource_author.resourceID
                    AND images.imagetypeID = resource_author.mediaID
                    WHERE images.ID = ?''', (imageID,))
    return c.fetchall()

def get_website(websiteID):
# DOESNT GET MEDIA MUST CHANGE
    c.execute('''SELECT websites.title, authors.name, websites.creation_date, subjects.subject, 
                publishers.publisher, websites.url, websites.access_date, websites.notes,  resource_medium.medium
                    FROM websites JOIN resource_medium JOIN authors JOIN resource_author 
                    JOIN publishers JOIN subjects
                    ON websites.website_nameID = publishers.ID
                    AND websites.mediaID = resource_medium.ID 
                    AND authors.ID = resource_author.authorID 
                    AND websites.ID = resource_author.resourceID
                    AND websites.mediaID = resource_author.mediaID
                    AND websites.subjectID = subjects.ID
                    WHERE websites.ID = ?''', (websiteID,))
    return c.fetchone()

def update_media(websiteID = None, title=None, author=None, creation_date=None, subject=None, website_name=None,
                 url=None, access_date=None,notes=None, medium=None):

    add_subject(subject)
    subjectID = get_subject_id(subject)
    add_publisher(website_name)
    website_nameID = get_publisher_id(website_name)

    c.execute('''UPDATE websites SET title = ?, creation_date = ?, website_nameID = ?, url = ?,
                    access_date = ?, notes = ?, mediaID = ?, subjectID = ? 
                WHERE ID = ?''', (title, creation_date, website_nameID, url, access_date,
                                  notes, medium, subjectID, websiteID,))
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
