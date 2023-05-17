import tkinter as tk
import numpy as np
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute, BasicAer
from PIL import Image, ImageTk
import customtkinter as ctk

screenWidth = 0
screenHeight = 0

mainOrange = '#E88531'
mainBlue = '#3375B1'
mainGreen = '#43877E'
secondaryOrange = '#FAA35A'
secondaryBlue = '#50B1D4'
secondaryGreen = '#50B1D4'

n = 16
quantumRegister = QuantumRegister(n, name='qr')
classicalRegister = ClassicalRegister(n, name='cr')

measurementList = []


class simInfoClass:
    def __int__(self):
        self.aliceKeys = None
        self.aliceBases = None


info = simInfoClass()


class FirstFrame(ctk.CTkFrame):
    def __init__(self, master):
        ctk.CTkFrame.__init__(self, master,
                              width=int(screenWidth * 0.5), height=int(screenHeight * .75),
                              fg_color=mainOrange)
        self.pack()

        self.startButton = ctk.CTkButton(master=self, command=self.goToSimPage,
                                         width=int(screenWidth * 0.18), height=int(screenHeight * 0.05),
                                         text="Start Simulation",
                                         fg_color=mainBlue, hover_color=secondaryBlue,
                                         border_color="white", border_width=1)
        self.startButton.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.informationButton = ctk.CTkButton(master=self, command=self.goToInfoPage,
                                               width=int(screenWidth * 0.25), height=int(screenHeight * 0.05),
                                               text="Learn About BB84 Protocol",
                                               fg_color=mainBlue, hover_color=secondaryBlue,
                                               border_color="white", border_width=1)
        self.informationButton.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

    def goToSimPage(self):
        self.pack_forget()
        bb84Simulation()
        simulationFrame.pack()

    def goToInfoPage(self):
        self.pack_forget()
        infoFrame.pack()


class InfoFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master,
                          width=int(screenWidth * 0.5), height=int(screenHeight * .75),
                          background=mainOrange)
        self.pack()

        # Top Frame for buttons
        topFrame = tk.Frame(self, bg=mainOrange)
        topFrame.pack(side=tk.TOP, padx=10, pady=10, anchor=tk.N, fill=tk.BOTH)

        # Create "Back" button
        self.backButton = tk.Button(topFrame, highlightbackground=mainOrange, text="Back", command=self.goToFirstPage)
        self.backButton.pack(side=tk.LEFT)
        # Create "Next" button
        self.nextButton = tk.Button(topFrame, highlightbackground=mainOrange, text="Next", command=self.goToInfo2Page)
        self.nextButton.pack(side=tk.RIGHT)

        # Frame for Information
        midFrame = tk.Frame(self, bg=mainOrange)
        midFrame.pack(anchor=tk.CENTER, fill=tk.BOTH, expand=True)

        # Add text label
        text = "Quantum Key Distribution (QKD) is a method for securely distributing cryptographic keys between two parties - Alice and Bob - by using the principles of quantum mechanics. The BB84 protocol is one of the most well-known QKD protocols, developed by Charles Bennett and Gilles Brassard in 1984. The BB84 protocol works by using two quantum bits (qubits) - one to transmit the key and the other to verify its integrity. Alice randomly encodes the bits she wants to send to Bob using one of four possible states, which are chosen from two different bases. Each state represents a specific bit value, either a 0 or a 1. Bob then receives the encoded qubits and measures them in one of the two bases, chosen randomly. Once Bob has measured the qubits, Alice and Bob publicly compare the bases they used. If they used the same basis, Bob's measurement result reveals the value of the corresponding bit, and they can use it to form their shared secret key. If they used different bases, they discard the bit value and repeat the process until enough bits are obtained.The security of the BB84 protocol comes from the fact that any attempt to eavesdrop on the transmission will inevitably introduce errors that can be detected by Alice and Bob. According to the principles of quantum mechanics, any attempt to observe or measure a qubit will change its state, which can be detected by the parties. Thus, if an eavesdropper tries to intercept the qubits, they will introduce errors that will be detected during the verification process, allowing Alice and Bob to discard the affected bits and prevent the eavesdropper from obtaining any information about the key. QKD, and specifically the BB84 protocol, provides a method for securely distributing cryptographic keys that is resistant to interception or tampering. While still in its early stages of development, QKD has the potential to revolutionize the way in which secure communications are established and maintained, and it is an exciting area of research in both physics and computer science."
        textMessage = tk.Message(midFrame, text=text, width=int(screenWidth * 0.75), justify="center", bg=mainOrange)
        textMessage.pack(side=tk.TOP)

    def showInfoPage(self):
        # Hide any previously shown frames
        self.hideAllPages()

        # Add the info_frame to the main window
        self.pack()

    def hideAllPages(self):
        # Hide all frames in the main window
        self.pack_forget()

    def goToFirstPage(self):
        self.pack_forget()
        firstFrame.pack()

    def goToInfo2Page(self):
        # Hide all frames in the main window
        self.hideAllPages()
        self.pack_forget()
        infoFrame2.pack()


