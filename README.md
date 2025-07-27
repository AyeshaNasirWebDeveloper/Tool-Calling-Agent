# Country Information Bot 🌍

A smart agent-powered bot that provides comprehensive country information including capitals, languages, populations, and cultural insights.

## Features ✨

- **Core Information**: Get capitals, official languages, and populations
- **Cultural Insights**: Learn about famous landmarks, traditional foods, and unique facts
- **Reliable Data**: Uses both predefined datasets and AI-generated insights
- **User-Friendly**: Simple text interface with clear formatting

## How It Works ⚙️

1. User enters a country name
2. The orchestrator agent:
   - Calls three specialized tools (capital, language, population)
   - Generates additional cultural information
   - Formats all information beautifully
3. Returns complete country profile

## Example Output 📋
┌─────────────────────────────────────┐
│ COUNTRY PROFILE                     │
├─────────────────────────────────────┤
│ Country: Italy                      │
│ Capital: Rome                       │
│ Language: Italian                   │
│ Population: 60 million              │
├─────────────────────────────────────┤
│ Must-See: Colosseum in Rome         |
│ Must-Try: Pizza Margherita - Classic│
│ tomato, mozzarella & basil          │
│ Did You Know: Italy has more UNESCO │
│ World Heritage Sites than any other │
│ country                             │
└─────────────────────────────────────┘

text

## Installation 🛠️

1. Clone the repository:
   ```bash
   git clone https://github.com/AyeshaNasirWebDeveloper/Agentic-AI-Assignment-1/country-info-bot.git
   cd country-info-bot
Set up environment:

bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
Install dependencies:

bash
Create .env file:

env
GEMINI_API_KEY=your_api_key_here
Usage 🚀
Run the bot:

bash
python main.py
Then enter country names when prompted (type 'quit' to exit).

Requirements 📦
Python 3.8+

agents framework

Google Gemini API key

Contributing 🤝
Contributions welcome! Please:

Fork the repository

Create a feature branch

Submit a pull request

License 📜
MIT License - see LICENSE for details

Made with ❤️ by [Ayesha Nasir] | https://linktr.ee/ayesha_nasir