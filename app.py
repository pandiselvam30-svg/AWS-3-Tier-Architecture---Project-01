from flask import Flask, request, jsonify
import pymysql
 
app = Flask(__name__)
 
DB_CONFIG = {
    'host':   'project01-db.cvq6w4sug3al.ap-south-1.rds.amazonaws.com',
    'user':   'admin',
    'password': 'Pandisp7492',
    'db':     'feedbackdb',
    'cursorclass': pymysql.cursors.DictCursor
}
 
@app.route('/')
def health():
    return jsonify({'status': 'Flask is running'})
 
@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    conn = pymysql.connect(**DB_CONFIG)
    with conn.cursor() as cur:
        cur.execute(
            'INSERT INTO feedback (name, email, feedback) VALUES (%s, %s, %s)',
            (data['name'], data['email'], data['feedback'])
        )
    conn.commit()
    conn.close()
    return jsonify({'message': 'Feedback submitted successfully!'})
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
