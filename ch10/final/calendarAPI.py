import build
import service_account

class CalendarAPI:
    SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
    SERVICE_ACCOUNT_FILE = 'your-service-account-file.json'
    creds = None
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)


    def __init__(self):
        self.url = "https://www.googleapis.com/calendar/v3/calendars/calendarId"
       
       
    def get_events(self, calendar_id, time_min, time_max):
        creds = service_account.Credentials.from_service_account_file(self.credentials_file_path, scopes=['https://www.googleapis.com/auth/calendar'])
        service = build('calendar', 'v3', credentials=creds)
        events_result = service.events().list(calendarId=calendar_id, timeMin=time_min, timeMax=time_max, singleEvents=True, orderBy='startTime').execute()
        events = events_result.get('items', [])
        return events