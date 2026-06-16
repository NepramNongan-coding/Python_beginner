def light(color):
    if color=="RED":
        return 0
    elif color=="YELLOW":
        return 1
    else:
        return 2
    
def trafficLight():
    user_input=input("Enter the color of the traffic light: ")
    if(user_input not in ("RED","GREEN","YELLOW")):
        print("Enter a correct color")
        
    else:
        signal_val=light(user_input)
        if signal_val==0:
            print("STOP,Your life is precious.")
        elif signal_val==1:
            print("Please,Go slow.")
        else:
            print("Go!!!!")

trafficLight()
print("SPEED THRILLS BUT KILLS.")