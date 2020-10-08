from fastapi import FastAPI
import sqlite3
import uvicorn
from sqlite3 import connect
from bs4 import BeautifulSoup
import urllib.request
import json
import sys
import pandas as pd
import os
from fastapi.responses import JSONResponse
from scraper import scraper

app = FastAPI()

password = """
d{|Dvz<43pN]{aH4)3)S.3+RBcaUY2,m.C-z22ZX+KV(,Ez8E@nTQv3:z3443^62|pr6%HtrC3m)9]!rxV#6R[?dm69FUyJ86C8a6fuf9n]q<jgK]92$VG9cZz<466dQ8mHa6v-MwC+wbKnn#X66i75YbKR#cHPt}[p)96)b7>+76>JYS5Ti(663KWU}/2nU}}2Z:=U
"""

@app.get("/start-scraper/{password}")
async def start_scraper():
    headers = {"Access-Control-Allow-Origin":""}
    scraper()
    return JSONResponse(content={'Etat':'Scraping terminé'}, headers=headers)

@app.get("/games")
async def all_game ():
    conn = sqlite3.connect('scrap_game.db')
    c = conn.cursor()
    c.execute("SELECT title, type, release_date,platform,price, publisher FROM games JOIN release_details ON games.id = release_details.game_id JOIN games_details ON games.id = games_details.game_id;")
    game = c.fetchall()
    conn.commit()
    conn.close()
    return game

@app.get("/games/count")
async def count_platform():
    conn = sqlite3.connect('scrap_game.db')
    c = conn.cursor()
    df = pd.read_sql_query("SELECT platform, COUNT(platform) FROM release_details GROUP BY platform;", conn)
    df = df.rename(columns={'COUNT(platform)': 'pourcent', "platform" : "name"})
    d = df.to_dict('records')
    headers = {"Access-Control-Allow-Origin":"*"}
    conn.commit()
    conn.close()
    return JSONResponse(content=d, headers=headers)

@app.get("/games/type")
async def diferents_types():
    conn = sqlite3.connect('scrap_game.db')
    c = conn.cursor()
    df = pd.read_sql_query("SELECT type, COUNT(type) FROM games GROUP BY type;", conn)
    df = df.rename(columns={'COUNT(type)': 'nombres', "type" : "genre"})
    d = df.to_dict('records')
    headers = {"Access-Control-Allow-Origin":"*"}
    conn.commit()
    conn.close()
    return JSONResponse(content=d, headers=headers)

@app.get("/games/count/publisher")
async def get_count_publisher():
  conn = sqlite3.connect('scrap_game.db')
  c = conn.cursor()
  df = pd.read_sql_query("SELECT publisher, COUNT(publisher) FROM games_details GROUP BY publisher;", conn)
  df = df.rename(columns={'COUNT(publisher)': 'nombre', "publisher" : "name"})
  d = df.to_dict('records')
  headers = {"Access-Control-Allow-Origin":"*"}
  conn.commit()
  conn.close()
  return JSONResponse(content=d, headers=headers)