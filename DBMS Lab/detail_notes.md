# 📘 Complete SQL for Backend Development - Detailed Guide with Examples

This comprehensive guide provides in-depth explanations and practical examples for every SQL concept needed for backend development.

---

## 🟢 1. SQL Fundamentals (Beginner Level)

### 📌 Core Concepts

#### Database Fundamentals
- **Database**: A structured collection of data stored electronically
- **Table**: A collection of related data organized in rows and columns
- **Row/Record**: A single entry in a table
- **Column/Field**: A specific attribute of data in a table
- **Schema**: The structure/blueprint of how data is organized

#### Relationships
- **1:1 (One-to-One)**: Each record in Table A relates to exactly one record in Table B
- **1:M (One-to-Many)**: One record in Table A can relate to multiple records in Table B
- **M:N (Many-to-Many)**: Multiple records in Table A can relate to multiple records in Table B

### 📘 Basic Operations with Examples

#### CREATE TABLE
```sql
-- Creating a users table
CREATE TABLE users (
    -- id: Primary key column that uniquely identifies each user
    -- INT: Integer data type (4 bytes, can hold -2,147,483,648 to 2,147,483,647)
    -- PRIMARY KEY: Makes this column the unique identifier for each row
    -- AUTO_INCREMENT: MySQL automatically generates next number (1, 2, 3, etc.)
    id INT PRIMARY KEY AUTO_INCREMENT,
    
    -- username: Store user's login name
    -- VARCHAR(50): Variable-length string, max 50 characters
    -- UNIQUE: No two users can have same username (creates unique index)
    -- NOT NULL: This field cannot be empty when inserting data
    username VARCHAR(50) UNIQUE NOT NULL,
    
    -- email: Store user's email address
    -- VARCHAR(100): Variable-length string, max 100 characters for email
    -- UNIQUE: Ensures no duplicate email addresses in system
    -- NOT NULL: Email is required for user registration
    email VARCHAR(100) UNIQUE NOT NULL,
    
    -- password_hash: Store encrypted/hashed password (never store plain text!)
    -- VARCHAR(255): Large enough for bcrypt, scrypt, or other hash algorithms
    -- NOT NULL: Password is mandatory for authentication
    password_hash VARCHAR(255) NOT NULL,
    
    -- created_at: Timestamp when user account was created
    -- TIMESTAMP: Date and time data type (YYYY-MM-DD HH:MM:SS)
    -- DEFAULT CURRENT_TIMESTAMP: Automatically set to current time on INSERT
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    -- updated_at: Timestamp when user data was last modified
    -- TIMESTAMP: Same as above
    -- DEFAULT CURRENT_TIMESTAMP: Set to current time on INSERT
    -- ON UPDATE CURRENT_TIMESTAMP: Automatically update when row is modified
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Creating a products table with foreign key
CREATE TABLE products (
    -- id: Primary key for products table
    -- AUTO_INCREMENT: MySQL assigns 1, 2, 3... automatically
    id INT PRIMARY KEY AUTO_INCREMENT,
    
    -- name: Product name/title
    -- VARCHAR(200): Up to 200 characters for product names
    -- NOT NULL: Product must have a name
    name VARCHAR(200) NOT NULL,
    
    -- description: Detailed product description
    -- TEXT: Can store up to 65,535 characters (larger than VARCHAR)
    -- No NOT NULL: Description is optional
    description TEXT,
    
    -- price: Product price in decimal format
    -- DECIMAL(10, 2): Total 10 digits, 2 after decimal (e.g., 12345678.99)
    -- NOT NULL: Product must have a price
    -- CHECK (price > 0): Constraint ensures price is always positive
    price DECIMAL(10, 2) NOT NULL CHECK (price > 0),
    
    -- category_id: Links to categories table
    -- INT: Same data type as categories.id for foreign key relationship
    -- Can be NULL if product doesn't belong to any category
    category_id INT,
    
    -- stock_quantity: How many items are in inventory
    -- INT: Whole numbers for counting items
    -- DEFAULT 0: If not specified, assume 0 items in stock
    stock_quantity INT DEFAULT 0,
    
    -- is_active: Whether product is available for sale
    -- BOOLEAN: TRUE/FALSE value (MySQL stores as TINYINT 0 or 1)
    -- DEFAULT TRUE: New products are active by default
    is_active BOOLEAN DEFAULT TRUE,
    
    -- created_by: Which user created this product
    -- INT: References users.id
    -- Can be NULL if user is deleted (see ON DELETE SET NULL below)
    created_by INT,
    
    -- created_at: When product was added to system
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    -- FOREIGN KEY constraint: Links created_by to users table
    -- created_by must exist in users.id or be NULL
    -- ON DELETE SET NULL: If user is deleted, set created_by to NULL
    FOREIGN KEY (created_by) REFERENCES users(id) ON DELETE SET NULL
);

-- Creating an orders table (many-to-many relationship)
CREATE TABLE orders (
    -- id: Unique identifier for each order
    id INT PRIMARY KEY AUTO_INCREMENT,
    
    -- user_id: Which user placed this order
    -- INT: Must match users.id data type
    -- NOT NULL: Every order must belong to a user
    user_id INT NOT NULL,
    
    -- total_amount: Total cost of the order
    -- DECIMAL(10, 2): Precise decimal for money (avoids floating point errors)
    -- NOT NULL: Order must have a total amount
    total_amount DECIMAL(10, 2) NOT NULL,
    
    -- status: Current state of the order
    -- ENUM: Restricts values to predefined list only
    -- DEFAULT 'pending': New orders start as pending
    status ENUM('pending', 'processing', 'shipped', 'delivered', 'cancelled') DEFAULT 'pending',
    
    -- order_date: When order was placed
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    -- FOREIGN KEY: Links user_id to users table
    -- ON DELETE CASCADE: If user is deleted, delete all their orders too
    -- (Alternative: ON DELETE SET NULL would keep orders but clear user_id)
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Junction table for many-to-many relationship
-- This table connects orders to products (one order can have multiple products)
CREATE TABLE order_items (
    -- id: Primary key for each order item
    id INT PRIMARY KEY AUTO_INCREMENT,
    
    -- order_id: Which order this item belongs to
    -- INT: Must match orders.id
    -- NOT NULL: Each item must belong to an order
    order_id INT NOT NULL,
    
    -- product_id: Which product this item represents
    -- INT: Must match products.id
    -- NOT NULL: Each item must reference a product
    product_id INT NOT NULL,
    
    -- quantity: How many of this product in the order
    -- INT: Whole numbers for counting
    -- NOT NULL: Must specify quantity
    -- CHECK (quantity > 0): Must order at least 1 item
    quantity INT NOT NULL CHECK (quantity > 0),
    
    -- unit_price: Price per item at time of order
    -- DECIMAL(10, 2): Precise decimal for money
    -- NOT NULL: Must store price (prevents issues if product price changes later)
    unit_price DECIMAL(10, 2) NOT NULL,
    
    -- FOREIGN KEY: Links order_id to orders table
    -- ON DELETE CASCADE: If order is deleted, delete all its items
    FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE,
    
    -- FOREIGN KEY: Links product_id to products table
    -- ON DELETE CASCADE: If product is deleted, remove from all orders
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE,
    
    -- UNIQUE KEY: Prevents duplicate product in same order
    -- (order_id=1, product_id=5) can only exist once
    UNIQUE KEY unique_order_product (order_id, product_id)
);
```

#### INSERT Operations
```sql
-- Single insert: Adding one user record
-- INSERT INTO: SQL command to add new data
-- users: Target table name
-- (username, email, password_hash): Columns we're providing values for
-- VALUES: Keyword that introduces the actual data
-- 'john_doe': String literal for username (quotes required for text)
-- 'john@example.com': String literal for email
-- 'hashed_password_123': String literal for password hash
-- Note: id, created_at, updated_at are automatically generated
INSERT INTO users (username, email, password_hash) 
VALUES ('john_doe', 'john@example.com', 'hashed_password_123');

-- Multiple insert: Adding several products at once
-- This is more efficient than multiple single INSERT statements
-- Each row is in parentheses, separated by commas
INSERT INTO products (name, description, price, stock_quantity) VALUES
    -- First product: All values provided
    ('Laptop Pro', 'High-performance laptop', 1299.99, 50),
    -- Second product: Different values
    ('Wireless Mouse', 'Ergonomic wireless mouse', 29.99, 200),
    -- Third product: Another set of values
    ('USB Cable', 'High-speed USB-C cable', 15.99, 500);

-- Insert with subquery: Creating order for specific user
-- SELECT: Subquery to find user's id by username
-- This allows inserting without knowing the exact user id
INSERT INTO orders (user_id, total_amount)
SELECT id, 0.00  -- id from users table, default total amount
FROM users       -- Source table for the subquery
WHERE username = 'john_doe';  -- Find specific user
```

#### SELECT Operations
```sql
-- Basic select: Retrieve all data from users table
-- SELECT *: Asterisk means "all columns"
-- FROM users: Specify which table to query
-- This returns every column and every row from users table
SELECT * FROM users;

-- Specific columns: Only get certain fields
-- SELECT: Specify exact columns you want
-- username, email, created_at: Column names separated by commas
-- This is better than SELECT * for performance (less data transfer)
SELECT username, email, created_at FROM users;

-- With alias: Rename columns in the result set
-- AS: Keyword to create an alias (can be omitted)
-- user_name: New name for username column in result
-- email_address: New name for email column
-- DATE(created_at): Function to extract only date part from timestamp
-- AS registration_date: Alias for the calculated date
SELECT 
    username AS user_name,
    email AS email_address,
    DATE(created_at) AS registration_date
FROM users;

-- Calculated fields: Perform calculations in SELECT
-- name, price, stock_quantity: Regular columns
-- (price * stock_quantity): Mathematical operation
-- AS total_inventory_value: Alias for calculated result
-- This calculates the total value of inventory for each product
SELECT 
    name,
    price,
    stock_quantity,
    (price * stock_quantity) AS total_inventory_value
FROM products;
```

#### UPDATE Operations
```sql
-- Simple update: Modify existing data
-- UPDATE users: Target table to modify
-- SET email = 'newemail@example.com': Set new value for email column
-- WHERE username = 'john_doe': Condition to identify which row(s) to update
-- WITHOUT WHERE clause, ALL rows would be updated (dangerous!)
UPDATE users 
SET email = 'newemail@example.com' 
WHERE username = 'john_doe';

-- Update with calculations: Modify value based on current value
-- SET stock_quantity = stock_quantity - 1: Subtract 1 from current stock
-- This is atomic operation (safe for concurrent access)
-- Used when someone buys a product to reduce inventory
UPDATE products 
SET stock_quantity = stock_quantity - 1 
WHERE id = 1;

-- Conditional update: Update multiple columns with conditions
-- SET status = 'shipped': Change status column
-- updated_at = CURRENT_TIMESTAMP: Update timestamp to current time
-- WHERE status = 'processing': Only update orders that are currently processing
-- AND order_date < DATE_SUB(NOW(), INTERVAL 2 DAY): Only orders older than 2 days
-- DATE_SUB(): Function to subtract time intervals
-- NOW(): Current timestamp
-- INTERVAL 2 DAY: 2 days time period
UPDATE orders 
SET status = 'shipped',
    updated_at = CURRENT_TIMESTAMP
WHERE status = 'processing' 
    AND order_date < DATE_SUB(NOW(), INTERVAL 2 DAY);

-- Update with JOIN: Update based on data from another table
-- UPDATE orders o: Target table with alias 'o'
-- JOIN users u ON o.user_id = u.id: Connect orders to users
-- SET o.total_amount = o.total_amount * 0.9: Apply 10% discount
-- WHERE u.username LIKE 'premium_%': Only for premium users
-- LIKE 'premium_%': Pattern matching (% means any characters after 'premium_')
UPDATE orders o
JOIN users u ON o.user_id = u.id
SET o.total_amount = o.total_amount * 0.9
WHERE u.username LIKE 'premium_%';
```

