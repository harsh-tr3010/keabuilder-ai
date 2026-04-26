from utils.helpers import load_json, save_json

def save_record(path, record):
    data = load_json(path, [])
    data.append(record)
    save_json(path, data)