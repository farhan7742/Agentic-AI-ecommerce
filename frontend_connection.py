# Farhan Sadik

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from connection import db  # connect to our  connection.py file

app = FastAPI(title="Basic E-Commerce Backend")

# Enable CORS for Next.js
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)





@app.get("/")
def home():
    return {"status": "Online", "message": "Backend server is running."}


@app.get("/test-db")
def test_database_connection():
    try:
        response = db.table("products").select("*").limit(1).execute()
        return {
            "status": "Success",
            "message": "Connected to Supabase!",
            "data": response.data,
        }
    except Exception as e:
        return {
            "status": "Error", "message": str(e)
    } 