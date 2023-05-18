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
        self.resultKey = None


info = simInfoClass()


class FirstFrame(ctk.CTkFrame):
    def __init__(self, master):
        ctk.CTkFrame.__init__(self, master,
                              width=int(screenWidth * 0.5), height=int(screenHeight * 0.75),
                              fg_color=mainOrange)
        self.pack()

        self.buttonFrame = ctk.CTkFrame(master=self, fg_color=secondaryOrange, corner_radius=9,
                                        width=int(screenWidth * 0.49))
        self.buttonFrame.place(relx=0.5, rely=0.5, anchor="center")
        self.buttonFrame.pack_propagate(False)
        self.startButton = ctk.CTkButton(master=self.buttonFrame, command=self.goToSimPage,
                                         width=int(screenWidth * 0.18), height=int(screenHeight * 0.05),
                                         text="Start Simulation",
                                         fg_color=mainBlue, hover_color=secondaryBlue,
                                         border_color="white", border_width=1)
        self.startButton.place(relx=0.5, rely=0.5, anchor="center")

        self.informationButton = ctk.CTkButton(master=self.buttonFrame, command=self.goToInfoPage,
                                               width=int(screenWidth * 0.25), height=int(screenHeight * 0.05),
                                               text="Learn About BB84 Protocol",
                                               fg_color=mainBlue, hover_color=secondaryBlue,
                                               border_color="white", border_width=1)
        self.informationButton.place(relx=0.5, rely=0.8, anchor="center")

    def goToSimPage(self):
        self.pack_forget()
        bb84Simulation()
        simulationFrame.pack()

    def goToInfoPage(self):
        self.pack_forget()
        infoFrame.grid()


