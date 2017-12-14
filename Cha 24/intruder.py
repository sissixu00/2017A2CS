#Sissi Xu S3C2 intruder
Inactive = "system inactive"
Active = "system active"
Alert = "alert mode"
Alarm = "alarm bell ringing"

def pressStart(state):
    if state == Inactive:
        state = Active
    print(state)
    return(state)
def enterPIN(state, time):
    if state == Active:
        state = Inactive
    elif state == Alert:
        state = Inactive
        time = 0
    elif state == Alarm:
        state = Inactive
    print(state)
    return(state, time)
def activateSensor(state):
    if state == Active:
        state = Alert
    print(state)
    return(state)
def Timepass(state, time):
    if state == Alert:
        time = time +1
    return(time)
def Bellring(state, time):
    if state == Alert and time == 2:
        state = Alarm
    print(state)
    return(state)
def events():
    print("1: press start button")
    print("2: enter PIN")
    print("3: activate sensor")
    print("4: wait for 2 minutes")
def main():
    state = Inactive
    time = 0
    print(state)
    while True:
        events()
        event = input("enter event:")
        if event == "1":
            state = pressStart(state)
        elif event == "2":
            state, time = enterPIN(state, time)
        elif event == "3":
            state = activateSensor(state)
        elif event == "4":
            time = Timepass(state, time)
            state = Bellring(state, time)
main()
