from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
DB_NAME = "sistema_custos"

client = AsyncIOMotorClient(MONGO_URI)
database = client[DB_NAME]
collection = database["custos"]
