import json
from pathlib import Path


with open("data/crab/transforms.json") as f:
    data = json.load(f)

base = {"camera_angle_x": data["camera_angle_x"]}
train = {"frames": data["frames"][0:][::3], "camera_angle_x": data["camera_angle_x"]}
val = {"frames": data["frames"][1:][::3], "camera_angle_x": data["camera_angle_x"]}
test = {"frames": data["frames"][2:][::3], "camera_angle_x": data["camera_angle_x"]}

with open("data/crab/transforms_train.json", "w") as f:
    json.dump(train, f, indent=4)

with open("data/crab/transforms_val.json", "w") as f:
    json.dump(val, f, indent=4)

with open("data/crab/transforms_test.json", "w") as f:
    json.dump(test, f, indent=4)
