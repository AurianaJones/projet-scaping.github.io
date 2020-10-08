from fastapi import FastAPI
import pandas as pd
import uvicorn
import sqlite3
import requests, json
from fastapi.responses import JSONResponse


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
    df = pd.read_sql_query("SELECT platform, COUNT(platform) FROM release_details GROUP BY platform;", conn)
    df = df.rename(columns={'COUNT(platform)': 'pourcent', "platform" : "name"})
    d = df.to_dict('records')
    headers = {"Access-Control-Allow-Origin":"*"}
    conn.commit()
    return JSONResponse(content=d, headers=headers) 
    
@app.get("/games/type")
async def diferents_types():
    df = pd.read_sql_query("SELECT type, COUNT(type) FROM games GROUP BY type;", conn)
    df = df.rename(columns={'COUNT(type)': 'nombres', "type" : "genre"})
    d = df.to_dict('records')
    headers = {"Access-Control-Allow-Origin":"*"}
    conn.commit()
    return JSONResponse(content=d, headers=headers) 