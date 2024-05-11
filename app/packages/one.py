import boto3
import json

region = "us-west-2"
session = boto3.Session(region_name=region)
client = session.client('bedrock-runtime')


def streaming(b):
    prompt = createPrompt(b)
    response = client.invoke_model_with_response_stream(
        body= prompt,
        modelId="anthropic.claude-3-haiku-20240307-v1:0",
        trace='ENABLED')
    for i in response["body"]:
        q = json.loads(i["chunk"]["bytes"].decode("utf-8"))
        print(q)
        if q["type"] == "content_block_delta":
            yield q["delta"]["text"]
        if q["type"] == "content_block_stop":
            yield "\n"
        if q["type"] == "message_stop":
            print(response)

def createPrompt(b):
    messages = []
    messages.append({
            "role": "user",
            "content": [
                { "type": "text", "text": f"Tell me a joke about {b} please" }
      ]
        })
    return json.dumps({
    "anthropic_version": "bedrock-2023-05-31",    
    "max_tokens": 100,
    "system": "You are a pirate",    
    "messages": messages,
    "temperature": 1,
    "top_k": 10,
})