import tkinter as tk
import textwrap
import numpy as np
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute, BasicAer
from PIL import Image, ImageTk

screenWidth = 800
screenHeight = 800

n = 16
quantumRegister = QuantumRegister(n, name='qr')
classicalRegister = ClassicalRegister(n, name='cr')

measurementList = []


class simInfoClass:
    def __int__(self):
        self.aliceKeys = None
        self.aliceBases = None


info = simInfoClass()


class FirstFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, width=screenWidth, height=screenHeight, background='navy')
        self.pack()

        self.startButton = tk.Button(self, text="Start Simulation", command=self.goToSimPage)
        self.startButton.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.informationButton = tk.Button(self, text="Learn About BB84 Protocol! ", command=self.goToInfoPage)
        self.informationButton.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

    def goToSimPage(self):
        self.pack_forget()
        simulationFrame.pack()
        bb84Simulation()

    def goToInfoPage(self):
        self.pack_forget()
        infoFrame.pack()


class InfoFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, width=screenWidth, height=screenHeight, background='grey')
        self.pack()

        # Top Frame for buttons
        topFrame = tk.Frame(self, bg="grey")
        topFrame.pack(side=tk.TOP, padx=10, pady=10, anchor=tk.N, fill=tk.BOTH)

        # Create "Back" button
        self.backButton = tk.Button(topFrame, text="Back", command=self.goToFirstPage)
        self.backButton.pack(side=tk.LEFT)
        # Create "Next" button
        self.nextButton = tk.Button(topFrame, text="Next", command=self.goToInfo2Page)
        self.nextButton.pack(side=tk.RIGHT)

        # Frame for Information
        midFrame = tk.Frame(self, bg="grey")
        midFrame.pack(anchor=tk.CENTER, fill=tk.BOTH, expand=True)

        # Add text label
        text = "Quantum Key Distribution (QKD) is a method for securely distributing cryptographic keys between two parties - Alice and Bob - by using the principles of quantum mechanics. The BB84 protocol is one of the most well-known QKD protocols, developed by Charles Bennett and Gilles Brassard in 1984. The BB84 protocol works by using two quantum bits (qubits) - one to transmit the key and the other to verify its integrity. Alice randomly encodes the bits she wants to send to Bob using one of four possible states, which are chosen from two different bases. Each state represents a specific bit value, either a 0 or a 1. Bob then receives the encoded qubits and measures them in one of the two bases, chosen randomly. Once Bob has measured the qubits, Alice and Bob publicly compare the bases they used. If they used the same basis, Bob's measurement result reveals the value of the corresponding bit, and they can use it to form their shared secret key. If they used different bases, they discard the bit value and repeat the process until enough bits are obtained.The security of the BB84 protocol comes from the fact that any attempt to eavesdrop on the transmission will inevitably introduce errors that can be detected by Alice and Bob. According to the principles of quantum mechanics, any attempt to observe or measure a qubit will change its state, which can be detected by the parties. Thus, if an eavesdropper tries to intercept the qubits, they will introduce errors that will be detected during the verification process, allowing Alice and Bob to discard the affected bits and prevent the eavesdropper from obtaining any information about the key. QKD, and specifically the BB84 protocol, provides a method for securely distributing cryptographic keys that is resistant to interception or tampering. While still in its early stages of development, QKD has the potential to revolutionize the way in which secure communications are established and maintained, and it is an exciting area of research in both physics and computer science."
        textMessage = tk.Message(midFrame, text=text, width=600, justify="center", bg="grey")
        textMessage.pack(side=tk.TOP)

        # wrapper = textwrap.TextWrapper(width=100)  # set the maximum width for each line
        # wrapped_text = wrapper.fill(text)
        # text_label = tk.Label(mid_frame, text=wrapped_text, width=300,height=500, justify="center", anchor="w", background="grey")
        # text_label.pack(side=tk.TOP, padx=10, pady=10)

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
        tk.Frame.__init__(self, master, width=screenWidth, height=screenHeight, background='white')
        self.pack()

        # Add other widgets to the frame as needed
        topFrame = tk.Frame(self)
        topFrame.pack(side=tk.TOP, padx=10, pady=10, anchor=tk.NW)
        # Create "Back" button
        self.backButton = tk.Button(topFrame, text="Back", command=self.goToInfoPage)
        self.backButton.pack(side=tk.LEFT)
        # Create "Next" button
        self.nextButton = tk.Button(topFrame, text="Return to Homepage", command=self.goToFirstPage)
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