#### DELETE Operations
```sql
-- Simple delete: Remove rows that match condition
-- DELETE FROM products: Remove rows from products table
-- WHERE stock_quantity = 0: Only delete products with no stock
-- BE CAREFUL: Without WHERE, this deletes ALL rows!
DELETE FROM products WHERE stock_quantity = 0;

-- Delete with conditions: Remove old cancelled orders
-- WHERE status = 'cancelled': Only cancelled orders
-- AND order_date < DATE_SUB(NOW(), INTERVAL 30 DAY): Older than 30 days
-- This helps clean up old data to save storage space
DELETE FROM orders 
WHERE status = 'cancelled' 
    AND order_date < DATE_SUB(NOW(), INTERVAL 30 DAY);

-- Soft delete (recommended for backend): Don't actually delete, just mark as deleted
-- UPDATE instead of DELETE: Modify existing row instead of removing it
-- SET deleted_at = CURRENT_TIMESTAMP: Mark when "deletion" happened
-- WHERE id = 123: Target specific user
-- Benefits: Can recover data, maintain referential integrity, audit trail
-- Query later with: WHERE deleted_at IS NULL (to get non-deleted users)
UPDATE users 
SET deleted_at = CURRENT_TIMESTAMP 
WHERE id = 123;
```

#### ALTER TABLE Operations
```sql
-- Add column: Add new field to existing table
-- ALTER TABLE users: Modify structure of users table
-- ADD COLUMN phone VARCHAR(20): Add new column named 'phone'
-- VARCHAR(20): Data type and size for phone numbers
-- Existing rows will have NULL for this new column
ALTER TABLE users ADD COLUMN phone VARCHAR(20);

-- Modify column: Change properties of existing column
-- MODIFY COLUMN description TEXT NOT NULL: Change description column
-- TEXT: Keep same data type
-- NOT NULL: Add constraint (all existing NULLs must be updated first!)
ALTER TABLE products MODIFY COLUMN description TEXT NOT NULL;

-- Add index: Create index for faster queries
-- ADD INDEX idx_email (email): Create index named 'idx_email' on email column
-- Indexes speed up SELECT, WHERE, JOIN, ORDER BY operations on that column
-- Trade-off: Faster reads, slower writes, more storage space
ALTER TABLE users ADD INDEX idx_email (email);

-- Add foreign key: Create relationship between tables
-- ADD CONSTRAINT fk_category: Name for the constraint
-- FOREIGN KEY (category_id): Column in this table
-- REFERENCES categories(id): Column in other table
-- This ensures category_id values must exist in categories.id
ALTER TABLE products ADD CONSTRAINT fk_category 
FOREIGN KEY (category_id) REFERENCES categories(id);

-- Drop column: Remove column from table
-- DROP COLUMN phone: Remove the phone column completely
-- WARNING: This permanently deletes all data in that column!
ALTER TABLE users DROP COLUMN phone;
```

---

## 🟡 2. Intermediate SQL for Backend APIs

### 📘 WHERE Clause and Filtering

```sql
-- Basic conditions: Single condition filtering
-- WHERE price > 100: Only products with price greater than 100
-- WHERE category_id = 1: Only products in category 1 (exact match)
-- WHERE created_at >= '2024-01-01': Users created on or after Jan 1, 2024
-- Date format: 'YYYY-MM-DD' or 'YYYY-MM-DD HH:MM:SS'
SELECT * FROM products WHERE price > 100;
SELECT * FROM products WHERE category_id = 1;
SELECT * FROM users WHERE created_at >= '2024-01-01';

-- Multiple conditions: Combine conditions with AND/OR
-- BETWEEN 50 AND 200: Price in range (inclusive of both endpoints)
-- AND: All conditions must be true
-- stock_quantity > 0: Must have items in stock
-- is_active = TRUE: Product must be active
-- This finds active, in-stock products in price range $50-$200
SELECT * FROM products 
WHERE price BETWEEN 50 AND 200 
    AND stock_quantity > 0 
    AND is_active = TRUE;

-- Pattern matching: Search for text patterns
-- LIKE: Pattern matching operator
-- '%@gmail.com': % is wildcard (any characters) + literal '@gmail.com'
-- This finds all Gmail users
-- 'Laptop%': Starts with 'Laptop', followed by any characters
-- This finds all products whose name starts with 'Laptop'
SELECT * FROM users WHERE email LIKE '%@gmail.com';
SELECT * FROM products WHERE name LIKE 'Laptop%';

-- NULL handling: Check for missing values
-- IS NOT NULL: Has a value (not empty)
-- IS NULL: No value (empty)
-- Use IS/IS NOT, never = or != with NULL
-- NULL comparisons with = always return FALSE
SELECT * FROM products WHERE description IS NOT NULL;
SELECT * FROM users WHERE deleted_at IS NULL;

-- IN operator: Check if value exists in a list
-- IN ('pending', 'processing'): status equals either 'pending' OR 'processing'
-- More efficient than: status = 'pending' OR status = 'processing'
-- IN (1, 2, 3): category_id is 1, 2, or 3
SELECT * FROM orders WHERE status IN ('pending', 'processing');
SELECT * FROM products WHERE category_id IN (1, 2, 3);

-- Subquery in WHERE: Use result of another query as condition
-- IN (...): Check if user id exists in the subquery result
-- SELECT DISTINCT user_id FROM orders WHERE total_amount > 1000:
--   Find all user IDs who have made orders over $1000
-- DISTINCT: Remove duplicate user IDs
-- This finds users who are "high-value customers"
SELECT * FROM users 
WHERE id IN (
    SELECT DISTINCT user_id 
    FROM orders 
    WHERE total_amount > 1000
);
```

### 📘 ORDER BY and LIMIT

```sql
-- Basic sorting: Sort results by one column
-- ORDER BY price DESC: Sort by price in descending order (highest first)
-- DESC: Descending (high to low), ASC: Ascending (low to high)
-- ORDER BY created_at ASC: Sort by creation time, oldest first
-- Default is ASC if not specified
SELECT * FROM products ORDER BY price DESC;
SELECT * FROM users ORDER BY created_at ASC;

-- Multiple column sorting: Sort by multiple criteria
-- ORDER BY category_id ASC, price DESC, name ASC:
--   1. First sort by category_id (ascending)
--   2. Within same category, sort by price (descending)
--   3. Within same category and price, sort by name (ascending)
-- SQL processes in left-to-right order
SELECT * FROM products 
ORDER BY category_id ASC, price DESC, name ASC;

-- Pagination (critical for APIs): Limit results and skip rows
-- LIMIT 20: Return maximum 20 rows
-- OFFSET 0: Skip 0 rows (start from beginning)
-- This gets the first page of results
SELECT * FROM products 
ORDER BY created_at DESC 
LIMIT 20 OFFSET 0;  -- First page

-- OFFSET 20: Skip first 20 rows
-- This gets the second page (rows 21-40)
-- Formula: OFFSET = (page_number - 1) * page_size
SELECT * FROM products 
ORDER BY created_at DESC 
LIMIT 20 OFFSET 20; -- Second page

-- Top N queries: Get best/worst records
-- WHERE stock_quantity > 0: Only in-stock products
-- ORDER BY price DESC: Most expensive first
-- LIMIT 5: Only return 5 results
-- This finds the 5 most expensive products that are in stock
SELECT * FROM products 
WHERE stock_quantity > 0 
ORDER BY price DESC 
LIMIT 5; -- Top 5 most expensive in-stock products
```

### 📘 JOIN Operations

```sql
-- INNER JOIN (most common): Only return rows that match in both tables
-- FROM users u: Main table with alias 'u'
-- INNER JOIN orders o: Join with orders table, alias 'o'
-- ON u.id = o.user_id: Join condition (how tables are related)
-- This only returns users who have placed orders
-- Users without orders are excluded from results
SELECT 
    u.username,        -- From users table
    u.email,           -- From users table
    o.id AS order_id,  -- From orders table, renamed to avoid confusion
    o.total_amount,    -- From orders table
    o.status           -- From orders table
FROM users u
INNER JOIN orders o ON u.id = o.user_id
WHERE o.status != 'cancelled';

-- LEFT JOIN: Return all rows from left table, matching from right table
-- LEFT JOIN orders o: Include ALL users, even those without orders
-- ON u.id = o.user_id AND o.status != 'cancelled': Join condition with filter
-- COUNT(o.id): Count orders for each user (0 if no orders)
-- COALESCE(SUM(o.total_amount), 0): Sum order amounts, use 0 if NULL
-- GROUP BY: Required when using aggregate functions (COUNT, SUM)
-- This returns all users with their order statistics
SELECT 
    u.username,
    u.email,
    COUNT(o.id) AS total_orders,                    -- Count of orders per user
    COALESCE(SUM(o.total_amount), 0) AS total_spent -- Total money spent
FROM users u
LEFT JOIN orders o ON u.id = o.user_id 
    AND o.status != 'cancelled'  -- Filter applied during join
GROUP BY u.id, u.username, u.email;

-- Multiple JOINs: Connect multiple tables together
-- Chain of relationships: users → orders → order_items → products
-- Each JOIN connects two tables using their relationship keys
-- This creates a complete view of user purchases
SELECT 
    u.username,                                      -- User who made purchase
    o.id AS order_id,                               -- Order number
    p.name AS product_name,                         -- Product name
    oi.quantity,                                    -- How many bought
    oi.unit_price,                                  -- Price per item
    (oi.quantity * oi.unit_price) AS line_total    -- Total for this line
FROM users u
INNER JOIN orders o ON u.id = o.user_id           -- Users to orders
INNER JOIN order_items oi ON o.id = oi.order_id   -- Orders to order items
INNER JOIN products p ON oi.product_id = p.id     -- Order items to products
WHERE o.status = 'delivered'
ORDER BY o.order_date DESC;

-- Self JOIN: Join table to itself (for hierarchical data)
-- Used when table references itself (like employee-manager relationship)
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    manager_id INT,  -- References another employee's id
    FOREIGN KEY (manager_id) REFERENCES employees(id)
);

-- Self join to show employee-manager relationships
-- FROM employees e: Employees table (alias 'e' for employee)
-- LEFT JOIN employees m: Same table again (alias 'm' for manager)
-- ON e.manager_id = m.id: Connect employee's manager_id to manager's id
-- LEFT JOIN ensures employees without managers are still shown
SELECT 
    e.name AS employee_name,
    m.name AS manager_name   -- Will be NULL for top-level managers
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.id;
```

### 📘 GROUP BY and Aggregations

```sql
-- Basic aggregations: Calculate summary statistics for entire table
-- COUNT(*): Count all rows in the table (including rows with NULL values)
-- COUNT(DISTINCT email): Count unique email addresses only
-- DISTINCT: Eliminates duplicate values before counting
-- This tells us total users and if there are any duplicate emails
SELECT 
    COUNT(*) AS total_users,
    COUNT(DISTINCT email) AS unique_emails
FROM users;

-- GROUP BY with aggregations: Calculate statistics for each group
-- GROUP BY status: Create separate groups for each order status
-- COUNT(*): Count orders in each status group
-- SUM(total_amount): Add up all order amounts for each status
-- AVG(total_amount): Calculate average order value for each status
-- MIN/MAX: Find smallest and largest order amounts for each status
-- This gives us a summary of orders by status
SELECT 
    status,                               -- Grouping column
    COUNT(*) AS order_count,             -- How many orders per status
    SUM(total_amount) AS total_revenue,  -- Total money per status
    AVG(total_amount) AS avg_order_value,-- Average order size per status
    MIN(total_amount) AS min_order,      -- Smallest order per status
    MAX(total_amount) AS max_order       -- Largest order per status
FROM orders
GROUP BY status;

-- Complex grouping for analytics: Multi-level analysis with date functions
-- DATE_FORMAT(created_at, '%Y-%m'): Extract year-month from timestamp
-- '%Y-%m': Format as '2024-01' (4-digit year, dash, 2-digit month)
-- COUNT(*): Total new users per month
-- COUNT(CASE WHEN...): Conditional counting
-- CASE WHEN email LIKE '%@gmail.com' THEN 1 END: Returns 1 for Gmail users, NULL for others
-- COUNT() ignores NULL values, so only Gmail users are counted
-- WHERE created_at >= DATE_SUB(NOW(), INTERVAL 12 MONTH): Last 12 months only
SELECT 
    DATE_FORMAT(created_at, '%Y-%m') AS month,
    COUNT(*) AS new_users,
    COUNT(CASE WHEN email LIKE '%@gmail.com' THEN 1 END) AS gmail_users
FROM users
WHERE created_at >= DATE_SUB(NOW(), INTERVAL 12 MONTH)
GROUP BY DATE_FORMAT(created_at, '%Y-%m')
ORDER BY month DESC;

-- HAVING clause: Filter groups after aggregation (like WHERE for groups)
-- WHERE: Filters individual rows before grouping
-- GROUP BY user_id: Group orders by user
-- HAVING: Filters groups after aggregation is complete
-- COUNT(*) >= 5: Only users with 5 or more orders
-- SUM(total_amount) > 1000: Only users who spent more than $1000
-- This finds "high-value customers" (frequent buyers with high spend)
SELECT 
    user_id,
    COUNT(*) AS order_count,
    SUM(total_amount) AS total_spent
FROM orders
WHERE status = 'delivered'              -- Filter: only completed orders
GROUP BY user_id                        -- Group: one row per user
HAVING COUNT(*) >= 5                    -- Filter groups: 5+ orders
    AND SUM(total_amount) > 1000        -- Filter groups: $1000+ spent
ORDER BY total_spent DESC;
```

