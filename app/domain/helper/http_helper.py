import http.client
import json

def request(domain: str, path: str, method: str, request_data = None) -> dict:
    conn = http.client.HTTPConnection(domain)
    headers = {'content-type': 'application/json'}
    body = json.dumps(request_data) if request_data is dict else None
    
    conn.request(method.upper(), path, headers=headers, body=body)
    response = conn.getresponse()
    if response.status == 302:
        # HTTPSにリダイレクト
        conn = http.client.HTTPSConnection(domain)
        conn.request(method.upper(), path, headers=headers, body=body)
        response = conn.getresponse()
        data = json.loads(response.read())
    else:
        data = json.loads(response.read())
    
    conn.close()
    return data