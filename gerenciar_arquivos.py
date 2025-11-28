import json
import os

base_dir = os.path.dirname(__file__)
save_to = os.path.join(base_dir, 'historico.json')

def arquivo_r():
    try:
        with open(save_to, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return None

def arquivo_w(historico):
    with open(save_to, "w", encoding="utf-8") as file:
        json.dump(historico, file, indent=2, ensure_ascii=False)