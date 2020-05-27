from flask import Flask, render_template, request, redirect, url_for, jsonify
import session_items as session

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/')
def index():
    return render_template('index.html', title='Home',items=session.get_items())

@app.route('/todo', methods=['POST'])
def new_todo():
    data = request.json
    print("data is " + format(data))
    session.add_item(data['title'])
    return jsonify(success=True)
    
@app.route('/todo/<item_id>', methods=['PUT'])
def update_todo(item_id):
    data = request.json
    print("data is " + format(data))
    item = session.get_item(item_id)
    item['status'] = data['status']
    session.save_item(item)
    return jsonify(success=True)
    
@app.route('/todo/<item_id>', methods=['DELETE'])
def delete_todo(item_id):
    item = session.get_item(item_id)
    session.remove_item(item)
    return jsonify(success=True)
    
if __name__ == '__main__':
    app.run()