### 📘 CASE Statements

```sql
-- Simple CASE: Create conditional logic in SQL
-- CASE: Start of conditional statement
-- WHEN price < 50 THEN 'Budget': If condition is true, return this value
-- WHEN price < 200 THEN 'Mid-range': Else if this condition is true
-- ELSE 'Premium': If no conditions match, return this default value
-- END: Close the CASE statement
-- AS price_category: Alias for the calculated column
-- This categorizes products by price range
SELECT 
    name,
    price,
    CASE 
        WHEN price < 50 THEN 'Budget'
        WHEN price < 200 THEN 'Mid-range'
        ELSE 'Premium'
    END AS price_category
FROM products;

-- CASE in aggregations: Conditional counting and calculations
-- COUNT(*): Total number of orders
-- COUNT(CASE WHEN status = 'delivered' THEN 1 END): Count only delivered orders
--   - CASE returns 1 for delivered orders, NULL for others
--   - COUNT() ignores NULL values, so only counts the 1s
-- ROUND(..., 2): Round result to 2 decimal places
-- * 100.0: Multiply by 100.0 (float) to get percentage
-- This calculates delivery success rate as a percentage
SELECT 
    COUNT(*) AS total_orders,
    COUNT(CASE WHEN status = 'delivered' THEN 1 END) AS delivered_orders,
    COUNT(CASE WHEN status = 'cancelled' THEN 1 END) AS cancelled_orders,
    ROUND(
        COUNT(CASE WHEN status = 'delivered' THEN 1 END) * 100.0 / COUNT(*), 
        2
    ) AS delivery_rate_percent
FROM orders;

-- CASE for data transformation: Categorize data for analysis
-- LIKE '%@gmail.com': Pattern matching for email domains
-- This groups users by their email provider for marketing analysis
SELECT 
    username,
    email,
    CASE 
        WHEN email LIKE '%@gmail.com' THEN 'Gmail'
        WHEN email LIKE '%@yahoo.com' THEN 'Yahoo'
        WHEN email LIKE '%@company.com' THEN 'Corporate'
        ELSE 'Other'  -- Catch-all for unknown domains
    END AS email_provider
FROM users;
```

### 📘 String and Date Functions

```sql
-- String functions: Manipulate text data
-- CONCAT(first_name, ' ', last_name): Join strings together with space
-- UPPER(username): Convert to uppercase letters
-- LENGTH(email): Count characters in string
-- SUBSTRING(email, 1, LOCATE('@', email) - 1): Extract part of string
--   - LOCATE('@', email): Find position of @ symbol
--   - SUBSTRING(email, 1, position-1): Get text from start to before @
-- REPLACE(phone, '-', ''): Replace all dashes with empty string
-- These functions clean and format data for display or processing
SELECT 
    CONCAT(first_name, ' ', last_name) AS full_name,
    UPPER(username) AS username_upper,
    LENGTH(email) AS email_length,
    SUBSTRING(email, 1, LOCATE('@', email) - 1) AS email_username,
    REPLACE(phone, '-', '') AS phone_clean
FROM users;

-- Date functions: Extract and manipulate date/time data
-- DATE(created_at): Extract only date part (removes time)
-- YEAR/MONTH/DAY: Extract specific parts of date
-- DAYNAME(): Get day of week as text (Monday, Tuesday, etc.)
-- DATEDIFF(NOW(), created_at): Calculate days between dates
-- NOW(): Current timestamp
-- DATE_ADD(created_at, INTERVAL 30 DAY): Add 30 days to date
-- These functions are useful for analytics and business logic
SELECT 
    created_at,
    DATE(created_at) AS created_date,
    YEAR(created_at) AS created_year,
    MONTH(created_at) AS created_month,
    DAYNAME(created_at) AS created_day,
    DATEDIFF(NOW(), created_at) AS days_since_creation,
    DATE_ADD(created_at, INTERVAL 30 DAY) AS expiry_date
FROM orders;

-- Date formatting for APIs: Convert dates to specific formats
-- DATE_FORMAT(): Convert date to custom string format
-- '%Y-%m-%d %H:%i:%s': Year-Month-Day Hour:Minute:Second (ISO format)
-- '%M %d, %Y': Full month name, day, year (readable format)
-- UNIX_TIMESTAMP(): Convert to Unix timestamp (seconds since 1970)
-- Different formats needed for different API consumers
SELECT 
    id,
    DATE_FORMAT(created_at, '%Y-%m-%d %H:%i:%s') AS formatted_datetime,
    DATE_FORMAT(created_at, '%M %d, %Y') AS readable_date,
    UNIX_TIMESTAMP(created_at) AS unix_timestamp
FROM orders;
```

---

## 🔵 3. Advanced SQL for Scalable Backends

### 📘 Subqueries

```sql
-- Scalar subquery (returns single value): Nested query that returns one value
-- (SELECT COUNT(*) FROM orders WHERE user_id = u.id): Inner query
-- This subquery runs once for each user row
-- WHERE user_id = u.id: Correlates inner query to outer query (u.id)
-- COUNT(*): Returns single number of orders for this user
-- AS order_count: Alias for the calculated column
-- This adds order count to each user without using JOIN
SELECT 
    *,
    (SELECT COUNT(*) FROM orders WHERE user_id = u.id) AS order_count
FROM users u;

-- EXISTS subquery (for performance): Check if matching rows exist
-- EXISTS: Returns TRUE if subquery returns any rows, FALSE if empty
-- SELECT 1: We don't care about actual data, just existence
-- WHERE o.user_id = u.id: Connect subquery to main query
-- AND o.total_amount > 500: Additional condition in subquery
-- EXISTS is faster than IN for large datasets
-- This finds users who have made orders over $500
SELECT * FROM users u
WHERE EXISTS (
    SELECT 1 FROM orders o 
    WHERE o.user_id = u.id 
        AND o.total_amount > 500
);

-- NOT EXISTS: Opposite of EXISTS, finds rows that DON'T match
-- This finds products that have never been ordered
-- Useful for identifying unpopular products
SELECT * FROM products p
WHERE NOT EXISTS (
    SELECT 1 FROM order_items oi 
    WHERE oi.product_id = p.id
);

-- Correlated subquery: Inner query references outer query columns
-- (SELECT AVG(oi.unit_price)...): Calculate average selling price
-- WHERE oi.product_id = p.id: For THIS specific product only
-- Correlated = inner query depends on outer query's current row
-- This shows list price vs. actual average selling price
SELECT 
    p.*,
    (SELECT AVG(oi.unit_price) 
     FROM order_items oi 
     WHERE oi.product_id = p.id) AS avg_selling_price
FROM products p;

-- Subquery in FROM clause: Use query result as a table
-- (SELECT ... FROM products ... GROUP BY category_id): Inner query creates virtual table
-- AS category_stats: Alias for the subquery "table"
-- WHERE category_stats.product_count > 5: Filter the grouped results
-- This creates category statistics first, then filters them
-- Useful for complex multi-step analysis
SELECT 
    category_stats.category_id,
    category_stats.product_count,
    category_stats.avg_price
FROM (
    SELECT 
        category_id,
        COUNT(*) AS product_count,
        AVG(price) AS avg_price
    FROM products
    WHERE is_active = TRUE
    GROUP BY category_id
) AS category_stats
WHERE category_stats.product_count > 5;
```

### 📘 Common Table Expressions (CTEs)

```sql
-- Basic CTE: Named temporary result set for complex queries
-- WITH monthly_sales AS (...): Create temporary "table" named monthly_sales
-- CTE makes complex queries more readable by breaking them into steps
-- DATE_FORMAT(order_date, '%Y-%m'): Group by year-month
-- Inside main query, use monthly_sales like a regular table
-- revenue / order_count: Calculate using CTE columns
-- CTEs are great for avoiding repeated subqueries
WITH monthly_sales AS (
    SELECT 
        DATE_FORMAT(order_date, '%Y-%m') AS month,
        SUM(total_amount) AS revenue,
        COUNT(*) AS order_count
    FROM orders
    WHERE status = 'delivered'
    GROUP BY DATE_FORMAT(order_date, '%Y-%m')
)
SELECT 
    month,
    revenue,
    order_count,
    revenue / order_count AS avg_order_value
FROM monthly_sales
ORDER BY month DESC;

-- Multiple CTEs: Chain multiple temporary result sets
-- user_stats: First CTE calculates basic user statistics
-- user_segments: Second CTE uses first CTE to categorize users
-- Main query: Uses both CTEs and joins with users table
-- This creates a data pipeline: raw data → stats → segments → final result
WITH user_stats AS (
    SELECT 
        user_id,
        COUNT(*) AS total_orders,
        SUM(total_amount) AS total_spent,
        MAX(order_date) AS last_order_date
    FROM orders
    WHERE status = 'delivered'
    GROUP BY user_id
),
user_segments AS (
    SELECT 
        user_id,
        total_orders,
        total_spent,
        last_order_date,
        CASE 
            WHEN total_spent > 1000 THEN 'VIP'
            WHEN total_spent > 500 THEN 'Premium'
            WHEN total_orders > 5 THEN 'Regular'
            ELSE 'New'
        END AS segment
    FROM user_stats
)
SELECT 
    u.username,
    u.email,
    us.segment,
    us.total_orders,
    us.total_spent
FROM users u
INNER JOIN user_segments us ON u.id = us.user_id
WHERE us.segment IN ('VIP', 'Premium')
ORDER BY us.total_spent DESC;

-- Recursive CTE: For hierarchical/tree-like data
-- WITH RECURSIVE: Special CTE that can reference itself
-- Base case: Start with root categories (parent_id IS NULL)
-- level: Track how deep in hierarchy (0 for root)
-- path: Build breadcrumb trail of category names
-- UNION ALL: Combine base case with recursive case
-- Recursive case: Find children of current level
-- ch.level + 1: Increment depth level
-- CONCAT(ch.path, ' > ', c.name): Extend breadcrumb path
-- This builds a complete category tree with paths like "Electronics > Laptops > Gaming"
WITH RECURSIVE category_hierarchy AS (
    -- Base case: root categories
    SELECT id, name, parent_id, 0 AS level, name AS path
    FROM categories
    WHERE parent_id IS NULL
    
    UNION ALL
    
    -- Recursive case: child categories
    SELECT 
        c.id, 
        c.name, 
        c.parent_id, 
        ch.level + 1,
        CONCAT(ch.path, ' > ', c.name)
    FROM categories c
    INNER JOIN category_hierarchy ch ON c.parent_id = ch.id
)
SELECT * FROM category_hierarchy ORDER BY path;
```

