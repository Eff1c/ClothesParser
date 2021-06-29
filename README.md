# ClothesParser
This parser is created for check all discounts in the most famous clothing stores USA (current only adidas).
## Installation
1. Create venv `python3 -m venv env`
2. His activate `source env/bin/activate` 
3. Install requirements `pip install -r requirements.txt`
4. Create database "clothing" and config it in website/website/settings.py
5. Migrate models to database `python manage.py migrate`
6. Open crontab `crontab –e` and write it:
```
LANG="en_US.utf8"

00 00 * * * cd /home/eff1c/ClothesParser/parser/spiders && /home/eff1c/ClothesParser/env/local/bin/scrapy crawl adidas_spider
```
## Requirements
* python 3.8
* Django 3.2
* Scrapy 2.5
* Postgres
