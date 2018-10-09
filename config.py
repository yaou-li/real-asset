config = {}

MYSQL_USER = config.get('MYSQL_USER', 'root')
MYSQL_PASS = config.get('MYSQL_PASS', 'root')
MYSQL_HOST = config.get('MYSQL_HOST', '127.0.0.1')
MYSQL_PORT = int(config.get('MYSQL_PORT', 3306))
MYSQL_DB = config.get('MYSQL_DB', 'real_asset')

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(MYSQL_USER, MYSQL_PASS, MYSQL_HOST, MYSQL_PORT, MYSQL_DB)
SQLALCHEMY_TRACK_MODIFICATIONS = True