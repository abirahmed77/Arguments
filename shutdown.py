import os

shutdown = input("Do you wish to shutdown your computer? (YES OR NO): ")

if shutdown=='NO':
    exit()
    
else:
    os.system("shutdown /s /t 1")