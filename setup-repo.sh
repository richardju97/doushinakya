#!/bin/sh

#  setup-repo.sh
#  script for setting up a web dev repo (or subdirectory if multiple things are inside the repo).
#
#  Created by Richard Ju on 1/20/18.
#  Last modified on 1/20/18.
#  Assumptions:
#   Deployment - Heroku
#   Technology/Framework: NodeJS
#   Primary backend code: server.js

# Procfile (needed for deploying on heroku)
echo "web: node server.js" > Procfile

# Create directories
mkdir Angular css
mkdir Angular/template Angular/lib

# Create basic files file
touch server.js Angular/index.html Angular/script.js

git add .
git commit -m "Setup"
git push origin master