class SecondFrame(tk.Frame):
    currentSimStage = 0

    def __init__(self, master):
        tk.Frame.__init__(self, master, width=screenWidth, height=screenHeight)
        self.pack()

        # Create top frame for the "Back" button
        topFrame = tk.Frame(self, bg="green")
        topFrame.pack(fill=tk.BOTH)

        # Create "Back" button
        self.backButton = tk.Button(topFrame, text="Back", command=self.goToFirstPage)
        self.backButton.grid(row=0, column=0, sticky="NW")
        self.backButton.pack(anchor=tk.NW)

        # Create middle frame for simulation
        midFrame = tk.Frame(self, bg="yellow")
        midFrame.pack(fill=tk.BOTH, expand=True)
        midFrame.pack_propagate(False)

        # Create canvas for middle frame
        self.canvas = tk.Canvas(midFrame, bg="blue", scrollregion=(0, 0, 0, 4000))
        self.canvas.pack(fill=tk.BOTH, padx=1, pady=1, expand=True)
        self.canvas.pack_propagate(False)

        # Create Scrollbar for middle frame
        scrollbar = tk.Scrollbar(self.canvas, orient='vertical')
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        scrollbar.config(command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=scrollbar.set)

        # Create bottom frame for "Next" button
        bottomFrame = tk.Frame(self, bg="red")
        bottomFrame.pack(fill=tk.BOTH)

        # Create "Next" button
        self.nextButton = tk.Button(bottomFrame, text="Next", command=self.showNextFrame)
        self.nextButton.pack(anchor=tk.S)

        # Create Frame List for measurement frames
        self.frameList = []

    def createSimInfoFrame(self):
        mainFrame = tk.Frame(self.canvas, width=600, bg="yellow")
        mainFrame.pack()
        # frame.pack_propagate(False)

        topFrame = tk.Frame(mainFrame)
        topFrame.pack(fill=tk.BOTH)
        bitsText = "As information page about protocol, at first Alice generates a random set of bits. This time Alice's random bits are:"
        bitsDescription = tk.Message(topFrame, text=bitsText, justify="center", width=600)
        bitsDescription.pack()
        bitsLabel = tk.Label(topFrame, text=info.aliceKeys, justify="center", anchor="center", font=("Arial", 25))
        bitsLabel.pack()

        baseText = "After that, Alice sends photons to Bob on different bases in quantum channel, Alice's bases are:"
        baseDescription = tk.Message(topFrame, text=baseText, justify="center", width=600)
        baseDescription.pack()

        baseFrame = tk.Frame(mainFrame,bg="white",height=250)
        baseFrame.pack(fill=tk.BOTH,expand=True,ipadx=5)
        baseFrame.pack_propagate(False)

        i = 0
        for base in info.aliceBases:
            imageName = './assets/diagonalbase.png' if base == "X" else './assets/rectilinearbase.png'
            #img = Image.open(imageName)
            #img.resize((40,40),Image.LANCZOS)

            img = tk.PhotoImage(file=imageName)
            imgLabel = tk.Label(baseFrame, image=img,padx=5,bg="red")
            imgLabel.pack(side=tk.RIGHT)
            i =+ 1


        # baseLabel = tk.Label(frame, text=info.aliceBases, justify="center", anchor="center", font=("Arial", 25))
        # baseLabel.pack()

        self.frameList.append(mainFrame)

    def createSimFrame(self):
        frame = tk.Frame(self.canvas)
        frame.pack(ipadx=50, ipady=50)
        frame.pack_propagate(False)

        titleLabel1 = tk.Label(frame, text="Alice's Bit")
        titleLabel1.grid(row=0, column=0)

        titleLabel2 = tk.Label(frame, text="Alice's Base")
        titleLabel2.grid(row=0, column=1)

        titleLabel3 = tk.Label(frame, text="Explanation")
        titleLabel3.grid(row=0, column=2)

        titleLabel4 = tk.Label(frame, text="Bob's Base")
        titleLabel4.grid(row=0, column=3)

        titleLabel5 = tk.Label(frame, text="Bob's Bit")
        titleLabel5.grid(row=0, column=4)

        # ---------------------------------------------------

        # Alice's Bit
        defLabel1 = tk.Label(frame, text=measurementList[self.currentSimStage - 1].aliceBit)
        defLabel1.grid(row=1, column=0)

        # Alice's Bases
        defLabel2 = tk.Label(frame, text=measurementList[self.currentSimStage - 1].aliceBase)
        defLabel2.grid(row=1, column=1)

        message = ("Same Base Choice for Alice and Bob, Bit added to the key"
                   if measurementList[self.currentSimStage - 1].result
                   else
                   "Different base choice for Alice and Bob, no bit added to the key")
        defLabel3 = tk.Message(frame, text=message, width=300, justify="center")
        defLabel3.grid(row=1, column=2)

        defLabel4 = tk.Label(frame, text=measurementList[self.currentSimStage - 1].bobBase)
        defLabel4.grid(row=1, column=3)

        text = (measurementList[self.currentSimStage - 1].aliceBit
                if measurementList[self.currentSimStage - 1].result
                else
                "No Bit Received")
        defLabel5 = tk.Message(frame, text=text, justify="center")
        defLabel5.grid(row=1, column=4)

        # Put Frame into list
        self.frameList.append(frame)

    def showNextFrame(self):
        # Increment the currentSimStage
        self.currentSimStage += 1

        if self.currentSimStage == 1:
            self.createSimInfoFrame()
            self.canvas.create_window(380, 150, anchor="center", window=self.frameList[0])
        else:
            self.createSimFrame()
            self.canvas.create_window(380, 300 + ((self.currentSimStage - 2) * 100),
                                      anchor="center",
                                      window=self.frameList[self.currentSimStage - 1],
                                      tags="measurementFrame")

        # Put Frame in window at canvas

    def goToFirstPage(self):
        # Clear the data about previous simulation
        self.canvas.delete('measurementFrame')

        measurementList.clear()
        self.currentSimStage = 0

        self.frameList.clear()

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

    # Command for full screen option
    # root.attributes('-fullscreen', True)

    root.resizable(False, False)

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
