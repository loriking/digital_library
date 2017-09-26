# -*- coding: utf-8 -*-
"""
Created on Sun Jan 1 15:38:30 2017

author: lak
"""

import sqlite3 

db = sqlite3.connect('library_data.db')
c = db.cursor()

c.executescript('''
PRAGMA Foreign_Keys=True;

DROP TABLE IF EXISTS languages;
DROP TABLE IF EXISTS keywords;
DROP TABLE IF EXISTS authors;
DROP TABLE IF EXISTS publishers;
DROP TABLE IF EXISTS resource_format;
DROP TABLE IF EXISTS project_category;
DROP TABLE IF EXISTS resource;


DROP TABLE IF EXISTS RESOURCE_AUTHOR;
DROP TABLE IF EXISTS RESOURCE_KEYWORDS;
DROP TABLE IF EXISTS PROJECT_REFERENCES;

DROP TABLE IF EXISTS projects;
DROP TABLE IF EXISTS reading_now;

CREATE TABLE languages (
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    language TEXT UNIQUE
    );

CREATE TABLE resource_medium (
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    medium TEXT UNIQUE
    );

CREATE TABLE project_category(
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    category TEXT UNIQUE
    );
    
CREATE TABLE keywords (
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    keyword TEXT UNIQUE
    );
    
CREATE TABLE authors (
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE NOT NULL
    );

CREATE TABLE publishers (
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    publisher TEXT UNIQUE NOT NULL
    );

CREATE TABLE resource (
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE NOT NULL,
    year INTEGER,
    pages INTEGER,
    languageID INTEGER REFERENCES languages(ID),
    mediaID INTEGER REFERENCES resource_medium(ID),
    publisherID INTEGER REFERENCES publishers(ID),
    abstract TEXT
    );

CREATE TABLE projects (
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    project_name TEXT NOT NULL,
    project_category INTEGER REFERENCES project_category(ID),
    description TEXT,
    date_start DATE, 
    date_end DATE 
    );
    
CREATE TABLE RESOURCE_AUTHOR(  
    resourceID INTEGER,
    authorID INTEGER,
    PRIMARY KEY (resourceID, authorID)
    );    


CREATE TABLE RESOURCE_KEYWORDS(
    resourceID INTEGER,
    keywordID INTEGER,
    PRIMARY KEY(resourceID, keywordID)
    );

CREATE TABLE PROJECT_REFERENCES(
    projectID INTEGER,
    resourceID INTEGER,
    PRIMARY KEY (projectID, resourceID)
    );
    
CREATE TABLE reading_now(
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    resourceID INTEGER REFERENCES resource(ID),
    date_start DATE, 
    date_end DATE
    );


    ''')

db.commit()
db.close()

