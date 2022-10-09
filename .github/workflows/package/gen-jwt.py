# -*- coding: utf-8 -*-
import hmac
import hashlib
import jwt
import base64
import json 
import datetime

consumer_key = '3MVG9dZJodJWITSsG.BrFRTEjksR1pjSwekGx1.Mnqx.t8XPdk4wvPbCoJyXAsJwlIHoRuEiWxcr0JVMpDPJz'

def create_jwt(payload):
    print("entrou")
    payload = json.dumps(payload).encode('utf-8')
    header = json.dumps({
        'alg': 'RS256'
    }).encode()
    b64_header = base64.urlsafe_b64encode(header).decode()
    b64_payload = base64.urlsafe_b64encode(payload).decode()
    signature = hmac.new(
        key=consumer_key.encode(),
        msg=f'{b64_header}.{b64_payload}'.encode(),
        digestmod=hashlib.sha256
    ).digest()
    jwt = f'{b64_header}.{b64_payload}.{base64.urlsafe_b64encode(signature).decode()}'
    print(jwt)
    return jwt

# def verify_and_decode_jwt(jwt):
#     b64_header, b64_payload, b64_signature = jwt.split('.')
#     b64_signature_checker = base64.urlsafe_b64encode(
#         hmac.new(
#             key=consumer_key.encode(),
#             msg=f'{b64_header}.{b64_payload}'.encode('utf-8'),
#             digestmod=hashlib.sha256
#         ).digest()
#     ).decode()

#     # payload extraido antes para checar o campo 'exp'
#     payload = json.loads(base64.urlsafe_b64decode(b64_payload))
#     unix_time_now = datetime.datetime.now().timestamp()

#     if payload.get('exp') and payload['exp'] < unix_time_now:
#         raise Exception('Token expirado')
    
#     if b64_signature_checker != b64_signature:
#         raise Exception('Assinatura inválida')
    
    
#     return payload 

if __name__ == '__main__':
    payload = {
        'iss': '3MVG9dZJodJWITSsG.BrFRTEjksR1pjSwekGx1.Mnqx.t8XPdk4wvPbCoJyXAsJwlIHoRuEiWxcr0JVMpDPJz', 
        'sub': 'emily.berteloni@companyteste1.com', 
        'aud': 'https://login.salesforce.com', 
        'exp': (datetime.datetime.now() + datetime.timedelta(minutes=500)).timestamp(),
    }
    
    # f = open("server.key", "r")   
    # print(payload)
    # print(jwt )
    # print(jwt.encode(payload, f.read(),algorithm="RS256"))
