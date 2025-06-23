import requests
import matplotlib.pyplot as plt
from datetime import datetime

# Configuration - Replace with your details
API_KEY = input("Enter your OpenWeatherMap API key: ")  # From OpenWeatherMap
CITIES = ["Kolkata", "Chennai", "Bangalore"]  
UNITS = "metric"  # "imperial" for Fahrenheit

def get_weather_data(city):
    """Fetch current weather and forecast for one city"""
    base_url = "http://api.openweathermap.org/data/2.5/"
    
    try:
        # Current weather
        current_url = f"{base_url}weather?q={city}&appid={API_KEY}&units={UNITS}"
        current = requests.get(current_url).json()
        
        # 5-day forecast
        forecast_url = f"{base_url}forecast?q={city}&appid={API_KEY}&units={UNITS}"
        forecast = requests.get(forecast_url).json()
        
        # Process data
        weather_info = {
            'city': city,
            'current': {
                'temp': current['main']['temp'],
                'feels_like': current['main']['feels_like'],
                'humidity': current['main']['humidity'],
                'wind': current['wind']['speed'],
                'weather': current['weather'][0]['description']
            },
            'alerts': current.get('alerts', [{'event': 'No severe weather alerts'}]),
            'forecast': []
        }
        
        # Process 5-day forecast
        daily_data = {}
        for item in forecast['list']:
            date = datetime.fromtimestamp(item['dt']).strftime('%Y-%m-%d')
            if date not in daily_data:
                daily_data[date] = {'temps': [], 'weather': []}
            daily_data[date]['temps'].append(item['main']['temp'])
            daily_data[date]['weather'].append(item['weather'][0]['main'])
        
        for date, data in daily_data.items():
            weather_info['forecast'].append({
                'date': date,
                'avg_temp': sum(data['temps'])/len(data['temps']),
                'main_weather': max(set(data['weather']), key=data['weather'].count)
            })
        
        return weather_info
    
    except Exception as e:
        print(f"Error getting data for {city}: {e}")
        return None

def display_weather(data):
    """Show weather information in console"""
    if not data:
        return
    
    print(f"\n🌆 {data['city'].upper()} 🌆")
    print(f"☀️ Current: {data['current']['weather'].title()}")
    print(f"🌡 Temp: {data['current']['temp']}°C (Feels like {data['current']['feels_like']}°C)")
    print(f"💧 Humidity: {data['current']['humidity']}%")
    print(f"🌬 Wind: {data['current']['wind']} m/s")
    
    print("\n⚠️ ALERTS:")
    for alert in data['alerts']:
        print(f"- {alert['event']}" if isinstance(alert, dict) else f"- {alert}")
    
    print("\n📅 5-DAY FORECAST:")
    for day in sorted(data['forecast'], key=lambda x: x['date'])[:5]:
        print(f"{day['date']}: {day['avg_temp']:.1f}°C, {day['main_weather']}")

def plot_weather(cities_data):
    """Create visualizations for all cities"""
    plt.figure(figsize=(15, 10))
    
    # Current temp comparison
    plt.subplot(2, 2, 1)
    cities = [data['city'] for data in cities_data]
    temps = [data['current']['temp'] for data in cities_data]
    plt.bar(cities, temps, color=['#FF9AA2', '#FFB7B2', '#FFDAC1'])
    plt.title('Current Temperature')
    plt.ylabel('°C')
    
    # Forecast trends
    plt.subplot(2, 2, 2)
    for data in cities_data:
        dates = [day['date'] for day in sorted(data['forecast'], key=lambda x: x['date'])[:5]]
        temps = [day['avg_temp'] for day in sorted(data['forecast'], key=lambda x: x['date'])[:5]]
        plt.plot(dates, temps, label=data['city'], marker='o')
    plt.title('5-Day Forecast')
    plt.ylabel('°C')
    plt.legend()
    plt.xticks(rotation=45)
    
    # Weather alerts
    plt.subplot(2, 2, 3)
    alert_counts = {}
    for data in cities_data:
        for alert in data['alerts']:
            alert_text = alert['event'] if isinstance(alert, dict) else alert
            alert_counts[alert_text] = alert_counts.get(alert_text, 0) + 1
    if alert_counts:
        plt.bar(alert_counts.keys(), alert_counts.values(), color='#FF6B6B')
        plt.title('Weather Alerts')
    else:
        plt.text(0.5, 0.5, 'No Severe Alerts', ha='center')
        plt.axis('off')
    
    # Humidity comparison
    plt.subplot(2, 2, 4)
    humidity = [data['current']['humidity'] for data in cities_data]
    plt.bar(cities, humidity, color='#45B7D1')
    plt.title('Humidity')
    plt.ylabel('%')
    
    plt.tight_layout()
    plt.savefig('weather_dashboard.png')
    plt.show()

# Main program
if __name__ == "__main__":
    print("⏳ Fetching weather data...")
    all_data = [get_weather_data(city) for city in CITIES]
    all_data = [data for data in all_data if data]
    
    for data in all_data:
        display_weather(data)
    
    if all_data:
        plot_weather(all_data)
        print("✅ Dashboard saved as 'weather_dashboard.png'")
    else:
        print("❌ Failed to get weather data")
