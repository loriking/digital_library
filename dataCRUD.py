# -*- coding: utf-8 -*-

"""
dataCRUD.py
Created on Sep 15, 2017

@author: lak
"""

import sqlite3 as sql

db = sql.connect('library_data.db')
c = db.cursor()


# Languages C.R.U.D.
def add_language(language):
    language = language.title()

    c.execute('''INSERT OR IGNORE INTO languages(language) VALUES(?)''', (language,))
    db.commit()


def list_languages():
    """    return: all the languages from database     """

    c.execute('''SELECT language FROM languages ORDER BY language''')
    languages = c.fetchall()
    results = [x for t in languages for x in t]
    results = ' '.join(results)
    return results


def get_languageID(language):
    """ return: the ID (PK) of a given language    """
    language = language.title()

    c.execute('''SELECT ID FROM languages WHERE language = ? ''', (language,))

    langID = c.fetchall()[0]
    langID = langID[0]

    return langID


def get_language(langID):
    """ :param langID: return: language from ID    """

    c.execute('''SELECT language FROM languages WHERE ID = ?''', (langID,))
    langID = c.fetchall()[0]
    language_name = langID[0]
    return language_name


def update_language(language):
    language = language.title()
    langID = get_languageID(language)
    c.execute('''UPDATE languages SET language = ? WHERE ID =?''', (language, langID))
    db.commit()


def delete_language():
    languageID = get_languageID()
    c.execute('''DELETE FROM languages WHERE ID = ?''', (languageID,))
    db.commit()

# AUTHORS
    
def add_author(author_name):
    """    Adds author to SQL database    """
    author_name = author_name.title()

    c.execute("INSERT OR IGNORE INTO authors(name) VALUES(?)", (author_name,))
    db.commit()


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


def get_authorID(author_name):
    """     :return: the ID of a given author    """
    author_name = author_name.title()

    c.execute('''SELECT ID FROM authors WHERE name = ? ''', (author_name,))

    authorID = c.fetchall()[0]
    authorID = authorID[0]

    return authorID


def get_author(authorID):
    """ return: author from ID    """

    c.execute('''SELECT name FROM authors WHERE ID = ?''', (authorID,))

    author_name = c.fetchall()[0]
    author_name = author_name[0]

    return author_name


def update_author(author_correction):
    author_correction = author_correction.title()
    authorID = get_authorID()

    c.execute('''UPDATE authors SET name = ? WHERE ID =?''', (author_correction, authorID))
    db.commit()


def delete_author(author_name):
    author_name = author_name.title()
    authorID = get_authorID(author_name)

    c.execute('''DELETE FROM authors WHERE ID = ?''', (authorID,))
    print("Deleting item: ", authorID)

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
    publishers = c.fetchall()
    results = [x for t in publishers for x in t]
    results = ' '.join(results)
    return results

def get_publisherID(publisher_entry):
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

    publisherID = get_publisherID(publisher)

    c.execute('''UPDATE publishers SET publisher = ? WHERE ID =?''', (publisher_correction, publisherID))
    db.commit()


def delete_publisher(publisher_entry):
    publisher = publisher_entry.title()
    publisherID = get_publisherID(publisher)
    c.execute('''DELETE FROM publishers WHERE ID = ?''', (publisherID,))

    db.commit()


# RESOURCE medium CRUD
def add_resource_medium(medium_entry):
    medium = medium_entry.lower()
    c.execute("INSERT OR IGNORE INTO resource_medium(medium) VALUES(?)", (medium,))
    db.commit()


def list_resource_medium():
    """ return: all the resource types from database    """

    c.execute('''SELECT medium FROM resource_medium ORDER BY medium''')
    media = c.fetchall()
    results = [x for t in media for x in t]
    results = ' '.join(results)
    return results


def get_resource_mediumID(medium_entry):
    """ Returns the ID (PK) of a given resource medium"""

    medium = medium_entry.lower()

    c.execute('''SELECT ID FROM resource_medium WHERE medium = ? ''', (medium,))
    return c.fetchone()[0]


def get_resource_type(resource_mediumID):
    """ Returns resource medium from ID"""

    c.execute('''SELECT medium FROM resource_medium WHERE ID = ?''', (resource_mediumID,))

    return c.fetchall()[0]

