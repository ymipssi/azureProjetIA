import os
import random
from matplotlib.pyplot import imread
import json
import operator
import requests

url = ''
api_keys = ''
headers={'content-type':'application/octet-stream','Prediction-Key':api_keys}

def open_waste_slot():

    """
        open the machine so that
        an user can enter the machine

    :return:
    """

    send_command_to_machine("open_waste_slot")
    return True


def close_waste_slot():
    """
    close the waste box for user safety
    :return:
    """

    send_command_to_machine("close_waste_slot")
    return True


def process_waste(waste_type):

    """
    move the good slot and shredd the waste
    :return:
    """

    move_container(waste_type)
    was_sucessful = shred_waste()

    return was_sucessful


def move_container(waste_type):

    BOTTLE_BOX = 0
    GLASS_BOX = 1
    command_name = "move_container"

    if waste_type == "bottle":
        send_command_to_machine(command_name, BOTTLE_BOX)
    elif waste_type == "glass":
        send_command_to_machine(command_name, GLASS_BOX)

    return True


def send_command_to_machine(command_name, value=None):

    """
    simulate command sending to rasberry pi
    do nothing to work even if the machine is not connected

    :param command_name:
    :param value:
    :return:
    """
    return True



def shred_waste():

    send_command_to_machine("shred_waste")

    return True


def take_trash_picture():

    """
        Call this function to ask the machine to
        take picutre of the trash

        return : np array of the picture
    """

    send_command_to_machine("take_picture")

    paths = os.listdir('camera')
    path = random.choice(paths)

    return open("camera/"+path,"rb")

def pred_func(data):
    print(data)
    r =requests.post(url,data=data,headers=headers).content
    pred = {x["tagName"]:x["probability"]  for x in json.loads(r)["predictions"]}
    return max(pred.items(), key=operator.itemgetter(1))[0]