class InfoFrame2(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master,
                          width=int(screenWidth * 0.5), height=int(screenHeight * .75),
                          background=mainOrange)
        self.pack()

        # Add other widgets to the frame as needed
        topFrame = tk.Frame(self, bg=mainOrange)
        topFrame.pack(side=tk.TOP, padx=10, pady=10, anchor=tk.NW)
        # Create "Back" button
        self.backButton = tk.Button(topFrame, highlightbackground=mainOrange, text="Back", command=self.goToInfoPage)
        self.backButton.pack(side=tk.LEFT)
        # Create "Next" button
        self.nextButton = tk.Button(topFrame, highlightbackground=mainOrange, text="Return to Homepage",
                                    command=self.goToFirstPage)
        self.nextButton.pack(side=tk.RIGHT)

        # Load and resize the image
        image = Image.open('./assets/imagee.jpeg')
        image = image.resize((600, 435), Image.LANCZOS)

        # Convert the image to a Tkinter-compatible format
        photo = ImageTk.PhotoImage(image)

        # Create a label to display the image
        imageLabel = tk.Label(self, image=photo)
        imageLabel.image = photo

        # Add the label to the frame
        imageLabel.pack(side=tk.BOTTOM, padx=10, pady=10, anchor=tk.CENTER)

    def showInfo2Page(self):
        # Hide any previously shown frames
        self.hideAllPages()

        # Add the info_frame to the main window
        self.pack()

    def hideAllPages(self):
        # Hide all frames in the main window
        self.pack_forget()

    def goToFirstPage(self):
        self.pack_forget()
        firstFrame.pack()

    def goToInfoPage(self):
        # Hide all frames in the main window
        self.pack_forget()
        infoFrame.pack()


