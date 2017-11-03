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
        
    CREATE TABLE IF NOT EXISTS  authors (
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

    
    CREATE TABLE IF NOT EXISTS resource_medium (
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        medium TEXT UNIQUE
        );
    
    CREATE TABLE IF NOT EXISTS resource (
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT NOT NULL UNIQUE,
        year INTEGER,
        pages INTEGER,
        publisherID INTEGER REFERENCES publishers(ID),
        mediaID INTEGER REFERENCES resource_medium(ID),
        languageID INTEGER REFERENCES languages(ID),
        notes TEXT
        );
    
    CREATE TABLE IF NOT EXISTS resource_author(  
        resourceID INTEGER,
        authorID INTEGER,
        mediaID INTEGER REFERENCES resource_medium(ID),
        PRIMARY KEY (resourceID, authorID, mediaID)
        );    
        
    CREATE TABLE IF NOT EXISTS resource_subject(
        resourceID INTEGER,
        subjectID INTEGER,
        mediaID INTEGER,
        PRIMARY KEY(resourceID, subjectID, mediaID)
        );

        
    CREATE TABLE IF NOT EXISTS project_category(
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        category TEXT UNIQUE
        );
        
    CREATE TABLE IF NOT EXISTS online_media(
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT,
        media_date TEXT,
        domainID INTEGER REFERENCES publisher(ID),
        media_URL TEXT,
        access_date TEXT,
        comments TEXT,
        mediaID INTEGER REFERENCES resource_medium(ID),
        audio_video INTEGER
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
    db.close()

if __name__ == '__main__':
    make_db()