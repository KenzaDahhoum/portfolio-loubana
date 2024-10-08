from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS to allow requests from Vue.js frontend

# Root route for the base URL
@app.route('/')
def index():
    return "Welcome to Kenza's Entrepreneurial Journey and Personal Portfolio API!"

# Sample API endpoint for fetching portfolio projects
@app.route('/api/portfolio', methods=['GET'])
def get_portfolio():
    portfolio_projects = [
    {
        'title': 'Loubana Skincare',
        'description': 'An e-commerce platform selling natural skincare products. Built with Vue.js and Flask.',
        'link': 'https://loubana-skincare.com'  
    },
    {
        'title': 'Personal Portfolio Website',
        'description': 'A web-based portfolio showcasing my web development skills and projects.',
        'link': 'https://github.com/KenzaDahhoum/portfolio'
    },
    {
        'title': 'HRZen System',
        'description': 'An HR management system built with Flask and Vue.js for managing employee data and attendance.',
        'link': 'https://github.com/KenzaDahhoum/hrzen-system'
    }
]

    return jsonify(portfolio_projects)

if __name__ == '__main__':
    app.run(debug=True)
