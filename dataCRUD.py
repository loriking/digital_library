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
    """    Adds language to SQL database    """

    #language = input("Language:\t")
    language = language.title()
    c.execute('''INSERT OR IGNORE INTO languages(language) VALUES(?)''', (language,))
    db.commit()


def list_languages():
    """    return: all the languages from database     """

    c.execute('''SELECT language FROM languages''')
    results = c.fetchall()
    
    return results


def get_languageID(language):
    """ return: the ID (PK) of a given language    """

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


def update_language():
    langID = get_languageID()
    language = input("Correction:\t")
    print("Updating", language)
    c.execute('''UPDATE languages SET language = ? WHERE ID =?''', (language, langID))
    db.commit()


def delete_language():
    languageID = get_languageID()
    c.execute('''DELETE FROM languages WHERE ID = ?''', (languageID,))
    db.commit()


# KEYWORDS CRUD FUNCTIONS

def add_keyword():
    """      Adds keyword to SQL database    """

    keyword = input("keyword:\t")
    keyword = keyword.title()
    c.execute('''INSERT INTO keywords(keyword) VALUES(?)''', (keyword,))
    db.commit()


def list_keyword():
    """ return:  all the keywords from database     """

    c.execute('''SELECT keyword FROM keywords''')
    results = c.fetchall()
    for i in results:
        print(i)
    return results


def get_keywordID():
    """ return: the ID of a given keyword    """

    keyword = input("Enter keyword:\t")
    keyword = keyword.title()
    c.execute('''SELECT ID FROM keywords WHERE keyword = ? ''', (keyword,))
    keywordID = c.fetchone()[0]
    print(keyword, "has ID of ", keywordID)
    return keywordID


def get_keyword():
    """ return: keyword from ID    """

    keywordID = input("Enter ID for keyword desired:\t")
    c.execute('''SELECT keyword FROM keywords WHERE ID = ?''', (keywordID,))
    return c.fetchall()[0]


def update_keyword():
    keywordID = get_keywordID()
    keyword = input("Correction:\t")
    print("Updating", keyword)
    c.execute('''UPDATE keywords SET keyword = ? WHERE ID =?''', (keyword, keywordID))
    db.commit()


def delete_keyword():
    keywordID = get_keywordID()
    c.execute('''DELETE FROM keywords WHERE ID = ?''', (keywordID,))
    print("Deleting item: ", keywordID)
    db.commit()


# AUTHOR CRUD

def add_author(author_name):
    """    Adds author to SQL database    """

    #name = input("Author full name:\t")

    c.execute("INSERT OR IGNORE INTO authors(name) VALUES(?)", (author_name,))
    db.commit()
    return author_name


def list_authors():
    """    :return: all the author from database    """

    c.execute("SELECT name FROM authors")
    results = c.fetchall()
    for i in results:
        print(i)
    return results


def find_author():
    """ return: Searches for author based on partial match  """

    name = input("Name:")
    search = "%" + name + "%"
    c.execute("SELECT name FROM authors WHERE name LIKE ?", (search,))
    matches = c.fetchall()

    for i in matches:
        print(i)

    return matches


def get_authorID():
    """     :return: the ID of a given author    """

    name = input("Enter name:\t")

    c.execute('''SELECT ID FROM authors WHERE name = ? ''', (name,))

    authorID = c.fetchall()[0]
    authorID = authorID[0]

    # print(name, "has ID of ", authorID)
    return authorID


def get_author():
    """ return: author from ID    """

    authorID = input("Enter ID for author desired:\t")
    c.execute('''SELECT name FROM authors WHERE ID = ?''', (authorID,))

    author_name = c.fetchall()[0]
    author_name = author_name[0]

    return author_name


def update_author():
    authorID = get_authorID()
    author = input("Correction:\t")

    print("Updating", author)

    c.execute('''UPDATE authors SET name = ? WHERE ID =?''', (author, authorID))
    db.commit()


def delete_author():
    authorID = get_authorID()

    c.execute('''DELETE FROM authors WHERE ID = ?''', (authorID,))
    print("Deleting item: ", authorID)

    db.commit()


# Publishers CRUD functions

def add_publisher(publisher):
    """ Adds publisher to SQL database"""

    c.execute('''INSERT OR IGNORE INTO publishers(publisher) VALUES(?)''', (publisher,))
    db.commit()


def list_publishers():
    """ Returns all the publisher from database"""
    
    c.execute('''SELECT publisher FROM publishers''')
    results = c.fetchall()
    for i in results:
        print(i)
    return results


def get_publisherID():
    """ Returns the ID (PK) of a given publisher"""
    
    publisher = input("Enter publisher:\t")

    c.execute('''SELECT ID FROM publishers WHERE publisher = ? ''', (publisher,))
    publisherID = c.fetchall()[0]
    publisherID = publisherID[0]
    # print(publisher, "has ID of ", publisherID)

    return publisherID


