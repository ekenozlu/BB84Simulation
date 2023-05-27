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
                                              text="2. About QKD",
                                              fg_color=mainBlue, hover_color=secondaryBlue,
                                              border_color="white", border_width=1, border_spacing=5)
        self.secondPageButton.grid(row=1, column=0, sticky="ew", padx=4, pady=4)

        self.thirdPageButton = ctk.CTkButton(self.navigationFrame, command=self.thirdInfoAction,
                                             text="3. How BB84 Works?",
                                             fg_color=mainBlue, hover_color=secondaryBlue,
                                             border_color="white", border_width=1, border_spacing=5)
        self.thirdPageButton.grid(row=2, column=0, sticky="ew", padx=4, pady=4)

        self.forthPageButton = ctk.CTkButton(self.navigationFrame, command=self.forthInfoAction,
                                             text="4. Example Table",
                                             fg_color=mainBlue, hover_color=secondaryBlue,
                                             border_color="white", border_width=1, border_spacing=5)
        self.forthPageButton.grid(row=3, column=0, sticky="ew", padx=4, pady=4)

        # -----------------------------------------

        # Create a general frame for information
        self.generalInfoFrame = ctk.CTkFrame(self.gridFrame, corner_radius=9, fg_color=secondaryOrange)
        self.generalInfoFrame.grid(row=0, column=1, rowspan=2, sticky="nsew", padx=4, pady=4)

        # First Info Frame
        self.InfoFrameIntroduction = ctk.CTkFrame(self.generalInfoFrame, corner_radius=9, fg_color=secondaryOrange)
        text = "\nQuantum Key Distribution (QKD) and the BB84 protocol represent groundbreaking advancements in the field of secure communication. In an era where data breaches and cyberattacks are increasingly prevalent, QKD offers a promising solution by harnessing the principles of quantum mechanics to establish unbreakable cryptographic keys. At the heart of this technology lies the BB84 protocol, a pioneering method developed by Charles Bennett and Gilles Brassard in 1984.\n\nQKD leverages the bizarre and counterintuitive properties of quantum mechanics to provide an unparalleled level of security. Unlike classical encryption algorithms that rely on computational complexity, QKD achieves its security through the fundamental laws of physics. By leveraging the principles of quantum superposition and uncertainty, QKD ensures that any attempt to intercept or tamper with the communication will inevitably be detected.\n\nThe BB84 protocol serves as a fundamental building block of QKD. It provides a robust framework for generating, transmitting, and verifying cryptographic keys between two parties, commonly referred to as Alice and Bob. Through a series of carefully orchestrated steps, BB84 enables the creation of a shared secret key that can be used to encrypt and decrypt messages securely.\n\nQKD and the BB84 protocol have the potential to revolutionize secure communication in various domains, including finance, government, and defense. The unbreakable security offered by QKD opens up new avenues for confidential and reliable information exchange, paving the way for a future where data can be transmitted and stored with absolute confidence.\n\nIn this educative simulation, we will delve deeper into the intricacies of QKD and explore the inner workings of the BB84 protocol. By understanding the principles and mechanisms underlying this revolutionary technology, we aim to empower you with the knowledge to appreciate and apply the immense potential of quantum secure communication."
        textMessage = tk.Message(self.InfoFrameIntroduction, text=text,
                                 width=int(screenWidth * 0.35),
                                 justify="left", bg=secondaryOrange)
        textMessage.pack(side=tk.TOP, padx=1, pady=4)

        # QKD Info Frame
        self.InfoFrameQKD = ctk.CTkFrame(self.generalInfoFrame, corner_radius=9, fg_color=secondaryOrange)
        text = "\nQuantum Key Distribution (QKD) is an innovative cryptographic technology that relies on the principles of quantum physics to establish secure communication channels. At its core, QKD takes advantage of the unique properties exhibited by quantum systems, such as superposition and entanglement. Quantum physics, also known as quantum mechanics, is the branch of physics that describes the behavior of particles at the atomic and subatomic levels. It challenges classical physics by introducing principles that are fundamentally different from everyday experiences. Superposition allows particles to exist in multiple states simultaneously, while measurement collapses the superposition into a single state. Quantum entanglement enables correlations between particles even at a distance.\n\nThe security of QKD is derived from the fact that any attempt to observe or measure the qubits during transmission will disturb their quantum states, revealing the presence of an eavesdropper. This fundamental principle of quantum physics ensures the confidentiality and integrity of the exchanged cryptographic keys.\n\nQKD represents a paradigm shift in secure communication, offering unconditional security based on the laws of quantum physics. QKD provides a robust framework for secure communication in a world increasingly challenged by sophisticated cyber threats. Ongoing research continues to advance QKD and its practical implementations, bringing us closer to a future where secure communication is guaranteed through the principles of quantum physics.\n\nQKD protocols are fundamental frameworks that govern the secure exchange of cryptographic keys between two parties in Quantum Key Distribution. These protocols provide step-by-step procedures to ensure the confidentiality and integrity of the key exchange process. Notable QKD protocols include the BB84 protocol, which uses quantum states and random basis measurements, and the E91 protocol, which relies on entangled particles to establish secure keys. Other protocols like the B92, SARG04, and DPS protocols offer alternative approaches to address specific challenges or optimize certain aspects of QKD. Each protocol has its unique characteristics, strengths, and limitations, contributing to the diverse landscape of secure quantum communication."
        textMessage = tk.Message(self.InfoFrameQKD, text=text,
                                 width=int(screenWidth * 0.35),
                                 justify="left", bg=secondaryOrange)
        textMessage.pack(side=tk.TOP, padx=1, pady=4)

        # BB84 Info Frame
        self.InfoFrameBB84 = ctk.CTkFrame(self.generalInfoFrame, corner_radius=9, fg_color=secondaryOrange)
        text = "\nThe BB84 protocol, devised by Bennett and Brassard in 1984, is a highly influential Quantum Key Distribution (QKD) protocol that facilitates secure key exchange between two parties, commonly known as Alice and Bob. It encompasses several crucial steps, including key generation, quantum encoding, transmission, basis measurement, announcement, comparison, error estimation, and key distillation.\n\n In BB84, Alice generates a random sequence of binary bits that she encodes into quantum states, using two mutually unbiased bases: rectilinear (Z) and diagonal (X). She then transmits the encoded qubits to Bob through a quantum channel. Upon receiving the qubits, Bob randomly selects a measurement basis for each qubit and performs measurements accordingly. He publicly announces the bases he used. Alice and Bob then compare a subset of their measurement results, discarding inconsistent ones due to mismatched bases. By estimating the error rate, they can identify potential eavesdropping attempts. Finally, Alice and Bob perform error correction and privacy amplification to distill a shared cryptographic key.\n\n \n\n"
        textMessage = tk.Message(self.InfoFrameBB84, text=text,
                                 width=int(screenWidth * 0.35),
                                 justify="left", bg=secondaryOrange)
        textMessage.pack(side=tk.TOP, padx=1, pady=4)

        # Table Info Frame
        self.InfoFrameTable = ctk.CTkFrame(self.generalInfoFrame, corner_radius=9, fg_color=secondaryOrange)
        image = Image.open('./assets/imagee.jpeg')
        image = image.resize((int(screenWidth * 0.35), int(screenHeight * 0.3)), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        imageLabel = tk.Label(self.InfoFrameTable, image=photo)
        imageLabel.image = photo
        imageLabel.pack(side=tk.TOP, padx=1, pady=1, anchor=tk.N)

        # -----------------------------------------
        # Show Default Frame
        self.showInfoFrameByName("1")

    def firstInfoAction(self):
        self.showInfoFrameByName("1")

    def secondInfoAction(self):
        self.showInfoFrameByName("2")

    def thirdInfoAction(self):
        self.showInfoFrameByName("3")

    def forthInfoAction(self):
        self.showInfoFrameByName("4")

    def showInfoFrameByName(self, name):
        # Show selected frame
        if name == "1":
            self.InfoFrameIntroduction.pack(fill=ctk.BOTH, expand=True, padx=4, pady=4)
        else:
            self.InfoFrameIntroduction.pack_forget()
        if name == "2":
            self.InfoFrameQKD.pack(fill=ctk.BOTH, expand=True, padx=4, pady=4)
        else:
            self.InfoFrameQKD.pack_forget()
        if name == "3":
            self.InfoFrameBB84.pack(fill=ctk.BOTH, expand=True, padx=4, pady=4)
        else:
            self.InfoFrameBB84.pack_forget()
        if name == "4":
            self.InfoFrameTable.pack(fill=ctk.BOTH, expand=True, padx=4, pady=4)
        else:
            self.InfoFrameTable.pack_forget()

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

        self.innerFrame.columnconfigure(2, weight=1)

        titleLabel1 = ctk.CTkLabel(self.innerFrame, text="Alice's Bit", corner_radius=9, fg_color=secondaryOrange,
                                   text_color="white", width=int(screenWidth * 0.07))
        titleLabel1.grid(row=0, column=0, padx=3, pady=3, sticky="nsew")

        titleLabel2 = ctk.CTkLabel(self.innerFrame, text="Alice's Base", corner_radius=9, fg_color=secondaryOrange,
                                   text_color="white", width=int(screenWidth * 0.07))
        titleLabel2.grid(row=0, column=1, padx=3, pady=3, sticky="nsew")

        titleLabel3 = ctk.CTkLabel(self.innerFrame, text="Explanation", corner_radius=9, fg_color=secondaryOrange,
                                   text_color="white")
        titleLabel3.grid(row=0, column=2, padx=3, pady=3, sticky="ew")

        titleLabel4 = ctk.CTkLabel(self.innerFrame, text="Bob's Base", corner_radius=9, fg_color=secondaryOrange,
                                   text_color="white", width=int(screenWidth * 0.07))
        titleLabel4.grid(row=0, column=3, padx=3, pady=3, sticky="nsew")

        titleLabel5 = ctk.CTkLabel(self.innerFrame, text="Bob's Bit", corner_radius=9, fg_color=secondaryOrange,
                                   text_color="white", width=int(screenWidth * 0.07))
        titleLabel5.grid(row=0, column=4, padx=3, pady=3, sticky="nsew")

        # ---------------------------------------------------

        # Alice's Bit
        defLabel1 = ctk.CTkLabel(self.innerFrame, text=measurementList[self.currentSimStage - 1].aliceBit,
                                 corner_radius=9, fg_color=secondaryOrange, text_color="white")
        defLabel1.grid(row=1, column=0, padx=3, pady=3, sticky="nsew")

        # Alice's Bases
        aliceImgPath = './assets/diagonalbase.png' if measurementList[self.currentSimStage - 1].aliceBase == "X" \
            else './assets/rectilinearbase.png'
        aliceImg = ctk.CTkImage(light_image=Image.open(aliceImgPath), dark_image=Image.open(aliceImgPath),
                                size=(int(screenWidth * 0.03), int(screenWidth * 0.03)))
        defLabel2 = ctk.CTkLabel(self.innerFrame, text="", image=aliceImg, corner_radius=9, fg_color=secondaryOrange)
        defLabel2.image = aliceImg
        defLabel2.grid(row=1, column=1, padx=3, pady=3, sticky="nsew")

        def3Frame = ctk.CTkFrame(self.innerFrame, fg_color=secondaryOrange, corner_radius=9)
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
                              size=(int(screenWidth * 0.03), int(screenWidth * 0.03)))

        defLabel4 = ctk.CTkLabel(self.innerFrame, text="", image=bobImg, corner_radius=9, fg_color=secondaryOrange)
        defLabel4.image = bobImg
        defLabel4.grid(row=1, column=3, padx=3, pady=3, sticky="nsew")

        def5Frame = ctk.CTkFrame(self.innerFrame, fg_color=secondaryOrange, corner_radius=9)
        def5Frame.grid(row=1, column=4, padx=3, pady=3, sticky="nsew")
        text = (measurementList[self.currentSimStage - 1].aliceBit
                if measurementList[self.currentSimStage - 1].result
                else
                "No Bit Received")
        defLabel5 = tk.Message(def5Frame, text=text, justify="center", bg=secondaryOrange, aspect=160)
        defLabel5.pack(fill=tk.BOTH, expand=True, padx=4, pady=4)

        # ---------------------------------------------------

        bottomFrame = ctk.CTkFrame(self.innerFrame, fg_color=secondaryOrange, corner_radius=9)
        bottomFrame.grid(row=2, column=0, columnspan=5, padx=3, pady=3, sticky="nsew")

        keyListToString = ''.join(map(str, measurementList[self.currentSimStage - 1].frameKey))
        keyDescriptionLabel = ctk.CTkLabel(master=bottomFrame, text=("Current key is:" "\n" + keyListToString),
                                           text_color="white")
        keyDescriptionLabel.pack(anchor=ctk.CENTER)

        self.frameList.append(frame)

    def createSimResultFrame(self):
        mainFrame = ctk.CTkFrame(master=self.midFrame, width=int(screenWidth * 0.45), fg_color="white",
                                 corner_radius=9)
        mainFrame.pack(anchor=ctk.CENTER, fill=ctk.BOTH, pady=5, padx=16)

        topFrame = ctk.CTkFrame(master=mainFrame, fg_color=mainOrange)
        topFrame.pack(fill=tk.BOTH, padx=5, pady=3)
        resultText = "After measuring and comparing all qubits send by Alice to the Bob, Alice and Bob share their results on classical channel which can be hearable by anyone even Eve. As measurements show, generated key is:"
        resultDescription = tk.Message(topFrame, text=resultText, justify="center", width=int(screenWidth * 0.44),
                                       fg="white", background=mainOrange)
        resultDescription.pack(pady=3, padx=3)
        resultLabel = tk.Label(topFrame, text=info.resultKey, justify="center", anchor="center", font=("Arial", 25),
                               fg="white", background=mainOrange)
        resultLabel.pack()

        baseText = "With this key, Alice and Bob can encrypt and decrypt files, messages or anything possible to transfer. Since quantum channel did not corrupted by any eavesdropper, It's secured."
        baseDescription = tk.Message(topFrame, text=baseText, justify="center", width=int(screenWidth * 0.44),
                                     fg="white", background=mainOrange)
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
    def __init__(self, qubitNo, aliceBit, aliceBase, bobBase, result, frameKey):
        self.qubitNo = qubitNo
        self.aliceBit = aliceBit
        self.aliceBase = aliceBase
        self.bobBase = bobBase
        self.result = result
        self.frameKey = frameKey

    def printResult(self):
        if self.result:
            print("Qubit No:{}, Same choice on basis: {}, Bit added to the Key: {}, Current Key is: {}".format(
                self.qubitNo,
                self.aliceBase,
                self.aliceBit,
                self.frameKey))
        else:
            print(
                "Qubit No:{}, Different Choice, Alice has {}, Bob has {}, No Bit added to the Key, No change on Key".format(
                    self.qubitNo,
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
    tempKeyArray = []
    for qubit, basis in enumerate(zip(aliceTable, bobTable)):
        if basis[0] == basis[1]:
            tempKeyArray.append(aliceKey[qubit])
            measurementList.append(MeasurementFrame(qubitNo=qubit,
                                                    aliceBit=aliceKey[qubit],
                                                    aliceBase=basis[0],
                                                    bobBase=basis[1],
                                                    result=True,
                                                    frameKey=tempKeyArray))
            keptBits.append(qubit)
        else:
            measurementList.append(MeasurementFrame(qubitNo=qubit,
                                                    aliceBit=aliceKey[qubit],
                                                    aliceBase=basis[0],
                                                    bobBase=basis[1],
                                                    result=False,
                                                    frameKey=tempKeyArray))
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
