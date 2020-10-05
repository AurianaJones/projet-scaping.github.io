from fastapi import FastAPI
import uvicorn
import sqlite3
import requests, json

conn = sqlite3.connect('scrap_game.db')
c = conn.cursor()
app = FastAPI()

@app.get("/games")
async def all_game ():
    c.execute("SELECT title, type, release_date, price, publisher, platform FROM games JOIN games_details ON games_details.game_id = games.id JOIN release_details ON release_details.game_id = games.id;")
    game = c.fetchall()
    conn.commit()
    return game

@app.get("/games/count")
async def count_platform():
    c.execute("SELECT platform, COUNT(platform) FROM release_details GROUP BY platform;")
    count = c.fetchall()
    count = dict(count)
    conn.commit()
    header = {'Access-Control-Allow-Origin':"*"}
    json_count = json.dumps(count)
    return json_count