class SecondFrame(ctk.CTkFrame):
    currentSimStage = 0

    def __init__(self, master):
        ctk.CTkFrame.__init__(self, master,
                              width=int(screenWidth * 0.5), height=int(screenHeight * 0.75),
                              fg_color=mainOrange)
        self.pack()
        self.pack_propagate(False)

        # Create top frame for the "Back" button
        self.topFrame = ctk.CTkFrame(master=self,
                                     width=int(screenWidth * 0.5),
                                     fg_color=secondaryOrange, corner_radius=9)
        self.topFrame.pack(fill=tk.BOTH, padx=4, pady=4)

        # Create "Back" button
        self.backButton = ctk.CTkButton(master=self.topFrame, command=self.goToFirstPage,
                                        width=int(screenWidth * 0.03), height=int(screenHeight * 0.03),
                                        text="Back",
                                        fg_color=mainBlue, hover_color=secondaryBlue,
                                        border_color="white", border_width=1)
        self.backButton.pack(side=tk.LEFT, padx=4, pady=4)

        # Create middle frame for simulation
        self.midFrame = ctk.CTkScrollableFrame(master=self,
                                               width=int(screenWidth * 0.5),
                                               fg_color=secondaryOrange, corner_radius=9,
                                               scrollbar_button_color=mainOrange,
                                               scrollbar_button_hover_color=mainOrange)
        self.midFrame.pack(fill=tk.BOTH, expand=True,padx=4)

        # Create canvas for middle frame
        # self.canvas = tk.Canvas(midFrame,width=screenWidth*0.46, height= screenHeight*0.7,bg=mainOrange, highlightbackground=mainOrange,scrollregion=(0, 0, 0, 4000))
        # self.canvas.pack(side=tk.LEFT,fill=tk.BOTH,expand=True,pady=4,padx=4)
        # self.canvas.pack_propagate(False)

        # Create Scrollbar for middle frame
        # scrollbar = tk.Scrollbar(midFrame, orient='vertical')
        # scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        # scrollbar.config(command=self.canvas.yview)
        # self.canvas.configure(yscrollcommand=scrollbar.set)

        # Create bottom frame for "Next" button
        self.bottomFrame = ctk.CTkFrame(master=self,
                                        width=int(screenWidth * 0.5),
                                        fg_color=secondaryOrange, corner_radius=9)
        self.bottomFrame.pack(fill=tk.BOTH, padx=4, pady=4)

        self.nextButton = ctk.CTkButton(master=self.bottomFrame, command=self.showNextFrame,
                                        width=int(screenWidth * 0.05),
                                        text="Next",
                                        fg_color=mainBlue, hover_color=secondaryBlue,
                                        border_color="white", border_width=1)
        self.nextButton.pack(anchor=tk.CENTER, pady=4)

        # Create Frame List for measurement frames
        self.frameList = []

    def createSimInfoFrame(self):
        mainFrame = ctk.CTkFrame(master=self.midFrame, width=int(screenWidth * 0.45), fg_color="yellow",
                                 corner_radius=9)
        mainFrame.pack(anchor=tk.CENTER, pady=5)

        topFrame = ctk.CTkFrame(master=mainFrame)
        topFrame.pack(fill=tk.BOTH, padx=3, pady=3)
        bitsText = "As information page about protocol, at first Alice generates a random set of bits. This time Alice's random bits are:"
        bitsDescription = tk.Message(topFrame, text=bitsText, justify="center", width=600)
        bitsDescription.pack()
        bitsLabel = tk.Label(topFrame, text=info.aliceKeys, justify="center", anchor="center", font=("Arial", 25))
        bitsLabel.pack()

        baseText = "After that, Alice sends photons to Bob on different bases in quantum channel, Alice's bases are:"
        baseDescription = tk.Message(topFrame, text=baseText, justify="center", width=600)
        baseDescription.pack()

        baseFrame = ctk.CTkFrame(master=mainFrame)
        baseFrame.pack(fill=tk.BOTH, padx=3, pady=3)

        for base in info.aliceBases:
            imageName = './assets/diagonalbase.png' if base == "X" else './assets/rectilinearbase.png'
            imgSize = int((screenWidth * 0.45 - (15 * 4)) / 16)
            img = ctk.CTkImage(light_image=Image.open(imageName), size=(imgSize, imgSize))
            imgLabel = ctk.CTkLabel(baseFrame, image=img, text="")
            imgLabel.pack(side=tk.LEFT, padx=2)

        self.frameList.append(mainFrame)

    def createSimFrame(self):
        frame = ctk.CTkFrame(master=self.midFrame,
                             width=int(screenWidth * 0.45), height=int(screenHeight * 0.08),
                             fg_color="yellow", corner_radius=9)
        frame.pack(anchor=tk.CENTER, pady=5)
        frame.pack_propagate(False)

        innerFrame = ctk.CTkFrame(master=frame)
        innerFrame.pack(fill=tk.BOTH, expand=True, padx=3, pady=3)

        innerFrame.rowconfigure(0, weight=1)
        innerFrame.rowconfigure(1, weight=4)

        innerFrame.columnconfigure(0, weight=1)
        innerFrame.columnconfigure(1, weight=1)
        innerFrame.columnconfigure(2, weight=5)
        innerFrame.columnconfigure(3, weight=1)
        innerFrame.columnconfigure(4, weight=1)

        titleLabel1 = tk.Label(innerFrame, text="Alice's Bit")
        titleLabel1.grid(row=0, column=0)

        titleLabel2 = tk.Label(innerFrame, text="Alice's Base")
        titleLabel2.grid(row=0, column=1)

        titleLabel3 = tk.Label(innerFrame, text="Explanation")
        titleLabel3.grid(row=0, column=2)

        titleLabel4 = tk.Label(innerFrame, text="Bob's Base")
        titleLabel4.grid(row=0, column=3)

        titleLabel5 = tk.Label(innerFrame, text="Bob's Bit")
        titleLabel5.grid(row=0, column=4)

        # ---------------------------------------------------

        # Alice's Bit
        defLabel1 = tk.Label(innerFrame, text=measurementList[self.currentSimStage - 1].aliceBit)
        defLabel1.grid(row=1, column=0)

        # Alice's Bases
        aliceImgPath = './assets/diagonalbase.png' if measurementList[self.currentSimStage - 1].aliceBase == "X" \
            else './assets/rectilinearbase.png'
        aliceImg = tk.PhotoImage(file=aliceImgPath)
        defLabel2 = tk.Label(innerFrame, image=aliceImg)
        defLabel2.image = aliceImg
        defLabel2.grid(row=1, column=1)

        message = ("Same Base Choice for Alice and Bob, Bit added to the key"
                   if measurementList[self.currentSimStage - 1].result
                   else
                   "Different base choice for Alice and Bob, no bit added to the key")
        defLabel3 = tk.Message(innerFrame, text=message, width=300, justify="center")
        defLabel3.grid(row=1, column=2)

        bobImgPath = './assets/diagonalbase.png' if measurementList[self.currentSimStage - 1].bobBase == "X" \
            else './assets/rectilinearbase.png'
        bobImg = tk.PhotoImage(file=bobImgPath)

        defLabel4 = tk.Label(innerFrame, image=bobImg)
        defLabel4.image = bobImg
        defLabel4.grid(row=1, column=3)

        text = (measurementList[self.currentSimStage - 1].aliceBit
                if measurementList[self.currentSimStage - 1].result
                else
                "No Bit Received")
        defLabel5 = tk.Message(innerFrame, text=text, justify="center")
        defLabel5.grid(row=1, column=4)

        # Put Frame into list
        self.frameList.append(frame)

    def showNextFrame(self):
        # Increment the currentSimStage
        self.currentSimStage += 1

        if self.currentSimStage == 1:
            self.createSimInfoFrame()
            # self.canvas.create_window(0, 0, anchor="center", window=self.frameList[0])
        else:
            self.createSimFrame()
            # self.canvas.create_window(380, 300 + ((self.currentSimStage - 2) * 100),anchor="center",window=self.frameList[self.currentSimStage - 1],tags="measurementFrame")

    def goToFirstPage(self):
        # Clear the data about previous simulation
        #self.canvas.delete('measurementFrame')

        for frame in self.frameList:
            frame.pack_forget()
            frame.destroy()

        self.frameList.clear()
        measurementList.clear()
        self.currentSimStage = 0
        # Go To First Frame
        self.pack_forget()
        firstFrame.pack()


