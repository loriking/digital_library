# -*- coding: utf-8 -*-
"""
Created on Sun Jan 1 15:38:30 2017

author: lak
"""

import sqlite3 

def make_db():
    db = sqlite3.connect('library_data.db')
    c = db.cursor()

    c.executescript('''
    PRAGMA Foreign_Keys=True;
    
    CREATE TABLE IF NOT EXISTS languages (
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        language TEXT UNIQUE NOT NULL
        );
        
    CREATE TABLE IF NOT EXISTS authors (
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE NOT NULL
        );
    
    CREATE TABLE IF NOT EXISTS publishers (
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        publisher TEXT UNIQUE NOT NULL
        );
    
    CREATE TABLE IF NOT EXISTS subjects (
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        subject TEXT UNIQUE
        );
        
    CREATE TABLE IF NOT EXISTS levels (
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        level TEXT NOT NULL
        );

    CREATE TABLE IF NOT EXISTS resource_medium (
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        medium TEXT UNIQUE
        );
    
    CREATE TABLE IF NOT EXISTS texts (
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT NOT NULL UNIQUE,
        year INTEGER,
        pages INTEGER,
        levelID INTEGER REFERENCES levels(ID),
        publisherID INTEGER REFERENCES publishers(ID),
        languageID INTEGER REFERENCES languages(ID),
        subjectID INTEGER REFERENCES subjects(ID),
        mediaID INTEGER REFERENCES resource_medium(ID),
        notes TEXT
        );
    
    CREATE TABLE IF NOT EXISTS websites (
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT NOT NULL,
        creation_date INTEGER,
        website_nameID INTEGER REFERENCES publishers(ID),
        url TEXT,
        access_date INTEGER,
        notes TEXT,
        mediaID INTEGER REFERENCES resource_medium(ID),
        subjectID INTEGER REFERENCES subjects(ID)
        );
            
        
    CREATE TABLE IF NOT EXISTS audio_video (
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT NOT NULL,
        duration_mins INTEGER NOT NULL,
        year INTEGER,
        program TEXT,
        url TEXT,
        languageID INTEGER REFERENCES languages(ID),
        mediaID INTEGER REFERENCES resource_medium(ID),
        subjectID INTEGER REFERENCES subjects(ID),
        publisherID INTEGER REFERENCES publishers(ID)
        );
        
    
    CREATE TABLE IF NOT EXISTS courses (
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT NOT NULL,
        start_date INTEGER NOT NULL,
        duration_hours TEXT,
        url TEXT,
        comments TEXT,
        levelID INTEGER REFERENCES levels(ID),
        platformID INTEGER REFERENCES publishers(ID),
        mediaID INTEGER REFERENCES resource_medium(ID),
        subjectID INTEGER REFERENCES subjects(ID)
        );
        
    CREATE TABLE IF NOT EXISTS interactive_media(
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT NOT NULL,
        year INTEGER,
        platform TEXT,
        version INTEGER,
        comments TEXT,
        engineID INTEGER REFERENCES publishers(ID),
        typeID INTEGER REFERENCES resource_medium(ID),
        genreID INTEGER REFERENCES subjects(ID)
        );
        
    CREATE TABLE IF NOT EXISTS images(
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT NOT NULL,
        date INTEGER,
        copywrite TEXT,
        website_name TEXT,
        dimensions TEXT,
        url TEXT,
        comments TEXT,       
        imagetypeID INTEGER REFERENCES resource_medium(ID)
        );
        
        
    CREATE TABLE IF NOT EXISTS resource_author(  
        resourceID INTEGER,
        authorID INTEGER,
        mediaID INTEGER,
        PRIMARY KEY (resourceID, authorID, mediaID)
        );    
        
        
    CREATE TABLE IF NOT EXISTS project_category(
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        category TEXT UNIQUE
        );
        
         
    CREATE TABLE IF NOT EXISTS projects (
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        project_name TEXT NOT NULL,
        project_category INTEGER REFERENCES project_category(ID),
        description TEXT,
        date_start TEXT, 
        date_end TEXT 
        );
        
    CREATE TABLE IF NOT EXISTS project_references(
        projectID INTEGER,
        resourceID INTEGER,
        mediaID INTEGER,
        PRIMARY KEY (projectID, resourceID, mediaID) 
        );
    ''')


    db.commit()


    default_languages = ['English']
    default_levels = ['Absolute Beginner', 'Beginner']
    default_project_type = ['Python App']
    default_publisher = ['Unpublished']

    for i in default_languages:
        c.execute('INSERT OR IGNORE INTO languages(language) VALUES(?)', (i,))
    for i in default_levels:
        c.execute('INSERT OR IGNORE INTO levels(level) VALUES(?)', (i,))
    for i in default_project_type:
        c.execute('INSERT OR IGNORE INTO project_category(category) VALUES(?)', (i,))
    for i in default_publisher:
        c.execute('INSERT OR IGNORE INTO publishers(publisher) VALUES(?)', (i,))

    db.commit()
    db.close()



if __name__ == '__main__':
    make_db()