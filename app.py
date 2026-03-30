from flask import Flask, render_template, request, jsonify
import os
from datetime import datetime, timedelta
import random
import secrets
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create Flask app
app = Flask(__name__, template_folder='templates')

# Configuration - Get password from environment variable
app.config['PASSWORD'] = os.environ.get('SITE_PASSWORD', 'jummuubot')
app.config['SECRET_KEY'] = secrets.token_hex(32)

# ============================================
# COMPLETE MARKETS DATA (ALL YOUR PAIRS - HIDDEN FROM USER)
# ============================================
MARKETS = [
    # Forex OTC Pairs
    {'value': 'GBPUSD_otc', 'label': 'GBP/USD (OTC)', 'group': 'Forex OTC Pairs'},
    {'value': 'USDJPY_otc', 'label': 'USD/JPY (OTC)', 'group': 'Forex OTC Pairs'},
    {'value': 'USDCHF_otc', 'label': 'USD/CHF (OTC)', 'group': 'Forex OTC Pairs'},
    {'value': 'AUDUSD_otc', 'label': 'AUD/USD (OTC)', 'group': 'Forex OTC Pairs'},
    {'value': 'USDCAD_otc', 'label': 'USD/CAD (OTC)', 'group': 'Forex OTC Pairs'},
    {'value': 'EURGBP_otc', 'label': 'EUR/GBP (OTC)', 'group': 'Forex OTC Pairs'},
    {'value': 'EURNZD_otc', 'label': 'EUR/NZD (OTC)', 'group': 'Forex OTC Pairs'},
    {'value': 'EURJPY_otc', 'label': 'EUR/JPY (OTC)', 'group': 'Forex OTC Pairs'},
    {'value': 'GBPJPY_otc', 'label': 'GBP/JPY (OTC)', 'group': 'Forex OTC Pairs'},
    {'value': 'AUDJPY_otc', 'label': 'AUD/JPY (OTC)', 'group': 'Forex OTC Pairs'},
    {'value': 'EURCHF_otc', 'label': 'EUR/CHF (OTC)', 'group': 'Forex OTC Pairs'},
    {'value': 'EURSGD_otc', 'label': 'EUR/SGD (OTC)', 'group': 'Forex OTC Pairs'},
    {'value': 'GBPCHF_otc', 'label': 'GBP/CHF (OTC)', 'group': 'Forex OTC Pairs'},
    {'value': 'NZDUSD_otc', 'label': 'NZD/USD (OTC)', 'group': 'Forex OTC Pairs'},
    {'value': 'NZDCHF_otc', 'label': 'NZD/CHF (OTC)', 'group': 'Forex OTC Pairs'},
    {'value': 'NZDCAD_otc', 'label': 'NZD/CAD (OTC)', 'group': 'Forex OTC Pairs'},
    {'value': 'NZDJPY_otc', 'label': 'NZD/JPY (OTC)', 'group': 'Forex OTC Pairs'},
    {'value': 'AUDCAD_otc', 'label': 'AUD/CAD (OTC)', 'group': 'Forex OTC Pairs'},
    {'value': 'AUDNZD_otc', 'label': 'AUD/NZD (OTC)', 'group': 'Forex OTC Pairs'},
    {'value': 'CADJPY_otc', 'label': 'CAD/JPY (OTC)', 'group': 'Forex OTC Pairs'},
    {'value': 'CHFJPY_otc', 'label': 'CHF/JPY (OTC)', 'group': 'Forex OTC Pairs'},
    {'value': 'EURAUD_otc', 'label': 'EUR/AUD (OTC)', 'group': 'Forex OTC Pairs'},
    {'value': 'EURCAD_otc', 'label': 'EUR/CAD (OTC)', 'group': 'Forex OTC Pairs'},
    {'value': 'GBPAUD_otc', 'label': 'GBP/AUD (OTC)', 'group': 'Forex OTC Pairs'},
    {'value': 'GBPNZD_otc', 'label': 'GBP/NZD (OTC)', 'group': 'Forex OTC Pairs'},
    {'value': 'GBPCAD_otc', 'label': 'GBP/CAD (OTC)', 'group': 'Forex OTC Pairs'},
    {'value': 'USDBDT_otc', 'label': 'USD/BDT (OTC)', 'group': 'Forex OTC Pairs'},
    {'value': 'BRLUSD_otc', 'label': 'BRL/USD (OTC)', 'group': 'Forex OTC Pairs'},
    {'value': 'USDINR_otc', 'label': 'USD/INR (OTC)', 'group': 'Forex OTC Pairs'},
    {'value': 'USDARS_otc', 'label': 'USD/ARS (OTC)', 'group': 'Forex OTC Pairs'},
    {'value': 'USDPHP_otc', 'label': 'USD/PHP (OTC)', 'group': 'Forex OTC Pairs'},
    {'value': 'USDPKR_otc', 'label': 'USD/PKR (OTC)', 'group': 'Forex OTC Pairs'},
    {'value': 'USDMXN_otc', 'label': 'USD/MXN (OTC)', 'group': 'Forex OTC Pairs'},
    {'value': 'USDCOP_otc', 'label': 'USD/COP (OTC)', 'group': 'Forex OTC Pairs'},
    {'value': 'USDEGP_otc', 'label': 'USD/EGP (OTC)', 'group': 'Forex OTC Pairs'},
    {'value': 'USDTRY_otc', 'label': 'USD/TRY (OTC)', 'group': 'Forex OTC Pairs'},
    {'value': 'USDDZD_otc', 'label': 'USD/DZD (OTC)', 'group': 'Forex OTC Pairs'},
    {'value': 'USDIDR_otc', 'label': 'USD/IDR (OTC)', 'group': 'Forex OTC Pairs'},
    {'value': 'USDZAR_otc', 'label': 'USD/ZAR (OTC)', 'group': 'Forex OTC Pairs'},

    # Cryptocurrencies
    {'value': 'BTCUSD_otc', 'label': 'Bitcoin (OTC)', 'group': 'Cryptocurrencies'},
    {'value': 'ARBUSD_otc', 'label': 'Arbitrum (OTC)', 'group': 'Cryptocurrencies'},
    {'value': 'AXIUSD_otc', 'label': 'Axie Infinity (OTC)', 'group': 'Cryptocurrencies'},
    {'value': 'HAMUSD_otc', 'label': 'Hamster (OTC)', 'group': 'Cryptocurrencies'},
    {'value': 'SHIUSD_otc', 'label': 'Shiba Inu (OTC)', 'group': 'Cryptocurrencies'},
    {'value': 'ETHUSD_otc', 'label': 'Ethereum (OTC)', 'group': 'Cryptocurrencies'},
    {'value': 'ADAUSD_otc', 'label': 'Cardano (OTC)', 'group': 'Cryptocurrencies'},
    {'value': 'BNBUSD_otc', 'label': 'Binance Coin (OTC)', 'group': 'Cryptocurrencies'},
    {'value': 'XRPUSD_otc', 'label': 'Ripple (OTC)', 'group': 'Cryptocurrencies'},
    {'value': 'LTCUSD_otc', 'label': 'Litecoin (OTC)', 'group': 'Cryptocurrencies'},
    {'value': 'DOGUSD_otc', 'label': 'Dogecoin (OTC)', 'group': 'Cryptocurrencies'},
    {'value': 'TRXUSD_otc', 'label': 'TRON (OTC)', 'group': 'Cryptocurrencies'},
    {'value': 'PEPUSD_otc', 'label': 'Pepe (OTC)', 'group': 'Cryptocurrencies'},
    {'value': 'GALUSD_otc', 'label': 'Gala (OTC)', 'group': 'Cryptocurrencies'},
    {'value': 'TRUUSD_otc', 'label': 'Trump (OTC)', 'group': 'Cryptocurrencies'},
    {'value': 'BONUSD_otc', 'label': 'Bonk (OTC)', 'group': 'Cryptocurrencies'},
    {'value': 'MANUSD_otc', 'label': 'Decentraland (OTC)', 'group': 'Cryptocurrencies'},
    {'value': 'MELUSD_otc', 'label': 'Melania Meme (OTC)', 'group': 'Cryptocurrencies'},
    {'value': 'APTUSD_otc', 'label': 'Aptos (OTC)', 'group': 'Cryptocurrencies'},
    {'value': 'AVAUSD_otc', 'label': 'Avalanche (OTC)', 'group': 'Cryptocurrencies'},
    {'value': 'BCHUSD_otc', 'label': 'Bitcoin Cash (OTC)', 'group': 'Cryptocurrencies'},
    {'value': 'DOTUSD_otc', 'label': 'Polkadot (OTC)', 'group': 'Cryptocurrencies'},
    {'value': 'LINKUSD_otc', 'label': 'Chainlink (OTC)', 'group': 'Cryptocurrencies'},
    {'value': 'ATOMUSD_otc', 'label': 'Cosmos (OTC)', 'group': 'Cryptocurrencies'},
    {'value': 'SOLUSD_otc', 'label': 'Solana (OTC)', 'group': 'Cryptocurrencies'},
    {'value': 'TONUSD_otc', 'label': 'Toncoin (OTC)', 'group': 'Cryptocurrencies'},
    {'value': 'FLOKIUSD_otc', 'label': 'Floki (OTC)', 'group': 'Cryptocurrencies'},
    {'value': 'DASHUSD_otc', 'label': 'Dash (OTC)', 'group': 'Cryptocurrencies'},

    # Commodities OTC
    {'value': 'UKBrent_otc', 'label': 'UK Brent Oil (OTC)', 'group': 'Commodities OTC'},
    {'value': 'USCrude_otc', 'label': 'US Crude Oil (OTC)', 'group': 'Commodities OTC'},
    {'value': 'XAUUSD_otc', 'label': 'Gold (OTC)', 'group': 'Commodities OTC'},
    {'value': 'XAGUSD_otc', 'label': 'Silver (OTC)', 'group': 'Commodities OTC'},

    # Stocks
    {'value': 'MSFT_otc', 'label': 'Microsoft (OTC)', 'group': 'Stocks'},
    {'value': 'PFE_otc', 'label': 'Pfizer (OTC)', 'group': 'Stocks'},
    {'value': 'BA_otc', 'label': 'Boeing (OTC)', 'group': 'Stocks'},
    {'value': 'JNJ_otc', 'label': 'Johnson & Johnson (OTC)', 'group': 'Stocks'},
    {'value': 'INTC_otc', 'label': 'Intel (OTC)', 'group': 'Stocks'},
    {'value': 'MCD_otc', 'label': "McDonald's (OTC)", 'group': 'Stocks'},
    {'value': 'AXP_otc', 'label': 'American Express (OTC)', 'group': 'Stocks'},
    {'value': 'FB_otc', 'label': 'Facebook (OTC)', 'group': 'Stocks'}
]

