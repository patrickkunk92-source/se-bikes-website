# Crypto Memecoin Hunter Workspace

This is the dedicated workspace for the **crypto-hunter** AI agent specialized in memecoin research and analysis.

## Quick Start

### Talk to Crypto Hunter on Telegram

Send messages to @GROKANABOT that contain crypto-related keywords:
- "crypto"
- "memecoin"
- "token"
- "coin"
- "100x"
- "moon"

The crypto-hunter agent will automatically respond to these messages!

### Manual Switch

You can also manually specify which agent to use:
```
@crypto-hunter what are the hottest memecoins right now?
```

## Tools Available

### 1. DexScreener API (`dexscreener-api.py`)
Real-time trading data and analytics:
```bash
python dexscreener-api.py <contract_address_or_name>
```

### 2. Twitter Scraper (`twitter-scraper.py`)
Monitor crypto Twitter for trending coins:
```bash
python twitter-scraper.py "memecoin"
```

## Research Workflow

1. **Discovery**: Ask agent to search for trending memecoins
2. **Analysis**: Agent will fetch on-chain data and social metrics
3. **Evaluation**: Get risk scores and potential ratings
4. **Tracking**: Monitor selected coins for entry opportunities

## Example Commands

Send these to the crypto-hunter agent:

- "Find me the hottest memecoins on Solana right now"
- "Analyze this contract: [address]"
- "What are the trending coins on Twitter today?"
- "Show me coins with <$1M market cap and high volume"
- "Check if [token] is a rug pull"

## Agent Capabilities

✅ Web scraping (Twitter, Reddit, Telegram)
✅ On-chain analysis via DexScreener
✅ Risk assessment and scoring
✅ Sentiment analysis
✅ Data visualization
✅ Report generation

## Important Notes

⚠️ **RISK WARNING**: Memecoins are extremely high-risk investments
⚠️ **NOT FINANCIAL ADVICE**: This is research assistance only
⚠️ **DYOR**: Always do your own research before investing

## Agent Info

- **Model**: DeepSeek Chat (good for research and analysis)
- **Workspace**: `C:\Users\patri\clawd\crypto-research`
- **System Prompt**: Specialized for crypto memecoin research
- **Auto-routing**: Responds to crypto-related messages on Telegram
