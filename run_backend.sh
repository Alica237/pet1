#!/bin/bash
PYTHONPATH=/home/alica/pet1/backend python3 -m uvicorn main:app --reload --app-dir backend
