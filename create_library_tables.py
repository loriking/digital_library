# -*- coding: utf-8 -*-
"""
Created on Sun Jan 1 15:38:30 2017

author: lak
"""

import sqlite3

conn = sqlite3.connect('library_data.db')
cur = conn.cursor()

cur.executescript('''
PRAGMA Foreign_Keys=True;

DROP TABLE IF EXISTS languages;
DROP TABLE IF EXISTS keywords;
DROP TABLE IF EXISTS authors;
DROP TABLE IF EXISTS publishers;
DROP TABLE IF EXISTS item_type;
DROP TABLE IF EXISTS items;

DROP TABLE IF EXISTS ITEM_AUTHOR;
DROP TABLE IF EXISTS ITEM_KEYWORDS;

DROP TABLE IF EXISTS projects;
DROP TABLE IF EXISTS reading_now;
DROP TABLE IF EXISTS code_project_references;


CREATE TABLE languages (
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    language TEXT
    );

CREATE TABLE item_type (
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    type TEXT UNIQUE
    );
    
CREATE TABLE keywords (
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    keyword TEXT
    );
    
CREATE TABLE authors (
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    author_name TEXT 
    );

CREATE TABLE publishers (
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    publisher TEXT
    );

CREATE TABLE items (
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    item_title TEXT UNIQUE,
    year INTEGER,
    pages INTEGER,
    languageID INTEGER REFERENCES languages(ID),
    item_typeID INTEGER REFERENCES item_type(ID),
    item_publisherID INTEGER REFERENCES publishers(ID),
    abstract TEXT
    );

CREATE TABLE projects (
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    project_name TEXT,
    languageID INTEGER REFERENCES languages(ID),
    item_typeID INTEGER REFERENCES item_type(ID),
    abstract TEXT,
    date_start DATE, 
    date_end DATE 
    );
    
CREATE TABLE ITEM_AUTHOR(  
    itemID INTEGER,
    authorID INTEGER,
    primary key (itemID, authorID)
    );    


CREATE TABLE ITEM_KEYWORDS(
    itemID INTEGER,
    keywordID INTEGER,
    primary key (itemID, keywordID)
    );    
    
CREATE TABLE reading_now(
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    itemID INTEGER REFERENCES items(ID),
    date_start DATE, 
    date_end DATE
    );

CREATE TABLE project_references (
    itemID INTEGER,
    projectID INTEGER,
    primary key (itemID, projectID)
    );

    ''')


