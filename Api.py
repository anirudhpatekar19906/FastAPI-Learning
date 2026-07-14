from fastapi import FastAPI, HTTPException, Path, Query
import json
from typing import List, Optional, Dict, Annotated

app = FastAPI()


def load_data():
    with open("data.json", "r") as f:
        data = json.load(f)
    return data


@app.get("/id")
def read_ids():
    data = load_data()
    return data


@app.get("/id/{Id_No}")
def view(Id_No: int = Path(..., description="The ID of the person to retrieve", example=1, ge=1, le=20)):
    data = load_data()
    for i in data:
        if i["id"] == Id_No:
            return i
    raise HTTPException(status_code=404, detail="Person not found")


@app.get("/sort")
def sort_ids(sort_by: str = Query(..., description="Sort by Age or Id"), order : Optional[str] = Query("asc", description="Sort order: asc or desc")):
    data = load_data()
    return sorted(data, key=lambda x: x[sort_by], reverse=(order == "desc"))