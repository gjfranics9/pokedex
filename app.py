# app.py
from flask import Flask, render_template, request, redirect, url_for
from utils import load_types
from repo import fetch_pokemon_list, fetch_stats, fetch_strongest
from databaseManager import *

app = Flask(__name__)


@app.route('/')
def index():
    search = request.args.get("search", "")
    type_filter = request.args.get("type1", "all")

    with get_db() as conn:
        pokemon_list = fetch_pokemon_list(conn, search, type_filter)
        stats        = fetch_stats(conn, search, type_filter)
        strongest    = fetch_strongest(conn, search, type_filter)

    types = load_types()
    return render_template(
        "index.html",
        pokemon_list=pokemon_list,
        stats=stats,
        strongest=strongest,
        types=types,
        current_search=search,
        current_type=type_filter,
    )

@app.route('/pokemon/<int:id>')
def pokemon_detail(id):
    conn = get_db()
    c = conn.cursor()
    c.execute('SELECT * FROM pokemon WHERE id = ?', (id,))
    pokemon = c.fetchone()
    conn.close()
    
    if pokemon is None:
        return redirect(url_for('index'))
    
    return render_template('detail.html', pokemon=pokemon)

@app.route('/stats')
def stats():
    conn = get_db()
    c = conn.cursor()
    
    
    return render_template('stats.html',)

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5050)