class MeasurementFrame:
    def __init__(self, qubitNo, aliceBit, aliceBase, bobBase, result):
        self.qubitNo = qubitNo
        self.aliceBit = aliceBit
        self.aliceBase = aliceBase
        self.bobBase = bobBase
        self.result = result

    def printResult(self):
        if self.result:
            print("Qubit No:{}, Same choice on basis: {}, Bit added to the Key: {}".format(self.qubitNo, self.aliceBase,
                                                                                           self.aliceBit))
        else:
            print(
                "Qubit No:{}, Different Choice, Alice has {}, Bob has {}, No Bit added to the Key".format(self.qubitNo,
                                                                                                          self.aliceBase,
                                                                                                          self.bobBase))


def SendState(qc1, qc2):
    qs = qc1.qasm().split(sep=';')[4:-1]

    for index, instruction in enumerate(qs):
        qs[index] = instruction.lstrip()

    for instruction in qs:
        old_qr = int(instruction[5:-1])
        if instruction[0] == 'x':
            qc2.x(quantumRegister[old_qr])
        elif instruction[0] == 'h':
            qc2.h(quantumRegister[old_qr])
        elif instruction[0] == 'm':
            pass
        else:
            raise Exception('Unable to parse instruction')


def bb84Simulation():
    alice = QuantumCircuit(quantumRegister, classicalRegister, name='Alice')
    aliceKey = np.random.randint(0, high=2 ** n)
    aliceKey = np.binary_repr(aliceKey, n)

    for index, digit in enumerate(aliceKey):
        if digit == '1':
            alice.x(quantumRegister[index])

    aliceTable = []
    for index in range(len(quantumRegister)):
        if 0.5 < np.random.random():
            alice.h(quantumRegister[index])
            aliceTable.append('X')
        else:
            aliceTable.append('+')

    print("Alice's Base Table:", aliceTable)

    bob = QuantumCircuit(quantumRegister, classicalRegister, name='Bob')

    SendState(alice, bob)

    bobTable = []
    for index in range(len(quantumRegister)):
        if 0.5 < np.random.random():
            bob.h(quantumRegister[index])
            bobTable.append('X')
        else:
            bobTable.append('+')

    print("Bob's Base Table:  ", bobTable)

    for index in range(len(quantumRegister)):
        bob.measure(quantumRegister[index], classicalRegister[index])

    backend = BasicAer.get_backend('qasm_simulator')
    result = execute(bob, backend=backend, shots=1).result()

    bobKey = list(result.get_counts(bob))[0]
    bobKey = bobKey[::-1]

    keptBits = []
    discardedBits = []
    for qubit, basis in enumerate(zip(aliceTable, bobTable)):
        if basis[0] == basis[1]:
            measurementList.append(MeasurementFrame(qubitNo=qubit,
                                                    aliceBit=aliceKey[qubit],
                                                    aliceBase=basis[0],
                                                    bobBase=basis[1],
                                                    result=True))
            keptBits.append(qubit)
        else:
            measurementList.append(MeasurementFrame(qubitNo=qubit,
                                                    aliceBit=aliceKey[qubit],
                                                    aliceBase=basis[0],
                                                    bobBase=basis[1],
                                                    result=False))
            discardedBits.append(qubit)

    acc = 0
    for bit in zip(aliceKey, bobKey):
        if bit[0] == bit[1]:
            acc += 1

    newAliceKey = [aliceKey[qubit] for qubit in keptBits]
    newBobKey = [bobKey[qubit] for qubit in keptBits]

    acc = 0
    for bit in zip(newAliceKey, newBobKey):
        if bit[0] == bit[1]:
            acc += 1

    if acc // len(newAliceKey) == 1:
        print("Key exchange has been successfull")
        for frame in measurementList:
            frame.printResult()
        print("New Alice's key: ", newAliceKey)
        print("New Bob's key:   ", newBobKey)
    else:
        print("Key exchange has been tampered! Check for eavesdropper or try again")
        print("New Alice's key is invalid: ", newAliceKey)
        print("New Bob's key is invalid: ", newBobKey)

    simInfoClass.aliceKeys = aliceKey
    simInfoClass.aliceBases = aliceTable


if __name__ == "__main__":
    # Create main window
    root = tk.Tk()
    root.title("Simulation")

    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()

    rootWidth = screenWidth * 0.5
    rootHeight = screenHeight * 0.75
    posX = (screenWidth / 2) - (rootWidth / 2)
    posY = (screenHeight / 2) - (rootHeight / 2)
    root.geometry('%dx%d+%d+%d' % (rootWidth, rootHeight, posX, posY))
    root.resizable(False, False)

    # Command for full screen option
    # root.attributes('-fullscreen', True)

    # Create first frame
    firstFrame = FirstFrame(root)

    # Create second frame
    simulationFrame = SecondFrame(root)
    simulationFrame.pack_propagate(False)
    simulationFrame.pack_forget()

    infoFrame = InfoFrame(root)
    infoFrame.pack_propagate(False)
    infoFrame.pack_forget()

    infoFrame2 = InfoFrame2(root)
    infoFrame2.pack_propagate(False)
    infoFrame2.pack_forget()

    # Start the tkinter event loop
    root.mainloop()