class InfoFrame(ctk.CTkFrame):
    def __init__(self, master):
        ctk.CTkFrame.__init__(self, master,
                              width=int(screenWidth * 0.5), height=int(screenHeight * 0.75),
                              fg_color=mainOrange)
        self.pack()

        self.gridFrame = ctk.CTkFrame(self, fg_color=mainOrange)
        self.gridFrame.pack(fill=tk.BOTH, expand=True)

        self.gridFrame.grid_rowconfigure(1, weight=1)
        self.gridFrame.grid_columnconfigure(1, weight=1)

        # Create frame for Back Button
        self.topLeftFrame = ctk.CTkFrame(self.gridFrame, corner_radius=9, fg_color=secondaryOrange)
        self.topLeftFrame.grid(row=0, column=0, sticky="nsew", padx=4, pady=4)
        self.backButton = ctk.CTkButton(self.topLeftFrame, command=self.goToFirstPage,
                                        text="Back",
                                        fg_color=mainBlue, hover_color=secondaryBlue,
                                        border_color="white", border_width=1, border_spacing=5)
        self.backButton.pack(anchor=ctk.NW, padx=4, pady=4)

        # Create a Navigation Frame
        self.navigationFrame = ctk.CTkFrame(self.gridFrame, corner_radius=9, fg_color=secondaryOrange)
        self.navigationFrame.grid(row=1, column=0, sticky="nsew", padx=4, pady=4)
        self.navigationFrame.grid_rowconfigure(6, weight=1)

        self.firstPageButton = ctk.CTkButton(self.navigationFrame, command=self.firstInfoAction,
                                             text="1. Introduction",
                                             fg_color=mainBlue, hover_color=secondaryBlue,
                                             border_color="white", border_width=1, border_spacing=5)
        self.firstPageButton.grid(row=0, column=0, sticky="ew", padx=4, pady=4)

        self.secondPageButton = ctk.CTkButton(self.navigationFrame, command=self.secondInfoAction,
                                              text="2. Example Table",
                                              fg_color=mainBlue, hover_color=secondaryBlue,
                                              border_color="white", border_width=1, border_spacing=5)
        self.secondPageButton.grid(row=1, column=0, sticky="ew", padx=4, pady=4)

        # -----------------------------------------

        # Create a general frame for information
        self.generalInfoFrame = ctk.CTkFrame(self.gridFrame, corner_radius=9, fg_color=secondaryOrange)
        self.generalInfoFrame.grid(row=0, column=1, rowspan=2, sticky="nsew", padx=4, pady=4)

        # First Info Frame
        self.firstInfoFrame = ctk.CTkFrame(self.generalInfoFrame, corner_radius=9, fg_color=secondaryOrange)
        text = "Quantum Key Distribution (QKD) is a method for securely distributing cryptographic keys between two parties - Alice and Bob - by using the principles of quantum mechanics. The BB84 protocol is one of the most well-known QKD protocols, developed by Charles Bennett and Gilles Brassard in 1984. The BB84 protocol works by using two quantum bits (qubits) - one to transmit the key and the other to verify its integrity. Alice randomly encodes the bits she wants to send to Bob using one of four possible states, which are chosen from two different bases. Each state represents a specific bit value, either a 0 or a 1. Bob then receives the encoded qubits and measures them in one of the two bases, chosen randomly. Once Bob has measured the qubits, Alice and Bob publicly compare the bases they used. If they used the same basis, Bob's measurement result reveals the value of the corresponding bit, and they can use it to form their shared secret key. If they used different bases, they discard the bit value and repeat the process until enough bits are obtained.The security of the BB84 protocol comes from the fact that any attempt to eavesdrop on the transmission will inevitably introduce errors that can be detected by Alice and Bob. According to the principles of quantum mechanics, any attempt to observe or measure a qubit will change its state, which can be detected by the parties. Thus, if an eavesdropper tries to intercept the qubits, they will introduce errors that will be detected during the verification process, allowing Alice and Bob to discard the affected bits and prevent the eavesdropper from obtaining any information about the key. QKD, and specifically the BB84 protocol, provides a method for securely distributing cryptographic keys that is resistant to interception or tampering. While still in its early stages of development, QKD has the potential to revolutionize the way in which secure communications are established and maintained, and it is an exciting area of research in both physics and computer science."
        textMessage = tk.Message(self.firstInfoFrame, text=text,
                                 width=int(screenWidth * 0.35),
                                 justify="left", bg=secondaryOrange)
        textMessage.pack(side=tk.TOP, padx=1, pady=1)

        # Second Info Frame
        self.secondInfoFrame = ctk.CTkFrame(self.generalInfoFrame, corner_radius=9, fg_color=secondaryOrange)
        image = Image.open('./assets/imagee.jpeg')
        image = image.resize((int(screenWidth * 0.35), int(screenHeight * 0.3)), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        imageLabel = tk.Label(self.secondInfoFrame, image=photo)
        imageLabel.image = photo
        imageLabel.pack(side=tk.TOP, padx=1, pady=1, anchor=tk.N)

        # -----------------------------------------
        # Show Default Frame
        self.showInfoFrameByName("1")

    def firstInfoAction(self):
        self.showInfoFrameByName("1")

    def secondInfoAction(self):
        self.showInfoFrameByName("2")

    def showInfoFrameByName(self, name):
        # Show selected frame
        if name == "1":
            self.firstInfoFrame.pack(fill=ctk.BOTH, expand=True, padx=4, pady=4)
        else:
            self.firstInfoFrame.pack_forget()
        if name == "2":
            self.secondInfoFrame.pack(fill=ctk.BOTH, expand=True, padx=4, pady=4)
        else:
            self.secondInfoFrame.pack_forget()

    def goToFirstPage(self):
        self.grid_forget()
        firstFrame.pack()


class SimulationFrame(ctk.CTkFrame):
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
        self.midFrame.pack(fill=tk.BOTH, expand=True, padx=4)

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
        mainFrame = ctk.CTkFrame(master=self.midFrame, width=int(screenWidth * 0.45), fg_color="white", corner_radius=9)
        mainFrame.pack(anchor=ctk.CENTER, fill=ctk.BOTH, pady=5, padx=16)

        topFrame = ctk.CTkFrame(master=mainFrame, fg_color=mainOrange)
        topFrame.pack(fill=tk.BOTH, padx=5, pady=3)
        bitsText = "As information page about protocol, at first Alice generates a random set of bits. This time Alice's random bits are:"
        bitsDescription = tk.Message(topFrame, text=bitsText, justify="center", width=int(screenWidth * 0.42),
                                     fg="white", background=mainOrange)
        bitsDescription.pack()
        bitsLabel = tk.Label(topFrame, text=info.aliceKeys, justify="center", anchor="center", font=("Arial", 25),
                             fg="white", background=mainOrange)
        bitsLabel.pack()

        baseText = "After that, Alice sends photons to Bob on different bases in quantum channel, Alice's bases are:"
        baseDescription = tk.Message(topFrame, text=baseText, justify="center", width=600, fg="white",
                                     background=mainOrange)
        baseDescription.pack()

        baseFrame = ctk.CTkFrame(master=mainFrame, fg_color=mainOrange)
        baseFrame.pack(fill=tk.BOTH, padx=5, pady=3)

        for base in info.aliceBases:
            imageName = './assets/diagonalbase.png' if base == "X" else './assets/rectilinearbase.png'
            imgSize = int((screenWidth * 0.45 - (16 * 4)) / 16)
            img = ctk.CTkImage(light_image=Image.open(imageName), dark_image=Image.open(imageName),
                               size=(imgSize, imgSize))
            imgLabel = ctk.CTkLabel(baseFrame, image=img, text="", fg_color="red")
            imgLabel.pack(side=tk.LEFT, padx=2, pady=5)

        self.frameList.append(mainFrame)

    def createSimFrame(self):
        frame = ctk.CTkFrame(master=self.midFrame,
                             width=int(screenWidth * 0.45),
                             fg_color="white", corner_radius=9)
        frame.pack(anchor=ctk.CENTER, fill=ctk.BOTH, pady=5, padx=16)

        self.innerFrame = ctk.CTkFrame(master=frame, fg_color=mainOrange, corner_radius=9)
        self.innerFrame.pack(fill=ctk.BOTH, expand=True, padx=5, pady=3)

        #self.innerFrame.grid_rowconfigure(1, weight=1)
        #self.innerFrame.grid_columnconfigure(6, weight=1)

        #self.innerFrame.columnconfigure(0, weight=1)
        #self.innerFrame.columnconfigure(1, weight=1)
        self.innerFrame.columnconfigure(2, weight=1)
        #self.innerFrame.columnconfigure(3, weight=1)
        #self.innerFrame.columnconfigure(4, weight=1)

        titleLabel1 = ctk.CTkLabel(self.innerFrame, text="Alice's Bit", corner_radius=9, fg_color=secondaryOrange, text_color="white",width=int(screenWidth * 0.07))
        titleLabel1.grid(row=0, column=0, padx=3, pady=3, sticky="nsew")

        titleLabel2 = ctk.CTkLabel(self.innerFrame, text="Alice's Base", corner_radius=9, fg_color=secondaryOrange, text_color="white",width=int(screenWidth * 0.07))
        titleLabel2.grid(row=0, column=1, padx=3, pady=3, sticky="nsew")

        titleLabel3 = ctk.CTkLabel(self.innerFrame, text="Explanation", corner_radius=9, fg_color=secondaryOrange, text_color="white")
        titleLabel3.grid(row=0, column=2, padx=3, pady=3, sticky="ew")

        titleLabel4 = ctk.CTkLabel(self.innerFrame, text="Bob's Base", corner_radius=9, fg_color=secondaryOrange, text_color="white",width=int(screenWidth * 0.07))
        titleLabel4.grid(row=0, column=3, padx=3, pady=3, sticky="nsew")

        titleLabel5 = ctk.CTkLabel(self.innerFrame, text="Bob's Bit", corner_radius=9, fg_color=secondaryOrange, text_color="white",width=int(screenWidth * 0.07))
        titleLabel5.grid(row=0, column=4, padx=3, pady=3, sticky="nsew")

        # ---------------------------------------------------

        # Alice's Bit
        defLabel1 = ctk.CTkLabel(self.innerFrame, text=measurementList[self.currentSimStage - 1].aliceBit,
                                 corner_radius=9, fg_color=secondaryOrange,text_color="white")
        defLabel1.grid(row=1, column=0, padx=3, pady=3, sticky="nsew")

        # Alice's Bases
        aliceImgPath = './assets/diagonalbase.png' if measurementList[self.currentSimStage - 1].aliceBase == "X" \
            else './assets/rectilinearbase.png'
        aliceImg = ctk.CTkImage(light_image=Image.open(aliceImgPath), dark_image=Image.open(aliceImgPath),
                                size=(int(screenWidth*0.03),int(screenWidth*0.03)))
        defLabel2 = ctk.CTkLabel(self.innerFrame, text="", image=aliceImg, corner_radius=9, fg_color=secondaryOrange)
        defLabel2.image = aliceImg
        defLabel2.grid(row=1, column=1, padx=3, pady=3, sticky="nsew")

        def3Frame = ctk.CTkFrame(self.innerFrame,fg_color=secondaryOrange,corner_radius=9)
        def3Frame.grid(row=1, column=2, padx=3, pady=3, sticky="ew")

        message = ("Same Base Choice for Alice and Bob.\n Bit added to the key"
                   if measurementList[self.currentSimStage - 1].result
                   else
                   "Different base choice for Alice and Bob.\n No bit added to the key")
        defLabel3 = tk.Message(def3Frame, text=message, justify="center", bg=secondaryOrange, aspect=300)
        defLabel3.pack()

        bobImgPath = './assets/diagonalbase.png' if measurementList[self.currentSimStage - 1].bobBase == "X" \
            else './assets/rectilinearbase.png'
        bobImg = ctk.CTkImage(light_image=Image.open(bobImgPath), dark_image=Image.open(bobImgPath),
                              size=(int(screenWidth*0.03),int(screenWidth*0.03)))

        defLabel4 = ctk.CTkLabel(self.innerFrame, text="", image=bobImg, corner_radius=9, fg_color=secondaryOrange)
        defLabel4.image = bobImg
        defLabel4.grid(row=1, column=3, padx=3, pady=3, sticky="nsew")

        def5Frame = ctk.CTkFrame(self.innerFrame,fg_color=secondaryOrange,corner_radius=9)
        def5Frame.grid(row=1, column=4, padx=3, pady=3, sticky="nsew")
        text = (measurementList[self.currentSimStage - 1].aliceBit
                if measurementList[self.currentSimStage - 1].result
                else
                "No Bit Received")
        defLabel5 = tk.Message(def5Frame, text=text, justify="center", bg=secondaryOrange ,aspect=160)
        defLabel5.pack(fill=tk.BOTH,expand=True,padx=4,pady=4)

        self.frameList.append(frame)

    def createSimResultFrame(self):
        mainFrame = ctk.CTkFrame(master=self.midFrame, width=int(screenWidth * 0.45), fg_color="white",
                                 corner_radius=9)
        mainFrame.pack(anchor=ctk.CENTER, fill=ctk.BOTH, pady=5, padx=16)

        topFrame = ctk.CTkFrame(master=mainFrame,fg_color=mainOrange)
        topFrame.pack(fill=tk.BOTH, padx=5, pady=3)
        resultText = "After measuring and comparing all qubits send by Alice to the Bob, Alice and Bob share their results on classical channel which can be hearable by anyone even Eve. As measurements show, generated key is:"
        resultDescription = tk.Message(topFrame, text=resultText, justify="center", width=int(screenWidth * 0.44),fg="white", background=mainOrange)
        resultDescription.pack(pady=3, padx=3)
        resultLabel = tk.Label(topFrame, text=info.resultKey, justify="center", anchor="center", font=("Arial", 25),fg="white", background=mainOrange)
        resultLabel.pack()

        baseText = "With this key, Alice and Bob can encrypt and decrypt files, messages or anything possible to transfer. Since quantum channel did not corrupted by any eavesdropper, It's secured."
        baseDescription = tk.Message(topFrame, text=baseText, justify="center", width=int(screenWidth * 0.44),fg="white", background=mainOrange)
        baseDescription.pack()

        self.frameList.append(mainFrame)

    def showNextFrame(self):
        # Increment the currentSimStage
        self.currentSimStage += 1

        if self.currentSimStage == 1:
            self.createSimInfoFrame()
        elif 1 < self.currentSimStage <= 16:
            self.createSimFrame()
        elif self.currentSimStage == 17:
            self.createSimResultFrame()
            # self.nextButton.config(state="disabled")
        else:
            print("end")

    def goToFirstPage(self):
        # Clear the data about previous simulation
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

        info.aliceKeys = aliceKey
        info.aliceBases = aliceTable
        info.resultKey = newAliceKey
    else:
        print("Key exchange has been tampered! Check for eavesdropper or try again")
        print("New Alice's key is invalid: ", newAliceKey)
        print("New Bob's key is invalid: ", newBobKey)


if __name__ == "__main__":
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

    # Create First Frame
    firstFrame = FirstFrame(root)
    firstFrame.pack_propagate(False)

    # Create Simulation Frame
    simulationFrame = SimulationFrame(root)
    simulationFrame.pack_propagate(False)
    simulationFrame.pack_forget()

    # Create Information Frame
    infoFrame = InfoFrame(root)
    infoFrame.pack_propagate(False)
    infoFrame.pack_forget()

    # Start the tkinter event loop
    root.mainloop()
