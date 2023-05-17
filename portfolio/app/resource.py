from flask import render_template
from dotenv import load_dotenv
from os import getenv

load_dotenv()

def presentation_card():
    return render_template("card.html")

def portfolio_web():
    GH_KEY = getenv("GH_API_KEY")
    return render_template("portfolio.html", GH_KEY=GH_KEY)