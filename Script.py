import json
import zipfile
import uuid
import sys

def uuid_str():
    return str(uuid.uuid4())

project = {
    "targets": [
        {
            "id": uuid_str(),
            "isStage": True,
            "name": "Stage",
            "variables": {},
            "lists": {},
            "broadcasts": {},
            "blocks": {},
            "comments": {},
            "currentCostume": 0,
            "costumes": [],
            "sounds": [],
            "volume": 100,
            "layerOrder": 0,
            "tempo": 60,
            "videoTransparency": 50,
            "videoState": "on",
            "textToSpeechLanguage": None
        },
        {
            "id": uuid_str(),
            "isStage": False,
            "name": "CubeDrawer",
            "variables": {},
            "lists": {},
            "broadcasts": {},
            "blocks": {},
            "comments": {},
            "currentCostume": 0,
            "costumes": [],
            "sounds": [],
            "volume": 100,
            "layerOrder": 1,
            "visible": True,
            "x": 0,
            "y": 0,
            "size": 30,
            "direction": 90,
            "draggable": False,
            "rotationStyle": "all around"
        }
    ],
    "meta": {
        "semver": "3.0.0",
        "vm": "0.2.0",
        "agent": "custom"
    },
    "extensions": ["pen"]
}

def build_sb3(project_obj, out_name="GameCube_Intro.sb3"):
    try:
        # Serialisiere sauber als UTF-8-Bytes und validiere
        json_bytes = json.dumps(project_obj, ensure_ascii=False, indent=2).encode("utf-8")
        json.loads(json_bytes.decode("utf-8"))  # einfache Validierung

        # Schreibe ZIP (SB3)
        with zipfile.ZipFile(out_name, "w", compression=zipfile.ZIP_DEFLATED) as zf:
            zf.writestr("project.json", json_bytes)

        # Zur Kontrolle: zeige Anfang von project.json
        print("---- project.json (erste 300 Zeichen) ----")
        print(json_bytes.decode("utf-8")[:300])
        print("---- Ende Vorschau ----")
    except Exception as e:
        print("Fehler beim Erstellen der SB3:", e, file=sys.stderr)
        return False
    return True

if __name__ == "__main__":
    ok = build_sb3(project)
    if ok:
        print("Fertig! GameCube_Intro.sb3 wurde erstellt.")
    else:
        print("Erstellung fehlgeschlagen.", file=sys.stderr)
