CREATE DATABASE IF NOT EXISTS transposons 
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;

USE transposons;

CREATE TABLE IF NOT EXISTS chromosome(
    id INT NOT NULL AUTO_INCREMENT
    , chromosomeNumber INT NOT NULL UNIQUE
    , PRIMARY KEY (id)
);


CREATE TABLE orientation(
    id INT NOT NULL AUTO_INCREMENT
    ,isFivePrime VARCHAR(5) NOT NULL UNIQUE
    ,PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS location (
    id INT NOT NULL AUTO_INCREMENT
    , minStart INT 
    , maxEnd INT
    , idOrientation INT NOT NULL
    , idChromosome INT NOT NULL
    , PRIMARY KEY (id)
    , FOREIGN KEY fk_location_orientation (idOrientation) REFERENCES orientation (id)
    , FOREIGN KEY fk_location_chromosome (idChromosome) REFERENCES chromosome (id)

);


CREATE TABLE IF NOT EXISTS superFamily(
    id INT NOT NULL AUTO_INCREMENT
    , superFamilyName VARCHAR(25) NOT NULL UNIQUE
    , PRIMARY KEY (id)
);
 
CREATE TABLE IF NOT EXISTS family(
    id INT NOT NULL AUTO_INCREMENT
    , familyName VARCHAR(25) NOT NULL UNIQUE
    , idSuperFamily INT NOT NULL
    , PRIMARY KEY (id)
    , FOREIGN KEY fk_family_superfamily (idSuperFamily) REFERENCES superFamily (id)
); 

CREATE TABLE IF NOT EXISTS transposon(
    id INT NOT NULL AUTO_INCREMENT
    , transposonName VARCHAR(10) NOT NULL UNIQUE
    , idLocation INT NOT NULL
    , idFamily INT NOT NULL
    , PRIMARY KEY (id)
    , FOREIGN KEY fk_transposon_location (idLocation) REFERENCES location (id)
    , FOREIGN KEY fk_transposon_family (idFamily) REFERENCES family (id)
);
