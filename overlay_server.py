
from flask import Flask, request, jsonify, send_from_directory, render_template_string

app = Flask(__name__)
likes_data = {}

@app.route('/like', methods=['POST'])
def receive_like():
    data = request.get_json()
    username = data.get('username')
    likes = data.get('likes', 0)
    if username:
        likes_data[username] = likes
    return 'OK', 200

@app.route('/overlay')
def overlay():
    sorted_likes = sorted(likes_data.items(), key=lambda x: x[1], reverse=True)
    html = '''
    <html>
    <head>
        <style>
            body { background: transparent; color: white; font-family: Arial; }
            .top1 { font-weight: bold; color: gold; }
            .like-entry { margin: 5px 0; font-size: 20px; }
            img { vertical-align: middle; height: 24px; }
        </style>
    </head>
    <body>
        <h3>Top Likes</h3>
        {% for i, (name, likes) in enumerate(likes_list) %}
            <div class="like-entry {% if i == 0 %}top1{% endif %}">
                {% if i == 0 %}
                    <img src="/static/png/top1.png"> 
                {% else %}
                    <img src="/static/png/heart.png"> 
                {% endif %}
                {{ name }} - {{ likes }} Likes
            </div>
        {% endfor %}
    </body>
    </html>
    '''
    return render_template_string(html, likes_list=sorted_likes)

@app.route('/static/png/<path:filename>')
def static_png(filename):
    return send_from_directory('png', filename)

app.run(host='0.0.0.0', port=8080)
