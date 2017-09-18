# -*- coding: utf-8 -*-

'''
dataCRUD.py
Created on Sep 15, 2017

@author: lak
'''
import sqlite3 as sql

db = sql.connect('library_data2.db')
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
    ''' Adds language to SQL database'''
    keyword = input("keyword:\t")
    keyword = keyword.title()
    c.execute('''INSERT INTO keywords(keyword) VALUES(?)''', (keyword,))
    db.commit()
    
def list_keyword():
    ''' Returns all the languages from database'''
    c.execute('''SELECT * FROM keywords''')
    results = c.fetchall()
    for i in results:
        print(i)
    return results
    
def get_keywordID():
    ''' Returns the ID (PK) of a given language'''
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
    first_name = input("Author first name:\t")
    last_name = input("Author last name:\t")
    
    first_name = first_name.title()
    last_name = last_name.title()
    c.execute('''INSERT INTO authors(first_name, last_name) VALUES(?, ?)''', (first_name, last_name))
    db.commit()
    
def list_authors():
    ''' Returns all the arthor from database'''
    c.execute('''SELECT * FROM authors''')
    results = c.fetchall()
    for i in results:
        print(i)
    return results
    
def get_authorID():
    ''' Returns the ID (PK) of a given author'''
    
    search_term = input("Search by first name, last name or full name? Enter: f/l/b)\n")
    if search_term.lower() == "f":
        first_name = input("Enter first name:\t")
        first_name = first_name.title()
        c.execute('''SELECT ID FROM authors where first_name = ?''', (first_name,))
        results =  c.fetchall()[0]
    elif search_term.lower() == "l":
        last_name = input("Enter last name:\t")
        last_name = last_name.title()
        results = c.execute('''SELECT ID FROM authors where last_name = ?''', (last_name,))
        results =  c.fetchall()[0]
    elif search_term.lower() == "b":
        first_name = input("Enter first name:\t")
        last_name = input("Enter last name:\t")
        results = c.execute('''SELECT ID FROM authors where first_name = ? AND last_name = ?''', 
                  (first_name, last_name,))
        results = c.fetchall()[0]
    
    return results


    
def get_author():
    ''' Returns author from ID'''
    authorID = input("Enter ID for author desired:\t")
    c.execute('''SELECT first_name, last_name FROM authors WHERE ID = ?''', (authorID,))
    return c.fetchall()[0]


    
def update_author():
    authorID = get_authorID()
    author = input("Correction:\t") 
    print("Updating", author)
    c.execute('''UPDATE authors SET author = ? WHERE ID =?''', (author, authorID))
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
    publisher = publisher.title()
    c.execute('''INSERT INTO publishers(publisher) VALUES(?)''', (publisher,))
    db.commit()
    
def list_publisher():
    ''' Returns all the publisher from database'''
    c.execute('''SELECT * FROM publishers''')
    results = c.fetchall()
    for i in results:
        print(i)
    return results
    
def get_publisherID():
    ''' Returns the ID (PK) of a given publisher'''
    publisher = input("Enter publisher:\t")
    publisher = publisher.title()
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
              (title, year, pages, languageID, resource_typeID, publisherID,abstract,))
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
    title = title.title()
    c.execute('''SELECT ID FROM resource WHERE title = ? ''', (title,))
    resourceID = c.fetchone()[0]
    print(title, "has ID of ", resourceID)
    return resourceID
    
def get_resource():
    ''' Returns resource  details from ID'''
    resourceID = input("Enter ID for resource desired:\t")
    c.execute('''SELECT title, pubyear, pages, languageID, typeID, 
              publisherID, abstract FROM resource WHERE ID = ?''', (resourceID,))
    return c.fetchall()[0]


def delete_resource():
    resourceID = get_resourceID()
    c.execute('''DELETE FROM resources WHERE ID = ?''', (resourceID,))
    print("Deleting item: ", resourceID)
    db.commit()
