# Author: Heitor Foschiani de Souza
# Email: heitor.foschiani@outlook.com
# Number: (11) 9 4825-3334

# Libraries
import requests
import json

def get_api_url():
    api_url = 'http://127.0.0.1:5001'
    return api_url


api_url = get_api_url()

def register_user(full_name, email, phone, username, password):
    # requesting API
    response = requests.post(
        f'{api_url}/user',
        headers = {'Content-type': 'application/json'},
        json = {
            'full_name': full_name,
            'email': email,
            'phone': phone,
            'username': username,
            'password': password,
        },
    )

    return response

def get_authenticated_user_infos(access_token):
    # requesting API
    response = requests.get(
        f'{api_url}/user',
        headers = {'Authorization': f'Bearer {access_token}'},
    )
    
    return response

def get_user_infos_by_userid(user_id, access_token):
    # requesting API
    response = requests.get(
        f'{api_url}/user/{user_id}',
        headers = {'Authorization': f'Bearer {access_token}'},
    )

    # getting user informations
    if response.status_code == 200:
        js = response.json()
        
        user_id = int(js[0]['user_id'])
        full_name = js[0]['full_name']
        email = js[0]['email']
        phone = js[0]['phone']
        username = js[0]['username']

        return user_id, full_name, email, phone, username
    else:
        print(response.status_code)

def authenticate_user(username, password):
    # requesting API
    response = requests.post(
        f'{api_url}/user/authenticate',
        headers = {'Content-type': 'application/json'},
        json = {
            'username': username,
            'password': password,
        },
    )

    return response

def refresh_authentication(refresh_token):
    # requesting API
    response = requests.post(
        f'{api_url}/user/refresh-authentication',
        headers={'Authorization': f'Bearer {refresh_token}'},
    )

    return response