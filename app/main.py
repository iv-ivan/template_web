from typing import Optional
from fastapi import FastAPI, APIRouter, Query, Body, status, HTTPException, Response, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
import sqlite3

app = FastAPI()

class Item(BaseModel):
    name: str = Field(..., description='help')
    description: Optional[str] = None

router = APIRouter(
    prefix=""
)

@app.on_event("startup")
def startup_event():
    app.state.test_phrase = "123 test"
    app.state.database = sqlite3.connect("/Users/iv-ivan/Desktop/other/bookcrossing2/app/mydatabase.db")
    # can use config here

@router.post('/items/{item_id}', response_model=Item)
async def root(*, response: Response, item_id: int, full_item: Item = Body(..., embed=True), item_name: Optional[int] = Query(None, lt=5, alias='item-name'), importance: int = Body(0), request: Request):
    print(request.app.state.test_phrase)
    cursor = request.app.state.database.cursor()
    cursor.execute("""SELECT * FROM books""")
    print(cursor.fetchall())
    # return {'item_id': item_id, 'item_name': item_name, 'importance': importance, 'full_item': full_item}
    # raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    response.set_cookie(key="fakesession", value="fake-cookie-session-value")
    response.headers["X-Cat-Dog"] = "alone in the world"
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=full_item.dict())

app.include_router(router)

# uvicorn app.main:app --reload