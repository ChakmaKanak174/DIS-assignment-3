from flask import Flask, render_template, request
import psycopg2 

app = Flask(__name__)

def get_DB_connection():
    con1 = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="13579",
        host="localhost",
        port="5432"
    )
    return con1

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/submit-location', methods=['POST'])
def submit_location():
    location = request.form['location']
    conn = get_DB_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * from student;",(location,)) 
        data = cursor.fetchall()

    except Exception as e:
        print("Error=", e)
        data = []

    finally:
        cursor.close()
        conn.close()

    return render_template('result.html', location='location', data=data)




    #return f"You selected: {selected_location}"

if __name__ == '__main__': 
    app.run(debug=True)