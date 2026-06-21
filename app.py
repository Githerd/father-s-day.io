from flask import Flask, render_template, jsonify, request
import random
import os
import sys

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

# Sample dad names and messages (can be extended)
DAD_NAMES = ['Dad', 'Papa', 'Daddy', 'Father', 'Pop']
PROVISION_MESSAGES = [
    "A father's true legacy is not in what he leaves behind, but in the strength, wisdom, and abundance he builds in those he loves.",
    "A father provides not just for today, but for generations to come.",
    "The greatest gift a father gives is the foundation of confidence and the tools to build a future.",
    "A father's provision is measured not in wealth, but in the opportunities he creates.",
    "True abundance flows from a father's love, guidance, and unwavering support.",
    "A father builds more than a home—he builds a legacy of resilience and prosperity."
]

@app.route('/')
def index():
    """Render the main Father's Day page."""
    context = {
        'dad_name': 'Dad',
        'message': random.choice(PROVISION_MESSAGES),
        'year': 2026
    }
    return render_template('index.html', **context)

@app.route('/api/message')
def get_message():
    """API endpoint to get a random provision message."""
    return jsonify({
        'message': random.choice(PROVISION_MESSAGES),
        'status': 'success'
    })

@app.route('/api/surprise')
def get_surprise():
    """API endpoint to get surprise messages focused on provision and wealth."""
    surprises = [
        {'text': '🏦 You build more than wealth — you build futures. Thank you, Dad!', 'icon': 'fa-building-columns'},
        {'text': '📈 Your wisdom is the greatest investment. It keeps growing in us.', 'icon': 'fa-arrow-trend-up'},
        {'text': '🌱 Every seed you\'ve planted in us has grown into abundance.', 'icon': 'fa-seedling'},
        {'text': '🛡️ You are our provider, protector, and pillar of strength.', 'icon': 'fa-shield-halved'},
        {'text': '🌟 Your legacy is not in gold, but in the values you\'ve given us.', 'icon': 'fa-star'},
        {'text': '💼 Thank you for working hard so we can dream bigger. You\'re our hero.', 'icon': 'fa-briefcase'},
        {'text': '💰 Your provision is the foundation of our dreams. We are forever grateful.', 'icon': 'fa-coins'},
        {'text': '🏆 You\'ve built an empire of love, wisdom, and opportunity for us.', 'icon': 'fa-trophy'},
    ]
    return jsonify(random.choice(surprises))

@app.route('/api/update-name', methods=['POST'])
def update_name():
    """Update the dad's name (for potential future customization)."""
    data = request.get_json()
    name = data.get('name', 'Dad')
    return jsonify({
        'status': 'success',
        'name': name,
        'message': f'Name updated to {name}'
    })

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({'error': 'Internal server error'}), 500

def main():
    """Main entry point for the application."""
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

if __name__ == '__main__':
    main()
