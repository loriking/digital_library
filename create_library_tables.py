# -*- coding: utf-8 -*-
"""
Created on Sun Jan 1 15:38:30 2017

author: lak
"""

import sqlite3 

def make_db():
    db = sqlite3.connect('test.db')
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
        subject TEXT UNIQUE NOT NULL
        );
        
    CREATE TABLE IF NOT EXISTS levels (
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        level TEXT NOT NULL
        );

    CREATE TABLE IF NOT EXISTS resource_medium (
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        medium TEXT UNIQUE NOT NULL
        );
    
    CREATE TABLE IF NOT EXISTS game_engine(
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE NOT NULL
        );
        
    CREATE TABLE IF NOT EXISTS platform (
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE  NOT NULL
        );
        
    CREATE TABLE IF NOT EXISTS website_name (
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE NOT NULL
        );
                
    CREATE TABLE IF NOT EXISTS provider(
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE NOT NULL
        );
        
    CREATE TABLE IF NOT EXISTS copyright(
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        status TEXT UNIQUE NULL
        );       
    
    CREATE TABLE IF NOT EXISTS texts (
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT UNIQUE NOT NULL,
        year INTEGER,
        pages INTEGER,
        subjectID INTEGER REFERENCES subjects(ID),
        publisherID INTEGER REFERENCES publishers(ID),
        languageID INTEGER REFERENCES languages(ID),
        mediaID INTEGER REFERENCES resource_medium(ID),
        levelID INTEGER REFERENCES levels(ID)
        );
    
            
    CREATE TABLE IF NOT EXISTS audio (
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT UNIQUE NOT NULL,
        duration TEXT NOT NULL,
        subjectID INTEGER REFERENCES subjects(ID),
        program TEXT,
        date TEXT,
        url TEXT,
        mediaID INTEGER REFERENCES resource_medium(ID),
        languageID INTEGER REFERENCES languages(ID)
        );
    
    CREATE TABLE IF NOT EXISTS courses (
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT UNIQUE NOT NULL,
        subjectID INTEGER REFERENCES subjects(ID),
        duration_weeks INTEGER,
        providerID INTEGER REFERENCES provider(ID),
        url TEXT,
        notes TEXT,
        mediaID INTEGER REFERENCES resource_medium(ID),
        levelID INTEGER REFERENCES levels(ID)
        );
        
    CREATE TABLE IF NOT EXISTS images(
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT UNIQUE NOT NULL,
        date_created INTEGER,
        date_accessed INTEGER,
        url TEXT,
        subjectID INTEGER REFERENCES subjects(ID),
        copyrightID INTEGER REFERENCES copyright(ID),       
        mediaID INTEGER REFERENCES resource_medium(ID)
        );

    CREATE TABLE IF NOT EXISTS interactive_media(
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT UNIQUE NOT NULL,
        year INTEGER,
        subjectID INTEGER REFERENCES subjects(ID),
        platformID INTEGER REFERENCES platform(ID),
        engineID INTEGER REFERENCES game_engine(ID),
        version REAL,
        mediaID INTEGER REFERENCES resource_medium(ID)        
        );
                             
    CREATE TABLE IF NOT EXISTS video (
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT UNIQUE NOT NULL,
        duration TEXT NOT NULL,
        subjectID INTEGER REFERENCES subjects(ID),
        producer TEXT,
        year INTEGER,
        url TEXT,
        mediaID INTEGER REFERENCES resource_medium(ID),
        languageID INTEGER REFERENCES languages(ID)
        );   

    CREATE TABLE IF NOT EXISTS websites (
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT UNIQUE NOT NULL,
        subjectID INTEGER REFERENCES subjects(ID),     
        url TEXT,
        date_created TEXT,
        date_accessed TEXT,
        notes TEXT,
        mediaID INTEGER REFERENCES resource_medium(ID)
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
    
    CREATE VIEW all_resources AS 
        SELECT texts.ID, texts.title, authors.name, subjects.subject, resource_medium.medium 
        FROM texts, authors, resource_author, resource_medium, subjects
        WHERE texts.mediaID = resource_medium.ID 
        AND texts.subjectID = subjects.ID
        AND texts.ID = resource_author.resourceID
        AND texts.mediaID = resource_author.mediaID
        AND authors.ID = resource_author.authorID
        
        UNION SELECT audio.ID, audio.title, authors.name, subjects.subject, resource_medium.medium 
        FROM audio, authors, resource_author, resource_medium, subjects
        WHERE audio.mediaID = resource_medium.ID
        AND audio.subjectID = subjects.ID
        AND audio.ID = resource_author.resourceID
        AND audio.mediaID = resource_author.mediaID
        AND authors.ID = resource_author.authorID
        
        UNION SELECT courses.ID, courses.title, authors.name, subjects.subject, resource_medium.medium 
        FROM courses, authors, resource_author, resource_medium, subjects
        WHERE courses.mediaID = resource_medium.ID
        AND courses.subjectID = subjects.ID
        AND courses.ID = resource_author.resourceID
        AND courses.mediaID = resource_author.mediaID
        AND authors.ID = resource_author.authorID
        
        UNION SELECT images.ID, images.title, authors.name, subjects.subject, resource_medium.medium 
        FROM images, authors, resource_author, resource_medium, subjects
        WHERE images.mediaID = resource_medium.ID 
        AND images.subjectID = subjects.ID
        AND images.ID = resource_author.resourceID
        AND images.mediaID = resource_author.mediaID
        AND authors.ID = resource_author.authorID
        
        UNION SELECT interactive_media.ID, interactive_media.title, authors.name, subjects.subject, resource_medium.medium 
        FROM interactive_media, authors, resource_author, resource_medium, subjects
        WHERE interactive_media.mediaID = resource_medium.ID 
        AND interactive_media.subjectID = subjects.ID
        AND interactive_media.ID = resource_author.resourceID
        AND interactive_media.mediaID = resource_author.mediaID
        AND authors.ID = resource_author.authorID
        
        UNION SELECT video.ID, video.title, authors.name, subjects.subject, resource_medium.medium 
        FROM video, authors, resource_author, resource_medium, subjects
        WHERE video.mediaID = resource_medium.ID 
        AND video.subjectID = subjects.ID
        AND video.ID = resource_author.resourceID
        AND video.mediaID = resource_author.mediaID
        AND authors.ID = resource_author.authorID
        
        UNION SELECT websites.ID, websites.title, authors.name, subjects.subject, resource_medium.medium 
        FROM websites, authors, resource_author, resource_medium, subjects
        WHERE websites.mediaID = resource_medium.ID 
        AND websites.subjectID = subjects.ID
        AND websites.ID = resource_author.resourceID
        AND websites.mediaID = resource_author.mediaID
        AND authors.ID = resource_author.authorID;
        ''')


    db.commit()


    default_languages = ['English']
    default_levels = ['Absolute Beginner', 'Beginner', 'Advanced Beginner', 'Low Intermediate', 'Intermediate',
                      'Low Advanced', 'Advanced', 'Professional']
    default_project_type = ['Python App']
    default_publisher = ['Unpublished']
    default_media_types = ['Book', 'Short story', 'Other text',
                           'Music', 'Sound', 'Podcast',
                           'Video Clip', 'Documentary', 'Other Video',
                           'Audio only', 'MOOC', 'Blended Class',
                           'Photo', 'Clipart/Sprite','Other image',
                           'Interactive Fiction', 'Video game', 'Other interactive',
                           'Website', 'Documentation', 'Q&A Site']
    default_copyright = ['Public Domain', 'Creative Commons', 'Copyrighted']

    for i in default_languages:
        c.execute('INSERT OR IGNORE INTO languages(language) VALUES(?)', (i,))
    for i in default_levels:
        c.execute('INSERT OR IGNORE INTO levels(level) VALUES(?)', (i,))
    for i in default_project_type:
        c.execute('INSERT OR IGNORE INTO project_category(category) VALUES(?)', (i,))
    for i in default_publisher:
        c.execute('INSERT OR IGNORE INTO publishers(publisher) VALUES(?)', (i,))
    for i in default_media_types:
        c.execute('INSERT OR IGNORE INTO resource_medium(medium) VALUES(?)', (i,))
    for i in default_copyright:
        c.execute('INSERT OR IGNORE INTO copyright(status) VALUES(?)', (i,))


    db.commit()
    db.close()

# def make_views():
#     db = sqlite3.connect('test.db')
#     c = db.cursor()
#
#     c.executescript(
#         '''PRAGMA Foreign_Keys=True;
#
#          ''')
#
#
#     db.commit()
#     db.close()
#


if __name__ == '__main__':
    make_db()
    # make_views()