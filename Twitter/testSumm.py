import nlpcloud
token = "aae4ef3c409a35ec4ef1442d6d4cb7c0e95f777a" 
client = nlpcloud.Client("bart-large-cnn", token)

aux = client.summarization("""Chinese leader Xi Jinping was captured by Canadian broadcasters chiding Canadian Prime Minister Justin Trudeau, over what he described as "leaked" discussions. Watch here:""")

print(aux)
