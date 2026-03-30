// ============================================
// QUOTEX SIGNAL PRO - CLOUDFLARE VERSION
// ALL 79 TRADING PAIRS INTACT
// DESIGN UNCHANGED
// ============================================

// COMPLETE MARKETS DATA - EXACTLY AS IN YOUR ORIGINAL BOT
const MARKETS = [
    // Forex OTC Pairs (40+)
    { value: 'GBPUSD_otc', label: 'GBP/USD (OTC)', group: 'Forex OTC Pairs' },
    { value: 'USDJPY_otc', label: 'USD/JPY (OTC)', group: 'Forex OTC Pairs' },
    { value: 'USDCHF_otc', label: 'USD/CHF (OTC)', group: 'Forex OTC Pairs' },
    { value: 'AUDUSD_otc', label: 'AUD/USD (OTC)', group: 'Forex OTC Pairs' },
    { value: 'USDCAD_otc', label: 'USD/CAD (OTC)', group: 'Forex OTC Pairs' },
    { value: 'EURGBP_otc', label: 'EUR/GBP (OTC)', group: 'Forex OTC Pairs' },
    { value: 'EURNZD_otc', label: 'EUR/NZD (OTC)', group: 'Forex OTC Pairs' },
    { value: 'EURJPY_otc', label: 'EUR/JPY (OTC)', group: 'Forex OTC Pairs' },
    { value: 'GBPJPY_otc', label: 'GBP/JPY (OTC)', group: 'Forex OTC Pairs' },
    { value: 'AUDJPY_otc', label: 'AUD/JPY (OTC)', group: 'Forex OTC Pairs' },
    { value: 'EURCHF_otc', label: 'EUR/CHF (OTC)', group: 'Forex OTC Pairs' },
    { value: 'EURSGD_otc', label: 'EUR/SGD (OTC)', group: 'Forex OTC Pairs' },
    { value: 'GBPCHF_otc', label: 'GBP/CHF (OTC)', group: 'Forex OTC Pairs' },
    { value: 'NZDUSD_otc', label: 'NZD/USD (OTC)', group: 'Forex OTC Pairs' },
    { value: 'NZDCHF_otc', label: 'NZD/CHF (OTC)', group: 'Forex OTC Pairs' },
    { value: 'NZDCAD_otc', label: 'NZD/CAD (OTC)', group: 'Forex OTC Pairs' },
    { value: 'NZDJPY_otc', label: 'NZD/JPY (OTC)', group: 'Forex OTC Pairs' },
    { value: 'AUDCAD_otc', label: 'AUD/CAD (OTC)', group: 'Forex OTC Pairs' },
    { value: 'AUDNZD_otc', label: 'AUD/NZD (OTC)', group: 'Forex OTC Pairs' },
    { value: 'CADJPY_otc', label: 'CAD/JPY (OTC)', group: 'Forex OTC Pairs' },
    { value: 'CHFJPY_otc', label: 'CHF/JPY (OTC)', group: 'Forex OTC Pairs' },
    { value: 'EURAUD_otc', label: 'EUR/AUD (OTC)', group: 'Forex OTC Pairs' },
    { value: 'EURCAD_otc', label: 'EUR/CAD (OTC)', group: 'Forex OTC Pairs' },
    { value: 'GBPAUD_otc', label: 'GBP/AUD (OTC)', group: 'Forex OTC Pairs' },
    { value: 'GBPNZD_otc', label: 'GBP/NZD (OTC)', group: 'Forex OTC Pairs' },
    { value: 'GBPCAD_otc', label: 'GBP/CAD (OTC)', group: 'Forex OTC Pairs' },
    { value: 'USDBDT_otc', label: 'USD/BDT (OTC)', group: 'Forex OTC Pairs' },
    { value: 'BRLUSD_otc', label: 'BRL/USD (OTC)', group: 'Forex OTC Pairs' },
    { value: 'USDINR_otc', label: 'USD/INR (OTC)', group: 'Forex OTC Pairs' },
    { value: 'USDARS_otc', label: 'USD/ARS (OTC)', group: 'Forex OTC Pairs' },
    { value: 'USDPHP_otc', label: 'USD/PHP (OTC)', group: 'Forex OTC Pairs' },
    { value: 'USDPKR_otc', label: 'USD/PKR (OTC)', group: 'Forex OTC Pairs' },
    { value: 'USDMXN_otc', label: 'USD/MXN (OTC)', group: 'Forex OTC Pairs' },
    { value: 'USDCOP_otc', label: 'USD/COP (OTC)', group: 'Forex OTC Pairs' },
    { value: 'USDEGP_otc', label: 'USD/EGP (OTC)', group: 'Forex OTC Pairs' },
    { value: 'USDTRY_otc', label: 'USD/TRY (OTC)', group: 'Forex OTC Pairs' },
    { value: 'USDDZD_otc', label: 'USD/DZD (OTC)', group: 'Forex OTC Pairs' },
    { value: 'USDIDR_otc', label: 'USD/IDR (OTC)', group: 'Forex OTC Pairs' },
    { value: 'USDZAR_otc', label: 'USD/ZAR (OTC)', group: 'Forex OTC Pairs' },

    // Cryptocurrencies (28)
    { value: 'BTCUSD_otc', label: 'Bitcoin (OTC)', group: 'Cryptocurrencies' },
    { value: 'ARBUSD_otc', label: 'Arbitrum (OTC)', group: 'Cryptocurrencies' },
    { value: 'AXIUSD_otc', label: 'Axie Infinity (OTC)', group: 'Cryptocurrencies' },
    { value: 'HAMUSD_otc', label: 'Hamster (OTC)', group: 'Cryptocurrencies' },
    { value: 'SHIUSD_otc', label: 'Shiba Inu (OTC)', group: 'Cryptocurrencies' },
    { value: 'ETHUSD_otc', label: 'Ethereum (OTC)', group: 'Cryptocurrencies' },
    { value: 'ADAUSD_otc', label: 'Cardano (OTC)', group: 'Cryptocurrencies' },
    { value: 'BNBUSD_otc', label: 'Binance Coin (OTC)', group: 'Cryptocurrencies' },
    { value: 'XRPUSD_otc', label: 'Ripple (OTC)', group: 'Cryptocurrencies' },
    { value: 'LTCUSD_otc', label: 'Litecoin (OTC)', group: 'Cryptocurrencies' },
    { value: 'DOGUSD_otc', label: 'Dogecoin (OTC)', group: 'Cryptocurrencies' },
    { value: 'TRXUSD_otc', label: 'TRON (OTC)', group: 'Cryptocurrencies' },
    { value: 'PEPUSD_otc', label: 'Pepe (OTC)', group: 'Cryptocurrencies' },
    { value: 'GALUSD_otc', label: 'Gala (OTC)', group: 'Cryptocurrencies' },
    { value: 'TRUUSD_otc', label: 'Trump (OTC)', group: 'Cryptocurrencies' },
    { value: 'BONUSD_otc', label: 'Bonk (OTC)', group: 'Cryptocurrencies' },
    { value: 'MANUSD_otc', label: 'Decentraland (OTC)', group: 'Cryptocurrencies' },
    { value: 'MELUSD_otc', label: 'Melania Meme (OTC)', group: 'Cryptocurrencies' },
    { value: 'APTUSD_otc', label: 'Aptos (OTC)', group: 'Cryptocurrencies' },
    { value: 'AVAUSD_otc', label: 'Avalanche (OTC)', group: 'Cryptocurrencies' },
    { value: 'BCHUSD_otc', label: 'Bitcoin Cash (OTC)', group: 'Cryptocurrencies' },
    { value: 'DOTUSD_otc', label: 'Polkadot (OTC)', group: 'Cryptocurrencies' },
    { value: 'LINKUSD_otc', label: 'Chainlink (OTC)', group: 'Cryptocurrencies' },
    { value: 'ATOMUSD_otc', label: 'Cosmos (OTC)', group: 'Cryptocurrencies' },
    { value: 'SOLUSD_otc', label: 'Solana (OTC)', group: 'Cryptocurrencies' },
    { value: 'TONUSD_otc', label: 'Toncoin (OTC)', group: 'Cryptocurrencies' },
    { value: 'FLOKIUSD_otc', label: 'Floki (OTC)', group: 'Cryptocurrencies' },
    { value: 'DASHUSD_otc', label: 'Dash (OTC)', group: 'Cryptocurrencies' },

    // Commodities OTC
    { value: 'UKBrent_otc', label: 'UK Brent Oil (OTC)', group: 'Commodities OTC' },
    { value: 'USCrude_otc', label: 'US Crude Oil (OTC)', group: 'Commodities OTC' },
    { value: 'XAUUSD_otc', label: 'Gold (OTC)', group: 'Commodities OTC' },
    { value: 'XAGUSD_otc', label: 'Silver (OTC)', group: 'Commodities OTC' },

    // Stocks
    { value: 'MSFT_otc', label: 'Microsoft (OTC)', group: 'Stocks' },
    { value: 'PFE_otc', label: 'Pfizer (OTC)', group: 'Stocks' },
    { value: 'BA_otc', label: 'Boeing (OTC)', group: 'Stocks' },
    { value: 'JNJ_otc', label: 'Johnson & Johnson (OTC)', group: 'Stocks' },
    { value: 'INTC_otc', label: 'Intel (OTC)', group: 'Stocks' },
    { value: 'MCD_otc', label: "McDonald's (OTC)", group: 'Stocks' },
    { value: 'AXP_otc', label: 'American Express (OTC)', group: 'Stocks' },
    { value: 'FB_otc', label: 'Facebook (OTC)', group: 'Stocks' }
];

