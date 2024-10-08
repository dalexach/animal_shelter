#!/bin/bash
git subtree split --prefix backend -b deploy
git push heroku deploy:main
git branch -D deploy