### 📘 Window Functions

```sql
-- ROW_NUMBER() for ranking: Assign unique sequential numbers
-- ROW_NUMBER(): Assigns 1, 2, 3, 4... to each row
-- OVER (ORDER BY created_at): Define the "window" - how to order rows
-- This assigns a registration order number to each user
-- Unlike RANK(), ROW_NUMBER() always gives unique numbers
SELECT 
    username,
    email,
    created_at,
    ROW_NUMBER() OVER (ORDER BY created_at) AS registration_order
FROM users;

-- RANK() and DENSE_RANK(): Handle ties differently
-- RANK(): Gives same number to ties, skips next numbers (1,2,2,4,5)
-- DENSE_RANK(): Gives same number to ties, doesn't skip (1,2,2,3,4)
-- ORDER BY p.price DESC: Rank by price, highest first
-- Use RANK() when you want to see gaps, DENSE_RANK() for continuous ranking
SELECT 
    p.name,
    p.price,
    RANK() OVER (ORDER BY p.price DESC) AS price_rank,
    DENSE_RANK() OVER (ORDER BY p.price DESC) AS price_dense_rank
FROM products p;

-- PARTITION BY: Create separate ranking within each group
-- PARTITION BY p.category_id: Create separate windows for each category
-- ROW_NUMBER() restarts at 1 for each category
-- ORDER BY p.price DESC: Within each category, rank by price
-- This finds the most expensive product in each category
SELECT 
    p.name,
    p.category_id,
    p.price,
    ROW_NUMBER() OVER (
        PARTITION BY p.category_id 
        ORDER BY p.price DESC
    ) AS rank_in_category
FROM products p;

-- Running totals and moving averages: Calculations over window of rows
-- SUM() OVER (...): Calculate sum over a window of rows
-- ROWS UNBOUNDED PRECEDING: From beginning of result set to current row
-- running_total: Cumulative sum of all orders up to this date
-- ROWS BETWEEN 6 PRECEDING AND CURRENT ROW: Window of 7 rows (including current)
-- moving_avg_7_days: Average of last 7 days including today
SELECT 
    order_date,
    total_amount,
    SUM(total_amount) OVER (
        ORDER BY order_date 
        ROWS UNBOUNDED PRECEDING
    ) AS running_total,
    AVG(total_amount) OVER (
        ORDER BY order_date 
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS moving_avg_7_days
FROM orders
WHERE status = 'delivered'
ORDER BY order_date;

-- LAG and LEAD: Access values from other rows in the window
-- LAG(total_amount, 1): Get value from 1 row before current row
-- LEAD(total_amount, 1): Get value from 1 row after current row
-- total_amount - LAG(...): Calculate difference from previous day
-- Useful for day-over-day, month-over-month comparisons
SELECT 
    order_date,
    total_amount,
    LAG(total_amount, 1) OVER (ORDER BY order_date) AS prev_day_amount,
    LEAD(total_amount, 1) OVER (ORDER BY order_date) AS next_day_amount,
    total_amount - LAG(total_amount, 1) OVER (ORDER BY order_date) AS day_over_day_change
FROM (
    SELECT 
        DATE(order_date) AS order_date,
        SUM(total_amount) AS total_amount
    FROM orders
    WHERE status = 'delivered'
    GROUP BY DATE(order_date)
) daily_sales
ORDER BY order_date;

-- NTILE: Divide data into equal-sized buckets/percentiles
-- NTILE(4): Divide users into 4 equal groups (quartiles)
-- ORDER BY total_spent: Order by spending amount
-- spending_quartile: 1=bottom 25%, 2=25-50%, 3=50-75%, 4=top 25%
-- Great for customer segmentation and analysis
SELECT 
    username,
    total_spent,
    NTILE(4) OVER (ORDER BY total_spent) AS spending_quartile
FROM (
    SELECT 
        u.username,
        COALESCE(SUM(o.total_amount), 0) AS total_spent
    FROM users u
    LEFT JOIN orders o ON u.id = o.user_id AND o.status = 'delivered'
    GROUP BY u.id, u.username
) user_spending;
```

### 📘 Views

```sql
-- Simple view for commonly used data
CREATE VIEW active_products_view AS
SELECT 
    p.id,
    p.name,
    p.price,
    p.stock_quantity,
    c.name AS category_name
FROM products p
LEFT JOIN categories c ON p.category_id = c.id
WHERE p.is_active = TRUE AND p.stock_quantity > 0;

-- Complex analytical view
CREATE VIEW user_analytics_view AS
SELECT 
    u.id,
    u.username,
    u.email,
    u.created_at AS registration_date,
    COUNT(o.id) AS total_orders,
    COALESCE(SUM(o.total_amount), 0) AS total_spent,
    COALESCE(AVG(o.total_amount), 0) AS avg_order_value,
    MAX(o.order_date) AS last_order_date,
    DATEDIFF(NOW(), MAX(o.order_date)) AS days_since_last_order,
    CASE 
        WHEN COALESCE(SUM(o.total_amount), 0) > 1000 THEN 'VIP'
        WHEN COUNT(o.id) > 5 THEN 'Regular'
        ELSE 'New'
    END AS customer_segment
FROM users u
LEFT JOIN orders o ON u.id = o.user_id AND o.status = 'delivered'
WHERE u.deleted_at IS NULL
GROUP BY u.id, u.username, u.email, u.created_at;

-- Using the view
SELECT * FROM user_analytics_view 
WHERE customer_segment = 'VIP' 
ORDER BY total_spent DESC;
```

### 📘 Indexes for Performance

```sql
-- Single column indexes
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_orders_user_id ON orders(user_id);
CREATE INDEX idx_orders_status ON orders(status);
CREATE INDEX idx_products_category ON products(category_id);

-- Composite indexes (order matters!)
CREATE INDEX idx_orders_user_status ON orders(user_id, status);
CREATE INDEX idx_orders_date_status ON orders(order_date, status);

-- Partial indexes (MySQL 8.0+, PostgreSQL)
CREATE INDEX idx_active_products ON products(name) WHERE is_active = TRUE;

-- Unique indexes
CREATE UNIQUE INDEX idx_users_username ON users(username);

-- Full-text search indexes
CREATE FULLTEXT INDEX idx_products_search ON products(name, description);

-- Query with EXPLAIN to check index usage
EXPLAIN SELECT * FROM orders 
WHERE user_id = 123 AND status = 'delivered'
ORDER BY order_date DESC;
```

### 📘 Transactions

```sql
-- Basic transaction
START TRANSACTION;

INSERT INTO orders (user_id, total_amount, status)
VALUES (123, 299.98, 'pending');

SET @order_id = LAST_INSERT_ID();

INSERT INTO order_items (order_id, product_id, quantity, unit_price)
VALUES 
    (@order_id, 1, 2, 99.99),
    (@order_id, 2, 1, 99.99);

UPDATE products 
SET stock_quantity = stock_quantity - 2 
WHERE id = 1;

UPDATE products 
SET stock_quantity = stock_quantity - 1 
WHERE id = 2;

COMMIT;

-- Transaction with error handling (in application code)
-- This would be wrapped in try-catch in your backend
START TRANSACTION;

-- Check stock availability first
SELECT stock_quantity FROM products WHERE id = 1 FOR UPDATE;

-- If stock is sufficient, proceed
UPDATE products SET stock_quantity = stock_quantity - 5 WHERE id = 1;

INSERT INTO orders (user_id, total_amount) VALUES (123, 499.95);

-- If any error occurs, ROLLBACK
-- ROLLBACK;

COMMIT;

-- Savepoints for partial rollbacks
START TRANSACTION;

SAVEPOINT sp1;
INSERT INTO users (username, email, password_hash) 
VALUES ('user1', 'user1@example.com', 'hash1');

SAVEPOINT sp2;
INSERT INTO users (username, email, password_hash) 
VALUES ('user2', 'user2@example.com', 'hash2');

-- Rollback to sp1 if user2 insertion fails
-- ROLLBACK TO sp1;

COMMIT;
```

### 📘 Triggers

```sql
-- Audit trigger for tracking changes
CREATE TABLE user_audit (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    action VARCHAR(10),
    old_values JSON,
    new_values JSON,
    changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    changed_by VARCHAR(100)
);

DELIMITER //
CREATE TRIGGER user_audit_trigger
AFTER UPDATE ON users
FOR EACH ROW
BEGIN
    INSERT INTO user_audit (user_id, action, old_values, new_values)
    VALUES (
        NEW.id,
        'UPDATE',
        JSON_OBJECT(
            'username', OLD.username,
            'email', OLD.email,
            'updated_at', OLD.updated_at
        ),
        JSON_OBJECT(
            'username', NEW.username,
            'email', NEW.email,
            'updated_at', NEW.updated_at
        )
    );
END//
DELIMITER ;

-- Automatic timestamp trigger
DELIMITER //
CREATE TRIGGER update_timestamp
BEFORE UPDATE ON products
FOR EACH ROW
BEGIN
    SET NEW.updated_at = CURRENT_TIMESTAMP;
END//
DELIMITER ;

-- Business logic trigger (update order total)
DELIMITER //
CREATE TRIGGER update_order_total
AFTER INSERT ON order_items
FOR EACH ROW
BEGIN
    UPDATE orders 
    SET total_amount = (
        SELECT SUM(quantity * unit_price) 
        FROM order_items 
        WHERE order_id = NEW.order_id
    )
    WHERE id = NEW.order_id;
END//
DELIMITER ;
```

### 📘 Stored Procedures

```sql
-- Simple procedure
DELIMITER //
CREATE PROCEDURE GetUserOrders(IN user_id INT)
BEGIN
    SELECT 
        o.id,
        o.total_amount,
        o.status,
        o.order_date
    FROM orders o
    WHERE o.user_id = user_id
    ORDER BY o.order_date DESC;
END//
DELIMITER ;

-- Call the procedure
CALL GetUserOrders(123);

-- Complex procedure with parameters and logic
DELIMITER //
CREATE PROCEDURE PlaceOrder(
    IN p_user_id INT,
    IN p_product_id INT,
    IN p_quantity INT,
    OUT p_order_id INT,
    OUT p_success BOOLEAN,
    OUT p_message VARCHAR(255)
)
BEGIN
    DECLARE v_stock INT DEFAULT 0;
    DECLARE v_price DECIMAL(10,2) DEFAULT 0;
    DECLARE v_total DECIMAL(10,2) DEFAULT 0;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SET p_success = FALSE;
        SET p_message = 'Order placement failed due to database error';
    END;

    START TRANSACTION;
    
    -- Check stock
    SELECT stock_quantity, price 
    INTO v_stock, v_price
    FROM products 
    WHERE id = p_product_id AND is_active = TRUE;
    
    IF v_stock IS NULL THEN
        SET p_success = FALSE;
        SET p_message = 'Product not found or inactive';
        ROLLBACK;
    ELSEIF v_stock < p_quantity THEN
        SET p_success = FALSE;
        SET p_message = CONCAT('Insufficient stock. Available: ', v_stock);
        ROLLBACK;
    ELSE
        SET v_total = v_price * p_quantity;
        
        -- Create order
        INSERT INTO orders (user_id, total_amount, status)
        VALUES (p_user_id, v_total, 'pending');
        
        SET p_order_id = LAST_INSERT_ID();
        
        -- Add order item
        INSERT INTO order_items (order_id, product_id, quantity, unit_price)
        VALUES (p_order_id, p_product_id, p_quantity, v_price);
        
        -- Update stock
        UPDATE products 
        SET stock_quantity = stock_quantity - p_quantity
        WHERE id = p_product_id;
        
        SET p_success = TRUE;
        SET p_message = 'Order placed successfully';
        COMMIT;
    END IF;
    
END//
DELIMITER ;

-- Call with output parameters
CALL PlaceOrder(123, 1, 2, @order_id, @success, @message);
SELECT @order_id, @success, @message;
```

---

## 🧪 4. Backend-Centric SQL Project Patterns

### 📘 CRUD API Patterns

