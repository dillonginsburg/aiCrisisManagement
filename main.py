import requests
from bs4 import BeautifulSoup
import tkinter as tk
from user_interface_module import UserInterface

# Define test scenarios
test_scenarios = [
    {"weather": {"temperature": 25, "humidity": 70}, "news": {"headline": "Heatwave Warning"}},
    {"weather": {"temperature": 10, "humidity": 50}, "news": {"headline": "Climate Agreement Signed"}},
    # Add more test scenarios as needed
]

class DataIntegrator:
    def fetch_live_weather_data_simulated(self):
        # Simulate fetching live weather data
        weather_data = {
            "temperature": 25,
            "humidity": 70
        }
        return weather_data

    def fetch_live_weather_data(self):
        # Fetch live weather data from the weather API
        weather_api_url = "https://api.weatherapi.com/v1/current.json"
        api_key = "9b93b2e7f5a818f063c989011590687d"  # Replace with your actual API key
        location = "New York"     # Replace with the desired location

        # Set up request parameters
        params = {
            "key": api_key,
            "q": location,
            "aqi": "no"
        }

        # Make an HTTP GET request to the weather API
        response = requests.get(weather_api_url, params=params)

        if response.status_code == 200:
            # Parse the API response
            weather_data = response.json()
            temperature = weather_data["current"]["temp_c"]
            humidity = weather_data["current"]["humidity"]

            return {"temperature": temperature, "humidity": humidity}
        else:
            return {"temperature": None, "humidity": None}

    def fetch_live_news_data(self):
        # Fetch live news data using web scraping from Reddit r/worldnews
        reddit_url = "https://www.reddit.com/r/worldnews/"  # URL of r/worldnews subreddit

        # Set user agent to avoid Reddit's bot detection
        headers = {"User-Agent": "Your User Agent Here"}

        # Make an HTTP GET request to the Reddit page
        response = requests.get(reddit_url, headers=headers)

        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.content, "html.parser")

            # Find news headlines using appropriate HTML tags and classes
            news_headlines = soup.find_all("h3", class_="_eYtD2XCVieq6emjKBH3m")

            # Extract and store the news headlines
            headlines = [headline.get_text() for headline in news_headlines]

            return {"headlines": headlines}
        else:
            return {"headlines": []}

class DecisionMaker:
    def make_decision(self, weather_data, news_data):
        # Simulate AI decision-making based on weather and news data
        # You can implement your decision-making logic here
        decision = "alert_heatwave"  # Replace with actual decision logic
        return decision

class ActionExecutor:
    def execute_actions(self, decision):
        # Simulate action execution based on AI decision
        action_results = {}  # Placeholder for simulated action results
        
        if decision == "alert_heatwave":
            action_results["heatwave_alert"] = "Heatwave alert issued."
        elif decision == "news_climate_agreement":
            action_results["news_announcement"] = "Climate agreement news announced."
        else:
            action_results["default_action"] = "No specific action taken."
        
        return action_results

class UserInterface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("AI Decision Interface")

        self.output_text = tk.Text(self.root, wrap=tk.WORD)
        self.output_text.pack()

    def display_decision(self, decision, action_results):
        # Display AI's decisions and actions on the interface
        self.output_text.insert(tk.END, f"AI Decision: {decision}\n")
        self.output_text.insert(tk.END, f"Action Results: {action_results}\n")
        self.output_text.insert(tk.END, "=" * 40 + "\n")

    def run(self):
        self.root.mainloop()

# Main function
def main():
    data_integrator = DataIntegrator()
    decision_maker = DecisionMaker()
    action_executor = ActionExecutor()
    user_interface = UserInterface()

    for scenario in test_scenarios:
        live_weather_data = data_integrator.fetch_live_weather_data_simulated()
        live_news_data = data_integrator.fetch_live_news_data()

        decision = decision_maker.make_decision(live_weather_data, live_news_data)

        action_results = action_executor.execute_actions(decision)

        user_interface.display_decision(decision, action_results)

        print("=" * 40)

    user_interface.run()  # Start the GUI main loop

if __name__ == "__main__":
    main()
