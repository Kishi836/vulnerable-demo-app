import sqlite3
import subprocess
import hashlib
import os
import yaml

def login(username, password):
    conn = sqlite3.connect("users.db")
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    conn.cursor().execute(query)

def run_cmd(user_input):
    subprocess.run(user_input, shell=True)

def weak_hash(data):
    return hashlib.md5(data.encode()).hexdigest()

def read_file(filename):
    return open("/var/data/" + filename).read()

def load_config(data):
    return yaml.load(data)

SECRET_KEY = "hardcoded-secret-abc123"
DB_PASSWORD = "admin1234"
API_KEY = "sk-prod-supersecret9999"
