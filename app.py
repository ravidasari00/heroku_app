from flask import Flask, render_template
from sqlalchemy import create_engine, text

app = Flask(__name__)

# Snowflake connection parameters
snowflake_account = 'kg28325.ap-southeast-1.snowflakecomputing.com'
snowflake_user = 'dasariravi'
snowflake_password = 'Ravi0011'
snowflake_warehouse = 'my_wh'

# SQLAlchemy connection string
connection_string = (
    f'snowflake://{snowflake_user}:{snowflake_password}@{snowflake_account}/'
    f'?warehouse={snowflake_warehouse}&account={snowflake_account}'
)

# Create an SQLAlchemy engine
engine = create_engine(connection_string)

@app.route('/')
def index():
    # Connect to Snowflake using SQLAlchemy
    connection = engine.connect()

    try:
        # Execute a query using SQLAlchemy
        query = text("SELECT * FROM my_db.public.employee")
        result = connection.execute(query).fetchall()

        return render_template('index.html', data=result)

    finally:
        # Close the connection
        connection.close()

# if __name__ == '__main__':
#     app.run(debug=True)