# Timeframes
TIMEFRAMES = [
    {'value': '1', 'label': '1m'},
    {'value': '2', 'label': '2m'},
    {'value': '5', 'label': '5m'},
    {'value': '10', 'label': '10m'},
    {'value': '15', 'label': '15m'},
    {'value': '30', 'label': '30m'},
    {'value': '60', 'label': '1h'},
    {'value': '120', 'label': '2h'},
    {'value': '240', 'label': '4h'}
]

# Cache to prevent duplicate signals (HIDDEN FROM USER)
generated_signals_cache = set()
analysis_cache = {}


# ============================================
# HIDDEN SIGNAL GENERATION LOGIC (USERS CANNOT SEE THIS)
# ============================================

def generate_random_interval():
    """Generate random interval between signals (3-6 minutes)"""
    return random.randint(3, 6)


def format_timeframe(tf):
    """Format timeframe for display"""
    tf_int = int(tf)
    return f"M{tf_int}" if tf_int < 60 else f"H{tf_int // 60}"


def calculate_signal_strength():
    """Hidden algorithm for signal strength (random but looks realistic)"""
    strengths = ['High', 'Medium', 'Low']
    weights = [0.6, 0.3, 0.1]  # 60% high, 30% medium, 10% low
    return random.choices(strengths, weights=weights)[0]


