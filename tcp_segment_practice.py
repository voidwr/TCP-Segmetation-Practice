#TCP segment practice
import random

def main(): #In a function so I can quit the program easier
    # Initial values
    ACK = random.randint(10, 5000) #Selects random ACK from range once to initialize 10#5000
    SEQ = random.randint(10, 5000) #Selects random SEQ from range once to initialize 10#5000
    DATA = random.randint(10, 8000) #Selects random DATA from rance once to initialize 10#8000
    segment = 1 #In what segment we are on mainly for displaying it to the user
    complete = 0 #How many times the challenge has been completed for promting the user if he wants to exit
    useraskcomplete = 3 + int(input("How many number of times you want to try before you are asked to quit? MIN 3 (3 + your input) ") or 0 ) #How many tries the user wants min 3
    #^(Because it gets frustrating to always ask If the user wants to quit)
    print("You can input the number 0 in ACK and SEQ respectively to exit at any time")
    if useraskcomplete < 0: #Just some validation because of funny people
        useraskcomplete = 3 #If for example someone inputs -9999999 we reset to 3 tries. or evil plan (don't uncomment evil plan)
        #print("Funny...") #Evil plan
        #useraskcomplete = 999999999999 #Evil plan
    print(f"You will be asked if you want to exit after completing the challenge more than '{useraskcomplete}' times") #Just some clarification for the user
    randSELECTSENDER = 0 #This governs how many times SENDER sent the packet if it's >0 we already sent the first packet so we switch to doing SEQ += DATA
    randSELECTRECEIVER = 0 #This governs how many times RECEIVER sent the packet if it's >0 we already sent the first packet so we switch to doing SEQ += DATA
    active = 0 #This is to check periodically if we try to solve something and had a mistake so the packet remains the same
    hint = 0 #Just for hinting purposes
   
    # Initial segment display
    print(f"You are on /SEGMENT {segment}: ACK: {ACK} DATA: {DATA} SEQ: {SEQ}/ SENDER -> RECEIVER")
    #SEQprev = SEQ this is out of place here i keep it for debug purposes
    #ACKprev = ACK this is out of place here i keep it for debug purposes
    DATAprev = DATA
    #SEQ = ACKprev #ACK becomes SEQ this is out of place here i keep it for debug purposes
    #ACK = DATA + SEQprev #SEQ + DATA become ACK this is out of place here i keep it for debug purposes
    segment += 1

    #Main Logic
    while True:
        # Generate random DATA and decide sender/receiver
        DATA = random.randint(10,8000) #Always generates random DATA based on range 10#8000
        randSENDRECV = random.randint(1,20) #Basically a D20 roll on who sends the packet
        
        #More logic
        if randSENDRECV <= 11: #1 to 11 SENDER sends packet
            randSENDRECVtext = "SENDER -> RECEIVER" #variable text
            randSELECTSENDER += 1 #Counting upwards every time we see <=11
            randSELECTRECEIVER = 0 #To return other value to 0 when we pass the statement
        elif randSENDRECV > 11: #11 or more RECEIVER sends packet (I know I could have used else but I'm paranoid a bit.) 
            randSENDRECVtext = "SENDER <- RECEIVER" #variable text
            randSELECTRECEIVER += 1 #Counting upwards every time we see >11
            randSELECTSENDER = 0 #To return other value to 0 when we pass the statement

        # Conditional processing based on sender/receiver state
        if (randSENDRECV <= 11 and randSELECTSENDER <= 1) or (randSENDRECV > 11 and randSELECTRECEIVER <= 1):
            if segment == 2: #this is needed because we display the first segment and we need to do calculations
                SEQprev = SEQ
                ACKprev = ACK
            else: #afterwards it just passes
                pass
            SEQ = ACK
            ACK = DATAprev + SEQprev #First Instance
        else: #don't like else here but got confused with greater minor a bit so my paranoia has to eat me away
            SEQ += DATAprev # Second instance
            #SEQ = SEQprev this is out of place here i keep it for debug purposes
        active = 1 #this starts the next loop where we don't refresh DATA every time got bored of while True
        
        while active == 1: 
            # Display current segment information
            print(f"You are on /SEGMENT {segment}/ {randSENDRECVtext}") #Displaying only the segment value and who sent the packet I was also displaying DATA but it became confusing
            
            #print(f"//DEBUG: ACK: {ACK}, DATA: {DATA}, SEQ: {SEQ}//") #!!!DEBUG INFORMATION DO NOT UNCOMMENT!!!

            #Hint logic
            if hint > 5 and randSENDRECV <= 11 and randSELECTSENDER <= 1 or hint > 5 and randSENDRECV > 11 and randSELECTRECEIVER <= 1: #Hint validation
                if hint > 10:
                    print(f"Previous segment {segment-1} / ACK: {ACKprev} DATA: {DATAprev} SEQ: {SEQprev}/") #This just outputs the previous segment just for clarification
                    print(f"New ACK = DATA({DATAprev}) + SEQ({SEQprev}) and new SEQ = ACK({ACKprev})") #This added line of code provides a clearer ansewer after 10 failed tries
                else:
                    print(f"Previous segment {segment-1} / ACK: {ACKprev} DATA: {DATAprev} SEQ: {SEQprev}/") #This just outputs the previous segment just for clarification
                    print(f"Remember: {randSENDRECVtext} so we do SEQ = ACK and ACK = DATA + SEQ") #First Hint always a nudge to the right direction no outright answer
            elif hint > 5 and randSENDRECV <=11 and randSELECTSENDER > 1 or hint > 5 and randSENDRECV > 11 and randSELECTRECEIVER > 1:
                if hint > 10:
                    print(f"Previous segment {segment-1} / ACK: {ACKprev} DATA: {DATAprev} SEQ: {SEQprev}/") #This just outputs the previous segment just for clarification
                    print(f"New ACK = PREVIOUS ACK({ACKprev}) and new SEQ = SEQ{SEQprev} + DATA({DATAprev})") #This added line of code provides a clearer ansewer after 10 failed tries
                else:
                    print(f"Previous segment {segment-1} / ACK: {ACKprev} DATA: {DATAprev} SEQ: {SEQprev}/") #This just outputs the previous segment just for clarification
                    print(f"Remember: {randSENDRECVtext} so we do ACK -> ACK and SEQ = DATA + SEQ") #First Hint always a nudge to the right direction no outright answer
            
            #The magic
            try:
                # Get ACK and SEQ inputs from the user
                answerACK = input("ACK: ")
                answerSEQ = input("SEQ: ")
                if answerACK == "exit" or answerSEQ == "exit":
                    while True:
                        if complete < useraskcomplete:
                            choice = input("You haven't completed the challenge, do you really want to quit? y/n\n").lower()
                        elif complete > useraskcomplete:
                            choice = input("Are you sure you want to quit? y/n\n").lower()
                        if choice == "yes" or choice == "y":
                            print(f"You completed {complete} segments")
                            print("Exiting...Goodbye!")
                            return
                        elif choice == "no" or choice == "n":
                            print("Continuing...")
                            print(f"Previous /SEGMENT {segment-1}: ACK:{ACKprev} DATA: {DATAprev} SEQ: {SEQprev}/")
                            break
                else:
                    answerACK = int(answerACK)
                    answerSEQ = int(answerSEQ)
                # ACK and SEQ validation
                if answerSEQ == SEQ and answerACK == ACK and complete < useraskcomplete: #There are two instances, the first one is to check if the user passed the requested completions
                    complete += 1 #we just count up for completions
                    print(f"CORRECT! / SEGMENT {segment}: ACK: {ACK} DATA: {DATA} SEQ: {SEQ} / you have completed: {complete} segment(s)") #flavor text
                    segment += 1 #count the segments up
                    active = 0 #close the loop and retrun to parent loop
                    DATAprev = DATA #we need those for the calculations of the next segment
                    SEQprev = SEQ #we need those for the calculations of the next segment
                    ACKprev = ACK #we need those for the calculations of the next segment I don't use ACKprev anywhere but never hurts to keep it active since paranoia
                    hint = 0
                else:
                    print("Incorrect ACK or SEQ. Please try again.") #this is the incorrect input statement it returns to active loop without changing values to anything
                    print(f"Previous /SEGMENT {segment-1}: ACK:{ACKprev} DATA: {DATAprev} SEQ: {SEQprev}/")
                    hint += 1
            except ValueError:
                print("Wrong input restarting") #this is if someone accidentaly presses a blank enter or something else that can't become an integer. It's just here so we don't have
                #^to restart the program on a missclick


if __name__ == "__main__":
    main() #I use this so I can exit the program with return rather than exit()

#------------------------NOTES------------------------
#There is a DEBUG statement in line 67.

#The governing ACK DATA SEQ calculations are happening on line 50 - 61

#There is a HINTING logic in line 69 - 83

#------------------------REVISED NOTES------------------------
#changed the way the user could exit// now user can exit by inputing 0 and 0 in ack and seq respectively
#modified some logic to incorporate the new exit function
#