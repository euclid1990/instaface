# Instaface

This project was developed with [Flask](http://flask.pocoo.org) version 0.12.2.
Architecture: Using blueprints with functional structure

## Install Python projects dependencies

```
pip3 install -r requirements.txt
```

## Install new packages and save it in requirements.txt

```
pip3 install [package_name] && pip3 freeze > requirements.txt
```

## Database migration commands

```
python3 -m manage db init
python3 -m manage db migrate
python3 -m manage db upgrade
```

## Start web server

```
python3 run.py
```

## Debug

```
import pdb; pdb.set_trace();
```
