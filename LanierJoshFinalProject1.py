"""
Program: LanierJoshFinalProject1.py
Author: Josh Lanier
Program that takes Trailer and Floor Kit data for semi-trailer floor board distribution companies and compares Trailers to Floor Kits to \
see if they are compatible together, will work with certain cautions, or if a different trailer should be chosen. Program also allows user \
to see a list of all Trailers and Floor Kits that are in the system currently through 'Assets' window and to see attributes for specific \
Trailers and Floor Kits through 'Stats' window.
"""

import tkinter as tk
from tkinter import *
from LanierJoshFinalProject2 import *     #module that contains classes for Trailer and FloorKit objects

window = Tk()       #main window
window.title("Trailer and Floor Kit Repository")
window.geometry("310x400")


#object data set for program to use
trailer1 = Trailer("Trailer 1", 51.5, 58.5, 57, True, True, "Red")
trailer2 = Trailer("Trailer 2", 52, 52.75, 56, False, True, "Red, yellow stairs")
trailer3 = Trailer("Trailer 3", 52.5, 56, 54.5, brackets=False, color="red")
trailer4 = Trailer("Trailer 4", 52.25, 56, 54.25, True, False, "Red")
trailer5 = Trailer("Trailer 5", 51, 58.25, 56.75, True, False, "Yellow top, red frame")
trailer6 = Trailer("Trailer 6", 51, 58, 56.25)

trailerList = [trailer1, trailer2, trailer3, trailer4, trailer5, trailer6]      #list of all Trailer objects available to program

kit1 = FloorKit("Kit 1", 50, 56.5, 55.75, 56, True)
kit2 = FloorKit("Kit 2", 51, 56.75, 55.75, 55.75, False)
kit3 = FloorKit("Kit 3", 53, 57, 55.5, 56, False)

kitList = [kit1, kit2, kit3]      #list of all FloorKit objects available to program
#end object data set



############# Line Break ###############

#ASSET WINDOW FUNCTIONS

def openAssets():
    """Runs and instantiates assetWindow and its widgets, and fills Text box with the string methods of all Trailer and FloorKit objects \
        in program."""
    #assetWindow opens by hitting 'Assets' button in ReposMain class window
    assetWindow = Toplevel(window)
    assetWindow.title("Repository Asset List")
    assetScrollbar = Scrollbar(assetWindow)
    assetScrollbar.pack(side=RIGHT, fill=Y)

    assetHeader = tk.Label(assetWindow, text = "Assets Available in Repository")
    assetList =  tk.Text(assetWindow, yscrollcommand=assetScrollbar.set)
    assetClose = tk.Button(assetWindow, text = "Close", command = lambda: closeAsset(assetWindow))
    
    assetHeader.pack()
    assetList.pack()
    assetClose.pack()

    dataTuple = ("TRAILERS",trailer1, trailer2, trailer3, trailer4, trailer5, trailer6, "FLOOR KITS", kit1, kit2, kit3)  #tuple of data set objects
    assetTextBuild = ""                                    #string holder variable for contents of asset list, populated by for loop below
    for words in dataTuple:                                #for loop to accumulate attribute data from program Trailer and FloorKit objects
        assetTextBuild += (str(words) + "\n")
    assetList.insert(INSERT, [assetTextBuild])
    assetList.config(state=DISABLED)                        #assetList Text box disabled so it acts only as a viewing area
    assetScrollbar.config(command=assetList.yview)

def outputAssets():                                         #function called from ReposMain class window
    """Redirect to openAsset function."""
    openAssets()                                            #opens assetWindow and displays Assets
    
def closeAsset(w):
   """Closes/destroys assetWindow. w is window to destroy, passed from Button command option."""  #function run from 'Close' button in Asset window, closes Asset window
   w.destroy()



############# Window Break ###############

#STAT WINDOW FUNCTIONS

def openStatWindow(stats):
    """Runs and instantiates statWindow and its widgets, displays attributes of Trailer or Floor Kit entered into main window. stats variable \
        is passesd from statPopulator() function, called by outputStats() function that is called from ReposMain class window, and contains \
        the string representation of the objects referenced by user inputs in main window."""
    #statWindow opens by hitting 'Stats' button on ReposMain class window, displays object statistics
    statWindow = Toplevel(window)
    statWindow.title("Statistics")

    statHeader = tk.Label(statWindow, text = "Statistics for Items Entered")
    statText = StringVar()
    statText.set(stats)                                         #contains statistics for user input referenced objects
    statList =  tk.Label(statWindow, textvariable=statText)     #body of the Stat Window containing statistics text data    
    statClose = tk.Button(statWindow, text = "Close", command = lambda: closeStatWindow(statWindow))

    statHeader.pack()
    statList.pack()
    statClose.pack()


