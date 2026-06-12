# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API using the FastAPI framework and practice defining routes, request bodies, and simple response models.

## 📝 Tasks

### 🛠️ Create the API App

#### Description
Set up a basic FastAPI application with a health check endpoint and an items collection.

#### Requirements
Completed program should:

- Import `FastAPI` and create an app instance
- Add a `GET /health` endpoint that returns `{ "status": "ok" }`
- Add a `GET /items` endpoint that returns a list of sample items

### 🛠️ Add Item Creation

#### Description
Allow clients to create a new item through a `POST /items` endpoint.

#### Requirements
Completed program should:

- Define a Pydantic model for an item with `name`, `price`, and `in_stock`
- Accept JSON input from the client
- Return the created item with a generated `id`

### 🛠️ Stretch Goal: Item Details

#### Description
Add a route to retrieve one item by its ID.

#### Requirements
Completed program should:

- Add `GET /items/{item_id}`
- Return the matching item when the ID exists
- Return a helpful error message when the item is not found
