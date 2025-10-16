-- =============================================
-- Файл: db.sql
-- База данных: messenger
-- Автор: Гриценко Г.М.
-- Дата: 16.10.2025
-- =============================================

-- Конфиги
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL';

-- Пересоздаём базу данных
DROP DATABASE IF EXISTS messenger;
CREATE DATABASE messenger;
USE messenger;

-- Создание независимых таблиц

-- Пользователи
CREATE TABLE users (
    id VARCHAR(100) PRIMARY KEY,
    username VARCHAR(30) NOT NULL,
    email VARCHAR(50) UNIQUE NOT NULL,
    pwd VARCHAR(200) NOT NULL,
    createdAt DATETIME,
    editedAt DATETIME
);

-- Посты
CREATE TABLE posts (
    id VARCHAR(100) PRIMARY KEY,
    authorId VARCHAR(50) NOT NULL,
    title TEXT NOT NULL,
    content TEXT,
    createdAt DATETIME,
    editedAt DATETIME
);

-- Зависимые таблицы

-- Хэштеги
CREATE TABLE hashtags (
    postId VARCHAR(100),
    tags TEXT
);

-- Избранное
CREATE TABLE saved (
    userId VARCHAR(100),
    posts TEXT
);

-- Подписки
CREATE TABLE subscriptions (
    userId VARCHAR(100),
    subscriptions TEXT
);

-- Комментарии
CREATE TABLE comments (
    id VARCHAR(100) PRIMARY KEY,
    userId VARCHAR(100) NOT NULL,
    postId VARCHAR(100) NOT NULL,
    content TEXT NOT NULL
);
