import os
import pandas as pd

schema = {
    'seconds': float, 
    'frontal_acceleration': float, 
    'vertical_acceleration': float, 
    'lateral_acceleration': float, 
    'antenna_id': int, 
    'signal_strength': float,
    'phase': float,
    'frequency': float,
    'label': float,
    }

patient_list = []
patient_folder = 'data/S1_Dataset/'

for filename in os.listdir(patient_folder):
    if filename != 'README.txt':
        filepath = os.path.join(patient_folder, filename)
        df = pd.read_csv(filepath, names=list(schema.keys()), dtype=schema)
        patient_list.append(df)

print(f"Patients length: {len(patient_list)}")
print(f"Patients dataset row length: {[df.shape[0] for df in patient_list]}")
