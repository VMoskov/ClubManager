CREATE TABLE IF NOTE EXISTS ROLE (
    role_id SERIAL PRIMARY KEY,
    role_name VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS User (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    pass VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    birth_date DATE
)

CREATE TABLE IF NOT EXISTS Coach (
    coach_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    birth_date DATE,
    years_of_experience INTEGER
);

CREATE TABLE IF NOT EXISTS  Team (
    team_id SERIAL PRIMARY KEY,
    team_name VARCHAR(50) UNIQUE NOT NULL,
    home_stadium VARCHAR(100),
    coach_id INTEGER REFERENCES Coach(coach_id)
);

CREATE TABLE IF NOT EXISTS Player (
    player_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    birth_date DATE,
    dominant_foot VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS Position (
    position_id SERIAL PRIMARY KEY,
    position_name VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS PlayerTeam (
    player_team_id SERIAL PRIMARY KEY,
    kit_number INTEGER,
    player_id INTEGER REFERENCES Player(player_id),
    team_id INTEGER REFERENCES Team(team_id),
    position_id INTEGER REFERENCES Position(position_id)
);

CREATE INDEX idx_player_id ON PlayerTeam(player_id);
CREATE INDEX idx_team_id ON PlayerTeam(team_id);

ALTER TABLE player
ADD CONSTRAINT chk_dominant_foot CHECK (dominant_foot IN ('Left', 'Right', 'Both'));

-- Roles
INSERT INTO Role (role_name) VALUES ('ADMIN');
INSERT INTO Role (role_name) VALUES ('USER');

-- Users
INSERT INTO User (username, pass, email, first_name, last_name, birth_date) 
VALUES ('admin', 'admin', 'admin@admin.com', 'Admin', 'Admin', '2003-26-02');

INSERT INTO User (username, pass, email, first_name, last_name, birth_date)
VALUES ('user', 'user', 'user@user.com', 'User', 'User', '2003-26-02');

-- Positions
INSERT INTO Position (position_name) VALUES ('GK');
INSERT INTO Position (position_name) VALUES ('CB');
INSERT INTO Position (position_name) VALUES ('RB');
INSERT INTO Position (position_name) VALUES ('LB');
INSERT INTO Position (position_name) VALUES ('CDM');
INSERT INTO Position (position_name) VALUES ('CM');
INSERT INTO Position (position_name) VALUES ('CAM');
INSERT INTO Position (position_name) VALUES ('RM');
INSERT INTO Position (position_name) VALUES ('LM');
INSERT INTO Position (position_name) VALUES ('RW');
INSERT INTO Position (position_name) VALUES ('LW');
INSERT INTO Position (position_name) VALUES ('ST');
INSERT INTO Position (position_name) VALUES ('CF');

-- Coaches
INSERT INTO Coach (first_name, last_name, birth_date, years_of_experience)
VALUES ('Carlo', 'Ancelotti', '1959-10-10', 30);

INSERT INTO Coach (first_name, last_name, birth_date, years_of_experience)
VALUES ('Zinedine', 'Zidane', '1972-06-23', 10);

INSERT INTO Coach (first_name, last_name, birth_date, years_of_experience)
VALUES ('Pep', 'Guardiola', '1971-01-18', 20);

INSERT INTO Coach (first_name, last_name, birth_date, years_of_experience)
VALUES ('Vincent', 'Kompany', '1986-04-10', 5);

INSERT INTO Coach (first_name, last_name, birth_date, years_of_experience)
VALUES ('Jurgen', 'Klopp', '1967-06-16', 25);

-- Teams
INSERT INTO Team (team_name, home_stadium, coach_id)
VALUES ('Real Madrid', 'Santiago Bernabeu', 1);

INSERT INTO Team (team_name, home_stadium, coach_id)
VALUES ('Manchester City', 'Etihad Stadium', 3);

INSERT INTO Team (team_name, home_stadium, coach_id)
VALUES ('Bayern Munich', 'Allianz Arena', 4);

INSERT INTO Team (team_name, home_stadium, coach_id)
VALUES ('Liverpool', 'Anfield', 5);

-- Players --

/* Real Madrid */
INSERT INTO Player (first_name, last_name, birth_date, dominant_foot)
VALUES ('Thibaut', 'Courtois', '1992-05-11', 'Right');
INSERT INTO PlayerTeam (kit_number, player_id, team_id, position_id)
VALUES (1, 1, 1, 1);

INSERT INTO Player (first_name, last_name, birth_date, dominant_foot)
VALUES ('Ferland', 'Mendy', '1995-06-08', 'Left');
INSERT INTO PlayerTeam (kit_number, player_id, team_id, position_id)
VALUES (23, 2, 1, 4);

INSERT INTO Player (first_name, last_name, birth_date, dominant_foot)
VALUES ('Antonio', 'Rudiger', '1993-03-03', 'Right');
INSERT INTO PlayerTeam (kit_number, player_id, team_id, position_id)
VALUES (4, 3, 1, 2);

INSERT INTO Player (first_name, last_name, birth_date, dominant_foot)
VALUES ('Eder', 'Militao', '1998-01-18', 'Right');
INSERT INTO PlayerTeam (kit_number, player_id, team_id, position_id)
VALUES (3, 4, 1, 2);

INSERT INTO Player (first_name, last_name, birth_date, dominant_foot)
VALUES ('Dani', 'Carvajal', '1992-01-11', 'Right');
INSERT INTO PlayerTeam (kit_number, player_id, team_id, position_id)
VALUES (2, 5, 1, 3);

INSERT INTO Player (first_name, last_name, birth_date, dominant_foot)
VALUES ('Luka', 'Modrić', '1985-09-09', 'Right');
INSERT INTO PlayerTeam (kit_number, player_id, team_id, position_id)
VALUES (10, 6, 1, 6);

INSERT INTO Player (first_name, last_name, birth_date, dominant_foot)
VALUES ('Toni', 'Kroos', '1990-01-04', 'Right');
INSERT INTO PlayerTeam (kit_number, player_id, team_id, position_id)
VALUES (8, 7, 1, 6);

INSERT INTO Player (first_name, last_name, birth_date, dominant_foot)
VALUES ('Federico', 'Valverde', '1998-07-22', 'Right');
INSERT INTO PlayerTeam (kit_number, player_id, team_id, position_id)
VALUES (15, 8, 1, 6);

INSERT INTO Player (first_name, last_name, birth_date, dominant_foot)
VALUES ('Vinicius', 'Junior', '2000-07-12', 'Right');
INSERT INTO PlayerTeam (kit_number, player_id, team_id, position_id)
VALUES (20, 9, 1, 11);

INSERT INTO Player (first_name, last_name, birth_date, dominant_foot)
VALUES ('Jude', 'Bellingham', '2003-06-29', 'Right');
INSERT INTO PlayerTeam (kit_number, player_id, team_id, position_id)
VALUES (22, 10, 1, 7);

INSERT INTO Player (first_name, last_name, birth_date, dominant_foot)
VALUES ('Kylian', 'Mbappé', '1998-12-20', 'Right');
INSERT INTO PlayerTeam (kit_number, player_id, team_id, position_id)
VALUES (7, 11, 1, 11);

/* Manchester City */
INSERT INTO Player (first_name, last_name, birth_date, dominant_foot)
VALUES ('Ederson', 'Moraes', '1993-08-17', 'Right');
INSERT INTO PlayerTeam (kit_number, player_id, team_id, position_id)
VALUES (31, 12, 2, 1);

INSERT INTO Player (first_name, last_name, birth_date, dominant_foot)
VALUES ('Joško', 'Gvardiol', '2002-01-23', 'Left');
INSERT INTO PlayerTeam (kit_number, player_id, team_id, position_id)
VALUES (6, 13, 2, 2);

INSERT INTO Player (first_name, last_name, birth_date, dominant_foot)
VALUES ('Ruben', 'Dias', '1997-05-14', 'Right');
INSERT INTO PlayerTeam (kit_number, player_id, team_id, position_id)
VALUES (3, 14, 2, 2);

INSERT INTO Player (first_name, last_name, birth_date, dominant_foot)
VALUES ('Aymeric', 'Laporte', '1994-05-27', 'Left');
INSERT INTO PlayerTeam (kit_number, player_id, team_id, position_id)
VALUES (14, 15, 2, 2);

INSERT INTO Player (first_name, last_name, birth_date, dominant_foot)
VALUES ('Kyle', 'Walker', '1990-05-28', 'Right');
INSERT INTO PlayerTeam (kit_number, player_id, team_id, position_id)
VALUES (2, 16, 2, 3);

INSERT INTO Player (first_name, last_name, birth_date, dominant_foot)
VALUES ('Rodri', 'Hernandez', '1996-06-22', 'Right');
INSERT INTO PlayerTeam (kit_number, player_id, team_id, position_id)
VALUES (16, 17, 2, 5);

INSERT INTO Player (first_name, last_name, birth_date, dominant_foot)
VALUES ('Kevin', 'De Bruyne', '1991-06-28', 'Right');
INSERT INTO PlayerTeam (kit_number, player_id, team_id, position_id)
VALUES (17, 18, 2, 7);

INSERT INTO Player (first_name, last_name, birth_date, dominant_foot)
VALUES ('Phil', 'Foden', '2000-05-28', 'Right');
INSERT INTO PlayerTeam (kit_number, player_id, team_id, position_id)
VALUES (47, 19, 2, 7);

INSERT INTO Player (first_name, last_name, birth_date, dominant_foot)
VALUES ('Mateo', 'Kovačić', '1994-05-06', 'Right');
INSERT INTO PlayerTeam (kit_number, player_id, team_id, position_id)
VALUES (8, 20, 2, 6);

INSERT INTO Player (first_name, last_name, birth_date, dominant_foot)
VALUES ('David', 'Silva', '1986-01-08', 'Left');
INSERT INTO PlayerTeam (kit_number, player_id, team_id, position_id)
VALUES (21, 21, 2, 7);

INSERT INTO Player (first_name, last_name, birth_date, dominant_foot)
VALUES ('Jack', 'Grealish', '1995-09-10', 'Right');
INSERT INTO PlayerTeam (kit_number, player_id, team_id, position_id)
VALUES (10, 22, 2, 11);

INSERT INTO Player (first_name, last_name, birth_date, dominant_foot)
VALUES ('Erling', 'Haaland', '2000-07-21', 'Right');
INSERT INTO PlayerTeam (kit_number, player_id, team_id, position_id)
VALUES (9, 23, 2, 13);

/* Bayern Munich */
INSERT INTO Player (first_name, last_name, birth_date, dominant_foot)
VALUES ('Manuel', 'Neuer', '1986-03-27', 'Right');
INSERT INTO PlayerTeam (kit_number, player_id, team_id, position_id)
VALUES (1, 24, 3, 1);

INSERT INTO Player (first_name, last_name, birth_date, dominant_foot)
VALUES ('Hiroki', 'Ito', '2003-06-29', 'Right');
INSERT INTO PlayerTeam (kit_number, player_id, team_id, position_id)
VALUES (2, 25, 3, 3);

INSERT INTO Player (first_name, last_name, birth_date, dominant_foot)
VALUES ('Matthijs', 'de Ligt', '1999-08-12', 'Right');
INSERT INTO PlayerTeam (kit_number, player_id, team_id, position_id)
VALUES (4, 26, 3, 2);

INSERT INTO Player (first_name, last_name, birth_date, dominant_foot)
VALUES ('Eric', 'Dier', '1994-01-15', 'Right');
INSERT INTO PlayerTeam (kit_number, player_id, team_id, position_id)
VALUES (5, 27, 3, 2);

INSERT INTO Player (first_name, last_name, birth_date, dominant_foot)
VALUES ('Joshua', 'Kimmich', '1995-02-08', 'Right');
INSERT INTO PlayerTeam (kit_number, player_id, team_id, position_id)
VALUES (6, 28, 3, 5);

INSERT INTO Player (first_name, last_name, birth_date, dominant_foot)
VALUES ('Leon', 'Goretzka', '1995-02-06', 'Right');
INSERT INTO PlayerTeam (kit_number, player_id, team_id, position_id)
VALUES (7, 29, 3, 6);

INSERT INTO Player (first_name, last_name, birth_date, dominant_foot)
VALUES ('João', 'Palhinha', '1995-07-09', 'Right');
INSERT INTO PlayerTeam (kit_number, player_id, team_id, position_id)
VALUES (8, 30, 3, 6);

INSERT INTO Player (first_name, last_name, birth_date, dominant_foot)
VALUES ('Xavi', 'Simons', '2003-04-21', 'Right');
INSERT INTO PlayerTeam (kit_number, player_id, team_id, position_id)
VALUES (9, 31, 3, 6);

INSERT INTO Player (first_name, last_name, birth_date, dominant_foot)
VALUES ('Jamal', 'Musiala', '2003-02-26', 'Right');
INSERT INTO PlayerTeam (kit_number, player_id, team_id, position_id)
VALUES (10, 32, 3, 7);

INSERT INTO Player (first_name, last_name, birth_date, dominant_foot)
VALUES ('Michael', 'Olise', '2001-12-12', 'Right');
INSERT INTO PlayerTeam (kit_number, player_id, team_id, position_id)
VALUES (11, 33, 3, 7);

INSERT INTO Player (first_name, last_name, birth_date, dominant_foot)
VALUES ('Harry', 'Kane', '1993-07-28', 'Right');
INSERT INTO PlayerTeam (kit_number, player_id, team_id, position_id)
VALUES (12, 34, 3, 13);

/* Liverpool */
INSERT INTO Player (first_name, last_name, birth_date, dominant_foot)
VALUES ('Alisson', 'Becker', '1992-10-02', 'Right');
INSERT INTO PlayerTeam (kit_number, player_id, team_id, position_id)
VALUES (1, 35, 4, 1);

INSERT INTO Player (first_name, last_name, birth_date, dominant_foot)
VALUES ('Trent', 'Alexander-Arnold', '1998-10-07', 'Right');
INSERT INTO PlayerTeam (kit_number, player_id, team_id, position_id)
VALUES (2, 36, 4, 3);

INSERT INTO Player (first_name, last_name, birth_date, dominant_foot)
VALUES ('Virgil', 'van Dijk', '1991-07-08', 'Right');
INSERT INTO PlayerTeam (kit_number, player_id, team_id, position_id)
VALUES (4, 37, 4, 2);

INSERT INTO Player (first_name, last_name, birth_date, dominant_foot)
VALUES ('Joe', 'Gomez', '1997-05-23', 'Right');
INSERT INTO PlayerTeam (kit_number, player_id, team_id, position_id)
VALUES (5, 38, 4, 2);

INSERT INTO Player (first_name, last_name, birth_date, dominant_foot)
VALUES ('Andrew', 'Robertson', '1994-03-11', 'Left');
INSERT INTO PlayerTeam (kit_number, player_id, team_id, position_id)
VALUES (3, 39, 4, 4);

INSERT INTO Player (first_name, last_name, birth_date, dominant_foot)
VALUES ('James', 'Milner', '1986-01-04', 'Right');
INSERT INTO PlayerTeam (kit_number, player_id, team_id, position_id)
VALUES (6, 40, 4, 6);

INSERT INTO Player (first_name, last_name, birth_date, dominant_foot)
VALUES ('Jordan', 'Henderson', '1990-06-17', 'Right');
INSERT INTO PlayerTeam (kit_number, player_id, team_id, position_id)
VALUES (7, 41, 4, 6);

INSERT INTO Player (first_name, last_name, birth_date, dominant_foot)
VALUES ('Georginio', 'Wijnaldum', '1990-11-11', 'Right');
INSERT INTO PlayerTeam (kit_number, player_id, team_id, position_id)
VALUES (8, 42, 4, 6);

INSERT INTO Player (first_name, last_name, birth_date, dominant_foot)
VALUES ('Sadio', 'Mane', '1992-04-10', 'Right');
INSERT INTO PlayerTeam (kit_number, player_id, team_id, position_id)
VALUES (10, 43, 4, 11);

INSERT INTO Player (first_name, last_name, birth_date, dominant_foot)
VALUES ('Mohamed', 'Salah', '1992-06-15', 'Left');
INSERT INTO PlayerTeam (kit_number, player_id, team_id, position_id)
VALUES (11, 44, 4, 11);

INSERT INTO Player (first_name, last_name, birth_date, dominant_foot)
VALUES ('Roberto', 'Firmino', '1991-10-02', 'Right');
INSERT INTO PlayerTeam (kit_number, player_id, team_id, position_id)
VALUES (9, 45, 4, 13);