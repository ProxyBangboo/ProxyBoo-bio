from twilio.rest import Client
import random

# Twilio credentials
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token'
twilio_phone_number = '+1234567890'

client = Client(account_sid, auth_token)

def generate_otp(length=6):
    """Generate a random OTP"""
    otp = ''.join([str(random.randint(0, 9)) for i in range(length)])
    return otp

def send_otp_via_sms(to_phone_number):
    """Send OTP to a specified phone number"""
    otp = generate_otp()
    message = client.messages.create(
        body=f"Your OTP code is {otp}",
        from_=twilio_phone_number,
        to=to_phone_number
    )
    print(f"Sent OTP {otp} to {to_phone_number}")
    return otp

# Example usage
if __name__ == "__main__":
    recipient_phone_number = '+0987654321'  # Replace with the recipient's phone number
    otp = send_otp_via_sms(recipient_phone_number)
    print(f"OTP sent: {otp}")