```sql
-- User Registration (CREATE)
INSERT INTO users (username, email, password_hash, created_at)
VALUES (?, ?, ?, NOW());

-- Get User Profile (READ)
SELECT 
    id, username, email, created_at, last_login,
    (SELECT COUNT(*) FROM orders WHERE user_id = users.id) AS order_count
FROM users 
WHERE id = ? AND deleted_at IS NULL;

-- Update User Profile (UPDATE)
UPDATE users 
SET email = ?, updated_at = NOW()
WHERE id = ? AND deleted_at IS NULL;

-- Soft Delete User (DELETE)
UPDATE users 
SET deleted_at = NOW()
WHERE id = ?;
```

### 📘 Search and Filter Patterns

```sql
-- Dynamic search with multiple filters
SELECT 
    p.id,
    p.name,
    p.price,
    p.stock_quantity,
    c.name AS category_name
FROM products p
LEFT JOIN categories c ON p.category_id = c.id
WHERE p.is_active = TRUE
    AND p.deleted_at IS NULL
    AND (? IS NULL OR p.name LIKE CONCAT('%', ?, '%'))
    AND (? IS NULL OR p.category_id = ?)
    AND (? IS NULL OR p.price >= ?)
    AND (? IS NULL OR p.price <= ?)
    AND (? IS NULL OR p.stock_quantity > 0)
ORDER BY 
    CASE WHEN ? = 'name' THEN p.name END ASC,
    CASE WHEN ? = 'price' THEN p.price END ASC,
    CASE WHEN ? = 'created' THEN p.created_at END DESC
LIMIT ? OFFSET ?;

-- Full-text search
SELECT 
    p.*,
    MATCH(p.name, p.description) AGAINST(? IN NATURAL LANGUAGE MODE) AS relevance_score
FROM products p
WHERE MATCH(p.name, p.description) AGAINST(? IN NATURAL LANGUAGE MODE)
    AND p.is_active = TRUE
ORDER BY relevance_score DESC;
```

### 📘 Multi-Tenant Pattern

```sql
-- Every query includes tenant_id filter
SELECT * FROM orders 
WHERE tenant_id = ? 
    AND user_id = ? 
    AND status = 'pending';

-- Create with tenant_id
INSERT INTO products (tenant_id, name, price, created_by)
VALUES (?, ?, ?, ?);

-- Update with tenant_id verification
UPDATE products 
SET price = ?
WHERE id = ? AND tenant_id = ?;

-- Multi-tenant analytics
SELECT 
    t.name AS tenant_name,
    COUNT(o.id) AS total_orders,
    SUM(o.total_amount) AS total_revenue
FROM tenants t
LEFT JOIN orders o ON t.id = o.tenant_id 
    AND o.status = 'delivered'
    AND o.order_date >= DATE_SUB(NOW(), INTERVAL 30 DAY)
GROUP BY t.id, t.name
ORDER BY total_revenue DESC;
```

### 📘 Role-Based Access Control

```sql
-- User roles and permissions
CREATE TABLE roles (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) UNIQUE NOT NULL,
    description TEXT
);

CREATE TABLE permissions (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) UNIQUE NOT NULL,
    resource VARCHAR(50) NOT NULL,
    action VARCHAR(50) NOT NULL
);

CREATE TABLE role_permissions (
    role_id INT,
    permission_id INT,
    PRIMARY KEY (role_id, permission_id),
    FOREIGN KEY (role_id) REFERENCES roles(id),
    FOREIGN KEY (permission_id) REFERENCES permissions(id)
);

CREATE TABLE user_roles (
    user_id INT,
    role_id INT,
    assigned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    assigned_by INT,
    PRIMARY KEY (user_id, role_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (role_id) REFERENCES roles(id),
    FOREIGN KEY (assigned_by) REFERENCES users(id)
);

-- Check user permissions
SELECT DISTINCT p.resource, p.action
FROM users u
JOIN user_roles ur ON u.id = ur.user_id
JOIN role_permissions rp ON ur.role_id = rp.role_id
JOIN permissions p ON rp.permission_id = p.id
WHERE u.id = ? AND u.deleted_at IS NULL;

-- Resource access with role check
SELECT o.* FROM orders o
JOIN users u ON o.user_id = u.id
JOIN user_roles ur ON u.id = ur.user_id
JOIN roles r ON ur.role_id = r.id
WHERE o.id = ?
    AND (
        r.name = 'admin' 
        OR (r.name = 'user' AND o.user_id = ?)
        OR (r.name = 'manager' AND o.tenant_id = ?)
    );
```

### 📘 Audit Logging Pattern

```sql
-- Comprehensive audit table
CREATE TABLE audit_log (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    table_name VARCHAR(50) NOT NULL,
    record_id INT NOT NULL,
    action ENUM('INSERT', 'UPDATE', 'DELETE') NOT NULL,
    old_values JSON,
    new_values JSON,
    changed_by INT,
    changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ip_address VARCHAR(45),
    user_agent TEXT,
    session_id VARCHAR(255),
    INDEX idx_table_record (table_name, record_id),
    INDEX idx_changed_by (changed_by),
    INDEX idx_changed_at (changed_at)
);

-- Audit trigger for products
DELIMITER //
CREATE TRIGGER products_audit_trigger
AFTER UPDATE ON products
FOR EACH ROW
BEGIN
    INSERT INTO audit_log (
        table_name, record_id, action, 
        old_values, new_values, changed_by
    ) VALUES (
        'products', 
        NEW.id, 
        'UPDATE',
        JSON_OBJECT(
            'name', OLD.name,
            'price', OLD.price,
            'stock_quantity', OLD.stock_quantity,
            'is_active', OLD.is_active
        ),
        JSON_OBJECT(
            'name', NEW.name,
            'price', NEW.price,
            'stock_quantity', NEW.stock_quantity,
            'is_active', NEW.is_active
        ),
        @current_user_id
    );
END//
DELIMITER ;

-- Query audit history
SELECT 
    al.*,
    u.username as changed_by_username
FROM audit_log al
LEFT JOIN users u ON al.changed_by = u.id
WHERE al.table_name = 'products' 
    AND al.record_id = ?
ORDER BY al.changed_at DESC;
```

### 📘 Time-Series and Analytics Patterns

```sql
-- Daily sales aggregation
CREATE TABLE daily_sales_summary (
    date DATE PRIMARY KEY,
    total_orders INT DEFAULT 0,
    total_revenue DECIMAL(12,2) DEFAULT 0,
    avg_order_value DECIMAL(10,2) DEFAULT 0,
    unique_customers INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Populate daily summary (run this as a scheduled job)
INSERT INTO daily_sales_summary (date, total_orders, total_revenue, avg_order_value, unique_customers)
SELECT 
    DATE(order_date) as date,
    COUNT(*) as total_orders,
    SUM(total_amount) as total_revenue,
    AVG(total_amount) as avg_order_value,
    COUNT(DISTINCT user_id) as unique_customers
FROM orders
WHERE status = 'delivered'
    AND DATE(order_date) = CURDATE() - INTERVAL 1 DAY
GROUP BY DATE(order_date)
ON DUPLICATE KEY UPDATE
    total_orders = VALUES(total_orders),
    total_revenue = VALUES(total_revenue),
    avg_order_value = VALUES(avg_order_value),
    unique_customers = VALUES(unique_customers),
    updated_at = CURRENT_TIMESTAMP;

-- Trending products (using window functions)
WITH product_sales AS (
    SELECT 
        p.id,
        p.name,
        DATE(o.order_date) as sale_date,
        SUM(oi.quantity) as daily_quantity,
        SUM(oi.quantity * oi.unit_price) as daily_revenue
    FROM products p
    JOIN order_items oi ON p.id = oi.product_id
    JOIN orders o ON oi.order_id = o.id
    WHERE o.status = 'delivered'
        AND o.order_date >= DATE_SUB(NOW(), INTERVAL 30 DAY)
    GROUP BY p.id, p.name, DATE(o.order_date)
),
product_trends AS (
    SELECT 
        *,
        AVG(daily_quantity) OVER (
            PARTITION BY id 
            ORDER BY sale_date 
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ) as avg_7day_quantity,
        LAG(daily_quantity, 7) OVER (
            PARTITION BY id ORDER BY sale_date
        ) as quantity_7days_ago
    FROM product_sales
)
SELECT 
    id,
    name,
    sale_date,
    daily_quantity,
    avg_7day_quantity,
    CASE 
        WHEN quantity_7days_ago > 0 THEN 
            ROUND((daily_quantity - quantity_7days_ago) * 100.0 / quantity_7days_ago, 2)
        ELSE NULL
    END as week_over_week_growth
FROM product_trends
WHERE sale_date = CURDATE() - INTERVAL 1 DAY
ORDER BY week_over_week_growth DESC;
```

### 📘 Bulk Processing Patterns

```sql
-- Bulk insert with temp table
CREATE TEMPORARY TABLE temp_product_updates (
    product_id INT,
    new_stock INT,
    new_price DECIMAL(10,2)
);

-- Insert bulk data (from CSV or API)
INSERT INTO temp_product_updates VALUES
    (1, 100, 99.99),
    (2, 50, 149.99),
    (3, 200, 29.99);

-- Bulk update using temp table
UPDATE products p
JOIN temp_product_updates tpu ON p.id = tpu.product_id
SET p.stock_quantity = tpu.new_stock,
    p.price = tpu.new_price,
    p.updated_at = NOW();

-- Bulk operations with WHERE IN
UPDATE products 
SET is_active = FALSE
WHERE id IN (1, 2, 3, 4, 5);

-- Batch processing for large datasets
DELIMITER //
CREATE PROCEDURE ProcessLargeDataset()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE batch_size INT DEFAULT 1000;
    DECLARE offset_val INT DEFAULT 0;
    
    process_loop: LOOP
        -- Process batch
        UPDATE products 
        SET updated_at = NOW()
        WHERE is_active = TRUE
        LIMIT batch_size;
        
        -- Check if we processed any rows
        IF ROW_COUNT() = 0 THEN
            LEAVE process_loop;
        END IF;
        
        -- Small delay to prevent overwhelming the database
        SELECT SLEEP(0.1);
        
    END LOOP;
END//
DELIMITER ;
```

---

## 🚀 5. Integration with Backend Frameworks

### 📘 FastAPI Integration Examples

