import json
from core import separator_decorator


@separator_decorator("Ejemplo IA Bloque 16")
def run_example():
    print("Este ejemplo escribe y lee archivos de texto y JSON.")

    text_path = "ia/data/ia_example.txt"
    json_path = "ia/data/ia_example.json"

    with open(text_path, "w", encoding="utf-8") as file:
        file.write("Ejemplo IA de archivo de texto\n")

    with open(text_path, "r", encoding="utf-8") as file:
        print("Contenido del archivo de texto:")
        print(file.read())

    data = {"nombre": "Carlos", "edad": 30}
    with open(json_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

    with open(json_path, "r", encoding="utf-8") as file:
        loaded = json.load(file)
        print("Contenido del archivo JSON:")
        print(loaded)
