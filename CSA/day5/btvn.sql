CREATE TABLE Product (
    ID INT,
    Name VARCHAR(255),
    Type VARCHAR(255),
    Price FLOAT,
    DateOfManufacture DATE,
    DateOfExpiry DATE
);

CREATE TABLE Manufacturer (
    ID INT,
    Name VARCHAR(255),
    Country VARCHAR(255)
);

CREATE TABLE Store (
    ID INT,
    Name VARCHAR(255),
    Address VARCHAR(255)
);

INSERT INTO Product (ID, Name, Type, Price, DateOfManufacture, DateOfExpiry)
VALUES
(1, 'A', 'A', 1.1, '2015-09-28', '2015-09-29'),
(2, 'B', 'B', 1.1, '2015-09-28', '2015-09-29'),
(3, 'C', 'C', 1.1, '2015-09-28', '2015-09-29'),
(4, 'D', 'D', 1.1, '2015-09-28', '2015-09-29'),
(5, 'E', 'E', 1.1, '2015-09-28', '2015-09-29'),
(6, 'F', 'F', 1.1, '2015-09-28', '2015-09-29'),
(7, 'G', 'G', 1.1, '2015-09-28', '2015-09-29'),
(8, 'H', 'H', 1.1, '2015-09-28', '2015-09-29'),
(9, 'I', 'I', 1.1, '2015-09-28', '2015-09-29'),
(10, 'J', 'J', 1.1, '2015-09-28', '2015-09-29');

INSERT INTO Manufacturer (ID, Name, Country)
VALUES 
(1, 'A', 'United States'),
(2, 'B', 'United States'),
(3, 'C', 'United States'),
(4, 'D', 'United States'),
(5, 'E', 'United States'),
(6, 'F', 'United States'),
(7, 'G', 'United States'),
(8, 'H', 'United States'),
(9, 'I', 'United States'),
(10, 'J', 'United States');

INSERT INTO Store (ID, Name, Address)
VALUES
(1, 'A', 'Texas'),
(2, 'B', 'Texas'),
(3, 'C', 'Texas'),
(4, 'D', 'Texas'),
(5, 'E', 'Texas'),
(6, 'F', 'Texas'),
(7, 'G', 'Texas'),
(8, 'H', 'Texas'),
(9, 'I', 'Texas'),
(10, 'J', 'Texas');
