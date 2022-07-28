# Google Sheet reader and saver bot
This is BlogSite where i'll put my tutorials for other developers

### Start project without docker
Hello, in the first, you sould clone rep:
* Cloning repository:
```
git clone https://github.com/AktanKasymaliev/google-sheets-tt.git
```
* Download virtual enviroment:
```
pip install python3-venv 
Setting enviroment: python3 -m venv venv
Activating: . venv/bin/activate
```
* Install all requirements: 
```
pip install -r requirements.txt
```

* Create a file settings.ini on self project level, copy under text, and add your value: 
```
[SYSTEM]
NAME=<db>
PASSWORD=<db>
HOST=<db>
PORT=<db>
USER=<db>
TG_TOKEN=<token>
CHAT_ID=<id>
```

* This project working on Postgresql, so install him:
```
sudo apt-get update
sudo apt-get install python3-pip python3-dev libpq-dev postgres postgres-contrib (MacOS) / 
sudo apt-get install postgresql postgresql-contrib (Ubuntu)
sudo -u postgres psql
```
* Enter in your postgresql, and create database:
```
sudo -u postgres psql
CREATE DATABASE <database name> owner <user>;
```

* And finally start project: `python schedule_job.py`

### Start project with Docker:
* Create a file settings.ini on self project level, copy under text, and add your telegram bot token and your chat id value: 
```
[SYSTEM]
NAME=postgres
PASSWORD=postgres
HOST=db
USER=postgres
TG_TOKEN=<token>
CHAT_ID=<id>
```

* And finally start project: `docker-compose up --build`
