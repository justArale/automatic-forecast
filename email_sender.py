import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import EMAIL_FROM, APP_PASSWORD

def send_forecast_email(forecast, location, mail_to):
    # Create E-Mail
    msg = MIMEMultipart()
    msg['From'] = EMAIL_FROM
    msg['To'] = mail_to
    msg['Subject'] = f'14-Tage Wettervorhersage für {location}'
    
    body = f"Wettervorhersage für {location}:\n\n{forecast}"
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        # Get SMTP connection and send E-Mail
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # TLS-key
            server.login(EMAIL_FROM, APP_PASSWORD)  # Login with EMAIL_FROM and APP_PASSWORD
            server.send_message(msg)  # Send E-Mail
        print("E-Mail wurde erfolgreich gesendet.")
    
    except smtplib.SMTPAuthenticationError:
        print("Authentifizierungsfehler: Überprüfe deine E-Mail-Adresse und das App-Passwort.")
    
    except smtplib.SMTPException as e:
        print(f"Fehler beim Senden der E-Mail: {e}")

