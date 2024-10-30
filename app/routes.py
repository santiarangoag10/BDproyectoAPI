from fastapi import APIRouter, HTTPException
from app.models import CourseCreate, Course, StudentCreate, Student
from app.database import get_db_connection
from typing import List

router = APIRouter()

