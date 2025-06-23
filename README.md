# API-INTEGRATION-AND-DATA-VISUALIZATION

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: SHARON MAKHROH KHARLYNGDOH

*INTERN ID*: CT04DN1345

*DOMAIN*: PYTHON PROGRAMMING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

*DESCRIPTION*: This Weather Dashboard is a Python application that fetches real-time weather data for multiple cities, displays current conditions, 5-day forecasts, and weather alerts in an easy-to-understand visual format. Designed for both beginners and experienced developers, it demonstrates practical API usage, data visualization, and secure coding practices.

Weather affects our daily lives - from planning outdoor activities to making travel decisions. This project solves the problem of checking multiple weather sources by providing:
- Consolidated weather data for multiple locations
- Visual comparisons between cities
- Early warnings for severe weather
- Future forecasts to help with planning

*IMPLEMENTATION DETAILS:*

1. Data Collection
The app uses OpenWeatherMap's API to fetch:
- Current weather (temperature, humidity, wind speed)
- 5-day forecasts (3-hour intervals)
- Weather alerts (storms, extreme temperatures)

Technical Implementation:
- We send HTTP requests using Python's requests library
- The API returns JSON data which we parse into Python dictionaries
- We process this raw data to extract only what we neeD

2. Data Processing
The raw weather data gets transformed into user-friendly formats:
- Temperature units converted to Celsius/Fahrenheit
- Forecast data averaged into daily summaries
- Alerts are categorized and prioritized

3. Visualization
We create four interactive charts using matplotlib:
 1. Current Conditions Comparison - Bar chart showing temperatures across cities
 2. 5-Day Forecast Trend - Line graph of predicted temperatures
 3. Weather Alerts - Visual warning display
 4. Humidity Comparison - Side-by-side moisture levels

*KEY FEATURES:*

1. Multi-City Support
   - Compare weather across different locations
   - Easily add/remove cities by editing a list
2. Comprehensive Forecasts
   - See temperature trends over 5 days
   - Identify predominant weather conditions
3. Alert System
   - Visual warnings for severe weather
   - Color-coded for quick recognition
4. User-Friendly Output
   - Clean console display
   - Professional-quality charts
   - Automatic image saving

*LEARNING OUTCOMES:*

1. API integration skills - Working with real-world data sources
2. Data processing experience - Cleaning and transforming raw data
3. Visualization techniques - Creating meaningful charts
4. Security awareness - Protecting sensitive credentials
5. Error handling - Managing API failures gracefully

*OUTPUT:*

![Image](https://github.com/user-attachments/assets/b5af6824-d4b8-42bb-b36a-c0eba1df78ee)
