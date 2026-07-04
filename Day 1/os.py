import os

path = r"F:\Pandas 30 DAYS"
for i in range(1, 31):
    foldername = f"Day {i}"
    folderpath = os.path.join(path, foldername)
    os.makedirs(folderpath, exist_ok=True)