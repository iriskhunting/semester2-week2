-- Enable readable output format
.mode columns
.headers on
.nullvalue '<null>'

-- Instructions for students:
-- 1. Open SQLite in terminal: sqlite3 library.db
-- 2. Load this script: .read code.sql
-- 3. Exit SQLite: .exit


-- write your sql code here

-- 1
SELECT title AS book_title, Members.name AS member_name, loan_date
FROM 
Loans JOIN Members
ON Loans.member_id = Members.id
JOIN Books
ON Loans.book_id = Books.id;


-- 2
SELECT title AS book_title, author, Members.name AS member_name, loan_date
FROM
Loans RIGHT JOIN Books
ON Books.id = Loans.book_id
LEFT JOIN Members
ON Loans.member_id = Members.id
ORDER BY book_title;


-- 3
SELECT LibraryBranch.name AS branch_name, title
FROM 
LibraryBranch JOIN Books
ON LibraryBranch.id = Books.branch_id;

-- 4
SELECT LibraryBranch.name AS branch_name, COUNT(Books.id) AS num_books
FROM 
LibraryBranch JOIN Books
ON LibraryBranch.id = Books.branch_id
GROUP BY branch_name;

-- 5
SELECT LibraryBranch.name AS branch_name, COUNT(Books.id) AS num_books
FROM 
LibraryBranch JOIN Books
ON LibraryBranch.id = Books.branch_id
GROUP BY branch_name HAVING num_books > 7;

-- 6
SELECT Members.name AS member_name, COUNT(Loans.id) AS num_loans
FROM 
Members LEFT JOIN Loans
ON Members.id = Loans.member_id
GROUP BY member_name;

-- 7 
SELECT Members.name AS member_name, COUNT(Loans.id) AS num_loans
FROM 
Members LEFT JOIN Loans
ON Members.id = Loans.member_id
GROUP BY member_name HAVING num_loans = 0;

-- 8
SELECT LibraryBranch.name AS branch_name, COUNT(Loans.id) AS total_loans
FROM
LibraryBranch LEFT JOIN Books
ON LibraryBranch.id = Books.branch_id
LEFT JOIN Loans
ON Books.id = Loans.book_id
GROUP BY branch_name;

-- 9
SELECT Members.name AS member_name, title