def update_resource_medium(resource_medium_entry, media_correction_entry):
    resource_medium = resource_medium_entry.lower()
    media_correction = media_correction_entry.lower()

    resource_mediumID = get_resource_mediumID(resource_medium)

    c.execute('''UPDATE resource_medium SET medium = ? WHERE ID =?''', (media_correction, resource_mediumID))
    db.commit()


def delete_resource_medium(resource_medium_entry):
    resource_medium = resource_medium_entry.lower()
    resource_mediumID = get_resource_mediumID(resource_medium)
    c.execute('''DELETE FROM resource_medium WHERE ID = ?''', (resource_mediumID,))
    db.commit()


# subject CRUD FUNCTIONS

def add_subject(subject_entry):
    subject = subject_entry.lower()
    c.execute('''INSERT OR IGNORE INTO subjects(subject) VALUES(?)''', (subject,))
    db.commit()


def list_subjects():
    c.execute('''SELECT subject FROM subjects''')

    subjects = c.fetchall()
    results = [x for t in subjects for x in t]
    results = ' '.join(results)

    return results




def get_subjectID(subject):
    subject = subject.lower()
    c.execute('''SELECT ID FROM subjects WHERE subject = ? ''', (subject,))
    return c.fetchone()[0]


def get_subject(subjectID):
    c.execute('''SELECT subject FROM subjects WHERE ID = ?''', (subjectID,))
    return c.fetchall()[0]


def update_subject(subject):
    subject = subject.lower()
    subjectID = get_subjectID(subject)
    c.execute('''UPDATE subjects SET subject = ? WHERE ID =?''', (subject, subjectID))
    db.commit()


def delete_subject(subjectID):
    c.execute('''DELETE FROM subjects WHERE ID = ?''', (subjectID,))
    db.commit()


# RESOURCE
def get_resource_id(resource_title_entry):
    resource_title = resource_title_entry.title()
    c.execute('''SELECT ID FROM resource WHERE title = ?''', (resource_title,))
    return c.fetchone()[0]

def add_resource(title, author, year, pages, publisher, language, medium, subject, abstract):
    """ Adds item to SQL database"""

    add_publisher(publisher)
    publisherID = get_publisherID(publisher)

    add_language(language)
    languageID = get_languageID(language)

    add_resource_medium(medium)
    mediaID = get_resource_mediumID(medium)

    title = title.title()

    c.execute('''INSERT OR IGNORE INTO resource(title, year, pages, publisherID, languageID, mediaID, abstract) 
                 VALUES(?,?,?,?,?,?,?)''',
              (title, year, pages, publisherID, languageID, mediaID, abstract,))

    resourceID = get_resource_id(title)

    add_author(author)
    authorID = get_authorID(author)

    add_subject(subject)
    subjectID = get_subjectID(subject)

    c.execute("INSERT OR IGNORE INTO resource_author VALUES(?,?)", (resourceID, authorID,))
    db.commit()

    c.execute('INSERT OR IGNORE INTO resource_subject VALUES(?,?)', (subjectID, resourceID))
    db.commit()

def list_resources():
    """ Returns all the resources from database"""

    c.execute('''SELECT resource.title, authors.name, resource.year, resource.pages, 
                publishers.publisher, languages.language, resource_medium.medium, resource.abstract
                FROM resource JOIN languages JOIN publishers JOIN resource_medium JOIN authors
                JOIN resource_author
                ON resource.languageID = languages.ID AND resource.mediaID = resource_medium.ID 
                AND resource.publisherID = publishers.ID AND authors.ID = resource_author.authorID 
                AND resource.ID = resource_author.resourceID
                ''')

    return c.fetchall()



# PROJECT Category CRUD

def add_project_category(project_category):
    """  Adds project_type to database    """
    project_category = project_category.title()

    c.execute('''INSERT OR IGNORE INTO project_category(category) VALUES(?)''', (project_category,))
    db.commit()


def list_project_category():
    """    :return: all the project categories from database    """

    c.execute('''SELECT category FROM project_category ORDER BY category''')
    categories = c.fetchall()
    results = [x for t in categories for x in t]
    results = ' '.join(results)
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
    return c.fetchall()

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
