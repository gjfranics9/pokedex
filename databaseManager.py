import sqlite3
import os

def init_db():
    conn = sqlite3.connect('databases/pokedex.db')
    c = conn.cursor()
    
    # Create pokemon table
    c.execute('''CREATE TABLE IF NOT EXISTS pokemon (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        type1 TEXT NOT NULL,
        type2 TEXT,
        hp INTEGER,
        attack INTEGER,
        defense INTEGER,
        sp_attack INTEGER,
        sp_defense INTEGER,
        speed INTEGER,
        height REAL,
        weight REAL,
        color TEXT,
        description TEXT
    )''')
    
    # Sample data
    sample_pokemon = [
        (1, 'Bulbasaur', 'Grass', 'Poison', 45, 49, 49, 65, 65, 45, 0.7, 6.9, '#78C850', 'A strange seed was planted on its back at birth. The plant sprouts and grows with this Pokémon.'),
        (4, 'Charmander', 'Fire', None, 39, 52, 43, 60, 50, 65, 0.6, 8.5, '#F08030', 'Obviously prefers hot places. When it rains, steam is said to spout from the tip of its tail.'),
        (7, 'Squirtle', 'Water', None, 44, 48, 65, 50, 64, 43, 0.5, 9.0, '#6890F0', 'After birth, its back swells and hardens into a shell. Powerfully sprays foam from its mouth.'),
        (25, 'Pikachu', 'Electric', None, 35, 55, 40, 50, 50, 90, 0.4, 6.0, '#F8D030', 'When several of these Pokémon gather, their electricity could build and cause lightning storms.'),
        (94, 'Gengar', 'Ghost', 'Poison', 60, 65, 60, 130, 75, 110, 1.5, 40.5, '#705898', 'Under a full moon, this Pokémon likes to mimic the shadows of people and laugh at their fright.'),
        (143, 'Snorlax', 'Normal', None, 160, 110, 65, 65, 110, 30, 2.1, 460.0, '#A8A878', 'Very lazy. Just eats and sleeps. As its rotund bulk builds, it becomes steadily more slothful.'),
        (149, 'Dragonite', 'Dragon', 'Flying', 91, 134, 95, 100, 100, 80, 2.2, 210.0, '#7038F8', 'An extremely rarely seen marine Pokémon. Its intelligence is said to match that of humans.'),
        (150, 'Mewtwo', 'Psychic', None, 106, 110, 90, 154, 90, 130, 2.0, 122.0, '#F85888', 'It was created by a scientist after years of horrific gene splicing and DNA engineering experiments.'),
    ]
    
    c.execute('SELECT COUNT(*) FROM pokemon')
    if c.fetchone()[0] == 0:
        c.executemany('INSERT INTO pokemon VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)', sample_pokemon)
        conn.commit()
    
    conn.close()

def get_db():
    conn = sqlite3.connect('databases/pokedex.db')
    conn.row_factory = sqlite3.Row
    return conn