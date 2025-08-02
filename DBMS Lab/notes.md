# Complete MySQL Tutorial: A to Z Guide

## Table of Contents

1. [Installation & Setup](#installation--setup)
2. [Getting Started](#getting-started)
3. [User Management](#user-management)
4. [Database Basics](#database-basics)
5. [Table Operations](#table-operations)
6. [Data Types](#data-types)
7. [CRUD Operations](#crud-operations)
8. [Queries & Filtering](#queries--filtering)
9. [Joins](#joins)
10. [Functions & Operators](#functions--operators)
11. [Constraints & Keys](#constraints--keys)
12. [Indexes](#indexes)
13. [Views](#views)
14. [Stored Procedures](#stored-procedures)
15. [Triggers](#triggers)
16. [Backup & Restore](#backup--restore)
17. [Performance Optimization](#performance-optimization)
18. [MySQL Workbench](#mysql-workbench)

---

## 1. Installation & Setup

### Ubuntu/Debian Installation

```bash
# Update package list
sudo apt update

# Install MySQL Server
sudo apt install mysql-server

# Secure installation
sudo mysql_secure_installation

# Start MySQL service
sudo systemctl start mysql

# Enable MySQL to start on boot
sudo systemctl enable mysql

# Check status
sudo systemctl status mysql
```

### CentOS/RHEL/Fedora Installation

```bash
# Install MySQL
sudo yum install mysql-server
# or for newer versions
sudo dnf install mysql-server

# Start and enable
sudo systemctl start mysqld
sudo systemctl enable mysqld

# Get temporary root password
sudo grep 'temporary password' /var/log/mysqld.log

# Secure installation
sudo mysql_secure_installation
```

### macOS Installation

```bash
# Using Homebrew
brew install mysql

# Start MySQL
brew services start mysql

# Secure installation
mysql_secure_installation
```

### Windows Installation

1. Download MySQL Installer from mysql.com
2. Run the installer
3. Choose "Server only" or "Full" installation
4. Configure root password
5. Start MySQL service

---

## 2. Getting Started

### Connecting to MySQL

```bash
# Connect as root
mysql -u root -p

# Connect to specific database
mysql -u username -p database_name

# Connect to remote server
mysql -h hostname -u username -p

# Connect with specific port
mysql -h hostname -P 3306 -u username -p

# Using socket (Linux/macOS)
sudo mysql

# Exit MySQL
EXIT;
# or
\q
```

### Basic Commands

```sql
-- Show MySQL version
SELECT VERSION();

-- Show current date and time
SELECT NOW();

-- Show current user
SELECT USER();

-- Show current database
SELECT DATABASE();

-- Show all databases
SHOW DATABASES;

-- Show MySQL status
\s

-- Clear screen
\c

-- Help
\h
-- or
HELP;
```

---

## 3. User Management

### Creating Users

```sql
-- Create new user
CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';

-- Create user for any host
CREATE USER 'username'@'%' IDENTIFIED BY 'password';

-- Create user for specific host
CREATE USER 'username'@'192.168.1.100' IDENTIFIED BY 'password';
```

### Granting Privileges

```sql
-- Grant all privileges on all databases
GRANT ALL PRIVILEGES ON *.* TO 'username'@'localhost';

-- Grant all privileges on specific database
GRANT ALL PRIVILEGES ON database_name.* TO 'username'@'localhost';

-- Grant specific privileges
GRANT SELECT, INSERT, UPDATE ON database_name.table_name TO 'username'@'localhost';

-- Grant with GRANT OPTION (user can grant privileges to others)
GRANT ALL PRIVILEGES ON *.* TO 'username'@'localhost' WITH GRANT OPTION;

-- Apply changes
FLUSH PRIVILEGES;
```

### Viewing Privileges

```sql
-- Show privileges for current user
SHOW GRANTS;

-- Show privileges for specific user
SHOW GRANTS FOR 'username'@'localhost';

-- Show all users
SELECT User, Host FROM mysql.user;
```

### Modifying Users

```sql
-- Change password
ALTER USER 'username'@'localhost' IDENTIFIED BY 'new_password';

-- Rename user
RENAME USER 'old_username'@'localhost' TO 'new_username'@'localhost';

-- Remove privileges
REVOKE ALL PRIVILEGES ON *.* FROM 'username'@'localhost';

-- Drop user
DROP USER 'username'@'localhost';
```

---

## 4. Database Basics

### Creating Databases

```sql
-- Create database
CREATE DATABASE database_name;

-- Create database with specific charset
CREATE DATABASE database_name CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Create database if not exists
CREATE DATABASE IF NOT EXISTS database_name;
```

### Using Databases

```sql
-- Use database
USE database_name;

-- Show current database
SELECT DATABASE();

-- Show all databases
SHOW DATABASES;
```

### Database Information

```sql
-- Show database creation statement
SHOW CREATE DATABASE database_name;

-- Show database size
SELECT
    table_schema AS 'Database',
    ROUND(SUM(data_length + index_length) / 1024 / 1024, 2) AS 'Size (MB)'
FROM information_schema.tables
WHERE table_schema = 'database_name';
```

### Dropping Databases

```sql
-- Drop database
DROP DATABASE database_name;

-- Drop database if exists
DROP DATABASE IF EXISTS database_name;
```

---

## 5. Table Operations

### Creating Tables

```sql
-- Basic table creation
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    column3 datatype
);

-- Example: Students table
CREATE TABLE students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    age INT CHECK (age >= 18),
    enrollment_date DATE DEFAULT (CURRENT_DATE),
    gpa DECIMAL(3,2) DEFAULT 0.00
);
```

### Table Information

```sql
-- Show tables in database
SHOW TABLES;

-- Describe table structure
DESCRIBE table_name;
-- or
DESC table_name;

-- Show table creation statement
SHOW CREATE TABLE table_name;

-- Show table status
SHOW TABLE STATUS LIKE 'table_name';
```

### Modifying Tables

```sql
-- Add column
ALTER TABLE table_name ADD COLUMN column_name datatype;

-- Add column with position
ALTER TABLE table_name ADD COLUMN column_name datatype AFTER existing_column;
ALTER TABLE table_name ADD COLUMN column_name datatype FIRST;

-- Modify column
ALTER TABLE table_name MODIFY COLUMN column_name new_datatype;

-- Change column name and type
ALTER TABLE table_name CHANGE old_column_name new_column_name datatype;

-- Drop column
ALTER TABLE table_name DROP COLUMN column_name;

-- Rename table
ALTER TABLE old_table_name RENAME TO new_table_name;
-- or
RENAME TABLE old_table_name TO new_table_name;
```

### Dropping Tables

```sql
-- Drop table
DROP TABLE table_name;

-- Drop table if exists
DROP TABLE IF EXISTS table_name;

-- Drop multiple tables
DROP TABLE table1, table2, table3;

-- Truncate table (delete all data, keep structure)
TRUNCATE TABLE table_name;
```

---

## 6. Data Types

### Numeric Types

```sql
-- Integer types
TINYINT     -- 1 byte (-128 to 127)
SMALLINT    -- 2 bytes (-32,768 to 32,767)
MEDIUMINT   -- 3 bytes (-8,388,608 to 8,388,607)
INT         -- 4 bytes (-2,147,483,648 to 2,147,483,647)
BIGINT      -- 8 bytes (very large range)

-- Unsigned (positive only)
INT UNSIGNED

-- Decimal types
DECIMAL(precision, scale)  -- Exact decimal
FLOAT(precision, scale)    -- Approximate decimal
DOUBLE(precision, scale)   -- Double precision

-- Examples
price DECIMAL(10,2)        -- 99999999.99
temperature FLOAT(5,2)     -- 999.99
```

### String Types

```sql
-- Fixed length
CHAR(length)               -- Fixed length string

-- Variable length
VARCHAR(length)            -- Variable length string (up to 65,535 chars)
TEXT                       -- Large text (up to 65,535 chars)
MEDIUMTEXT                 -- Medium text (up to 16,777,215 chars)
LONGTEXT                   -- Long text (up to 4,294,967,295 chars)

-- Binary data
BINARY(length)             -- Fixed binary data
VARBINARY(length)          -- Variable binary data
BLOB                       -- Binary large object

-- Examples
name VARCHAR(100)
description TEXT
profile_picture BLOB
```

### Date and Time Types

```sql
DATE                       -- YYYY-MM-DD
TIME                       -- HH:MM:SS
DATETIME                   -- YYYY-MM-DD HH:MM:SS
TIMESTAMP                  -- YYYY-MM-DD HH:MM:SS (auto-updating)
YEAR                       -- YYYY

-- Examples
birth_date DATE
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
```

### Other Types

```sql
-- Boolean (stored as TINYINT)
BOOLEAN                    -- TRUE/FALSE

-- Enumeration
ENUM('value1', 'value2', 'value3')

-- Set (multiple values)
SET('value1', 'value2', 'value3')

-- JSON (MySQL 5.7+)
JSON

-- Examples
is_active BOOLEAN DEFAULT TRUE
status ENUM('active', 'inactive', 'pending')
permissions SET('read', 'write', 'execute')
metadata JSON
```

---

## 7. CRUD Operations

### CREATE (Insert Data)

```sql
-- Insert single row
INSERT INTO table_name (column1, column2, column3)
VALUES (value1, value2, value3);

-- Insert multiple rows
INSERT INTO table_name (column1, column2, column3)
VALUES
    (value1, value2, value3),
    (value4, value5, value6),
    (value7, value8, value9);

-- Insert with auto-increment
INSERT INTO students (first_name, last_name, email)
VALUES ('John', 'Doe', 'john.doe@email.com');

-- Insert from another table
INSERT INTO table1 (column1, column2)
SELECT column1, column2 FROM table2 WHERE condition;

-- Insert or ignore duplicates
INSERT IGNORE INTO table_name (columns) VALUES (values);

-- Insert or update on duplicate
INSERT INTO table_name (id, name, email)
VALUES (1, 'John', 'john@email.com')
ON DUPLICATE KEY UPDATE
    name = VALUES(name),
    email = VALUES(email);
```

### READ (Select Data)

```sql
-- Select all columns
SELECT * FROM table_name;

-- Select specific columns
SELECT column1, column2 FROM table_name;

-- Select with alias
SELECT first_name AS name, email AS contact FROM students;

-- Select distinct values
SELECT DISTINCT column_name FROM table_name;

-- Select with limit
SELECT * FROM table_name LIMIT 10;
SELECT * FROM table_name LIMIT 10 OFFSET 20;  -- Skip first 20 rows

-- Select with conditions
SELECT * FROM students WHERE age > 20;
SELECT * FROM students WHERE name LIKE 'John%';
SELECT * FROM students WHERE age BETWEEN 18 AND 25;
SELECT * FROM students WHERE major IN ('Computer Science', 'Mathematics');
```

### UPDATE (Modify Data)

```sql
-- Update single column
UPDATE table_name SET column1 = value1 WHERE condition;

-- Update multiple columns
UPDATE table_name
SET column1 = value1, column2 = value2
WHERE condition;

-- Update with calculation
UPDATE students SET gpa = gpa + 0.1 WHERE gpa < 3.0;

-- Update from another table
UPDATE table1 t1
JOIN table2 t2 ON t1.id = t2.id
SET t1.column1 = t2.column1
WHERE condition;

-- Update all rows (be careful!)
UPDATE table_name SET column1 = value1;
```

### DELETE (Remove Data)

```sql
-- Delete specific rows
DELETE FROM table_name WHERE condition;

-- Delete with joins
DELETE t1 FROM table1 t1
JOIN table2 t2 ON t1.id = t2.id
WHERE condition;

-- Delete all rows (keep table structure)
DELETE FROM table_name;

-- Truncate (faster than DELETE for all rows)
TRUNCATE TABLE table_name;
```

---

## 8. Queries & Filtering

### WHERE Clause

```sql
-- Comparison operators
SELECT * FROM students WHERE age = 20;
SELECT * FROM students WHERE age != 20;
SELECT * FROM students WHERE age <> 20;  -- Same as !=
SELECT * FROM students WHERE age > 20;
SELECT * FROM students WHERE age >= 20;
SELECT * FROM students WHERE age < 20;
SELECT * FROM students WHERE age <= 20;

-- Logical operators
SELECT * FROM students WHERE age > 18 AND gpa > 3.0;
SELECT * FROM students WHERE major = 'CS' OR major = 'Math';
SELECT * FROM students WHERE NOT age < 18;

-- Range and pattern matching
SELECT * FROM students WHERE age BETWEEN 18 AND 25;
SELECT * FROM students WHERE name LIKE 'John%';      -- Starts with 'John'
SELECT * FROM students WHERE name LIKE '%son';      -- Ends with 'son'
SELECT * FROM students WHERE name LIKE '%oh%';      -- Contains 'oh'
SELECT * FROM students WHERE name LIKE 'J_hn';      -- Single character wildcard

-- IN and NOT IN
SELECT * FROM students WHERE major IN ('CS', 'Math', 'Physics');
SELECT * FROM students WHERE major NOT IN ('Art', 'Music');

-- NULL checks
SELECT * FROM students WHERE phone IS NULL;
SELECT * FROM students WHERE phone IS NOT NULL;
```

### ORDER BY

```sql
-- Sort ascending (default)
SELECT * FROM students ORDER BY last_name;
SELECT * FROM students ORDER BY last_name ASC;

-- Sort descending
SELECT * FROM students ORDER BY gpa DESC;

-- Multiple columns
SELECT * FROM students ORDER BY major ASC, gpa DESC;

-- Sort by column position
SELECT first_name, last_name, gpa FROM students ORDER BY 3 DESC;
```

### GROUP BY and HAVING

```sql
-- Group by single column
SELECT major, COUNT(*) as student_count
FROM students
GROUP BY major;

-- Group by multiple columns
SELECT major, year_level, COUNT(*) as count
FROM students
GROUP BY major, year_level;

-- Group with aggregate functions
SELECT major, AVG(gpa) as avg_gpa, MAX(gpa) as max_gpa, MIN(gpa) as min_gpa
FROM students
GROUP BY major;

-- HAVING (filter groups)
SELECT major, COUNT(*) as student_count
FROM students
GROUP BY major
HAVING COUNT(*) > 5;

-- GROUP BY with ORDER BY
SELECT major, AVG(gpa) as avg_gpa
FROM students
GROUP BY major
ORDER BY avg_gpa DESC;
```

### LIMIT and OFFSET

```sql
-- Limit results
SELECT * FROM students LIMIT 10;

-- Pagination
SELECT * FROM students LIMIT 10 OFFSET 20;  -- Skip 20, take 10
SELECT * FROM students LIMIT 20, 10;        -- MySQL syntax (offset, limit)
```

---

## 9. Joins

### Sample Tables for Join Examples

```sql
-- Students table
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    major_id INT
);

-- Majors table
CREATE TABLE majors (
    major_id INT PRIMARY KEY,
    major_name VARCHAR(50)
);

-- Enrollments table
CREATE TABLE enrollments (
    enrollment_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    grade CHAR(2)
);
```

### INNER JOIN

```sql
-- Basic inner join
SELECT s.name, m.major_name
FROM students s
INNER JOIN majors m ON s.major_id = m.major_id;

-- Multiple table join
SELECT s.name, m.major_name, e.grade
FROM students s
INNER JOIN majors m ON s.major_id = m.major_id
INNER JOIN enrollments e ON s.student_id = e.student_id;
```

### LEFT JOIN (LEFT OUTER JOIN)

```sql
-- Include all students, even without majors
SELECT s.name, m.major_name
FROM students s
LEFT JOIN majors m ON s.major_id = m.major_id;

-- Find students without majors
SELECT s.name
FROM students s
LEFT JOIN majors m ON s.major_id = m.major_id
WHERE m.major_id IS NULL;
```

### RIGHT JOIN (RIGHT OUTER JOIN)

```sql
-- Include all majors, even without students
SELECT s.name, m.major_name
FROM students s
RIGHT JOIN majors m ON s.major_id = m.major_id;
```

### FULL OUTER JOIN (MySQL doesn't support directly)

```sql
-- Simulate full outer join with UNION
SELECT s.name, m.major_name
FROM students s
LEFT JOIN majors m ON s.major_id = m.major_id
UNION
SELECT s.name, m.major_name
FROM students s
RIGHT JOIN majors m ON s.major_id = m.major_id;
```

### CROSS JOIN

```sql
-- Cartesian product (every combination)
SELECT s.name, m.major_name
FROM students s
CROSS JOIN majors m;
```

### SELF JOIN

```sql
-- Employees table with manager relationship
SELECT e1.name as employee, e2.name as manager
FROM employees e1
LEFT JOIN employees e2 ON e1.manager_id = e2.employee_id;
```

---

## 10. Functions & Operators

### Aggregate Functions

```sql
-- Count
SELECT COUNT(*) FROM students;                    -- Count all rows
SELECT COUNT(phone) FROM students;               -- Count non-null values
SELECT COUNT(DISTINCT major) FROM students;      -- Count unique values

-- Sum, Average, Min, Max
SELECT SUM(salary) FROM employees;
SELECT AVG(gpa) FROM students;
SELECT MIN(age), MAX(age) FROM students;

-- Group concat
SELECT GROUP_CONCAT(name) FROM students;
SELECT GROUP_CONCAT(name SEPARATOR '; ') FROM students;
```

### String Functions

```sql
-- String manipulation
SELECT CONCAT(first_name, ' ', last_name) as full_name FROM students;
SELECT CONCAT_WS(' - ', first_name, last_name, email) FROM students;

-- Case conversion
SELECT UPPER(name), LOWER(name) FROM students;

-- String length and substring
SELECT LENGTH(name), CHAR_LENGTH(name) FROM students;
SELECT SUBSTRING(name, 1, 3) FROM students;      -- First 3 characters
SELECT LEFT(name, 3), RIGHT(name, 3) FROM students;

-- Trim and pad
SELECT TRIM(name), LTRIM(name), RTRIM(name) FROM students;
SELECT LPAD(name, 10, '*'), RPAD(name, 10, '*') FROM students;

-- Replace and locate
SELECT REPLACE(email, '@', ' AT ') FROM students;
SELECT LOCATE('@', email) FROM students;

-- String comparison
SELECT * FROM students WHERE name SOUNDS LIKE 'John';
```

### Numeric Functions

```sql
-- Mathematical functions
SELECT ABS(-5), CEIL(4.3), FLOOR(4.7), ROUND(4.567, 2);
SELECT SQRT(25), POWER(2, 3), MOD(10, 3);

-- Random
SELECT RAND(), ROUND(RAND() * 100);
```

### Date and Time Functions

```sql
-- Current date and time
SELECT NOW(), CURDATE(), CURTIME();
SELECT CURRENT_TIMESTAMP, CURRENT_DATE, CURRENT_TIME;

-- Date formatting
SELECT DATE_FORMAT(NOW(), '%Y-%m-%d %H:%i:%s');
SELECT DATE_FORMAT(birth_date, '%M %d, %Y') FROM students;

-- Date arithmetic
SELECT DATE_ADD(NOW(), INTERVAL 7 DAY);
SELECT DATE_SUB(NOW(), INTERVAL 1 MONTH);
SELECT DATEDIFF(NOW(), birth_date) as days_old FROM students;

-- Extract parts
SELECT YEAR(birth_date), MONTH(birth_date), DAY(birth_date) FROM students;
SELECT DAYNAME(birth_date), MONTHNAME(birth_date) FROM students;

-- Age calculation
SELECT name, birth_date,
       TIMESTAMPDIFF(YEAR, birth_date, CURDATE()) as age
FROM students;
```

### Conditional Functions

```sql
-- IF function
SELECT name, IF(gpa >= 3.5, 'Honor', 'Regular') as status FROM students;

-- CASE statement
SELECT name, gpa,
    CASE
        WHEN gpa >= 3.8 THEN 'Excellent'
        WHEN gpa >= 3.5 THEN 'Good'
        WHEN gpa >= 3.0 THEN 'Average'
        ELSE 'Below Average'
    END as grade_status
FROM students;

-- COALESCE (return first non-null value)
SELECT name, COALESCE(phone, email, 'No contact') as contact FROM students;

-- NULLIF (return NULL if two values are equal)
SELECT NULLIF(gpa, 0) FROM students;
```

---

## 11. Constraints & Keys

### Primary Key

```sql
-- Single column primary key
CREATE TABLE students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50)
);

-- Composite primary key
CREATE TABLE enrollments (
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    PRIMARY KEY (student_id, course_id)
);

-- Add primary key to existing table
ALTER TABLE table_name ADD PRIMARY KEY (column_name);

-- Drop primary key
ALTER TABLE table_name DROP PRIMARY KEY;
```

### Foreign Key

```sql
-- Foreign key in CREATE TABLE
CREATE TABLE enrollments (
    enrollment_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- Foreign key with constraints
CREATE TABLE enrollments (
    enrollment_id INT PRIMARY KEY,
    student_id INT,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- Add foreign key to existing table
ALTER TABLE enrollments
ADD CONSTRAINT fk_student
FOREIGN KEY (student_id) REFERENCES students(student_id);

-- Drop foreign key
ALTER TABLE enrollments DROP FOREIGN KEY fk_student;
```

### UNIQUE Constraint

```sql
-- Unique constraint in CREATE TABLE
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    email VARCHAR(100) UNIQUE,
    ssn VARCHAR(11) UNIQUE
);

-- Composite unique constraint
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    birth_date DATE,
    UNIQUE KEY unique_student (first_name, last_name, birth_date)
);

-- Add unique constraint
ALTER TABLE students ADD UNIQUE (email);
ALTER TABLE students ADD CONSTRAINT uk_email UNIQUE (email);

-- Drop unique constraint
ALTER TABLE students DROP INDEX email;
```

### NOT NULL Constraint

```sql
-- NOT NULL in CREATE TABLE
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

-- Add NOT NULL to existing column
ALTER TABLE students MODIFY COLUMN email VARCHAR(100) NOT NULL;

-- Remove NOT NULL
ALTER TABLE students MODIFY COLUMN phone VARCHAR(15);
```

### CHECK Constraint (MySQL 8.0+)

```sql
-- CHECK constraint in CREATE TABLE
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    age INT CHECK (age >= 18 AND age <= 65),
    gpa DECIMAL(3,2) CHECK (gpa >= 0.0 AND gpa <= 4.0),
    email VARCHAR(100) CHECK (email LIKE '%@%.%')
);

-- Add CHECK constraint
ALTER TABLE students ADD CONSTRAINT chk_age CHECK (age >= 18);

-- Drop CHECK constraint
ALTER TABLE students DROP CHECK chk_age;
```

### DEFAULT Values

```sql
-- DEFAULT in CREATE TABLE
CREATE TABLE students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    enrollment_date DATE DEFAULT (CURRENT_DATE),
    status ENUM('active', 'inactive') DEFAULT 'active',
    credits INT DEFAULT 0
);

-- Add DEFAULT to existing column
ALTER TABLE students ALTER COLUMN status SET DEFAULT 'active';

-- Remove DEFAULT
ALTER TABLE students ALTER COLUMN status DROP DEFAULT;
```

---

## 12. Indexes

### Creating Indexes

```sql
-- Simple index
CREATE INDEX idx_lastname ON students (last_name);

-- Composite index
CREATE INDEX idx_name ON students (last_name, first_name);

-- Unique index
CREATE UNIQUE INDEX idx_email ON students (email);

-- Index with length (for long strings)
CREATE INDEX idx_description ON articles (description(100));

-- Functional index (MySQL 8.0+)
CREATE INDEX idx_upper_name ON students ((UPPER(last_name)));
```

### Viewing Indexes

```sql
-- Show indexes for a table
SHOW INDEX FROM table_name;

-- Show index usage
SHOW INDEX FROM students WHERE Key_name = 'idx_lastname';

-- Index information from information_schema
SELECT * FROM information_schema.statistics
WHERE table_name = 'students';
```

### Dropping Indexes

```sql
-- Drop index
DROP INDEX idx_lastname ON students;

-- Alternative syntax
ALTER TABLE students DROP INDEX idx_lastname;
```

### Index Types

```sql
-- B-Tree index (default)
CREATE INDEX idx_name ON students (name) USING BTREE;

-- Hash index (MEMORY engine only)
CREATE INDEX idx_id ON students (id) USING HASH;

-- Full-text index
CREATE FULLTEXT INDEX idx_content ON articles (title, content);

-- Spatial index (for geometry data)
CREATE SPATIAL INDEX idx_location ON places (coordinates);
```

### Query Optimization with Indexes

```sql
-- Use EXPLAIN to see query execution plan
EXPLAIN SELECT * FROM students WHERE last_name = 'Smith';

-- Force index usage
SELECT * FROM students FORCE INDEX (idx_lastname) WHERE last_name = 'Smith';

-- Ignore index
SELECT * FROM students IGNORE INDEX (idx_lastname) WHERE last_name = 'Smith';
```

---

## 13. Views

### Creating Views

```sql
-- Simple view
CREATE VIEW active_students AS
SELECT student_id, first_name, last_name, email
FROM students
WHERE status = 'active';

-- Complex view with joins
CREATE VIEW student_courses AS
SELECT
    s.student_id,
    CONCAT(s.first_name, ' ', s.last_name) as student_name,
    c.course_name,
    e.grade
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
JOIN courses c ON e.course_id = c.course_id;

-- View with aggregation
CREATE VIEW student_stats AS
SELECT
    major,
    COUNT(*) as student_count,
    AVG(gpa) as average_gpa,
    MAX(gpa) as highest_gpa
FROM students
GROUP BY major;
```

### Using Views

```sql
-- Query view like a table
SELECT * FROM active_students;
SELECT * FROM student_courses WHERE grade = 'A';

-- Views in joins
SELECT s.student_name, ss.average_gpa
FROM student_courses s
JOIN student_stats ss ON s.major = ss.major;
```

### Managing Views

```sql
-- Show views
SHOW TABLES;  -- Views appear with tables
SHOW FULL TABLES WHERE Table_type = 'VIEW';

-- View definition
SHOW CREATE VIEW view_name;

-- Modify view
CREATE OR REPLACE VIEW active_students AS
SELECT student_id, first_name, last_name, email, gpa
FROM students
WHERE status = 'active' AND gpa >= 2.0;

-- Drop view
DROP VIEW view_name;
DROP VIEW IF EXISTS view_name;
```

### Updatable Views

```sql
-- Simple updatable view
CREATE VIEW active_students AS
SELECT student_id, first_name, last_name, email
FROM students
WHERE status = 'active'
WITH CHECK OPTION;

-- Update through view
UPDATE active_students SET email = 'new@email.com' WHERE student_id = 1;

-- Insert through view
INSERT INTO active_students (first_name, last_name, email)
VALUES ('John', 'Doe', 'john@email.com');
```

---

## 14. Stored Procedures

### Creating Stored Procedures

```sql
-- Change delimiter for procedure definition
DELIMITER //

-- Simple procedure
CREATE PROCEDURE GetStudentCount()
BEGIN
    SELECT COUNT(*) as total_students FROM students;
END //

-- Procedure with parameters
CREATE PROCEDURE GetStudentsByMajor(IN major_name VARCHAR(100))
BEGIN
    SELECT * FROM students WHERE major = major_name;
END //

-- Procedure with IN, OUT, and INOUT parameters
CREATE PROCEDURE GetStudentStats(
    IN major_name VARCHAR(100),
    OUT student_count INT,
    OUT avg_gpa DECIMAL(3,2)
)
BEGIN
    SELECT COUNT(*), AVG(gpa)
    INTO student_count, avg_gpa
    FROM students
    WHERE major = major_name;
END //

-- Restore delimiter
DELIMITER ;
```

### Calling Stored Procedures

```sql
-- Call simple procedure
CALL GetStudentCount();

-- Call with parameters
CALL GetStudentsByMajor('Computer Science');

-- Call with OUT parameters
CALL GetStudentStats('Computer Science', @count, @avg_gpa);
SELECT @count, @avg_gpa;
```

### Advanced Stored Procedures

```sql
DELIMITER //

CREATE PROCEDURE UpdateStudentGPA(
    IN student_id INT,
    IN new_gpa DECIMAL(3,2)
)
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE old_gpa DECIMAL(3,2);

    -- Get current GPA
    SELECT gpa INTO old_gpa FROM students WHERE id = student_id;

    -- Update GPA
    UPDATE students SET gpa = new_gpa WHERE id = student_id;

    -- Log the change
    INSERT INTO gpa_history (student_id, old_gpa, new_gpa, change_date)
    VALUES (student_id, old_gpa, new_gpa, NOW());

    SELECT 'GPA updated successfully' as message;
END //

DELIMITER ;
```

### Managing Stored Procedures

```sql
-- Show procedures
SHOW PROCEDURE STATUS;
SHOW PROCEDURE STATUS WHERE Db = 'university';

-- Show procedure definition
SHOW CREATE PROCEDURE procedure_name;

-- Drop procedure
DROP PROCEDURE procedure_name;
DROP PROCEDURE IF EXISTS procedure_name;
```

---

## 15. Triggers

### Creating Triggers

```sql
-- BEFORE INSERT trigger
DELIMITER //

CREATE TRIGGER before_student_insert
BEFORE INSERT ON students
FOR EACH ROW
BEGIN
    -- Automatically set enrollment date
    IF NEW.enrollment_date IS NULL THEN
        SET NEW.enrollment_date = CURDATE();
    END IF;

    -- Validate email format
    IF NEW.email NOT LIKE '%@%.%' THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Invalid email format';
    END IF;
END //

DELIMITER ;

-- AFTER INSERT trigger
DELIMITER //

CREATE TRIGGER after_student_insert
AFTER INSERT ON students
FOR EACH ROW
BEGIN
    -- Log new student enrollment
    INSERT INTO audit_log (table_name, operation, record_id, timestamp)
    VALUES ('students', 'INSERT', NEW.student_id, NOW());

    -- Send welcome email (placeholder)
    INSERT INTO email_queue (recipient, subject, body)
    VALUES (NEW.email, 'Welcome!', CONCAT('Welcome ', NEW.first_name, ' to our university!'));
END //

DELIMITER ;

-- BEFORE UPDATE trigger
DELIMITER //

CREATE TRIGGER before_student_update
BEFORE UPDATE ON students
FOR EACH ROW
BEGIN
    -- Prevent GPA from going negative
    IF NEW.gpa < 0 THEN
        SET NEW.gpa = 0;
    END IF;

    -- Update modified timestamp
    SET NEW.updated_at = NOW();
END //

DELIMITER ;

-- AFTER UPDATE trigger
DELIMITER //

CREATE TRIGGER after_student_update
AFTER UPDATE ON students
FOR EACH ROW
BEGIN
    -- Log changes to audit table
    INSERT INTO student_audit (
        student_id,
        old_gpa,
        new_gpa,
        changed_by,
        change_date
    )
    VALUES (
        NEW.student_id,
        OLD.gpa,
        NEW.gpa,
        USER(),
        NOW()
    );
END //

DELIMITER ;

-- BEFORE DELETE trigger
DELIMITER //

CREATE TRIGGER before_student_delete
BEFORE DELETE ON students
FOR EACH ROW
BEGIN
    -- Archive student data before deletion
    INSERT INTO deleted_students (
        student_id, first_name, last_name, email, deletion_date
    )
    VALUES (
        OLD.student_id, OLD.first_name, OLD.last_name, OLD.email, NOW()
    );
END //

DELIMITER ;
```

### Managing Triggers

```sql
-- Show triggers
SHOW TRIGGERS;
SHOW TRIGGERS FROM database_name;
SHOW TRIGGERS LIKE 'student%';

-- Show trigger definition
SHOW CREATE TRIGGER trigger_name;

-- Drop trigger
DROP TRIGGER trigger_name;
DROP TRIGGER IF EXISTS trigger_name;

-- Disable/Enable triggers (MySQL doesn't support directly)
-- You need to drop and recreate
```

---

## 16. Backup & Restore

### mysqldump - Database Backup

```bash
# Backup single database
mysqldump -u username -p database_name > backup.sql

# Backup multiple databases
mysqldump -u username -p --databases db1 db2 db3 > backup.sql

# Backup all databases
mysqldump -u username -p --all-databases > all_backup.sql

# Backup specific tables
mysqldump -u username -p database_name table1 table2 > tables_backup.sql

# Backup with compression
mysqldump -u username -p database_name | gzip > backup.sql.gz

# Backup structure only (no data)
mysqldump -u username -p --no-data database_name > structure.sql

# Backup data only (no structure)
mysqldump -u username -p --no-create-info database_name > data.sql

# Backup with additional options
mysqldump -u username -p \
  --single-transaction \
  --routines \
  --triggers \
  --events \
  database_name > complete_backup.sql
```

### Restore Database

```bash
# Restore database
mysql -u username -p database_name < backup.sql

# Restore compressed backup
gunzip < backup.sql.gz | mysql -u username -p database_name

# Restore all databases
mysql -u username -p < all_backup.sql

# Create database and restore
mysql -u username -p -e "CREATE DATABASE new_database;"
mysql -u username -p new_database < backup.sql
```

### Binary Log Backup (Point-in-time Recovery)

```sql
-- Enable binary logging (add to my.cnf)
-- log-bin=mysql-bin
-- server-id=1

-- Show binary logs
SHOW BINARY LOGS;

-- Show current binary log position
SHOW MASTER STATUS;

-- Backup binary logs
-- Use mysqlbinlog utility
```

```bash
# Extract SQL from binary log
mysqlbinlog mysql-bin.000001 > binlog.sql

# Point-in-time recovery
mysqlbinlog --start-datetime="2024-01-01 10:00:00" \
            --stop-datetime="2024-01-01 11:00:00" \
            mysql-bin.000001 | mysql -u username -p
```

### Automated Backup Script

```bash
#!/bin/bash
# backup_script.sh

# Configuration
DB_USER="backup_user"
DB_PASS="backup_password"
DB_NAME="university"
BACKUP_DIR="/var/backups/mysql"
DATE=$(date +%Y%m%d_%H%M%S)

# Create backup directory
mkdir -p $BACKUP_DIR

# Perform backup
mysqldump -u $DB_USER -p$DB_PASS \
  --single-transaction \
  --routines \
  --triggers \
  $DB_NAME > $BACKUP_DIR/${DB_NAME}_${DATE}.sql

# Compress backup
gzip $BACKUP_DIR/${DB_NAME}_${DATE}.sql

# Remove backups older than 7 days
find $BACKUP_DIR -name "*.sql.gz" -mtime +7 -delete

echo "Backup completed: ${DB_NAME}_${DATE}.sql.gz"
```

---

## 17. Performance Optimization

### Query Optimization

```sql
-- Use EXPLAIN to analyze queries
EXPLAIN SELECT * FROM students WHERE last_name = 'Smith';
EXPLAIN FORMAT=JSON SELECT * FROM students s JOIN courses c ON s.id = c.student_id;

-- Index optimization
-- Create indexes on frequently queried columns
CREATE INDEX idx_lastname ON students (last_name);
CREATE INDEX idx_email ON students (email);

-- Composite indexes for multi-column queries
CREATE INDEX idx_name_major ON students (last_name, first_name, major);

-- Avoid SELECT *
-- Bad
SELECT * FROM students WHERE gpa > 3.5;

-- Good
SELECT student_id, first_name, last_name FROM students WHERE gpa > 3.5;

-- Use LIMIT for large result sets
SELECT * FROM students ORDER BY gpa DESC LIMIT 10;

-- Optimize JOIN queries
-- Use proper indexes on JOIN columns
-- Keep JOIN conditions simple
SELECT s.name, c.course_name
FROM students s
INNER JOIN enrollments e ON s.student_id = e.student_id
INNER JOIN courses c ON e.course_id = c.course_id
WHERE s.gpa > 3.0;
```

### Database Configuration

```sql
-- Check current configuration
SHOW VARIABLES LIKE 'innodb%';
SHOW VARIABLES LIKE 'key_buffer_size';

-- Important variables to tune (in my.cnf):
-- [mysqld]
-- innodb_buffer_pool_size = 70% of available RAM
-- innodb_log_file_size = 256M
-- max_connections = 200
-- query_cache_size = 64M
-- key_buffer_size = 256M
```

### Monitoring and Analysis

```sql
-- Show processlist (active queries)
SHOW PROCESSLIST;
SHOW FULL PROCESSLIST;

-- Kill long-running query
KILL QUERY process_id;

-- Show engine status
SHOW ENGINE INNODB STATUS;

-- Query performance analysis
-- Enable slow query log (in my.cnf):
-- slow_query_log = 1
-- slow_query_log_file = /var/log/mysql/slow.log
-- long_query_time = 2

-- Show query cache statistics
SHOW STATUS LIKE 'Qcache%';

-- Show table statistics
SHOW TABLE STATUS LIKE 'students';

-- Analyze table
ANALYZE TABLE students;

-- Optimize table
OPTIMIZE TABLE students;
```

### Performance Best Practices

```sql
-- 1. Use appropriate data types
-- Bad: VARCHAR(255) for short strings
-- Good: VARCHAR(50) for names

-- 2. Normalize database design
-- Avoid data duplication
-- Use proper relationships

-- 3. Use transactions for consistency
START TRANSACTION;
INSERT INTO students (...) VALUES (...);
INSERT INTO enrollments (...) VALUES (...);
COMMIT;

-- 4. Batch operations
-- Bad: Multiple single INSERTs
INSERT INTO students (...) VALUES (...);
INSERT INTO students (...) VALUES (...);

-- Good: Single multi-row INSERT
INSERT INTO students (...) VALUES (...), (...), (...);

-- 5. Use prepared statements (in application code)
-- Prevents SQL injection and improves performance

-- 6. Regular maintenance
-- Update table statistics
ANALYZE TABLE students;

-- Defragment tables
OPTIMIZE TABLE students;

-- Check table integrity
CHECK TABLE students;
```

---

## 18. MySQL Workbench

### Connection Setup

```
1. Open MySQL Workbench
2. Click "+" next to "MySQL Connections"
3. Configure connection:
   - Connection Name: University DB
   - Hostname: 127.0.0.1 (or localhost)
   - Port: 3306
   - Username: root (or your username)
   - Password: (store in keychain/vault)
   - Default Schema: university
4. Test Connection
5. Click OK
```

### Workbench Features

#### Database Administration

```sql
-- Server Status Dashboard
-- Shows server performance metrics
-- CPU, memory, network usage
-- Active connections
-- Query statistics

-- User and Privileges Management
-- Create/modify users
-- Grant/revoke privileges
-- Password management

-- Import/Export Data
-- Table Data Import/Export Wizard
-- Dump projects
-- Result set export
```

#### SQL Development

```sql
-- Query Editor
-- Syntax highlighting
-- Auto-completion
-- Query execution
-- Result visualization

-- Visual Query Builder
-- Drag-and-drop query creation
-- Join visualization
-- Filter conditions

-- Schema Browser
-- Database/table navigation
-- Object information
-- Quick actions (edit, drop, etc.)
```

#### Database Design

```sql
-- EER (Enhanced Entity-Relationship) Diagrams
-- Visual database design
-- Forward/reverse engineering
-- Relationship management

-- Create EER Diagram:
-- 1. Database → Reverse Engineer
-- 2. Select connection and database
-- 3. Choose objects to include
-- 4. Generate diagram

-- Forward Engineering:
-- 1. Design database visually
-- 2. Database → Forward Engineer
-- 3. Generate SQL script
-- 4. Execute on server
```

#### Useful Workbench Shortcuts

```
Ctrl+T          - New query tab
Ctrl+Enter      - Execute query
Ctrl+Shift+R    - Execute current statement
Ctrl+B          - Format query
Ctrl+/          - Toggle comment
F5              - Refresh
Ctrl+Space      - Auto-complete
Ctrl+D          - Duplicate line
```

---

## Quick Reference Commands

### Connection & Database

```sql
-- Connect
mysql -u username -p

-- Database operations
SHOW DATABASES;
CREATE DATABASE db_name;
USE db_name;
DROP DATABASE db_name;
```

### Table Operations

```sql
-- Show and describe
SHOW TABLES;
DESCRIBE table_name;
SHOW CREATE TABLE table_name;

-- Create table
CREATE TABLE table_name (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL
);

-- Modify table
ALTER TABLE table_name ADD COLUMN new_col VARCHAR(50);
ALTER TABLE table_name DROP COLUMN col_name;
ALTER TABLE table_name MODIFY COLUMN col_name VARCHAR(100);
```

### Data Operations

```sql
-- Insert
INSERT INTO table_name (col1, col2) VALUES (val1, val2);

-- Select
SELECT * FROM table_name WHERE condition;
SELECT col1, col2 FROM table_name ORDER BY col1 LIMIT 10;

-- Update
UPDATE table_name SET col1 = val1 WHERE condition;

-- Delete
DELETE FROM table_name WHERE condition;
```

### Common Functions

```sql
-- Aggregate
COUNT(*), SUM(col), AVG(col), MIN(col), MAX(col)

-- String
CONCAT(str1, str2), UPPER(str), LOWER(str), LENGTH(str)

-- Date
NOW(), CURDATE(), DATE_FORMAT(date, format)

-- Conditional
IF(condition, true_val, false_val)
CASE WHEN condition THEN result END
```

---

## Troubleshooting Common Issues

### Connection Issues

```bash
# Check if MySQL is running
sudo systemctl status mysql

# Start MySQL
sudo systemctl start mysql

# Check port
netstat -tlnp | grep 3306

# Reset root password
sudo mysql_secure_installation
```

### Permission Issues

```sql
-- Check current user privileges
SHOW GRANTS;

-- Grant privileges
GRANT ALL PRIVILEGES ON database.* TO 'user'@'localhost';
FLUSH PRIVILEGES;
```

### Performance Issues

```sql
-- Check slow queries
SHOW PROCESSLIST;

-- Analyze query performance
EXPLAIN SELECT ...;

-- Check table status
SHOW TABLE STATUS;
```

### Data Issues

```sql
-- Check table for errors
CHECK TABLE table_name;

-- Repair table
REPAIR TABLE table_name;

-- Optimize table
OPTIMIZE TABLE table_name;
```