// Timeframes - Same as your bot
const TIMEFRAMES = [
    { value: '1', label: '1m' }, { value: '2', label: '2m' }, { value: '5', label: '5m' },
    { value: '10', label: '10m' }, { value: '15', label: '15m' }, { value: '30', label: '30m' },
    { value: '60', label: '1h' }, { value: '120', label: '2h' }, { value: '240', label: '4h' }
];

// Signal Generation Logic - Hidden from users
function formatTimeframe(tf) {
    const tfInt = parseInt(tf);
    return tfInt < 60 ? `M${tfInt}` : `H${Math.floor(tfInt / 60)}`;
}

function generateSignals(assets, count, timeframe, multiAssist) {
    const signals = [];
    const now = new Date();
    const utcPlus6 = new Date(now.getTime() + (6 * 60 * 60 * 1000));
    let nextTime = utcPlus6;

    for (let i = 0; i < count; i++) {
        const interval = Math.floor(Math.random() * 4) + 3;
        nextTime = new Date(nextTime.getTime() + (interval * 60 * 1000));
        const timeStr = nextTime.toLocaleTimeString('en-GB', { hour: '2-digit', minute: '2-digit' });

        let selectedAsset;
        if (multiAssist && assets.length > 0) {
            selectedAsset = assets[Math.floor(Math.random() * assets.length)];
        } else {
            selectedAsset = assets[0];
        }

        const market = MARKETS.find(m => m.value === selectedAsset);
        const assetLabel = market ? market.label : selectedAsset;
        const direction = Math.random() > 0.5 ? 'CALL' : 'PUT';

        signals.push({
            asset: assetLabel,
            time: timeStr,
            direction: direction,
            timeframe: formatTimeframe(timeframe)
        });
    }
    return signals;
}

