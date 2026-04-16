import json

def load_graph():
    try:
        with open("data/campus_map.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_graph(graph):
    with open("data/campus_map.json", "w") as f:
        json.dump(graph, f, indent=4)