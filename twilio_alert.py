from twilio.rest import Client

def send_call():
    account_sid = 'YOUR_TWILIO_SID'
    auth_token = 'YOUR_TWILIO_AUTH'
    client = Client(account_sid, auth_token)

    call = client.calls.create(
        twiml='<Response><Say>Emergency! A fall was detected at home. Please respond.</Say></Response>',
        to='+YOUR_PHONE',
        from_='+YOUR_TWILIO_NUMBER'
    )

