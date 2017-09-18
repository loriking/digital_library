# -*- coding: utf-8 -*-
"""
Created on Sun Jan 1 15:38:30 2017

author: lak
"""

import sqlite3 

db = sqlite3.connect('library_data2.db')
c = db.cursor()

c.executescript('''
PRAGMA Foreign_Keys=True;

DROP TABLE IF EXISTS languages;
DROP TABLE IF EXISTS keywords;
DROP TABLE IF EXISTS authors;
DROP TABLE IF EXISTS publishers;
DROP TABLE IF EXISTS resource_type;
DROP TABLE IF EXISTS resource;

DROP TABLE IF EXISTS RESOURCE_AUTHOR;
DROP TABLE IF EXISTS RESOURCE_KEYWORDS;

DROP TABLE IF EXISTS projects;
DROP TABLE IF EXISTS reading_now;
DROP TABLE IF EXISTS project_references;


CREATE TABLE languages (
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    language TEXT
    );

CREATE TABLE resource_type (
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    type TEXT UNIQUE
    );
    
CREATE TABLE keywords (
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    keyword TEXT
    );
    
CREATE TABLE authors (
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    first_name TEXT,
    middle_name TEXT,
    last_name TEXT
    );

CREATE TABLE publishers (
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    publisher TEXT
    );

CREATE TABLE resource (
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    year INTEGER,
    pages INTEGER,
    languageID INTEGER REFERENCES languages(ID),
    resource_typeID INTEGER REFERENCES resource_type(ID),
    publisherID INTEGER REFERENCES publishers(ID),
    abstract TEXT
    );

CREATE TABLE projects (
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    project_name TEXT,
    languageID INTEGER REFERENCES languages(ID),
    resource_typeID INTEGER REFERENCES resource_type(ID),
    abstract TEXT,
    date_start DATE, 
    date_end DATE 
    );
    
CREATE TABLE RESOURCE_AUTHOR(  
    resourceID INTEGER,
    authorID INTEGER,
    primary key (resourceID, authorID)
    );    


CREATE TABLE RESOURCE_KEYWORDS(
    resourceID INTEGER,
    keywordID INTEGER,
    primary key (resourceID, keywordID)
    );    
    
CREATE TABLE reading_now(
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    resourceID INTEGER REFERENCES resource(ID),
    date_start DATE, 
    date_end DATE
    );

CREATE TABLE project_references (
    resourceID INTEGER,
    projectID INTEGER,
    primary key (resourceID, projectID)
    );

    ''')

db.commit()
db.close()

