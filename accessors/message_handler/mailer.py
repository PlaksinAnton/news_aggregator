import os.path
import base64
from email.mime.text import MIMEText
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from email.mime.multipart import MIMEMultipart

SCOPES = ["https://www.googleapis.com/auth/gmail.send"]

def authenticate_gmail():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
        print(creds)
        print('---------------------------------------------')
        print(creds.valid)
    # If no valid credentials, initiate the OAuth flow
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return build("gmail", "v1", credentials=creds)

def create_message(sender, to, subject, html_body):
    message = MIMEMultipart("alternative")
    message["to"] = to
    message["from"] = sender
    message["subject"] = subject
    message.attach(MIMEText(html_body, "html"))
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {"raw": raw}

def send_email(service, sender, to, subject, body):
    try:
        html_body = add_html_headers(body)
        message = create_message(sender, to, subject, html_body)
        service.users().messages().send(userId="me", body=message).execute()
    except HttpError as error:
        print(f"An error occurred: {error}")

def add_html_headers(body):
    html_body = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Latest News</title>
    </head>
    <body>
        {body}
    </body>
    </html>
    """
    return html_body
    

def main():
    try:
        service = authenticate_gmail()
        sender = "aplaksin691@gmail.com"
        recipient = "aplaksin2000@gmail.com"
        subject = "Hello from Gmail API"
        body = "This is a test email sent using the Gmail API."
        send_email(service, sender, recipient, subject, body)
    except HttpError as error:
        print(f"An error occurred: {error}")


if __name__ == "__main__":
    main()
