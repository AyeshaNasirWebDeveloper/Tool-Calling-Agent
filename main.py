import os
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, function_tool
from typing import Optional
from agents.run import RunConfig
from dotenv import load_dotenv

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client,
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# Tools
@function_tool
def get_capital(country: str) -> str:
    """Returns the capital of the given country (case-insensitive)"""
    country = country.lower().strip()
    capitals = {
        "france": "Paris",
        "germany": "Berlin",
        "japan": "Tokyo",
        "brazil": "Brasília",
        "egypt": "Cairo",
        "pakistan": "Islamabad",
        "india": "New Delhi",
        "united states": "Washington, D.C.",
        "canada": "Ottawa",
        "australia": "Canberra",
        "united kingdom": "London",
        "china": "Beijing",
        "russia": "Moscow",
        "south africa": "Pretoria",
        "mexico": "Mexico City",
        "italy": "Rome",
        "spain": "Madrid",
        "south korea": "Seoul",
        "turkey": "Ankara",
        "argentina": "Buenos Aires",
        "indonesia": "Jakarta",
        "nigeria": "Abuja",
        "philippines": "Manila",
        "vietnam": "Hanoi",
        "thailand": "Bangkok",
        "saudi arabia": "Riyadh",
        "netherlands": "Amsterdam",
        "sweden": "Stockholm",
        "norway": "Oslo",
        "finland": "Helsinki",
        "poland": "Warsaw",
        "ukraine": "Kyiv",
        "belgium": "Brussels",
        "switzerland": "Bern",
        "austria": "Vienna",
        "denmark": "Copenhagen",
        "portugal": "Lisbon",
        "greece": "Athens",
        "czech republic": "Prague",
        "hungary": "Budapest",
        "ireland": "Dublin"
    }
    return capitals.get(country, "Capital not found")

@function_tool
def get_language(country: str) -> str:
    """Returns the primary language(s) of the given country (case-insensitive)"""
    country = country.lower().strip()
    languages = {
        "france": "French",
        "germany": "German",
        "japan": "Japanese",
        "brazil": "Portuguese",
        "egypt": "Arabic",
        "pakistan": "Urdu",
        "india": "Hindi, English",
        "united states": "English",
        "canada": "English, French",
        "australia": "English",
        "united kingdom": "English",
        "china": "Mandarin",
        "russia": "Russian",
        "mexico": "Spanish",
        "italy": "Italian",
        "spain": "Spanish",
        "south korea": "Korean",
        "turkey": "Turkish",
        "argentina": "Spanish",
        "indonesia": "Indonesian",
        "nigeria": "English",
        "philippines": "Filipino, English",
        "vietnam": "Vietnamese",
        "thailand": "Thai",
        "saudi arabia": "Arabic",
        "netherlands": "Dutch",
        "sweden": "Swedish",
        "norway": "Norwegian",
        "finland": "Finnish, Swedish",
        "poland": "Polish",
        "ukraine": "Ukrainian",
        "belgium": "Dutch, French, German",
        "switzerland": "German, French, Italian, Romansh",
        "austria": "German",
        "denmark": "Danish",
        "portugal": "Portuguese",
        "greece": "Greek",
        "czech republic": "Czech",
        "hungary": "Hungarian",
        "ireland": "Irish, English"
    }
    return languages.get(country, "Language not found")

@function_tool
def get_population(country: str) -> str:
    """Returns the approximate population of the given country (case-insensitive)"""
    country = country.lower().strip()
    populations = {
        "france": "68 million",
        "germany": "83 million",
        "japan": "125 million",
        "brazil": "213 million",
        "egypt": "109 million",
        "pakistan": "240 million",
        "india": "1.4 billion",
        "united states": "331 million",
        "canada": "38 million",
        "australia": "26 million",
        "united kingdom": "67 million",
        "china": "1.4 billion",
        "russia": "146 million",
        "south africa": "60 million",
        "mexico": "126 million",
        "italy": "60 million",
        "spain": "47 million",
        "south korea": "52 million",
        "turkey": "85 million",
        "argentina": "45 million",
        "indonesia": "276 million",
        "nigeria": "223 million",
        "philippines": "113 million",
        "vietnam": "98 million",
        "thailand": "70 million",
        "saudi arabia": "35 million",
        "netherlands": "17 million",
        "sweden": "10 million",
        "norway": "5 million",
        "finland": "5.5 million",
        "poland": "38 million",
        "ukraine": "41 million",
        "belgium": "11 million",
        "switzerland": "8.5 million",
        "austria": "9 million",
        "denmark": "5.8 million",
        "portugal": "10 million",
        "greece": "10 million",
        "czech republic": "10.5 million",
        "hungary": "9.6 million",
        "ireland": "5 million"
    }
    return populations.get(country, "Population data not available")

# Agent
orchestrator = Agent(
    name="CountryInfoOrchestrator",
    instructions="""You are a world-class country information expert. When given a country name, follow these steps EXACTLY:

1. FIRST use these tools in order:
   - get_capital (for capital city)
   - get_language (for official language)
   - get_population (for current population)

2. THEN generate additional interesting information including:
   - 1 famous tourist attraction (must be specific)
   - 1 traditional dish (with brief description)
   - 1 cultural fact (unique to this country)

3. FINALLY format the complete response as follows:
   ┌──────────────────────────────────────┐
   │           COUNTRY PROFILE            │
   ├──────────────────────────────────────┤
   │ Country: [Name]                      │
   │ Capital: [City]                      │
   │ Language: [Language]                 │
   │ Population: [Number]                 │
   ├──────────────────────────────────────┤
   │ Must-See: [Attraction]               │
   │ Must-Try: [Dish] - [Brief description]│
   │ Did You Know: [Cultural fact]        │
   └──────────────────────────────────────┘

Important Rules:
- Always call all three tools first
- Never say "sorry" or "unfortunately"
- If data is missing, say "Not available"
- Keep additional facts concise and accurate
- Make the information engaging and interesting""",
    tools=[get_capital, get_language, get_population],
    model=model
)

def get_country_info():
    print("Country Information Bot (type 'quit' to exit)")
    while True:
        try:
            country = input("\nEnter a country name: ").strip()
            if country.lower() == 'quit':
                break
                
            if not country:
                print("Please enter a country name")
                continue
                
            result = Runner.run_sync(
                orchestrator,
                f"Get complete information for: {country}",
                run_config=config
            )
            
            print(f"\n{result.final_output}")
            
        except Exception as e:
            print(f"\nError: {str(e)}")
            print("Please try another Country")

if __name__ == "__main__":
    get_country_info()