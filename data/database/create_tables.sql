DROP DATABASE IF EXISTS transposons;

CREATE DATABASE transposons 
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;

USE transposons;

CREATE TABLE IF NOT EXISTS location (
 id INT NOT NULL AUTO_INCREMENT,
 isFivePrima TINYINT(1),
 minStart INT,
 maxEnd INT,
 PRIMARY KEY (id)
);


CREATE TABLE IF NOT EXISTS chromosome(
    id INT NOT NULL AUTO_INCREMENT
    , chromosomeNumber INT
    , PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS superFamily(
    id INT NOT NULL AUTO_INCREMENT
    , superFamilyName VARCHAR(25)
    , PRIMARY KEY (id)
);
 
CREATE TABLE IF NOT EXISTS family(
    id INT NOT NULL AUTO_INCREMENT
    , familyName VARCHAR(25)
    , idSuperFamily INT
    , PRIMARY KEY (id)
    , FOREIGN KEY fk_family_superfamily (idSuperFamily) REFERENCES superFamily (id)
); 

CREATE TABLE IF NOT EXISTS transposon(
    id INT NOT NULL AUTO_INCREMENT
    , transposonName VARCHAR(10)
    , idOrientation INT 
    , idLocation INT 
    , idFamily INT 
    , idChromosome INT
    , PRIMARY KEY (id)
    , FOREIGN KEY fk_transposon_position (idLocation) REFERENCES location (id)
    , FOREIGN KEY fk_transposon_family (idFamily) REFERENCES family (id)
    , FOREIGN KEY fk_transposon_chromosome (idChromosome) REFERENCES chromosome (id)
);
