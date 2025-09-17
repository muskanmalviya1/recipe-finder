from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY ="bbf2786cd85149fd955099af14ee9cc1"

@app.get("/recipes")
def get_recipes(ingredient: str = Query(..., description=" search recipes")):

    url = f"https://api.spoonacular.com/recipes/complexSearch?query={ingredient}&number=6&addRecipeInformation=true&apiKey={API_KEY}"

    response = requests.get(url).json()
    recipes = []

    for item in response.get("results", []):
        recipes.append({
            "title": item.get("title"),
            "image": item.get("image"),
            "instructions": item.get("instructions") or "No instructions available",
            "sourceUrl": item.get("sourceUrl")
        })
    return {"recipes": recipes}