def calculate_confidence():
    """Hidden algorithm for confidence percentage"""
    return random.randint(75, 98)


def generate_signals_logic(assets, count, timeframe, multi_assist=False):
    """
    Core signal generation logic - COMPLETELY HIDDEN FROM USERS
    Uses random math but appears realistic to users
    """
    signals = []

    # Get current UTC time and add 6 hours for UTC+6 (Bangladesh)
    utc_now = datetime.utcnow()
    utc_plus_6 = utc_now + timedelta(hours=6)

    # Start from current UTC+6 time
    next_time = utc_plus_6

    for i in range(count):
        # Add random interval between 3-6 minutes for future signals
        interval = generate_random_interval()
        next_time = next_time + timedelta(minutes=interval)
        time_str = next_time.strftime('%H:%M')

        # Select asset (random if multi-assist, otherwise first selected)
        if multi_assist and assets:
            selected_asset = random.choice(assets)
        else:
            selected_asset = assets[0] if assets else "BTCUSD_otc"

        # Find market label
        market = next((m for m in MARKETS if m['value'] == selected_asset), None)
        asset_label = market['label'] if market else selected_asset

        # Create unique key to prevent duplicates
        signal_key = f"{selected_asset}|{time_str}"

        if signal_key not in generated_signals_cache:
            # Random direction with slight bias for variety
            direction = random.choice(['CALL', 'PUT'])

            # Hidden calculations for signal metadata
            signal_strength = calculate_signal_strength()
            confidence = calculate_confidence()

            signals.append({
                'asset': asset_label,
                'time': time_str,
                'direction': direction,
                'timeframe': format_timeframe(timeframe),
                'strength': signal_strength,  # Hidden from frontend but available
                'confidence': confidence  # Hidden from frontend but available
            })

            # Add to cache
            generated_signals_cache.add(signal_key)

            # Prevent cache from growing too large
            if len(generated_signals_cache) > 1000:
                generated_signals_cache.clear()

    return signals


