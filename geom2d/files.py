import json

with open("/home/musicmtr/PycharmProjects/kursBARANCEV/geom2d/config.json") as f:
    try:
        res = json.load(f)
    except ValueError as ex:
        print(ex)
        res = {}

print(res)