```python
# Database connection setup
import mysql.connector
from mysql.connector import pooling
import os
from typing import Optional, List
from pydantic import BaseModel

# Connection pool configuration
config = {
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME'),
    'pool_name': 'web_app_pool',
    'pool_size': 10,
    'pool_reset_session': True
}

pool = pooling.MySQLConnectionPool(**config)

# Pydantic models
class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    category_id: Optional[int] = None
    stock_quantity: int = 0

class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    stock_quantity: int
    is_active: bool

# Database operations with proper error handling
async def create_product(product: ProductCreate) -> int:
    connection = pool.get_connection()
    try:
        cursor = connection.cursor()
        query = """
            INSERT INTO products (name, description, price, category_id, stock_quantity)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (
            product.name, 
            product.description, 
            product.price,
            product.category_id,
            product.stock_quantity
        ))
        connection.commit()
        return cursor.lastrowid
    except mysql.connector.Error as err:
        connection.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {err}")
    finally:
        cursor.close()
        connection.close()

async def get_products(
    skip: int = 0, 
    limit: int = 20,
    search: Optional[str] = None,
    category_id: Optional[int] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None
) -> List[ProductResponse]:
    connection = pool.get_connection()
    try:
        cursor = connection.cursor(dictionary=True)
        
        # Dynamic query building
        conditions = ["p.is_active = TRUE", "p.deleted_at IS NULL"]
        params = []
        
        if search:
            conditions.append("(p.name LIKE %s OR p.description LIKE %s)")
            search_param = f"%{search}%"
            params.extend([search_param, search_param])
            
        if category_id:
            conditions.append("p.category_id = %s")
            params.append(category_id)
            
        if min_price:
            conditions.append("p.price >= %s")
            params.append(min_price)
            
        if max_price:
            conditions.append("p.price <= %s")
            params.append(max_price)
        
        where_clause = " AND ".join(conditions) if conditions else "1=1"
        
        query = f"""
            SELECT 
                p.id, p.name, p.price, p.stock_quantity, p.is_active,
                c.name as category_name
            FROM products p
            LEFT JOIN categories c ON p.category_id = c.id
            WHERE {where_clause}
            ORDER BY p.created_at DESC
            LIMIT %s OFFSET %s
        """
        
        params.extend([limit, skip])
        cursor.execute(query, params)
        
        return cursor.fetchall()
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Database error: {err}")
    finally:
        cursor.close()
        connection.close()

# Transaction example
async def process_order(user_id: int, items: List[dict]) -> int:
    connection = pool.get_connection()
    try:
        connection.start_transaction()
        cursor = connection.cursor()
        
        # Create order
        cursor.execute(
            "INSERT INTO orders (user_id, total_amount, status) VALUES (%s, %s, %s)",
            (user_id, 0, 'pending')
        )
        order_id = cursor.lastrowid
        
        total_amount = 0
        for item in items:
            # Check stock
            cursor.execute(
                "SELECT stock_quantity, price FROM products WHERE id = %s FOR UPDATE",
                (item['product_id'],)
            )
            result = cursor.fetchone()
            
            if not result or result[0] < item['quantity']:
                raise HTTPException(status_code=400, detail="Insufficient stock")
            
            # Add order item
            cursor.execute("""
                INSERT INTO order_items (order_id, product_id, quantity, unit_price)
                VALUES (%s, %s, %s, %s)
            """, (order_id, item['product_id'], item['quantity'], result[1]))
            
            # Update stock
            cursor.execute(
                "UPDATE products SET stock_quantity = stock_quantity - %s WHERE id = %s",
                (item['quantity'], item['product_id'])
            )
            
            total_amount += result[1] * item['quantity']
        
        # Update order total
        cursor.execute(
            "UPDATE orders SET total_amount = %s WHERE id = %s",
            (total_amount, order_id)
        )
        
        connection.commit()
        return order_id
        
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        cursor.close()
        connection.close()
```

### 📘 SQL Injection Prevention

```python
# ❌ NEVER DO THIS - Vulnerable to SQL injection
def get_user_bad(username: str):
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)  # Dangerous!

# ✅ ALWAYS DO THIS - Use parameterized queries
def get_user_safe(username: str):
    query = "SELECT * FROM users WHERE username = %s"
    cursor.execute(query, (username,))

# ✅ Dynamic query building safely
def search_products_safe(filters: dict):
    base_query = "SELECT * FROM products WHERE 1=1"
    params = []
    
    if filters.get('name'):
        base_query += " AND name LIKE %s"
        params.append(f"%{filters['name']}%")
    
    if filters.get('category_id'):
        base_query += " AND category_id = %s"
        params.append(filters['category_id'])
    
    if filters.get('min_price'):
        base_query += " AND price >= %s"
        params.append(filters['min_price'])
    
    cursor.execute(base_query, params)
```

### 📘 Performance Optimization Techniques

```sql
-- Use EXPLAIN to analyze query performance
EXPLAIN SELECT 
    u.username,
    COUNT(o.id) as order_count,
    SUM(o.total_amount) as total_spent
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE u.created_at >= '2024-01-01'
GROUP BY u.id, u.username;

-- Query optimization patterns
-- ✅ Use covering indexes
CREATE INDEX idx_orders_user_date_amount ON orders(user_id, order_date, total_amount);

-- ✅ Use EXISTS instead of IN for subqueries
SELECT * FROM users u
WHERE EXISTS (
    SELECT 1 FROM orders o 
    WHERE o.user_id = u.id AND o.total_amount > 1000
);

-- ✅ Use LIMIT for large result sets
SELECT * FROM products 
WHERE category_id = 1 
ORDER BY created_at DESC 
LIMIT 50;

-- ✅ Avoid SELECT * in production
SELECT id, name, price, stock_quantity 
FROM products 
WHERE is_active = TRUE;

-- ✅ Use appropriate JOIN types
-- INNER JOIN when you need matching records only
-- LEFT JOIN when you need all records from left table
SELECT 
    p.name,
    COALESCE(AVG(r.rating), 0) as avg_rating,
    COUNT(r.id) as review_count
FROM products p
LEFT JOIN reviews r ON p.id = r.product_id
GROUP BY p.id, p.name;
```

### 📘 Database Migration Patterns

```sql
-- Migration structure
-- migrations/001_create_users_table.sql
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- migrations/002_add_user_profile_fields.sql
ALTER TABLE users 
ADD COLUMN first_name VARCHAR(50),
ADD COLUMN last_name VARCHAR(50),
ADD COLUMN phone VARCHAR(20),
ADD COLUMN date_of_birth DATE;

-- migrations/003_create_products_table.sql
CREATE TABLE products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(200) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    stock_quantity INT DEFAULT 0,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_name (name),
    INDEX idx_price (price),
    INDEX idx_active (is_active)
);

-- Migration tracking table
CREATE TABLE schema_migrations (
    version VARCHAR(50) PRIMARY KEY,
    applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Python migration runner example
def run_migrations():
    migrations_dir = './migrations'
    applied_migrations = get_applied_migrations()
    
    migration_files = sorted([f for f in os.listdir(migrations_dir) if f.endswith('.sql')])
    
    for migration_file in migration_files:
        version = migration_file.replace('.sql', '')
        
        if version not in applied_migrations:
            with open(f'{migrations_dir}/{migration_file}', 'r') as f:
                sql = f.read()
            
            try:
                cursor.execute(sql)
                cursor.execute(
                    "INSERT INTO schema_migrations (version) VALUES (%s)",
                    (version,)
                )
                connection.commit()
                print(f"Applied migration: {version}")
            except Exception as e:
                connection.rollback()
                print(f"Failed to apply migration {version}: {e}")
                break
```

### 📘 Testing SQL in Backend Applications

```python
import pytest
import mysql.connector
from unittest.mock import Mock, patch

# Test data setup
@pytest.fixture
def test_db():
    # Use test database
    connection = mysql.connector.connect(
        host='localhost',
        user='test_user',
        password='test_pass',
        database='test_db'
    )
    
    # Setup test data
    cursor = connection.cursor()
    cursor.execute("TRUNCATE TABLE users")
    cursor.execute("TRUNCATE TABLE products")
    cursor.execute("TRUNCATE TABLE orders")
    
    # Insert test data
    cursor.execute("""
        INSERT INTO users (username, email, password_hash) VALUES 
        ('testuser', 'test@example.com', 'hashed_password')
    """)
    
    cursor.execute("""
        INSERT INTO products (name, price, stock_quantity) VALUES
        ('Test Product', 99.99, 10)
    """)
    
    connection.commit()
    yield connection
    
    # Cleanup
    cursor.execute("TRUNCATE TABLE users")
    cursor.execute("TRUNCATE TABLE products") 
    cursor.execute("TRUNCATE TABLE orders")
    connection.commit()
    connection.close()

# Test CRUD operations
def test_create_user(test_db):
    cursor = test_db.cursor()
    
    cursor.execute("""
        INSERT INTO users (username, email, password_hash)
        VALUES (%s, %s, %s)
    """, ('newuser', 'new@example.com', 'hashed'))
    
    test_db.commit()
    
    cursor.execute("SELECT username FROM users WHERE email = %s", ('new@example.com',))
    result = cursor.fetchone()
    
    assert result[0] == 'newuser'

def test_order_creation_with_stock_check(test_db):
    cursor = test_db.cursor()
    
    # Test successful order
    test_db.start_transaction()
    try:
        # Check stock
        cursor.execute("SELECT stock_quantity FROM products WHERE id = 1")
        stock = cursor.fetchone()[0]
        assert stock >= 2
        
        # Create order
        cursor.execute("""
            INSERT INTO orders (user_id, total_amount, status)
            VALUES (1, 199.98, 'pending')
        """)
        order_id = cursor.lastrowid
        
        # Add order items
        cursor.execute("""
            INSERT INTO order_items (order_id, product_id, quantity, unit_price)
            VALUES (%s, 1, 2, 99.99)
        """, (order_id,))
        
        # Update stock
        cursor.execute("""
            UPDATE products SET stock_quantity = stock_quantity - 2 
            WHERE id = 1
        """)
        
        test_db.commit()
        
        # Verify stock was updated
        cursor.execute("SELECT stock_quantity FROM products WHERE id = 1")
        new_stock = cursor.fetchone()[0]
        assert new_stock == stock - 2
        
    except Exception:
        test_db.rollback()
        raise

# Mock testing for external dependencies
@patch('mysql.connector.connect')
def test_database_connection_error(mock_connect):
    mock_connect.side_effect = mysql.connector.Error("Connection failed")
    
    with pytest.raises(mysql.connector.Error):
        connection = mysql.connector.connect(host='localhost')
```

---

## 📚 6. Advanced Topics and Best Practices

### 📘 Query Performance Monitoring

```sql
-- Enable slow query log (MySQL)
SET GLOBAL slow_query_log = 'ON';
SET GLOBAL long_query_time = 1; -- Log queries taking > 1 second

-- Query profiling
SET profiling = 1;
SELECT * FROM products WHERE name LIKE '%laptop%';
SHOW PROFILES;
SHOW PROFILE FOR QUERY 1;

-- Performance schema queries
SELECT 
    DIGEST_TEXT,
    COUNT_STAR,
    AVG_TIMER_WAIT/1000000000 AS avg_time_seconds,
    SUM_TIMER_WAIT/1000000000 AS total_time_seconds
FROM performance_schema.events_statements_summary_by_digest
ORDER BY SUM_TIMER_WAIT DESC
LIMIT 10;

-- Index usage analysis
SELECT 
    OBJECT_NAME,
    INDEX_NAME,
    COUNT_FETCH,
    COUNT_INSERT,
    COUNT_UPDATE,
    COUNT_DELETE
FROM performance_schema.table_io_waits_summary_by_index_usage
WHERE OBJECT_SCHEMA = 'your_database'
ORDER BY COUNT_FETCH DESC;
```

### 📘 Database Backup and Recovery

```sql
-- Backup strategies
-- Full backup
mysqldump -u root -p --single-transaction --routines --triggers your_database > backup.sql

-- Backup with compression
mysqldump -u root -p --single-transaction your_database | gzip > backup.sql.gz

-- Incremental backup using binary logs
FLUSH LOGS;
-- Copy binary log files for point-in-time recovery

-- Restore
mysql -u root -p your_database < backup.sql

-- Point-in-time recovery
mysqlbinlog --start-datetime="2024-01-01 10:00:00" \
           --stop-datetime="2024-01-01 11:00:00" \
           binlog.000001 | mysql -u root -p your_database
```

### 📘 Security Best Practices

```sql
-- User management
CREATE USER 'app_user'@'%' IDENTIFIED BY 'strong_password';
GRANT SELECT, INSERT, UPDATE, DELETE ON your_database.* TO 'app_user'@'%';

-- Read-only user for analytics
CREATE USER 'analytics_user'@'%' IDENTIFIED BY 'analytics_password';
GRANT SELECT ON your_database.* TO 'analytics_user'@'%';

-- Revoke dangerous permissions
REVOKE FILE, PROCESS, SUPER ON *.* FROM 'app_user'@'%';

-- Enable SSL
-- In my.cnf:
-- ssl-ca=ca.pem
-- ssl-cert=server-cert.pem
-- ssl-key=server-key.pem

-- Require SSL for users
ALTER USER 'app_user'@'%' REQUIRE SSL;

-- Row-level security (PostgreSQL example)
CREATE POLICY user_data_policy ON orders
    FOR ALL TO app_user
    USING (user_id = current_setting('app.current_user_id')::INT);

ALTER TABLE orders ENABLE ROW LEVEL SECURITY;
```

---

## 🎯 7. Real-World Project Implementation

### 📘 E-commerce Backend Schema

