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
        
    CREATE TABLE IF NOT EXISTS level (
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
        levelID INTEGER REFERENCES level(ID),
        publisherID INTEGER REFERENCES publishers(ID),
        languageID INTEGER REFERENCES languages(ID),
        subjectID INTEGER REFERENCES subject(ID),
        mediaID INTEGER REFERENCES resource_medium(ID),
        notes TEXT
        );
    
    CREATE TABLE IF NOT EXISTS websites (
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT NOT NULL,
        date INTEGER,
        website_nameID INTEGER REFERENCES publisher(ID),
        url TEXT,
        access_date INTEGER,
        notes TEXT,
        mediaID INTEGER REFERENCES resource_medium(ID),
        subjectID INTEGER REFERENCES subjectID
        );
            
        
    CREATE TABLE IF NOT EXISTS audio_video (
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT NOT NULL,
        duration_mins INTEGER NOT NULL,
        format TEXT NOT NULL,
        year INTEGER,
        location TEXT,
        comments TEXT,
        mediaID INTEGER REFERENCES resource_medium(ID),
        subjectID INTEGER REFERENCE subjectID
        );
        
    
    CREATE TABLE IF NOT EXISTS courses (
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT NOT NULL,
        start_date INTEGER NOT NULL,
        duration_hours INTEGER,
        url TEXT,
        levelID INTEGER REFERENCES level(ID),
        platformID INTEGER REFERENCES publishers(ID),
        mediaID INTEGER REFERENCES resource_medium(ID),
        subjectID INTEGER REFERENCE subjectID
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
        genreID INTEGER REFERENCE subjectID
        );
        
    CREATE TABLE IF NOT EXISTS images(
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT NOT NULL,
        format TEXT NOT NULL,
        date INTEGER,
        material TEXT,
        dimensions TEXT,
        location TEXT,
        comments TEXT,        
        imagetypeID INTEGER REFERENCES resource_medium(ID)
        );
        
        
    CREATE TABLE IF NOT EXISTS resource_author(  
        resourceID INTEGER,
        authorID INTEGER,
        mediaID INTEGER REFERENCES resource_medium(ID),
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
    db.close()

if __name__ == '__main__':
    make_db()