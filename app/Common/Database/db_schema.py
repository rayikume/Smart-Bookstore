from pydantic import BaseModel

class user(BaseModel):
    def userSchema():
        return {
            "username": "string",
            "email": "string",
            "password": "string",
            "role" : "String",
            "description":"String",
            "preferences": "String"

        }


class book(BaseModel):
    def bookSchema():
        return {
            "book_id": "string",
            "title": "string",
            "author_id": "integer",
            "genre": "string",
            "description": "string",
            "author": "string"
        }


class author(BaseModel):
    def authorSchema():
        return {
            "author_name": "string",
            "biography": "string",
            "genre": "integer",
            "description": "string",
            "books": "string"
        }


class userPreference(BaseModel):
    def userPreferenceSchema():
        return {
            "preferences": "string",
            "username": "string",
            "author_id": "integer",
            "genre": "integer",
            "description": "string"
        }