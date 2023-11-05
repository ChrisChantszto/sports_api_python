from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Define the game types as an enumeration
class GameType(str, Enum):
    badminton = "Badminton"
    tennis = "Tennis"
    table_tennis = "Table Tennis"
    football = "Football"
    baseball = "Baseball"
    volleyball = "Volleyball"

# Define the model for a form field
class FormField(BaseModel):
    field_name: str
    field_type: str

# Define the model for the game form
class GameForm(BaseModel):
    game_types: List[GameType]
    other_fields: List[FormField]

@app.get("/game_form", response_model=GameForm)
async def get_game_form():
    game_form = {
        "game_types": [game_type for game_type in GameType],
        "other_fields": [
            {"field_name": "number_of_joiners", "field_type": "integer"},
            {"field_name": "timeslots", "field_type": "list_of_strings"},
        ]
    }
    return game_form