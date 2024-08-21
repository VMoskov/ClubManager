CREATE TABLE Coach IF NOT EXISTS (
    coach_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    birth_date DATE,
    years_of_experience INTEGER
);

CREATE TABLE Team IF NOT EXISTS (
    team_id SERIAL PRIMARY KEY,
    team_name VARCHAR(50) UNIQUE NOT NULL,
    home_stadium VARCHAR(100),
    coach_id INTEGER REFERENCES Coach(coach_id)
);

CREATE TABLE Player IF NOT EXISTS (
    player_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    birth_date DATE,
    dominant_foot VARCHAR(20)
);

CREATE TABLE PlayerTeam IF NOT EXISTS (
    player_team_id SERIAL PRIMARY KEY,
    player_position VARCHAR(50),
    player_id INTEGER REFERENCES Player(player_id),
    team_id INTEGER REFERENCES Team(team_id)
);

CREATE INDEX idx_player_id ON player_team(player_id);
CREATE INDEX idx_team_id ON player_team(team_id);

ALTER TABLE player
ADD CONSTRAINT chk_dominant_foot CHECK (dominant_foot IN ('Left', 'Right', 'Both'));

