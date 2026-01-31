# Daily Crypto Report Generator
# Sends top trending tokens report via Telegram at 8 AM

$env:OPENROUTER_API_KEY = "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"

# Your Telegram User ID (get this from @userinfobot on Telegram)
$TELEGRAM_USER_ID = "7607491409"  # Your user ID from earlier pairing

$MESSAGE = @"
🌅 **DAILY CRYPTO REPORT** - $(Get-Date -Format 'MMMM dd, yyyy')

🔍 **Top Trending Memecoins Today**

Please analyze the following and provide me with:
1. Top 5 trending memecoins under \$5M market cap
2. Highest volume coins in the last 24h
3. New launches with strong social presence
4. Any smart money movements detected

Focus on Solana and Ethereum chains. Include risk scores and entry timing recommendations.

📊 Sort by: Volume/MCap ratio and holder growth
⚠️ Exclude: Known scams and rugs
✅ Prioritize: Locked liquidity + doxxed teams

Let's find the next 100x! 🚀
"@

Write-Host "Sending daily crypto report at $(Get-Date)" -ForegroundColor Cyan

# Send message via clawdbot
try {
    $result = clawdbot message send --channel telegram --target $TELEGRAM_USER_ID --message $MESSAGE --json 2>&1
    Write-Host "✅ Daily report sent successfully!" -ForegroundColor Green
    Write-Host $result
} catch {
    Write-Host "❌ Failed to send report: $_" -ForegroundColor Red
}
