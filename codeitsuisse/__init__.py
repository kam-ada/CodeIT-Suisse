from flask import Flask
app = Flask(__name__)
import codeitsuisse.routes.square
import codeitsuisse.routes.arena
import codeitsuisse.routes.asteroids
import codeitsuisse.routes.virus

