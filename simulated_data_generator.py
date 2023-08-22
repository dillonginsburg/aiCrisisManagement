# simulated_data_generator.py

import random

class SimulatedDataGenerator:
    def generate_weather_data(self):
        # Generate simulated weather data (temperature, humidity, etc.)
        weather_data = {
            "temperature": random.uniform(-10, 35),  # Simulated temperature in Celsius
            "humidity": random.uniform(30, 90),      # Simulated humidity in percentage
            # Add more simulated weather attributes as needed
        }
        return weather_data
    
    def generate_news_data(self):
        # Generate simulated news data
        news_data = {
            "headline": "Simulated News Headline",
            "content": "This is a simulated news article about climate change.",
            # Add more simulated news attributes as needed
        }
        return news_data
