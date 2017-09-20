# -*- coding: utf-8 -*-

'''
dataCRUD.py
Created on Sep 15, 2017

@author: lak
'''
import sqlite3 as sql

db = sql.connect('library_data.db')
c = db.cursor()


# Languages C.R.U.D.
def add_language():
    ''' Adds language to SQL database'''
    language = input("Language:\t")
    language = language.title()
    c.execute('''INSERT INTO languages(language) VALUES(?)''', (language,))
    db.commit()
    
def list_languages():
    ''' Returns all the languages from database'''
    c.execute('''SELECT * FROM languages''')
    results = c.fetchall()
    for i in results:
        print(i)
    return results
    
def get_languageID():
    ''' Returns the ID (PK) of a given language'''
    
    language = input("Enter language:\t")
    language = language.title()
    c.execute('''SELECT ID FROM languages WHERE language = ? ''', (language,))
    
    langID = c.fetchall()[0]
    langID = langID[0]
    
    print(language, "has ID of ", langID)
    return langID
    
def get_language(langID):
    ''' Returns language from ID'''
    
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
    print("Deleting item: ", languageID)
    db.commit()
    


######## KEYWORDS CRUD FUNCTIONS


def add_keyword():
    ''' Adds keyword to SQL database'''
    keyword = input("keyword:\t")
    keyword = keyword.title()
    c.execute('''INSERT INTO keywords(keyword) VALUES(?)''', (keyword,))
    db.commit()
    
def list_keyword():
    ''' Returns all the keywords from database'''
    c.execute('''SELECT * FROM keywords''')
    results = c.fetchall()
    for i in results:
        print(i)
    return results
    
def get_keywordID():
    ''' Returns the ID (PK) of a given keyword'''
    keyword = input("Enter keyword:\t")
    keyword = keyword.title()
    c.execute('''SELECT ID FROM keywords WHERE keyword = ? ''', (keyword,))
    keywordID = c.fetchone()[0]
    print(keyword, "has ID of ", keywordID)
    return keywordID
    
def get_keyword():
    ''' Returns kewword from ID'''
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

############## AUTHORS ##################

def add_author():
    ''' Adds author to SQL database'''
    name = input("Author full name:\t")
    
    c.execute('''INSERT INTO authors(name) VALUES(?)''', (name,))
    db.commit()
    
def list_authors():
    ''' Returns all the author from database'''
    c.execute('''SELECT * FROM authors''')
    results = c.fetchall()
    for i in results:
        print(i)
    return results

def find_author():
    ''' Searches for author based on partial match'''
    # TODO ADD Return statement

    name = input("Name:")
    search = "%" + name + "%"
    c.execute("SELECT name FROM authors WHERE name LIKE ?", (search,))
    matches = c.fetchall()

    for i in matches:
        print(i)
    
def get_authorID():
    ''' Returns the ID (PK) of a given author'''
       
    name = input("Enter name:\t")
    
    c.execute('''SELECT ID FROM authors WHERE name = ? ''', (name,))
    
    authorID = c.fetchall()[0]
    authorID = authorID[0]
    
    # print(name, "has ID of ", authorID)
    return authorID

    
def get_author():
    ''' Returns author from ID'''

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

############## Publishers CRUD fuctions ##################

def add_publisher():
    ''' Adds publisher to SQL database'''
    publisher = input("publisher:\t")
    
    c.execute('''INSERT INTO publishers(publisher) VALUES(?)''', (publisher,))
    db.commit()
    
def list_publishers():
    ''' Returns all the publisher from database'''
    c.execute('''SELECT * FROM publishers''')
    results = c.fetchall()
    for i in results:
        print(i)
    return results
    
def get_publisherID():
    ''' Returns the ID (PK) of a given publisher'''
    publisher = input("Enter publisher:\t")

    c.execute('''SELECT ID FROM publishers WHERE publisher = ? ''', (publisher,))
    publisherID = c.fetchall()[0]
    publisherID = publisherID[0]
    # print(publisher, "has ID of ", publisherID)

    return publisherID
    
def get_publisher(publisherID):
    ''' Returns publisher from ID'''
    
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

############## Resource CRUD FUNCTIONS

def add_resource():
    ''' Adds item to SQL database'''
    title = input("Title:\n")
    year = input("Year:\n")
    pages = input("Number of pages:\n")
    languageID = get_languageID()
    resource_typeID = input("type:\n")
    publisherID = get_publisherID()
    
    abstract = input("Description of item:\n")  
    
    c.execute('''INSERT INTO resource(title, year, pages, languageID, resource_typeID, 
                                   publisherID, abstract) VALUES(?,?,?,?,?,?,?)''', 
              (title, year, pages, languageID, resource_typeID, publisherID,abstract))
    db.commit()



def list_resources():
    ''' Returns all the resources from database'''
    c.execute('''SELECT * FROM resource''')
    results = c.fetchall()
    for i in results:
        print(i)
    return results
    
