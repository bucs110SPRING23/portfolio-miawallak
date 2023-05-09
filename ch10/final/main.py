from calendarAPI import CalendarAPI
from weatherAPI import WeatherAPI
import datetime



def main(): 
    weather_proxy = WeatherAPI(api_key="your_accuweather_api_key")
    calendar_proxy = CalendarAPI(credentials_file_path="path/to/your/credentials.json")

    calendar_id = "primary"  
    start_date = datetime.datetime(2023, 5, 9) 
    end_date = datetime.datetime(2023, 5, 19, 23, 59, 59)  

    events = calendar_proxy.get_events(calendar_id=calendar_id, time_min=start_date.isoformat(), time_max=end_date.isoformat())

    for day in range((end_date - start_date).days + 1):
        date = start_date + datetime.timedelta(days=day)
        print(f"Date: {date.strftime('%Y-%m-%d')}")
    
   
    location_key = "12345"  
    daily_forecasts = weather_proxy.get_daily_forecasts(location_key)
    forecast_date = None
    for forecast in daily_forecasts:
        forecast_date = datetime.datetime.strptime(forecast['Date'], "%Y-%m-%dT%H:%M:%S%z").date()
        if forecast_date == date.date():
            print(f"Weather forecast: {forecast['Day']['IconPhrase']}")
            break
    else:
        print("None")