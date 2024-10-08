#!/bin/bash
echo "Running release tasks..."
python backend/manage.py migrate
echo "Migrations completed."