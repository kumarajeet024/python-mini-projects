from twilio.rest import Client

account_sid = "your sid"
auth_token = "your token"
client = Client(account_sid, auth_token)
message = client.messages.create(
    body ="Hey there, its AJ here. How You doing",
    to ="+919795094510",
    from_="+18596970413"
)

print (message.sid)
