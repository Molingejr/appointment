from twilio.rest import Client

# Credentials for twilio account
ACCOUNT_SID = "ACbb2e1d788c2f357359a6875f422e38fe"
AUTH_TOKEN = "2061c3f5e1388f8cec7cd5e02d9fa0e9"
SENDER_TEL = "+14242215553"


def send_sms(receiver, sender, message):
    """
    Send SMS from the sender to the receiver
    :param receiver: Receiver's phone number
    :param sender: Sender's phone number
    :param message: Content of the sms
    """
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    client.messages.create(
        to=receiver,
        from_=sender,
        body=message,
    )


def remind_appointment_schedule(appointment):
    """
    Provide our send message function with required arguments for sending sms
    :param appointment: Contains our current saved appointment object
    """
    send_sms(appointment.tel, SENDER_TEL, appointment.title)
