import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Formi Chatbot Logs").sheet1

def log_data(data):
    sheet.append_row([
        data['modality'], data['time'], data['phone'], data['outcome'],
        data['room'], data['booking_date'], data['booking_time'],
        data['guests'], data['summary']
    ])
