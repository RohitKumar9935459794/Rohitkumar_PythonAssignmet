-- schema.sql
CREATE TABLE IF NOT EXISTS apps (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    app_name TEXT NOT NULL,
    version TEXT NOT NULL,
    description TEXT NOT NULL
);

-- Insert sample data
INSERT INTO apps (app_name, version, description)
VALUES
    ('MyApp', '1.0', 'A simple app to demonstrate database integration'),
    ('WeatherApp', '2.1', 'An app that provides real-time weather updates'),
    ('NewsApp', '1.5', 'An app that displays news headlines');
