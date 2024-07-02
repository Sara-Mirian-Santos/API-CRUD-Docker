from app import app
from flaskext.mysql import MySQL

mysql = MySQL(app)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '161199Banco@'
app.config['MYSQL_DATABASE_DB'] = 'catalogo_produtos'
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_HOST'] = 'mysql-db'
# app.config['MYSQL_DATABASE_PORT'] = 3307
app.config['MYSQL_DATABASE_PORT'] = 3306
mysql.init_app(app)