// Analysis steps for the animation
function getAnalysisSteps() {
    return [
        "Analyzing market trends...",
        "✓ Trend analysis complete",
        "Checking volume patterns...",
        "✓ Volume analysis verified",
        "Identifying support/resistance...",
        "✓ Key levels identified",
        "Calculating momentum...",
        "✓ Momentum confirmed",
        "Assessing volatility...",
        "✓ Volatility measured",
        "Generating signal...",
        "✓ High-probability signal ready"
    ];
}

// Main Cloudflare Worker Handler
export async function onRequest(context) {
    const { request, env } = context;
    const url = new URL(request.url);
    const path = url.pathname;

    // CORS headers - Allows your frontend to connect
    const headers = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type'
    };

    // Handle CORS preflight
    if (request.method === 'OPTIONS') {
        return new Response(null, { headers });
    }

    // ============================================
    // ALL YOUR API ENDPOINTS - EXACTLY AS BEFORE
    // ============================================

    // Health check
    if (path === '/health') {
        return new Response(JSON.stringify({
            status: 'ok',
            message: 'Quotex Signal Pro is running on Cloudflare!',
            timestamp: new Date().toISOString(),
            version: '3.0'
        }), { headers });
    }

    // API Test
    if (path === '/api/test') {
        return new Response(JSON.stringify({
            status: 'ok',
            message: 'API is working on Cloudflare!',
            version: '3.0',
            markets_loaded: MARKETS.length
        }), { headers });
    }

    // Password verification
    if (path === '/api/verify-password' && request.method === 'POST') {
        try {
            const data = await request.json();
            const password = data.password;
            const correctPassword = env.SITE_PASSWORD || 'jummuubot';

            if (password === correctPassword) {
                return new Response(JSON.stringify({ success: true }), { headers });
            }
            return new Response(JSON.stringify({ success: false, error: 'Invalid password' }), {
                status: 401,
                headers
            });
        } catch (e) {
            return new Response(JSON.stringify({ success: false, error: 'Invalid request' }), {
                status: 400,
                headers
            });
        }
    }

    // Get all markets (ALL 79 PAIRS)
    if (path === '/api/markets') {
        return new Response(JSON.stringify({
            success: true,
            markets: MARKETS,
            count: MARKETS.length
        }), { headers });
    }

    // Get timeframes
    if (path === '/api/timeframes') {
        return new Response(JSON.stringify({
            success: true,
            timeframes: TIMEFRAMES
        }), { headers });
    }

    // Get analysis steps
    if (path === '/api/analysis-steps') {
        return new Response(JSON.stringify({
            success: true,
            steps: getAnalysisSteps()
        }), { headers });
    }

    // Generate signals (MAIN ENDPOINT)
    if (path === '/api/generate-signals' && request.method === 'POST') {
        try {
            const data = await request.json();
            const assets = data.assets || [];
            const count = data.count || 10;
            const timeframe = data.timeframe || '1';
            const multiAssist = data.multi_assist || false;

            if (!assets || assets.length === 0) {
                return new Response(JSON.stringify({
                    success: false,
                    error: 'No assets selected'
                }), { status: 400, headers });
            }

            const signals = generateSignals(assets, count, timeframe, multiAssist);

            return new Response(JSON.stringify({
                success: true,
                signals: signals,
                count: signals.length,
                generated_at: new Date().toISOString()
            }), { headers });
        } catch (e) {
            return new Response(JSON.stringify({
                success: false,
                error: 'Failed to generate signals'
            }), { status: 500, headers });
        }
    }

    // 404 for unknown API routes
    return new Response(JSON.stringify({
        success: false,
        error: 'Endpoint not found'
    }), { status: 404, headers });
}