def get_publisher(publisherID):
    """ Returns publisher from ID"""

    c.execute('''SELECT publisher FROM publishers WHERE ID = ?''', (publisherID,))
    return c.fetchall()[0]


def update_publisher():
    publisherID = get_publisherID()
    publisher = input("Correction:\t")

    # print("Updating", publisher)
    c.execute('''UPDATE publishers SET publisher = ? WHERE ID =?''', (publisher, publisherID))
    db.commit()


def delete_publisher():
    publisherID = get_publisherID()
    c.execute('''DELETE FROM publishers WHERE ID = ?''', (publisherID,))
    # print("Deleting item: ", publisherID)
    db.commit()


# RESOURCE medium CRUD
def add_resource_medium(medium):
    c.execute("INSERT OR IGNORE INTO resource_medium(medium) VALUES(?)", (medium,))
    db.commit()

def list_resource_medium():
    """ return: all the resource types from database    """

    c.execute('''SELECT medium FROM resource_medium''')
    results = c.fetchall()
    for i in results:
        print(i)
    return results


def get_resource_mediumID():
    """ Returns the ID (PK) of a given resource medium"""

    resource_medium = input("Enter resource type:\t")

    c.execute('''SELECT ID FROM resource_medium WHERE medium = ? ''', (resource_medium,))
    resource_mediumID = c.fetchone()[0]
    print(resource_medium, "has ID of ", resource_mediumID)
    return resource_mediumID


def get_resource_type(resource_mediumID):
    """ Returns resource medium from ID"""

    c.execute('''SELECT medium FROM resource_medium WHERE ID = ?''', (resource_mediumID,))

    medium = c.fetchall()[0]
    medium = medium[0]
    return medium


def update_resource_medium():
    resource_mediumID = get_resource_mediumID()
    medium = input("Correction:\t")
    print("Updating", medium)
    c.execute('''UPDATE resource_medium SET medium = ? WHERE ID =?''', (medium, resource_mediumID))
    db.commit()


def delete_resource_medium():
    resource_mediumID = get_resource_mediumID()
    c.execute('''DELETE FROM resource_medium WHERE ID = ?''', (resource_mediumID,))
    print("Deleting item: ", resource_mediumID)
    db.commit()


# Resource CRUD FUNCTIONS
#
def add_resource(resource_title, author, publisher, year, pages, medium, language, abstract):
    """ Adds item to SQL database"""

    add_language(language)
    c.execute("SELECT ID FROM languages WHERE language = ?", (language,))
    languageID = c.fetchone()[0]

   # medium = input("Type of resource (medium):\t")
    add_resource_medium(medium)
    c.execute("SELECT ID FROM resource_medium WHERE medium = ?", (medium,))
    mediaID = c.fetchone()[0]

    #publisher = input("Publisher:\t")
    add_publisher(publisher)
    c.execute("SELECT ID FROM publishers WHERE publisher = ?", (publisher,))
    publisherID = c.fetchone()[0]

    c.execute('''INSERT INTO resource(title, year, pages, languageID, mediaID, 
                                       publisherID, abstract) VALUES(?,?,?,?,?,?,?)''',
              (resource_title, year, pages, languageID, mediaID, publisherID, abstract))

    c.execute("SELECT ID FROM resource WHERE title = ?", (resource_title,))
    resourceID = c.fetchone()[0]

    add_author(author)
    c.execute("SELECT ID FROM authors WHERE name = ?", (author,))
    authorID = c.fetchone()[0]

    c.execute("INSERT OR IGNORE INTO  RESOURCE_AUTHOR VALUES(?,?)", (resourceID, authorID))
    db.commit()

"""
    number_of_authors = int(input("Number of authors:\t"))

    if number_of_authors != 0:
        while number_of_authors > 0:
            name = add_author()
            c.execute("SELECT ID FROM authors WHERE name = ?", (name,))
            authorID = c.fetchone()[0]

            c.execute("INSERT OR IGNORE INTO  RESOURCE_AUTHOR VALUES(?,?)", (resourceID, authorID))
            number_of_authors -= 1
"""
    #db.commit()


def list_resources():
    """ Returns all the resources from database"""
    
    c.execute('''SELECT resource.title, resource.year, resource.pages, publishers.publisher, 
                    languages.language, resource_medium.medium
                FROM resource JOIN languages JOIN publishers JOIN resource_medium
                ON resource.languageID = languages.ID AND resource.mediaID = resource_medium.ID 
                AND resource.publisherID = publishers.ID
                ''')


    results = c.fetchall()
    return results


def get_resourceID():
    """ Returns the ID (PK) of a given resource"""
    
    title = input("Enter Title:\t")

    c.execute('''SELECT ID FROM resource WHERE title = ? ''', (title,))
    resourceID = c.fetchone()[0]
    print(title, "has ID of ", resourceID)
    return resourceID


def get_resource(resourceID):
    """ Returns resource  details from ID"""

    c.execute('''SELECT title, year, pages, languageID, mediaID, 
               publisherID, abstract FROM resource WHERE ID = ?''', (resourceID,))

    return c.fetchall()[0]


