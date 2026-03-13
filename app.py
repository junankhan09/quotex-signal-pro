from flask import Flask, render_template, request, jsonify
import os
from datetime import datetime, timedelta
import random
import time
import secrets

# Create Flask app
app = Flask(__name__)

# Configuration - Password (same as your "j")
app.config['PASSWORD'] = 'jummuubot'
app.config['SECRET_KEY'] = secrets.token_hex(32)

# ============================================
# COMPLETE MARKETS DATA (EXACTLY FROM YOUR HTML)
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

    # Commodities (Real Market)
    {'value': 'XAUUSD', 'label': 'Gold', 'group': 'Commodities (Real Market)'},
    {'value': 'XAGUSD', 'label': 'Silver', 'group': 'Commodities (Real Market)'},
    {'value': 'XBRUSD', 'label': 'Brent Oil', 'group': 'Commodities (Real Market)'},
    {'value': 'XTIUSD', 'label': 'WTI Oil', 'group': 'Commodities (Real Market)'},
    {'value': 'NATGAS', 'label': 'Natural Gas', 'group': 'Commodities (Real Market)'},

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

# Timeframes (same as your HTML)
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

# Cache to prevent duplicate signals (same as your existingSignals Set)
generated_signals_cache = set()


# ============================================
# SIGNAL GENERATION LOGIC (EXACTLY LIKE YOUR HTML, BUT HIDDEN)
# ============================================

def generate_random_interval():
    """Same as your HTML: Math.floor(Math.random() * 4) + 3"""
    return random.randint(3, 6)


def format_timeframe(tf):
    """Same as your HTML: return tf < 60 ? `M${tf}` : `H${tf/60}`"""
    tf_int = int(tf)
    return f"M{tf_int}" if tf_int < 60 else f"H{tf_int // 60}"


def generate_signals_logic(assets, count, timeframe, multi_assist=False):
    """
    EXACT same logic as your HTML:
    - generateSingleAssetSignals
    - generateMultiAssistSignals
    """
    signals = []
    next_time = datetime.now()

    for i in range(count):
        # Add random interval (same as your generateRandomInterval)
        next_time = next_time + timedelta(minutes=generate_random_interval())
        time_str = next_time.strftime('%H:%M')

        # Select asset (same logic)
        if multi_assist and assets:
            selected_asset = random.choice(assets)
        else:
            selected_asset = assets[0] if assets else "BTCUSD_otc"

        # Find market label
        market = next((m for m in MARKETS if m['value'] == selected_asset), None)
        if market:
            asset_label = market['label']
        else:
            asset_label = selected_asset

        # Create unique key to prevent duplicates (same as your existingSignals Set)
        signal_key = f"{selected_asset}|{time_str}"

        if signal_key not in generated_signals_cache:
            # Random direction (same as your Math.random() < 0.5)
            direction = random.choice(['CALL', 'PUT'])

            signals.append({
                'asset': asset_label,
                'time': time_str,
                'direction': direction,
                'timeframe': format_timeframe(timeframe)
            })

            # Add to cache
            generated_signals_cache.add(signal_key)

            # Prevent cache from growing too large
            if len(generated_signals_cache) > 1000:
                generated_signals_cache.clear()

    return signals


# ============================================
# API ROUTES
# ============================================

@app.route('/')
def index():
    """Serve your HTML page"""
    return render_template('index.html')


@app.route('/api/verify-password', methods=['POST'])
def verify_password():
    """Verify password - HIDDEN FROM USER"""
    try:
        data = request.json
        password = data.get('password', '')

        if password == app.config['PASSWORD']:
            return jsonify({'success': True})
        else:
            return jsonify({'success': False}), 401
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/generate-signals', methods=['POST'])
def generate_signals():
    """Generate signals - ALL LOGIC HIDDEN HERE"""
    try:
        data = request.json
        assets = data.get('assets', [])
        count = data.get('count', 10)
        timeframe = data.get('timeframe', '1')
        multi_assist = data.get('multi_assist', False)

        # Validate
        if not assets:
            return jsonify({'success': False, 'error': 'No assets selected'}), 400

        # Generate signals
        signals = generate_signals_logic(assets, count, timeframe, multi_assist)

        return jsonify({
            'success': True,
            'signals': signals
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print("=" * 50)
    print("Quotex Signal Pro - Backend Server")
    print("=" * 50)
    print(f"📍 URL: http://localhost:{port}")
    print(f"🔑 Password: {app.config['PASSWORD']}")
    print("=" * 50)
    app.run(host='0.0.0.0', port=port, debug=True)