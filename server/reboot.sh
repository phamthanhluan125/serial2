#!/bin/sh
cd ../front
ng build
cd ../server
python app.py