```sql
-- Complete e-commerce schema
CREATE DATABASE ecommerce_db;
USE ecommerce_db;

-- Users and Authentication
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    phone VARCHAR(20),
    email_verified BOOLEAN DEFAULT FALSE,
    status ENUM('active', 'inactive', 'suspended') DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    deleted_at TIMESTAMP NULL,
    INDEX idx_email (email),
    INDEX idx_username (username),
    INDEX idx_status (status)
);

-- Address management
CREATE TABLE addresses (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    type ENUM('shipping', 'billing') DEFAULT 'shipping',
    street_address VARCHAR(200) NOT NULL,
    city VARCHAR(100) NOT NULL,
    state VARCHAR(100),
    postal_code VARCHAR(20),
    country VARCHAR(100) NOT NULL,
    is_default BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    INDEX idx_user_type (user_id, type)
);

-- Categories
CREATE TABLE categories (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    slug VARCHAR(100) UNIQUE NOT NULL,
    description TEXT,
    parent_id INT,
    image_url VARCHAR(500),
    is_active BOOLEAN DEFAULT TRUE,
    sort_order INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (parent_id) REFERENCES categories(id) ON DELETE SET NULL,
    INDEX idx_parent (parent_id),
    INDEX idx_active (is_active),
    INDEX idx_slug (slug)
);

-- Products
CREATE TABLE products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(200) NOT NULL,
    slug VARCHAR(200) UNIQUE NOT NULL,
    description TEXT,
    short_description VARCHAR(500),
    sku VARCHAR(100) UNIQUE,
    price DECIMAL(10, 2) NOT NULL,
    sale_price DECIMAL(10, 2),
    cost DECIMAL(10, 2),
    weight DECIMAL(8, 2),
    dimensions VARCHAR(100),
    stock_quantity INT DEFAULT 0,
    low_stock_threshold INT DEFAULT 5,
    manage_stock BOOLEAN DEFAULT TRUE,
    category_id INT,
    brand_id INT,
    status ENUM('active', 'inactive', 'out_of_stock') DEFAULT 'active',
    featured BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE SET NULL,
    INDEX idx_category (category_id),
    INDEX idx_status (status),
    INDEX idx_featured (featured),
    INDEX idx_price (price),
    INDEX idx_slug (slug),
    FULLTEXT idx_search (name, description, short_description)
);

-- Product images
CREATE TABLE product_images (
    id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT NOT NULL,
    image_url VARCHAR(500) NOT NULL,
    alt_text VARCHAR(200),
    sort_order INT DEFAULT 0,
    is_primary BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE,
    INDEX idx_product (product_id)
);

-- Reviews and ratings
CREATE TABLE reviews (
    id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT NOT NULL,
    user_id INT NOT NULL,
    order_id INT,
    rating INT NOT NULL CHECK (rating BETWEEN 1 AND 5),
    title VARCHAR(200),
    comment TEXT,
    is_verified BOOLEAN DEFAULT FALSE,
    helpful_votes INT DEFAULT 0,
    status ENUM('pending', 'approved', 'rejected') DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE SET NULL,
    UNIQUE KEY unique_user_product_order (user_id, product_id, order_id),
    INDEX idx_product (product_id),
    INDEX idx_rating (rating),
    INDEX idx_status (status)
);

-- Coupons and discounts
CREATE TABLE coupons (
    id INT PRIMARY KEY AUTO_INCREMENT,
    code VARCHAR(50) UNIQUE NOT NULL,
    type ENUM('fixed', 'percentage') NOT NULL,
    value DECIMAL(10, 2) NOT NULL,
    minimum_amount DECIMAL(10, 2) DEFAULT 0,
    usage_limit INT,
    used_count INT DEFAULT 0,
    valid_from TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    valid_until TIMESTAMP NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_code (code),
    INDEX idx_active_dates (is_active, valid_from, valid_until)
);

-- Wishlist
CREATE TABLE wishlist_items (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    product_id INT NOT NULL,
    added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE,
    UNIQUE KEY unique_user_product (user_id, product_id),
    INDEX idx_user (user_id)
);
```

### 📘 Advanced E-commerce Queries

```sql
-- Product search with filters and sorting
SELECT 
    p.id,
    p.name,
    p.price,
    p.sale_price,
    p.stock_quantity,
    c.name AS category_name,
    COALESCE(AVG(r.rating), 0) AS avg_rating,
    COUNT(r.id) AS review_count,
    pi.image_url AS primary_image,
    MATCH(p.name, p.description) AGAINST(? IN NATURAL LANGUAGE MODE) AS relevance_score
FROM products p
LEFT JOIN categories c ON p.category_id = c.id
LEFT JOIN reviews r ON p.id = r.product_id AND r.status = 'approved'
LEFT JOIN product_images pi ON p.id = pi.product_id AND pi.is_primary = TRUE
WHERE p.status = 'active'
    AND (? IS NULL OR MATCH(p.name, p.description) AGAINST(? IN NATURAL LANGUAGE MODE))
    AND (? IS NULL OR p.category_id = ?)
    AND (? IS NULL OR p.price >= ?)
    AND (? IS NULL OR p.price <= ?)
    AND (? IS NULL OR p.stock_quantity > 0)
GROUP BY p.id, p.name, p.price, p.sale_price, p.stock_quantity, c.name, pi.image_url
HAVING (? IS NULL OR avg_rating >= ?)
ORDER BY 
    CASE WHEN ? = 'relevance' THEN relevance_score END DESC,
    CASE WHEN ? = 'price_asc' THEN p.price END ASC,
    CASE WHEN ? = 'price_desc' THEN p.price END DESC,
    CASE WHEN ? = 'rating' THEN avg_rating END DESC,
    CASE WHEN ? = 'newest' THEN p.created_at END DESC,
    p.featured DESC,
    p.created_at DESC
LIMIT ? OFFSET ?;

-- User order history with items
SELECT 
    o.id,
    o.order_number,
    o.status,
    o.total_amount,
    o.order_date,
    JSON_ARRAYAGG(
        JSON_OBJECT(
            'product_id', oi.product_id,
            'product_name', p.name,
            'quantity', oi.quantity,
            'unit_price', oi.unit_price,
            'total_price', oi.total_price,
            'image_url', pi.image_url
        )
    ) AS items
FROM orders o
INNER JOIN order_items oi ON o.id = oi.order_id
INNER JOIN products p ON oi.product_id = p.id
LEFT JOIN product_images pi ON p.id = pi.product_id AND pi.is_primary = TRUE
WHERE o.user_id = ?
GROUP BY o.id, o.order_number, o.status, o.total_amount, o.order_date
ORDER BY o.order_date DESC
LIMIT 20;

-- Product recommendations based on purchase history
WITH user_purchases AS (
    SELECT DISTINCT oi.product_id
    FROM orders o
    INNER JOIN order_items oi ON o.id = oi.order_id
    WHERE o.user_id = ? AND o.status = 'delivered'
),
similar_users AS (
    SELECT o.user_id, COUNT(*) AS common_products
    FROM orders o
    INNER JOIN order_items oi ON o.id = oi.order_id
    INNER JOIN user_purchases up ON oi.product_id = up.product_id
    WHERE o.user_id != ? AND o.status = 'delivered'
    GROUP BY o.user_id
    HAVING COUNT(*) >= 2
    ORDER BY common_products DESC
    LIMIT 10
),
recommended_products AS (
    SELECT 
        oi.product_id,
        COUNT(*) AS recommendation_score
    FROM similar_users su
    INNER JOIN orders o ON su.user_id = o.user_id
    INNER JOIN order_items oi ON o.id = oi.order_id
    LEFT JOIN user_purchases up ON oi.product_id = up.product_id
    WHERE up.product_id IS NULL -- Products user hasn't bought
        AND o.status = 'delivered'
    GROUP BY oi.product_id
    ORDER BY recommendation_score DESC
    LIMIT 20
)
SELECT 
    p.id,
    p.name,
    p.price,
    p.sale_price,
    rp.recommendation_score,
    pi.image_url,
    COALESCE(AVG(r.rating), 0) AS avg_rating
FROM recommended_products rp
INNER JOIN products p ON rp.product_id = p.id
LEFT JOIN product_images pi ON p.id = pi.product_id AND pi.is_primary = TRUE
LEFT JOIN reviews r ON p.id = r.product_id AND r.status = 'approved'
WHERE p.status = 'active' AND p.stock_quantity > 0
GROUP BY p.id, p.name, p.price, p.sale_price, rp.recommendation_score, pi.image_url
ORDER BY rp.recommendation_score DESC, avg_rating DESC;

-- Sales analytics dashboard
WITH daily_sales AS (
    SELECT 
        DATE(order_date) AS sale_date,
        COUNT(*) AS order_count,
        SUM(total_amount) AS revenue,
        AVG(total_amount) AS avg_order_value,
        COUNT(DISTINCT user_id) AS unique_customers
    FROM orders
    WHERE status IN ('delivered', 'shipped')
        AND order_date >= DATE_SUB(NOW(), INTERVAL 30 DAY)
    GROUP BY DATE(order_date)
),
product_performance AS (
    SELECT 
        p.id,
        p.name,
        SUM(oi.quantity) AS units_sold,
        SUM(oi.total_price) AS revenue,
        COUNT(DISTINCT o.user_id) AS unique_buyers
    FROM products p
    INNER JOIN order_items oi ON p.id = oi.product_id
    INNER JOIN orders o ON oi.order_id = o.id
    WHERE o.status IN ('delivered', 'shipped')
        AND o.order_date >= DATE_SUB(NOW(), INTERVAL 30 DAY)
    GROUP BY p.id, p.name
),
customer_segments AS (
    SELECT 
        CASE 
            WHEN total_spent >= 1000 THEN 'VIP'
            WHEN total_spent >= 500 THEN 'Premium'
            WHEN order_count >= 5 THEN 'Regular'
            ELSE 'New'
        END AS segment,
        COUNT(*) AS customer_count,
        AVG(total_spent) AS avg_customer_value
    FROM (
        SELECT 
            user_id,
            COUNT(*) AS order_count,
            SUM(total_amount) AS total_spent
        FROM orders
        WHERE status IN ('delivered', 'shipped')
        GROUP BY user_id
    ) user_stats
    GROUP BY segment
)
SELECT 
    'Daily Sales Summary' AS metric_type,
    JSON_OBJECT(
        'total_revenue', (SELECT SUM(revenue) FROM daily_sales),
        'total_orders', (SELECT SUM(order_count) FROM daily_sales),
        'avg_order_value', (SELECT AVG(avg_order_value) FROM daily_sales),
        'unique_customers', (SELECT SUM(unique_customers) FROM daily_sales)
    ) AS data
UNION ALL
SELECT 
    'Top Products' AS metric_type,
    JSON_ARRAYAGG(
        JSON_OBJECT(
            'name', name,
            'units_sold', units_sold,
            'revenue', revenue,
            'unique_buyers', unique_buyers
        )
    ) AS data
FROM (SELECT * FROM product_performance ORDER BY revenue DESC LIMIT 5) top_products
UNION ALL
SELECT 
    'Customer Segments' AS metric_type,
    JSON_ARRAYAGG(
        JSON_OBJECT(
            'segment', segment,
            'customer_count', customer_count,
            'avg_customer_value', avg_customer_value
        )
    ) AS data
FROM customer_segments;

-- Inventory management queries
-- Low stock alert
SELECT 
    p.id,
    p.name,
    p.sku,
    p.stock_quantity,
    p.low_stock_threshold,
    c.name AS category_name,
    COALESCE(SUM(oi.quantity), 0) AS units_sold_30_days,
    CASE 
        WHEN COALESCE(SUM(oi.quantity), 0) > 0 THEN
            p.stock_quantity / (COALESCE(SUM(oi.quantity), 0) / 30.0)
        ELSE NULL
    END AS days_of_stock_remaining
FROM products p
LEFT JOIN categories c ON p.category_id = c.id
LEFT JOIN order_items oi ON p.id = oi.product_id
LEFT JOIN orders o ON oi.order_id = o.id 
    AND o.status IN ('delivered', 'shipped')
    AND o.order_date >= DATE_SUB(NOW(), INTERVAL 30 DAY)
WHERE p.status = 'active'
    AND p.manage_stock = TRUE
    AND p.stock_quantity <= p.low_stock_threshold
GROUP BY p.id, p.name, p.sku, p.stock_quantity, p.low_stock_threshold, c.name
ORDER BY p.stock_quantity ASC;

-- ABC analysis for inventory
WITH product_revenue AS (
    SELECT 
        p.id,
        p.name,
        p.stock_quantity,
        p.cost,
        COALESCE(SUM(oi.total_price), 0) AS revenue_90_days,
        p.stock_quantity * p.cost AS inventory_value
    FROM products p
    LEFT JOIN order_items oi ON p.id = oi.product_id
    LEFT JOIN orders o ON oi.order_id = o.id
        AND o.status IN ('delivered', 'shipped')
        AND o.order_date >= DATE_SUB(NOW(), INTERVAL 90 DAY)
    WHERE p.status = 'active'
    GROUP BY p.id, p.name, p.stock_quantity, p.cost
),
revenue_percentiles AS (
    SELECT 
        *,
        PERCENT_RANK() OVER (ORDER BY revenue_90_days DESC) AS revenue_percentile
    FROM product_revenue
)
SELECT 
    id,
    name,
    stock_quantity,
    inventory_value,
    revenue_90_days,
    CASE 
        WHEN revenue_percentile <= 0.2 THEN 'A'
        WHEN revenue_percentile <= 0.5 THEN 'B'
        ELSE 'C'
    END AS abc_category,
    CASE 
        WHEN revenue_percentile <= 0.2 THEN 'Focus on availability'
        WHEN revenue_percentile <= 0.5 THEN 'Moderate management'
        ELSE 'Minimize holding costs'
    END AS management_strategy
FROM revenue_percentiles
ORDER BY revenue_90_days DESC;
```

