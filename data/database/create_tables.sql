CREATE DATABASE IF NOT EXISTS transposons 
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;

USE transposons;

CREATE TABLE IF NOT EXISTS chromosome(
    id INT NOT NULL AUTO_INCREMENT
    , chromosomeNumber INT
    , PRIMARY KEY (id)
);


CREATE TABLE orientation(
    id INT NOT NULL AUTO_INCREMENT
    ,isFivePrima VARCHAR(5)
    ,PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS location (
    id INT NOT NULL AUTO_INCREMENT
    , minStart INT
    , maxEnd INT
    , idOrientation INT
    , idChromosome INT
    , PRIMARY KEY (id)
    , FOREIGN KEY fk_location_orientation (idOrientation) REFERENCES orientation (id)
    , FOREIGN KEY fk_location_chromosome (idChromosome) REFERENCES chromosome (id)

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
    , FOREIGN KEY fk_transposon_location (idLocation) REFERENCES location (id)
    , FOREIGN KEY fk_transposon_family (idFamily) REFERENCES family (id)
);