def statPopulator(kI, tI):
    """Takes kI and tI (Kit and Trailer name user inputs from main window, respectively), traverses trailerList and kitList and compares kI and tI to names in each \
        to find the object referenced by each. If one of the main window Entry boxes is left empty, function will bypass it and only return information for Entry boxes \
        with user inputs. If both boxes are empty, 'None' will be displayed in statWindow. If one of the referenced objects is not found, function will return an 
        appropriate error message for that object.""" 
    trailerFlag = False                                     #flag is assigned True if referenced Trailer object is found
    kitFlag = False                                         #flag is assigned True if referenced FloorKit object is found
    trailerText = ""                                        #empty string starting assignment
    kitText = ""                                            #empty string starting assignment
    for trailers in trailerList:                            #traversing trailerList to attempt to find referenced Trailer object
        if tI.get() == getattr(trailers, 'name', ''):       #comparing user Trailer input to trailer name attribute of current trailer in for loop
            trailerFlag = True                              #flag assigned True if name is found
            trailerText = trailers                          #temporary variable is assigned value of object if name is found
            break                                           #no need to keep traversing trailerList if object is found
    for kits in kitList:                                    #same logic as previous for loop, except with kits
        if kI.get() == getattr(kits, 'name', ''):
            kitFlag = True
            kitText = kits
            break
    if trailerFlag == False or kitFlag == False:            #preliminary error message filter placed first in selection statement to stop function from continuing on
        if trailerFlag == False:                            #specifying which input is invalid
            trailerText = "Trailer not found."              #assigning error message to text placeholder
        if kitFlag == False:
            kitText = "Kit not found." 
    if kI.get() != "" and tI.get() != "":                   #three selection statements determining which input boxes user has entered data into, by which boxes still have default value empty string representing no data entered
        return str(str(kitText) + "\n"*2 + str(trailerText))#each selection returns a string of the user referenced object's attributes in a cascading list form
    if kI.get() == "" and tI.get() != "":
        return str(trailerText)                             #returned value for each of the three selection statements is returned to outputStats() and passed to openStatWindow() as statText variable
    if kI.get() != "" and tI.get() == "":
        return str(kitText)

def outputStats(kI, tI):
    """Passes kI and tI, strings of user inputs from main window Kit and Trailer Entry boxes respectively, to statPopulator(); passes \
        string representation of attributes of object referenced by kI and tI from statPopulator() as statText variable to and calls statWindow() function."""
    statText = statPopulator(kI, tI)                        #variable holds returned string of object statistics to pass to openStatWindow() function
    openStatWindow(statText)                                #opens statWindow and displays statistics
    
def closeStatWindow(w):     #function run from 'Close' button in Stat window, closes Stat window
    """Closes/destroys statWindow. w is window to destroy, passed from Button command option."""
    w.destroy()



############# Window Break ###############

#COMBO TEST WINDOW FUNCTIONS

def openComboTest(result):
    """Runs and instantiates comboTest and its widgets. result is string of comboTest result, passed from comboTest() function called by outputCombo() function after \
        comboTest() was supplied with main window user inputs kI and tI (Kit and Trailer inputs, respectively), passed from main window calling of outputCombo() fucntion."""
    #comboTest opens by hitting 'Test Combo' button in ReposMain class window
    comboTestWindow = Toplevel(window)
    comboTestWindow.title("Combo Test")
    comboFrame = Frame(comboTestWindow)
    comboFrame.pack()

    ctHeader = tk.Label(comboFrame, text = "Results of Combo Test")
    resultText = StringVar()
    resultText.set(result)      #body of the window, displays comboTest() function results
    ctResult = tk.Label(comboFrame, textvariable=resultText)
    
    assetClose = tk.Button(comboFrame, text = "Close", command = lambda: closeComboTest(comboTestWindow))

    ctHeader.pack()
    ctResult.pack()
    assetClose.pack()

def closeComboTest(w):
    """Closes/destroys comboTestWindow. w is window to destroy, passed from Button command option."""  #function run from 'Close' button in comboTestWindow, closes comboTestWindow
    w.destroy()

def outputCombo(kI, tI):
    """Passes kI and tI, strings of user inputs from main window Kit and Trailer name Entry boxes respectively, to comboTest(); passes \
        string representation returned by comboTest() which compares attributes of objects referenced by kI and tI, and passes string representation \
        of results to openComboTest() as result variable and calls openComboTest()."""      
    result = comboTest(kI, tI)                              #variable holds returned string of comboTest result to pass to openComboTest() function
    openComboTest(result)                                   #opens comboTestWindow and displays results
    