def modify_resource(ID=None, title=None, year=None, pages=None, languageID=None,
                    mediaID=None, publisherID=None, abstract=None):
    """ Modifies resource"""

    ID = input("Enter resource ID number:\t")

    fields = get_resource(ID)

    if not title:
        title = fields[0]
    if not year:
        year = fields[1]
    if not pages:
        pages = fields[2]
    if not languageID:
        languageID = fields[3]
    if not mediaID:
        mediaID = fields[4]
    if not publisherID:
        publisherID = fields[5]
    if not abstract:
        abstract = fields[6]

    c.execute(''' UPDATE resource 
        SET title = ?, year = ?, pages = ?, languageID = ?, mediaID = ?, 
            publisherID = ?, abstract = ?
        WHERE ID = ? ''', (title, year, pages, languageID, mediaID,
                           publisherID, abstract, ID))

    db.commit()


def delete_resource():
    resourceID = get_resourceID()
    c.execute('''DELETE FROM resource WHERE ID = ?''', (resourceID,))
    print("Deleting item: ", resourceID)
    db.commit()


# PROJECT Category CRUD

def add_project_category():
    """  Adds project_type to database    """

    project_category = input("Enter project type:\t")

    c.execute('''INSERT INTO project_category(category) VALUES(?)''', (project_category,))
    db.commit()


def list_project_category():
    """    :return: all the project categories from database    """

    c.execute('''SELECT category FROM project_category''')
    results = c.fetchall()
    for row in results:
        ID = row[0]
        category = row[1]
        print(ID, category)

    return results


def get_project_categoryID():
    """    :return: the ID (PK) of a given project_category'    """

    project_category = input("Enter Project category:\t")

    try:
        c.execute('''SELECT ID FROM project_category WHERE category = ? ''', (project_category,))
        project_categoryID = c.fetchone()[0]

    except TypeError:
        c.execute('''INSERT OR IGNORE INTO project_category(category) VALUES(?)''', (project_category,))
        db.commit()

        c.execute('''SELECT ID FROM project_category WHERE category = ? ''', (project_category,))
        project_categoryID = c.fetchone()[0]

    print(project_category, "has ID of ", project_categoryID)
    return project_categoryID


def get_project_category():
    """     return: project type from ID    """

    project_categoryID = input("Enter ID for project category desired:\t")
    c.execute('''SELECT category FROM project_category WHERE ID = ?''', (project_categoryID,))

    return c.fetchall()[0]


def update_project_category():
    """ Modifies project category"""

    project_categoryID = get_project_categoryID()

    project_category = input("Enter correction to project category:\t")

    print("Updating", project_category)

    c.execute('''UPDATE project_category SET category = ? WHERE ID =?''', (project_category, project_categoryID))
    db.commit()


def delete_project_category():
    project_categoryID = get_project_categoryID()
    c.execute('''DELETE FROM project_category WHERE ID = ?''', (project_categoryID,))
    print("Deleting item: ", project_category)
    db.commit()


# Project CRUD functions

def add_project():
    """    Adds item to SQL database    """

    project_name = input("Title:\n")
    project_category = get_project_categoryID()

    description = input("Description of item:\n")

    date_start = input("Starting date:\n")
    date_end = input("Projected completion date:\n")

    c.execute(
        '''INSERT INTO projects(project_name, project_category, description, date_start, date_end ) VALUES(?,?,?,?,?)''',
        (project_name, project_category, description, date_start, date_end))
    db.commit()

def get_projectID():
    """ Returns the ID of a given project """
    c.execute('''SELECT ID FROM project WHERE project_name = ?''', (project_name,))
    return c.fetchall()


def list_projects():
    """ :return list of projects """
    c.execute('''SELECT project_name, category, description, date_start, date_end
            FROM projects JOIN project_category 
            ON projects.project_category = project_category.ID           
                ''')
    return c.fetchall()


def get_project(projectID):
    c.execute('''SELECT project_name, category, description, date_start, date_end 
                FROM projects JOIN project_category 
                ON projects.project_category = project_category.ID 
                WHERE projects.ID = ? ''', (projectID,))
    return c.fetchall()


def update_project(ID = None, project_name = None, project_category = None, description = None, date_start = None, date_end = None):

    projectID = input("Enter Project ID number:\t")

    fields = get_project(projectID)

    
    if not project_name:
        project_name  = fields[0]
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
    

def delete_project(projectID):
    c.execute(''' DELETE from projects WHERE projects.ID = ?''', (projectID,))
    db.commit()

def get_books_by_author():
    author_name = input("Author's name:\t")
    c.execute("""SELECT resource.title, resource.abstract
                    FROM RESOURCE_AUTHOR JOIN resource JOIN authors
                    ON resourceID = resource.ID AND authorID = authors.ID
                    WHERE authors.name = ?""", (author_name,))
    results = c.fetchall()
    # print("Resources by " + author_name + ":")
    # for item in results:
    #     print(item)
    return results
