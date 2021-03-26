#----------Automatic arduino bootloader------
#-------------------WikumJCK-----------------


#To get positions of the button run this code only
#
import pyautogui #importing pyautogui library

BootLoadedICs = 1 #Variable to store Bootloaded ICs

while True:
    pyautogui.click(3342,439) # Location of "Tools" button
    pyautogui.click(3350,760) # Location of "Burn Bootloader" button

    Status = pyautogui.confirm("Bootloaded ICs : "+str(BootLoadedICs))#To manually continue to next IC

    if Status =="OK": #Check Wheather the ICs programmes correctly or not
        BootLoadedICs+=1
    else:
        continue

    