def comboTest(kI, tI):
    """Takes kI and tI (Kit and Trailer name user inputs from main window, respectively), traverses trailerList and kitList and compares kI and tI to names in each \
        to find the object referenced by each. Function returns error message if one of the referenced objects is not found or if Entry box is left empty. If both \
        trailer and kit objects are found, trailers and kits are compared for compatibility and function returns one of three messages representing determined compatibility."""
    trailerFlag = False                                     #flag is assigned True if referenced Trailer object is found
    kitFlag = False                                         #flag is assigned True if referenced FloorKit object is found
    for trailers in trailerList:                            #traversing trailerList to attempt to find referenced Trailer object
        if tI.get() == getattr(trailers, 'name', ''):       #comparing user Trailer input to trailer name attribute of current trailer in for loop
            trailerFlag = True                              #flag assigned True if name is found
            trailer = trailers                              #temporary variable is assigned value of object if name is found
            break                                           #no need to keep traversing trailerList if object is found
    for kits in kitList:                                    #same logic as previous for loop, except with kits
        if kI.get() == getattr(kits, 'name', ''):
            kitFlag = True
            kit = kits
            break
    if trailerFlag == False or kitFlag == False:            #preliminary error message filter placed first in selection statement to stop function from continuing on
        if kitFlag == False:                                #specifying which input is invalid
            return "Kit not found. \n Please see Asset List for valid kits."  #object specific error message
        elif trailerFlag == False:
            return "Trailer not found. \n Please see Asset List for valid trailers."
    else:                                                   #if both flags are assigned True, comboTest continues on to comparative logic to return test results
        if kit.woodOnly == True:  #wood only kits can go 4 inches above top of pillar, combo aluminum and wood will give warning #if middle cinch measurement goes above pillar
            margin = 4            #margin variable holds integer explained by previous line comment
        else: 
            margin = 0
        if kit.cinchMiddle - margin > trailer.pToTop:       #if both referenced trailer and kit objects are found, one of three result strings are returned to outputCombo() function and passed to openComboTest() function as 'result' variable
            return ("Middle of kit will be too high above pillar for safe travel. Recommend using different trailer.")
        elif kit.cinchMiddle - margin > trailer.pToSlant and (kit.cinchBack - margin > trailer.pToTop or kit.cinchMiddle - margin > trailer.pToTop):
            return "Trailer may work with care. Recommend using different trailer, or band ends sticking above pillars before cinching and start tightening in the middle."
        elif kit.cinchMiddle - margin < trailer.pToSlant or (kit.cinchBack - margin < trailer.pToTop or kit.cinchMiddle - margin < trailer.pToTop):
            return ("Trailer and kit are compatible well.")
            

      

############# Window Break ###############

#MAIN WINDOW CLASS AND FUNCTIONS

class ReposMain(Frame):
    """Class holding method to create main window for Trailer Floor Repository program."""

    def __init__(self):
        """Sets up window and all widgets."""
        Frame.__init__(self)
        
        self.assetsLabel = tk.Label(window, text = "List of current assets in repository").grid(row = 1, column = 0, columnspan = 3, sticky="NSEW")
        self.kitLabel = tk.Label(window, text = "Enter kit name: ").grid(row = 5, column = 0, sticky = "W")
        self.instructions = tk.Label(window, text = "***Enter names exactly as they appear in asset list***").grid(row = 3, column = 0, columnspan=3)
        self.trailerLabel = tk.Label(window, text = "Enter trailer name: ").grid(row = 7, column = 0, sticky = "W")
        self.statsLabel = tk.Label(window, text = "See stats for entered items").grid(row = 9, column = 0, columnspan=3, sticky="NSEW")
        self.comboLabel = tk.Label(window, text = "Will combination work together?").grid(row = 11, column = 0, columnspan=3, sticky="NSEW")
        kI = StringVar()        #holds value for user inputted kit name
        kI.set("")              #default value set
        self.kitInput = tk.Entry(window, width = 20, textvariable=kI).grid(row = 5, column = 2, sticky="E")
        tI = StringVar()        #holds value for user inputted kit name
        tI.set("")              #default value set
        self.trailerInput = tk.Entry(window, width = 20, textvariable=tI).grid(row = 7, column = 2, sticky="E")
               
        self.assetButton = tk.Button(window, text = "Assets", command = outputAssets).grid(row = 2, column = 1, sticky="NSEW")
        self.statsButton = tk.Button(window, text = "Stats", command = lambda: outputStats(kI, tI)).grid(row = 10, column = 1, sticky="NSEW")
        self.comboButton = tk.Button(window, text = "Test Combo", command = lambda: outputCombo(kI, tI)).grid(row = 12, column = 1, sticky="NSEW")
        self.image = tk.PhotoImage(file=r"C:\Users\jclan\Documents\College-Josh\Intro to Soft Dev\VS Code Files\Homework\trailer.gif")
        self.imageLabel = tk.Label(window, text = "trailer", image=self.image).grid(row = 14, column = 0, columnspan=3)
        self.image2 = tk.PhotoImage(file=r"C:\Users\jclan\Documents\College-Josh\Intro to Soft Dev\VS Code Files\Homework\semi.gif")
        self.imageLabel2 = tk.Label(window, text="semi", image=self.image2).grid(row=0, column=0, columnspan=3)

        

def main():
    """Instantiates and pops up the window."""
    ReposMain().mainloop()

if __name__ == "__main__":
    main()
