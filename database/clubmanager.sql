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
    team_id INTEGER REFERENCES Team(team_id)
    position_id INTEGER REFERENCES Position(position_id)
);

CREATE INDEX idx_player_id ON PlayerTeam(player_id);
CREATE INDEX idx_team_id ON PlayerTeam(team_id);

ALTER TABLE player
ADD CONSTRAINT chk_dominant_foot CHECK (dominant_foot IN ('Left', 'Right', 'Both'));

