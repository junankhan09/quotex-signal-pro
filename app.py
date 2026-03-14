from flask import Flask, render_template, request, jsonify
import os
from datetime import datetime, timedelta
import random
import secrets

# CRITICAL: Flask app must be named 'app' and template folder specified
app = Flask(__name__, template_folder='templates')

# Configuration - Get password from environment variable
app.config['PASSWORD'] = os.environ.get('SITE_PASSWORD', 'jummuubot')
app.config['SECRET_KEY'] = secrets.token_hex(32)

# Markets data (keep your full list here)
MARKETS = [
    {'value': 'GBPUSD_otc', 'label': 'GBP/USD (OTC)', 'group': 'Forex OTC Pairs'},
    {'value': 'USDJPY_otc', 'label': 'USD/JPY (OTC)', 'group': 'Forex OTC Pairs'},
    # ... (keep all your 100+ markets here)
]


# Simple test route to verify it's working
@app.route('/api/test')
def test():
    return jsonify({'status': 'ok', 'message': 'Server is running!'})


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/verify-password', methods=['POST'])
def verify_password():
    try:
        data = request.get_json()
        if data and data.get('password') == app.config['PASSWORD']:
            return jsonify({'success': True})
        return jsonify({'success': False}), 401
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


# Signal generation logic
generated_signals_cache = set()


def generate_random_interval():
    return random.randint(3, 6)


def format_timeframe(tf):
    tf_int = int(tf)
    return f"M{tf_int}" if tf_int < 60 else f"H{tf_int // 60}"


def generate_signals_logic(assets, count, timeframe, multi_assist=False):
    signals = []
    next_time = datetime.now()

    for i in range(count):
        next_time = next_time + timedelta(minutes=generate_random_interval())
        time_str = next_time.strftime('%H:%M')

        if multi_assist and assets:
            selected_asset = random.choice(assets)
        else:
            selected_asset = assets[0] if assets else "BTCUSD_otc"

        market = next((m for m in MARKETS if m['value'] == selected_asset), None)
        asset_label = market['label'] if market else selected_asset

        signal_key = f"{selected_asset}|{time_str}"

        if signal_key not in generated_signals_cache:
            direction = random.choice(['CALL', 'PUT'])
            signals.append({
                'asset': asset_label,
                'time': time_str,
                'direction': direction,
                'timeframe': format_timeframe(timeframe)
            })
            generated_signals_cache.add(signal_key)

            if len(generated_signals_cache) > 1000:
                generated_signals_cache.clear()

    return signals


@app.route('/api/generate-signals', methods=['POST'])
def generate_signals():
    try:
        data = request.get_json()
        assets = data.get('assets', [])
        count = data.get('count', 10)
        timeframe = data.get('timeframe', '1')
        multi_assist = data.get('multi_assist', False)

        if not assets:
            return jsonify({'success': False, 'error': 'No assets selected'}), 400

        signals = generate_signals_logic(assets, count, timeframe, multi_assist)

        return jsonify({'success': True, 'signals': signals})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


# For local development
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"Server running at http://localhost:{port}")
    print(f"Password: {app.config['PASSWORD']}")
    app.run(host='0.0.0.0', port=port, debug=True)