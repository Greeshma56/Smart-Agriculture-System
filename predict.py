import pandas as pd
import pickle

model = pickle.load(open("crop_model.pkl", "rb"))

sample = pd.DataFrame(
    [[90,42,43,20.87,82,6.5,202.93]],
    columns=[
        "N",
        "P",
        "K",
        "temperature",
        "humidity",
        "ph",
        "rainfall"
    ]
)

prediction = model.predict(sample)

print("Recommended Crop:", prediction[0])