### 📘 Performance Optimization for E-commerce

```sql
-- Optimized indexes for e-commerce queries
-- Product search optimization
CREATE INDEX idx_products_search_filter ON products(status, category_id, price);
CREATE INDEX idx_products_featured_created ON products(featured, created_at);

-- Order queries optimization
CREATE INDEX idx_orders_user_status_date ON orders(user_id, status, order_date);
CREATE INDEX idx_orders_status_date ON orders(status, order_date);

-- Analytics optimization
CREATE INDEX idx_order_items_product_order ON order_items(product_id, order_id);
CREATE INDEX idx_reviews_product_status ON reviews(product_id, status, rating);

-- Partitioning for large tables (MySQL 8.0+)
ALTER TABLE orders PARTITION BY RANGE (YEAR(order_date)) (
    PARTITION p2023 VALUES LESS THAN (2024),
    PARTITION p2024 VALUES LESS THAN (2025),
    PARTITION p2025 VALUES LESS THAN (2026),
    PARTITION p_future VALUES LESS THAN MAXVALUE
);

-- Materialized views for analytics (PostgreSQL)
CREATE MATERIALIZED VIEW daily_sales_summary AS
SELECT 
    DATE(order_date) AS sale_date,
    COUNT(*) AS order_count,
    SUM(total_amount) AS total_revenue,
    AVG(total_amount) AS avg_order_value,
    COUNT(DISTINCT user_id) AS unique_customers
FROM orders
WHERE status IN ('delivered', 'shipped')
GROUP BY DATE(order_date);

-- Refresh materialized view (run daily)
REFRESH MATERIALIZED VIEW daily_sales_summary;

-- Query optimization techniques
-- Use prepared statements
PREPARE product_search FROM 
'SELECT p.*, AVG(r.rating) as avg_rating 
 FROM products p 
 LEFT JOIN reviews r ON p.id = r.product_id 
 WHERE p.category_id = ? AND p.price BETWEEN ? AND ?
 GROUP BY p.id 
 ORDER BY avg_rating DESC 
 LIMIT ?';

-- Execute prepared statement
EXECUTE product_search USING @category_id, @min_price, @max_price, @limit;

-- Use query hints when necessary (MySQL)
SELECT /*+ USE_INDEX(products, idx_products_search_filter) */
    p.name, p.price
FROM products p
WHERE p.status = 'active' AND p.category_id = 1;
```

### 📘 Database Monitoring and Maintenance

```sql
-- Database health monitoring queries
-- Table sizes
SELECT 
    table_name,
    ROUND(((data_length + index_length) / 1024 / 1024), 2) AS table_size_mb,
    ROUND((data_length / 1024 / 1024), 2) AS data_size_mb,
    ROUND((index_length / 1024 / 1024), 2) AS index_size_mb,
    table_rows
FROM information_schema.tables
WHERE table_schema = 'ecommerce_db'
ORDER BY (data_length + index_length) DESC;

-- Index effectiveness
SELECT 
    t.table_name,
    t.index_name,
    t.cardinality,
    t.sub_part,
    t.packed,
    s.cardinality / t.cardinality * 100 AS selectivity_percent
FROM information_schema.statistics t
JOIN information_schema.statistics s ON t.table_name = s.table_name
WHERE t.table_schema = 'ecommerce_db'
    AND t.cardinality > 0
ORDER BY selectivity_percent DESC;

-- Slow query analysis
SELECT 
    query_time,
    lock_time,
    rows_sent,
    rows_examined,
    db,
    sql_text
FROM mysql.slow_log
WHERE start_time >= DATE_SUB(NOW(), INTERVAL 1 DAY)
ORDER BY query_time DESC
LIMIT 10;

-- Database maintenance tasks
-- Optimize tables
OPTIMIZE TABLE products, orders, order_items, users;

-- Analyze tables for better query planning
ANALYZE TABLE products, orders, order_items, users;

-- Update table statistics
UPDATE mysql.innodb_table_stats 
SET n_rows = (SELECT COUNT(*) FROM products) 
WHERE table_name = 'products';

-- Archive old data
-- Move old orders to archive table
CREATE TABLE orders_archive LIKE orders;

INSERT INTO orders_archive 
SELECT * FROM orders 
WHERE order_date < DATE_SUB(NOW(), INTERVAL 2 YEAR)
    AND status IN ('delivered', 'cancelled');

DELETE FROM orders 
WHERE order_date < DATE_SUB(NOW(), INTERVAL 2 YEAR)
    AND status IN ('delivered', 'cancelled');
```

---

## 🏆 8. Final Checklist and Best Practices Summary

### 📘 SQL Mastery Checklist

**Fundamentals (✅ Must Know)**
- [ ] CRUD operations (CREATE, READ, UPDATE, DELETE)
- [ ] Data types and constraints
- [ ] Primary keys, foreign keys, indexes
- [ ] Basic JOINs (INNER, LEFT, RIGHT, FULL)
- [ ] WHERE clauses and filtering
- [ ] ORDER BY and LIMIT for pagination
- [ ] GROUP BY and aggregate functions

**Intermediate (✅ Should Know)**
- [ ] Subqueries and correlated subqueries
- [ ] CASE statements for conditional logic
- [ ] String and date functions
- [ ] UNION and set operations
- [ ] EXISTS and NOT EXISTS
- [ ] Window functions basics (ROW_NUMBER, RANK)
- [ ] Views for data abstraction

**Advanced (✅ Great to Know)**
- [ ] Common Table Expressions (CTEs)
- [ ] Advanced window functions (LAG, LEAD, NTILE)
- [ ] Recursive queries
- [ ] Stored procedures and functions
- [ ] Triggers for business logic
- [ ] Transactions and ACID properties
- [ ] Performance optimization techniques

**Production Ready (✅ Must Know for Backend)**
- [ ] SQL injection prevention
- [ ] Connection pooling
- [ ] Error handling and transactions
- [ ] Database migrations
- [ ] Backup and recovery strategies
- [ ] Monitoring and performance tuning
- [ ] Security best practices

### 📘 Backend Integration Best Practices

```python
# Essential patterns for backend developers

# 1. Always use parameterized queries
def get_user_orders(user_id: int, status: str = None):
    query = "SELECT * FROM orders WHERE user_id = %s"
    params = [user_id]
    
    if status:
        query += " AND status = %s"
        params.append(status)
    
    cursor.execute(query, params)
    return cursor.fetchall()

# 2. Implement proper error handling
def create_order(user_id: int, items: List[dict]):
    connection = get_db_connection()
    try:
        connection.start_transaction()
        cursor = connection.cursor()
        
        # Your order creation logic here
        
        connection.commit()
        return order_id
    except Exception as e:
        connection.rollback()
        logger.error(f"Order creation failed: {e}")
        raise HTTPException(status_code=500, detail="Order creation failed")
    finally:
        cursor.close()
        connection.close()

# 3. Use connection pooling
pool = mysql.connector.pooling.MySQLConnectionPool(
    pool_name="web_app_pool",
    pool_size=20,
    pool_reset_session=True,
    host=DB_HOST,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)

# 4. Implement proper pagination
def get_products(page: int = 1, per_page: int = 20, filters: dict = None):
    offset = (page - 1) * per_page
    
    base_query = """
        SELECT p.*, COUNT(*) OVER() as total_count
        FROM products p
        WHERE p.status = 'active'
    """
    
    # Add dynamic filters
    # ... filter logic
    
    query += " ORDER BY p.created_at DESC LIMIT %s OFFSET %s"
    cursor.execute(query, params + [per_page, offset])
    
    results = cursor.fetchall()
    total_count = results[0]['total_count'] if results else 0
    
    return {
        'items': results,
        'page': page,
        'per_page': per_page,
        'total': total_count,
        'pages': (total_count + per_page - 1) // per_page
    }

# 5. Implement caching for read-heavy operations
import redis
redis_client = redis.Redis(host='localhost', port=6379, db=0)

def get_product_with_cache(product_id: int):
    cache_key = f"product:{product_id}"
    
    # Try cache first
    cached_result = redis_client.get(cache_key)
    if cached_result:
        return json.loads(cached_result)
    
    # Query database
    cursor.execute("""
        SELECT p.*, AVG(r.rating) as avg_rating, COUNT(r.id) as review_count
        FROM products p
        LEFT JOIN reviews r ON p.id = r.product_id
        WHERE p.id = %s AND p.status = 'active'
        GROUP BY p.id
    """, (product_id,))
    
    result = cursor.fetchone()
    
    # Cache for 1 hour
    if result:
        redis_client.setex(cache_key, 3600, json.dumps(result))
    
    return result
```

### 📘 Performance Optimization Checklist

- [ ] **Indexes**: Create appropriate indexes for frequent WHERE, JOIN, and ORDER BY clauses
- [ ] **Query Analysis**: Use EXPLAIN to understand query execution plans
- [ ] **Pagination**: Always use LIMIT and OFFSET for large result sets
- [ ] **Selective Columns**: Avoid SELECT * in production queries
- [ ] **JOIN Optimization**: Use appropriate JOIN types and order
- [ ] **Connection Pooling**: Implement connection pooling for concurrent requests
- [ ] **Caching**: Cache frequently accessed, rarely changed data
- [ ] **Batch Operations**: Use batch inserts/updates for bulk operations
- [ ] **Database Partitioning**: Consider partitioning for very large tables
- [ ] **Regular Maintenance**: Schedule regular OPTIMIZE, ANALYZE table operations

### 📘 Security Checklist

- [ ] **SQL Injection Prevention**: Always use parameterized queries
- [ ] **Least Privilege**: Grant minimum necessary database permissions
- [ ] **SSL/TLS**: Encrypt database connections
- [ ] **Regular Updates**: Keep database software updated
- [ ] **Backup Encryption**: Encrypt database backups
- [ ] **Audit Logging**: Log database access and changes
- [ ] **Password Policies**: Use strong passwords and rotate regularly
- [ ] **Network Security**: Restrict database access to authorized IPs
- [ ] **Data Masking**: Mask sensitive data in non-production environments
- [ ] **Regular Security Audits**: Conduct periodic security assessments

---

## 🎓 Conclusion

This comprehensive guide covers everything you need to know about SQL for backend development, from basic CRUD operations to advanced performance optimization techniques. The key to mastering SQL for backend development is: