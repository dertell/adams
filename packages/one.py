import boto3
import json
from botocore.exceptions import ClientError

region = "us-east-1"
session = boto3.Session(region_name=region, profile_name="one")
client = session.client('bedrock-runtime')

#"anthropic.claude-3-sonnet-20240229-v1:0"
#"anthropic.claude-3-haiku-20240307-v1:0"
def streaming(b):
    prompt = createPrompt(b)
    try:
        response = client.invoke_model_with_response_stream(
        body= prompt,
        modelId="anthropic.claude-3-sonnet-20240229-v1:0",
        trace='ENABLED')
    except ClientError as e:
        yield json.dumps({"error": e})
        return

    res = ""
    for i in response["body"]:
        q = json.loads(i["chunk"]["bytes"].decode("utf-8"))
        if q["type"] == "content_block_delta":
            res += q["delta"]["text"]
            yield q["delta"]["text"]
        if q["type"] == "content_block_stop":
            yield "\n"
        if q["type"] == "message_stop":
            # save response
            print(res)

def createPrompt(b):
    messages = []
    messages.append({
            "role": "user",
            "content": [
                { "type": "text", "text": f"Write a poem about {b} please" }
      ]
        })
    return json.dumps({
    "anthropic_version": "bedrock-2023-05-31",    
    "max_tokens": 200,
    "system": "You are a pirate and you need to talk like one",    
    "messages": messages,
    "temperature": 1,
    "top_k": 10,
})

def getChatHistory():
    pass
    #todo

def saveChatHistory():
    pass
    ##todo

def retrieveDocs():
    pass 