def get_analysis_steps():
    """Hidden analysis steps that look professional to users"""
    steps = [
        "📊 Analyzing price action patterns...",
        "✓ Pattern recognition complete",
        "📈 Calculating RSI and momentum indicators...",
        "✓ Technical indicators processed",
        "🔍 Identifying support and resistance levels...",
        "✓ Key levels identified",
        "📉 Analyzing volume profile...",
        "✓ Volume analysis verified",
        "🎯 Calculating entry points...",
        "✓ Entry levels optimized",
        "💰 Setting take profit targets...",
        "✓ Profit targets calculated",
        "🛡️ Determining stop loss levels...",
        "✓ Risk management parameters set",
        "⚡ Generating final signal...",
        "✓ High-probability signal ready for execution"
    ]
    return steps


# ============================================
# API ROUTES - ALL WORKING FOR RAILWAY
# ============================================

@app.route('/')
def index():
    """Serve your HTML page"""
    logger.info("Serving index page")
    return render_template('index.html')


@app.route('/health')
def health():
    """Health check endpoint for Railway"""
    return jsonify({
        'status': 'ok',
        'message': 'Quotex Signal Pro is running!',
        'timestamp': datetime.now().isoformat(),
        'version': '3.0'
    })


@app.route('/api/verify-password', methods=['POST'])
def verify_password():
    """Verify password - HIDDEN FROM USER"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'success': False, 'error': 'No data provided'}), 400

        password = data.get('password', '')

        # Simple comparison - hidden logic
        if password == app.config['PASSWORD']:
            logger.info("Successful login attempt")
            return jsonify({'success': True})
        else:
            logger.warning("Failed login attempt")
            return jsonify({'success': False, 'error': 'Invalid password'}), 401
    except Exception as e:
        logger.error(f"Password verification error: {e}")
        return jsonify({'success': False, 'error': 'Server error'}), 500


@app.route('/api/analysis-steps', methods=['GET'])
def get_analysis_steps_api():
    """Return analysis steps for frontend animation - HIDDEN LOGIC"""
    try:
        steps = get_analysis_steps()
        return jsonify({
            'success': True,
            'steps': steps
        })
    except Exception as e:
        logger.error(f"Analysis steps error: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/generate-signals', methods=['POST'])
def generate_signals_api():
    """Generate signals - ALL LOGIC HIDDEN HERE"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'success': False, 'error': 'No data provided'}), 400

        assets = data.get('assets', [])
        count = data.get('count', 10)
        timeframe = data.get('timeframe', '1')
        multi_assist = data.get('multi_assist', False)

        # Validate
        if not assets:
            return jsonify({'success': False, 'error': 'No assets selected'}), 400

        # Validate count
        if count < 1 or count > 50:
            count = 10

        # Generate signals using hidden logic
        signals = generate_signals_logic(assets, count, timeframe, multi_assist)

        # Remove hidden fields before sending to frontend
        clean_signals = []
        for signal in signals:
            clean_signals.append({
                'asset': signal['asset'],
                'time': signal['time'],
                'direction': signal['direction'],
                'timeframe': signal['timeframe']
            })

        logger.info(f"Generated {len(clean_signals)} signals for {len(assets)} assets")

        return jsonify({
            'success': True,
            'signals': clean_signals,
            'count': len(clean_signals),
            'generated_at': datetime.now().isoformat()
        })
    except Exception as e:
        logger.error(f"Signal generation error: {e}")
        return jsonify({'success': False, 'error': 'Failed to generate signals'}), 500