def get_resourceID():
    ''' Returns the ID (PK) of a given resource'''
    title = input("Enter Title:\t")
    
    c.execute('''SELECT ID FROM resource WHERE title = ? ''', (title,))
    resourceID = c.fetchone()[0]
    print(title, "has ID of ", resourceID)
    return resourceID


def get_resource(resourceID):
    ''' Returns resource  details from ID'''

    c.execute('''SELECT title, year, pages, languageID, resource_typeID, 
               publisherID, abstract FROM resource WHERE ID = ?''', (resourceID,))

    return c.fetchall()[0]

def modify_resource(ID=None, title=None, year=None, pages=None, languageID=None,
                    resource_typeID=None, publisherID=None, abstract=None):
    ''' Modifies resource'''

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
    if not resource_typeID:
        resource_typeID = fields[4]
    if not publisherID:
        publisherID = fields[5]
    if not abstract:
        abstract = fields[6]
    c.execute(''' UPDATE resource 
        SET title = ?, year = ?, pages = ?, languageID = ?, resource_typeID = ?, 
            publisherID = ?, abstract = ?
        WHERE ID = ? ''', (title, year, pages, languageID, resource_typeID,
                           publisherID, abstract, ID))

    db.commit()

def delete_resource():
    resourceID = get_resourceID()
    c.execute('''DELETE FROM resource WHERE ID = ?''', (resourceID,))
    print("Deleting item: ", resourceID)
    db.commit()


##### PROJECT TYPE CRUD

def add_project_category():
    ''' Adds project_type to SQL database'''
    project_category = input("Enter project type:\t")
    
    c.execute('''INSERT INTO project_category(category) VALUES(?)''', (project_category,))
    db.commit()

    
def list_project_category():
    ''' Returns all the project types from database'''
    
    c.execute('''SELECT * FROM project_category''')
    results = c.fetchall()
    for i in results:
        print(i)

    return results


def get_project_categoryID():
    ''' Returns the ID (PK) of a given project_category'''
    project_category = input("Enter Project type:\t")

    c.execute('''SELECT ID FROM project_category WHERE category = ? ''', (project_category,))

    project_categoryID = c.fetchone()[0]

    print(project_category, "has ID of ", project_categoryID)
    return project_categoryID



def get_project_category():
    ''' Returns project type from ID'''

    project_categoryID = input("Enter ID for project type desired:\t")
    c.execute('''SELECT category FROM project_category WHERE ID = ?''', (project_categoryID,))


    return c.fetchall()[0]
    
def update_project_category():
    project_categoryID = get_project_typeID()
    
    project_type = input("Correction:\t") 

    print("Updating", project_type)

    c.execute('''UPDATE project_type SET category = ? WHERE ID =?''', (category, project_categoryID))
    db.commit()
    
def delete_project_category():
    project_categoryID = get_project_categoryID()
    c.execute('''DELETE FROM project_category WHERE ID = ?''', (project_categoryID,))
    print("Deleting item: ", project_category)
    db.commit()

# RESOURCE type CRUD
def list_resource_type():
    ''' Returns all the resource types from database'''
    c.execute('''SELECT * FROM resource_type''')
    results = c.fetchall()
    for i in results:
        print(i)
    return results


def get_resource_typeID():
    ''' Returns the ID (PK) of a given resource type'''
    resource_type = input("Enter resource type:\t")
    
    c.execute('''SELECT ID FROM resource_type WHERE type = ? ''', (resource_type,))
    resource_typeID = c.fetchone()[0]
    print(resource_type, "has ID of ", resource_typeID)
    return resource_typeID
    
def get_resource_type():
    ''' Returns resource type from ID'''
    resource_typeID = input("Enter ID for resource type desired:\t")
    c.execute('''SELECT type FROM resource_type WHERE ID = ?''', (resource_typeID,))

    resource_type = c.fetchall()[0]
    resource_type = resource_type[0]
    return resource_type

    
def update_resource_type():
    resource_typeID = get_resource_typeID()
    resource_type = input("Correction:\t") 
    print("Updating", resource_type)
    c.execute('''UPDATE resource_type SET type = ? WHERE ID =?''', (category, resource_typeID))
    db.commit()
    
def delete_resource_type():
    resource_typeID = get_resource_typeID()
    c.execute('''DELETE FROM resource_type WHERE ID = ?''', (resource_typeID,))
    print("Deleting item: ", resource_typeID)
    db.commit()

# Project CRUD functions

def add_project():
    ''' Adds item to SQL database'''
    
    project_name = input("Title:\n")
    project_category = get_project_categoryID()
    
    description = input("Description of item:\n")

    date_start = input("Starting date:\n")
    date_end = input("Projected completion date:\n")
    
    c.execute('''INSERT INTO projects(project_name, project_category, description, date_start, date_end ) VALUES(?,?,?,?,?)''', 
              (project_name, project_category, description, date_start, date_end))
    db.commit()

