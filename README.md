# FastAPI Practice Project

This is a small FastAPI project made for learning.
It is written in a simple way so it is easy to follow if you are still new.

## Project Folder

- `Api.py` - main API file where the routes are written.
- `data.json` - sample data used by the API.
- `Testing.py` - small practice file with simple routes.
- `myenv/` - Python virtual environment.

## What This Project Does

The API reads data from `data.json` and sends it back through different routes.

### Routes in `Api.py`

- `GET /id` - returns all data.
- `GET /id/{Id_No}` - returns one record by ID.
- `GET /sort` - returns the data sorted by a field like `age` or `id`.

### Routes in `Testing.py`

- `GET /` - returns `Hello, World!`.
- `GET /items` - returns a simple sample item.

## How To Run

If your virtual environment is already active, run:

```bash
uvicorn Api:app --reload
```

If it does not work, make sure you are inside the project folder first.

## How To Test It

After starting the server, try these links in your browser:

- `http://127.0.0.1:8000/id`
- `http://127.0.0.1:8000/id/1`
- `http://127.0.0.1:8000/sort?sort_by=age&order=asc`
- `http://127.0.0.1:8000/docs`

## Learning Notes

This project shows a few beginner ideas:

- how to read JSON data in Python
- how to create API routes with FastAPI
- how to use path parameters like `Id_No`
- how to use query parameters like `sort_by` and `order`

## Simple Example

If you request `/id/1`, the API looks in `data.json` and returns the person with `id` `1`.

If you request `/sort?sort_by=age`, the API sorts the data by age.

## Note

This project is mainly for practice and learning, so the code is kept simple on purpose.

## Author

Made by Anirudh Patekar.

## Work In Process

This project is still a work in process.
More practice features and improvements can be added later.