@app.route('/api/test')
def test():
    """Test endpoint to verify API is working"""
    return jsonify({
        'status': 'ok',
        'message': 'API is working on Railway!',
        'version': '3.0',
        'password_protected': bool(app.config['PASSWORD']),
        'markets_loaded': len(MARKETS)
    })


@app.route('/api/markets', methods=['GET'])
def get_markets():
    """Get all available markets"""
    try:
        return jsonify({
            'success': True,
            'markets': MARKETS,
            'count': len(MARKETS)
        })
    except Exception as e:
        logger.error(f"Markets error: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/timeframes', methods=['GET'])
def get_timeframes():
    """Get all available timeframes"""
    try:
        return jsonify({
            'success': True,
            'timeframes': TIMEFRAMES
        })
    except Exception as e:
        logger.error(f"Timeframes error: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


# ============================================
# ERROR HANDLERS
# ============================================

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({'success': False, 'error': 'Endpoint not found'}), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    logger.error(f"Internal server error: {error}")
    return jsonify({'success': False, 'error': 'Internal server error'}), 500


# ============================================
# MAIN ENTRY POINT
# ============================================

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug_mode = os.environ.get('FLASK_ENV', 'production') == 'development'

    print("=" * 60)
    print("🚀 QUOTEX SIGNAL PRO - Backend Server")
    print("=" * 60)
    print(f"📍 Server URL: http://localhost:{port}")
    print(f"🔑 Access Password: {app.config['PASSWORD']}")
    print(f"🌍 Environment: {os.environ.get('FLASK_ENV', 'production')}")
    print(f"📊 Markets Loaded: {len(MARKETS)}")
    print(f"⏱️  Timeframes Available: {len(TIMEFRAMES)}")
    print("=" * 60)
    print("✅ Server is ready to accept connections")
    print("=" * 60)

    app.run(host='0.0.0.0', port=port, debug=debug_mode)