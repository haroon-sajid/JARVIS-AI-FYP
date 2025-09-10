import ctypes
import os
import random
import time

def change_wallpaper(image_path):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)

def get_random_image_from_folder(folder_path):
    image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    return os.path.join(folder_path, random.choice(image_files))

def change_wallpaper_once(folder_path):
    random_image = get_random_image_from_folder(folder_path)
    change_wallpaper(random_image)


# if __name__ == "__main__":
#     folder_path = "C:\\J.A.R.V.I.S_A.I\\Wallpapers"
#     change_interval = 60  

#     while True: 
#         random_image = get_random_image_from_folder(folder_path) 
#         change_wallpaper(random_image)
#         time.sleep(change_interval)


