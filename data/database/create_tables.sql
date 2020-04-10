DROP DATABASE IF EXISTS atTransposons;

CREATE DATABASE atTransposons 
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;

DROP TABLE IF EXISTS position;
CREATE TABLE position(
    id PRIMARY KEY AUTO_INCREMENT NOT NULL
    , minStart INT 
    , maxEnd INT 
);

DROP TABLE IF EXISTS orientation;
CREATE TABLE orientation(
    id PRIMARY KEY AUTO_INCREMENT NOT NULL
    , isFivePrima TINYINT(1)
); 

DROP TABLE IF EXISTS chromosome;
CREATE TABLE chromosome(
    id PRIMARY KEY AUTO_INCREMENT NOT NULL
    , chromosomNumber INT
);

DROP TABLE IF EXISTS superFamily;
CREATE TABLE superFamily(
    id PRIMARY KEY AUTO_INCREMENT NOT NULL
    , superFamilyName VARCHAR(25)
);
 
DROP TABLE IF EXISTS family;
CREATE TABLE family(
    id PRIMARY KEY AUTO_INCREMENT NOT NULL
    , familyName VARCHAR(25)
    , idSuperFamily INT
    FOREIGN KEY fk_family_superfamily (idSuperFamily) REFERENCES superFamily (id)
); 

DROP TABLE IF EXISTS transposon;
CREATE TABLE transposon(
    id PRIMARY KEY AUTO_INCREMENT NOT NULL
    , transposonName VARCHAR(10)
    , idOrientation INT 
    , idPosition INT 
    , idFamily INT 
    , idChromosome INT
    FOREIGN KEY fk_transposon_orientation (idOrientation) REFERENCES orientation (id)
    FOREIGN KEY fk_transposon_position (idPosition) REFERENCES position (id)
    FOREIGN KEY fk_transposon_family (idFamily) REFERENCES family (id)
    FOREIGN KEY fk_transposon_chromosome (idChromosome) REFERENCES chromosome (id)
);