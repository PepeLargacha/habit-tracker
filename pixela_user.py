"""handles the pixela API requests"""

from os import environ
import datetime
import requests

PIXELA_END_POINT = "https://pixe.la/v1/users"
USERNAME = environ.get('PIXELA_USERNAME')
TOKEN = environ.get('PIXELA_TOKEN')
HEADERS = {'X-USER-TOKEN': TOKEN}
graph_end_point = f"{PIXELA_END_POINT}/{USERNAME}/graphs"


def create_user():
    """create a new user on pixela"""
    user_params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }
    response = requests.post(url=PIXELA_END_POINT, json=user_params)
    print(response.text)
    return response.text


def create_graph(graph_id: str, name: str, unit: str, graph_type: str):
    """creat a new graph with the given parameters"""
    graph_parameters = {
        'id': graph_id,
        'name': name,
        'unit': unit,
        'type': graph_type,
        'color': 'momiji'
    }
    response = requests.post(url=graph_end_point, json=graph_parameters,
                             headers=HEADERS)
    print(response.text)
    return response.text


def create_pixel(graph_id: str, day: datetime.date, quantity: int):
    """create a pixel from a given date"""
    graph_pixel_end_point = f'{graph_end_point}/{graph_id}'
    add_event_params = {
        'date': day.strftime('%Y%m%d'),
        'quantity': str(quantity),
    }
    response = requests.post(url=graph_pixel_end_point, json=add_event_params,
                             headers=HEADERS)
    print(response.text)
    return response.text


def update_pixel(graph_id, day: datetime.date, quantity):
    """update a pixel from a given date"""
    day = day.strftime('%Y%m%d')
    pixel_end_point = f'{graph_end_point}/{graph_id}/{day}'
    update_pixel_params = {'quantity': str(quantity)}
    response = requests.put(url=pixel_end_point, json=update_pixel_params,
                            headers=HEADERS)
    print(response.text)
    return response.text


def delet_pixel(graph_id, day: datetime.date):
    """delete a pixel from a given graph_id and date"""
    day = day.strftime('%Y%m%d')
    pixel_end_point = f'{graph_end_point}/{graph_id}/{day}'
    response = requests.delete(url=pixel_end_point, headers=HEADERS)
    print(response.text)
    return response.text
