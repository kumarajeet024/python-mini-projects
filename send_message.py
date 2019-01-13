from twilio.rest import Client

account_sid = "ACfa8ff1fb49a26e436c962b073870c5d5"
auth_token = "73c53f840849d8805169da397124ca95"
client = Client(account_sid, auth_token)
message = client.messages.create(
    body ="Hey there, its AJ here. How You doing",
    to ="+919795094510",
    from_="+18596970413"
)

print (message.sid)
