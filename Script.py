import json, zipfile, io

project = {
    "targets": [
        {
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

with zipfile.ZipFile("GameCube_Intro.sb3", "w") as zf:
    zf.writestr("project.json", json.dumps(project))

print("Fertig! GameCube_Intro.sb3 wurde erstellt.")
