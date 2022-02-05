import mysql.connector.pooling

_config={
    "host":"localhost",
    "port":3306,
    "user":"root",
    "password":"123456",
    "database":"vega"
}

try:
    pool=mysql.connector.pooling.MySQLConnectionPool(
        **_config,
        pool_size=10
    )
except Exception as e:
    print(e)