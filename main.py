'''
This simulation was designed and developed by Eken Özlü, Melisa Çevik and Elin Su Şentürk
for the 2022-2023 academic year Capstone Project of Quantum Key Distribution.
The purpose of the simulations is demonstrating the properties of BB84 Protocol
for those who want to gain knowledge on the topic.
'''

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

textFont = ('Arial', 14)
textFontBold = ('Arial', 14, 'bold')
titleFont = ('Arial', 18)
titleFontBold = ('Arial', 18, 'bold')
bigFont = ('Arial', 26)
bigFontBold = ('Arial', 26, 'bold')

measurementList = []


class SimInfoClass:
    def __int__(self):
        self.aliceKeys = None
        self.aliceBases = None
        self.bobBases = None
        self.resultKey = None


info = SimInfoClass()


class FirstFrame(ctk.CTkFrame):
    bitSize = 16

    def __init__(self, master):
        ctk.CTkFrame.__init__(self, master,
                              width=int(screenWidth * 0.75), height=int(screenHeight * 0.85),
                              fg_color=mainOrange)
        self.pack()
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_propagate(False)

        self.mainTopFrame = ctk.CTkFrame(master=self, corner_radius=9, fg_color=mainOrange)
        self.mainTopFrame.grid(row=0, column=0, sticky="nsew", padx=4, pady=4)

        image = Image.open("assets/simulation_logo.jpg")
        image = image.resize((int(screenHeight * 0.6), int(screenHeight * 0.3)), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(self.mainTopFrame, image=photo,background=mainOrange)
        image_label.image = photo
        image_label.pack(side=tk.TOP, padx=1, pady=1, anchor=tk.N)

        self.mainMiddleFrame = ctk.CTkFrame(master=self, fg_color="white", corner_radius=9,
                                            width=int(screenWidth * 0.75), height=int(screenHeight * 0.27))
        self.mainMiddleFrame.grid(row=1, column=0, sticky="nsew", padx=4, pady=4)

        self.topButtonFrame = ctk.CTkFrame(master=self.mainMiddleFrame, fg_color=secondaryOrange, corner_radius=9)
        self.topButtonFrame.pack(fill=tk.BOTH, padx=5, pady=3, expand=True)

        self.sliderValueLabel = ctk.CTkLabel(master=self.topButtonFrame,
                                             text_color="white", font=titleFontBold,
                                             text=("Bit Length for Simulation: " + str(round(self.bitSize))))
        self.sliderValueLabel.pack(anchor=ctk.CENTER, pady=10)

        self.simulationBitSlider = ctk.CTkSlider(master=self.topButtonFrame, command=self.simSliderEvent,
                                                 width=int(screenWidth * 0.18),
                                                 from_=4, to=22,
                                                 number_of_steps=19,
                                                 fg_color=secondaryBlue, progress_color=mainBlue)
        self.simulationBitSlider.pack(anchor=ctk.CENTER)
        self.simulationBitSlider.set(self.bitSize)

        self.startButton = ctk.CTkButton(master=self.topButtonFrame, command=self.goToSimPage,
                                         width=int(screenWidth * 0.18), height=int(screenHeight * 0.05),
                                         text="Start Simulation",
                                         text_color="white", font=titleFontBold,
                                         fg_color=mainBlue, hover_color=secondaryBlue,
                                         border_color="white", border_width=1)
        self.startButton.pack(anchor=ctk.CENTER, pady=10)

        self.bottomButtonFrame = ctk.CTkFrame(master=self.mainMiddleFrame, fg_color=secondaryOrange, corner_radius=9)
        self.bottomButtonFrame.pack(fill=tk.BOTH, padx=5, pady=3)

        self.informationButton = ctk.CTkButton(master=self.bottomButtonFrame, command=self.goToInfoPage,
                                               width=int(screenWidth * 0.18), height=int(screenHeight * 0.05),
                                               text="Learn About BB84 Protocol",
                                               text_color="white", font=titleFontBold,
                                               fg_color=mainBlue, hover_color=secondaryBlue,
                                               border_color="white", border_width=1)
        self.informationButton.pack(anchor=ctk.CENTER, pady=20)

        self.mainBottomFrame = ctk.CTkFrame(master=self, fg_color=mainOrange, corner_radius=9,
                                            width=int(screenWidth * 0.75), height=int(screenHeight * 0.27))
        self.mainBottomFrame.grid(row=2, column=0, sticky="nsew", padx=4, pady=4)

        creditText = "This simulation was designed and developed by Eken Özlü, Melisa Çevik and Elin Su Şentürk for the 2022-2023 academic year Capstone Project of Quantum Key Distribution." \
                     "\nThe purpose of the simulations is demonstrating the properties of BB84 Protocol for those who want to gain knowledge on the topic."
        self.bottomMessage = tk.Message(self.mainBottomFrame, text=creditText,
                                 foreground="white", font=textFont,
                                 width=int(screenWidth * 0.6),
                                 justify="center", bg=mainOrange)
        self.bottomMessage.pack(side=ctk.BOTTOM, anchor=ctk.S, pady=4)

    def simSliderEvent(self, value):
        self.bitSize = round(value)
        self.sliderValueLabel.configure(
            text=("Bit Length for Simulation: " + str(round(self.simulationBitSlider.get()))))

    def goToSimPage(self):
        self.pack_forget()
        BB84Simulation(self.bitSize)
        simulationFrame.pack()

    def goToInfoPage(self):
        self.pack_forget()
        infoFrame.grid()


class InfoFrame(ctk.CTkFrame):
    def __init__(self, master):
        ctk.CTkFrame.__init__(self, master,
                              width=int(screenWidth * 0.75), height=int(screenHeight * 0.85),
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
                                        text_color="white", font=textFontBold,
                                        fg_color=mainBlue, hover_color=secondaryBlue,
                                        border_color="white", border_width=1, border_spacing=5)
        self.backButton.pack(anchor=ctk.NW, fill=ctk.BOTH, padx=4, pady=4)

        # Create a Navigation Frame
        self.navigationFrame = ctk.CTkFrame(self.gridFrame, corner_radius=9, fg_color=secondaryOrange)
        self.navigationFrame.grid(row=1, column=0, sticky="nsew", padx=4, pady=4)
        self.navigationFrame.grid_rowconfigure(6, weight=1)

        self.pageButton1 = ctk.CTkButton(self.navigationFrame, command=self.infoAction1,
                                         text="1. About Simulation",
                                         text_color="white", font=textFontBold, anchor="w",
                                         fg_color=mainBlue, hover_color=secondaryBlue,
                                         border_color="white", border_width=1, border_spacing=5)
        self.pageButton1.grid(row=0, column=0, sticky="ew", padx=4, pady=4)

        self.pageButton2 = ctk.CTkButton(self.navigationFrame, command=self.infoAction2,
                                         text="2. Introduction",
                                         text_color="white", font=textFontBold, anchor="w",
                                         fg_color=mainBlue, hover_color=secondaryBlue,
                                         border_color="white", border_width=1, border_spacing=5)
        self.pageButton2.grid(row=1, column=0, sticky="ew", padx=4, pady=4)

        self.pageButton3 = ctk.CTkButton(self.navigationFrame, command=self.infoAction3,
                                         text="3. About QKD",
                                         text_color="white", font=textFontBold, anchor="w",
                                         fg_color=mainBlue, hover_color=secondaryBlue,
                                         border_color="white", border_width=1, border_spacing=5)
        self.pageButton3.grid(row=2, column=0, sticky="ew", padx=4, pady=4)

        self.pageButton4 = ctk.CTkButton(self.navigationFrame, command=self.infoAction4,
                                         text="4. How BB84 Works?",
                                         text_color="white", font=textFontBold, anchor="w",
                                         fg_color=mainBlue, hover_color=secondaryBlue,
                                         border_color="white", border_width=1, border_spacing=5)
        self.pageButton4.grid(row=3, column=0, sticky="ew", padx=4, pady=4)

        self.pageButton5 = ctk.CTkButton(self.navigationFrame, command=self.infoAction5,
                                         text="5. Example Table",
                                         text_color="white", font=textFontBold, anchor="w",
                                         fg_color=mainBlue, hover_color=secondaryBlue,
                                         border_color="white", border_width=1, border_spacing=5)
        self.pageButton5.grid(row=4, column=0, sticky="ew", padx=4, pady=4)

        # -----------------------------------------

        # Create a general frame for information
        self.generalInfoFrame = ctk.CTkFrame(self.gridFrame, corner_radius=9, fg_color=secondaryOrange)
        self.generalInfoFrame.grid(row=0, column=1, rowspan=2, sticky="nsew", padx=4, pady=4)

        # Simulation Info Frame
        self.InfoFrameSim = ctk.CTkFrame(self.generalInfoFrame, corner_radius=9, fg_color=secondaryOrange)
        text1 = "\nWe tried to create an educative simulation where we explore the fascinating world of Quantum Key Distribution (QKD) and delve into the inner workings of the BB84 protocol. Our aim is to provide you with a comprehensive understanding of this revolutionary technology, empowering you to appreciate and harness the immense potential of quantum secure communication." \
                "\n\nWhen you launch the application, you will be greeted by the main screen, which features two buttons and a slider. The first button takes you to the simulation page, where you can explore the step-by-step process of the protocol. The second button leads you to the information page, which provides detailed explanations about the protocol itself. The slider gives you the opportunity to choose the bit length to be used in the simulation." \
                "\n\nLet's start with the simulation page. Here, you can progress through the simulation steps by clicking a button. Each step will display relevant information, allowing you to understand the progress and outcomes of the simulation. You have the flexibility to go back to the main screen whenever necessary or when the simulation is completed by using the “back” button on the top left side of the screen." \
                "\n\nThe simulation page includes a “next” button for controlling the simulation steps, allowing you to move forward at your own pace. With each click, you will see a new frame in a scrollable area, providing insights into each bit's step in the simulation." \
                "\n\nWithin the frame, you will find information about the random bit selected by Alice (the sender) and the corresponding random base. The same information is presented for Bob (the receiver). Additionally, the frame offers a brief explanation of the result for the current step of measurement, helping you grasp the significance of each step." \
                "\n\nOn the information page, we have prepared a tabbed layout with different title buttons representing various subtopics. By selecting each button, you can access detailed pages that delve into specific aspects of the protocol. We highly recommend beginners to explore this page first, as it will provide a solid foundation of knowledge before engaging with the simulation." \
                "\n\nThrough this simulation, we aim to enhance your understanding of QKD and the BB84 protocol, enabling you to appreciate the groundbreaking potential of quantum secure communication. So, let's dive in and unlock the secrets of this cutting-edge technology!"
        textMessage = tk.Message(self.InfoFrameSim, text=text1,
                                 foreground="white", font=textFont,
                                 width=int(screenWidth * 0.6),
                                 justify="left", bg=secondaryOrange)
        textMessage.pack(side=ctk.LEFT, anchor=ctk.N, padx=4, pady=4)

        # Introduction Info Frame
        self.InfoFrameIntroduction = ctk.CTkFrame(self.generalInfoFrame, corner_radius=9, fg_color=secondaryOrange)
        text1 = "\nQuantum Key Distribution (QKD) and the BB84 protocol represent groundbreaking advancements in the field of secure communication. In an era where data breaches and cyberattacks are increasingly prevalent, QKD offers a promising solution by harnessing the principles of quantum mechanics to establish unbreakable cryptographic keys. At the heart of this technology lies the BB84 protocol, a pioneering method developed by Gilles Brassard and Charles Bennett in 1984."
        text2 = "QKD leverages the bizarre and counterintuitive properties of quantum mechanics to provide an unparalleled level of security. Unlike classical encryption algorithms that rely on computational complexity, QKD achieves its security through the fundamental laws of physics. By leveraging the principles of quantum superposition and uncertainty, QKD ensures that any attempt to intercept or tamper with the communication will inevitably be detected."
        text3 = "The BB84 protocol serves as a fundamental building block of QKD. It provides a robust framework for generating, transmitting, and verifying cryptographic keys between two parties, commonly referred to as Alice and Bob. Through a series of carefully orchestrated steps, BB84 enables the creation of a shared secret key that can be used to encrypt and decrypt messages securely."
        textMessage1 = tk.Message(self.InfoFrameIntroduction, text=text1,
                                 foreground="white", font=textFont,
                                 width=int(screenWidth * 0.6),
                                 justify="left", bg=secondaryOrange)
        textMessage1.pack(fill=ctk.BOTH, padx=4, pady=4)

        image = Image.open('assets/infopage_photo1.jpg')
        image = image.resize((int(screenWidth * 0.3), int(screenWidth * 0.21)), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        imageText = "Gilles Brassard and Charles H. Bennett in order \n src: https://perimeterinstitute.ca/news/quantum-computing-pioneers-earn-breakthrough-prize"
        imageLabel = tk.Label(self.InfoFrameIntroduction,
                              image=photo, background=secondaryOrange,
                              text=imageText, compound="top")
        imageLabel.image = photo
        imageLabel.pack(side=tk.TOP, padx=2, pady=2, anchor=tk.N)

        textMessage2 = tk.Message(self.InfoFrameIntroduction, text=text2,
                                 foreground="white", font=textFont,
                                 width=int(screenWidth * 0.6),
                                 justify="left", bg=secondaryOrange)
        textMessage2.pack(fill=ctk.BOTH, padx=4, pady=4)
        textMessage3 = tk.Message(self.InfoFrameIntroduction, text=text3,
                                 foreground="white", font=textFont,
                                 width=int(screenWidth * 0.6),
                                 justify="left", bg=secondaryOrange)
        textMessage3.pack(fill=ctk.BOTH, padx=4, pady=4)

        # QKD Info Frame
        self.InfoFrameQKD = ctk.CTkFrame(self.generalInfoFrame, corner_radius=9, fg_color=secondaryOrange)
        text1 = "\nQuantum Key Distribution (QKD) is an innovative cryptographic technology that relies on the principles of quantum physics to establish secure communication channels. At its core, QKD takes advantage of the unique properties exhibited by quantum systems, such as superposition and entanglement. Quantum physics, also known as quantum mechanics, is the branch of physics that describes the behavior of particles at the atomic and subatomic levels. It challenges classical physics by introducing principles that are fundamentally different from everyday experiences. Superposition allows particles to exist in multiple states simultaneously, while measurement collapses the superposition into a single state. Quantum entanglement enables correlations between particles even at a distance."
        text2 = "The security of QKD is derived from the fact that any attempt to observe or measure the qubits during transmission will disturb their quantum states, revealing the presence of an eavesdropper. This fundamental principle of quantum physics ensures the confidentiality and integrity of the exchanged cryptographic keys."
        text3 = "QKD represents a paradigm shift in secure communication, offering unconditional security based on the laws of quantum physics. It provides a robust framework for secure communication in a world increasingly challenged by sophisticated cyber threats, advancing us toward a future where secure communication is guaranteed through the principles of quantum physics. With the potential to revolutionize secure communication in domains such as finance, government, and defense, QKD and the BB84 protocol offer unbreakable security, opening new avenues for confidential and reliable information exchange and paving the way for a future where data can be transmitted and stored with absolute confidence."
        text4 = "QKD protocols are fundamental frameworks that govern the secure exchange of cryptographic keys between two parties in Quantum Key Distribution. These protocols provide step-by-step procedures to ensure the confidentiality and integrity of the key exchange process. Notable QKD protocols include the BB84 protocol, which uses quantum states and random basis measurements, and the E91 protocol, which relies on entangled particles to establish secure keys. Other protocols like the B92, SARG04, and DPS protocols offer alternative approaches to address specific challenges or optimize certain aspects of QKD. Each protocol has its unique characteristics, strengths, and limitations, contributing to the diverse landscape of secure quantum communication."
        textMessage1 = tk.Message(self.InfoFrameQKD, text=text1,
                                 foreground="white", font=textFont,
                                 width=int(screenWidth * 0.6),
                                 justify="left", bg=secondaryOrange)
        textMessage1.pack(fill=ctk.BOTH, padx=4, pady=4)

        textMessage2 = tk.Message(self.InfoFrameQKD, text=text2,
                                 foreground="white", font=textFont,
                                 width=int(screenWidth * 0.6),
                                 justify="left", bg=secondaryOrange)
        textMessage2.pack(fill=ctk.BOTH, padx=4, pady=4)

        image = Image.open('assets/infopage_photo2.jpg')
        image = image.resize((int(screenWidth * 0.3), int(screenWidth * 0.15)), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        imageLabel = tk.Label(self.InfoFrameQKD,
                              image=photo, background=secondaryOrange,
                              text="src: https://governmenttechnologyinsider.com/quantum-key-distribution-podcast-on-securing-future-network-communications/", compound="top")
        imageLabel.image = photo
        imageLabel.pack(side=tk.TOP, padx=2, pady=2, anchor=tk.N)

        textMessage3 = tk.Message(self.InfoFrameQKD, text=text3,
                                  foreground="white", font=textFont,
                                  width=int(screenWidth * 0.6),
                                  justify="left", bg=secondaryOrange)
        textMessage3.pack(fill=ctk.BOTH, padx=4, pady=4)

        textMessage4 = tk.Message(self.InfoFrameQKD, text=text4,
                                  foreground="white", font=textFont,
                                  width=int(screenWidth * 0.6),
                                  justify="left", bg=secondaryOrange)
        textMessage4.pack(fill=ctk.BOTH, padx=4, pady=4)

        # BB84 Info Frame
        self.InfoFrameBB84 = ctk.CTkFrame(self.generalInfoFrame, corner_radius=9, fg_color=secondaryOrange)
        text1 = "\nThe BB84 protocol, devised by Bennett and Brassard in 1984, is a highly influential Quantum Key Distribution (QKD) protocol that facilitates secure key exchange between two parties, commonly known as Alice and Bob. It encompasses several crucial steps, including key generation, quantum encoding, transmission, basis measurement, announcement, comparison, error estimation, and key distillation."
        text2 = "In BB84, Alice generates a random sequence of binary bits that she encodes into quantum states, using two mutually unbiased bases: rectilinear (Z) and diagonal (X). She then transmits the encoded qubits to Bob through a quantum channel. Upon receiving the qubits, Bob randomly selects a measurement basis for each qubit and performs measurements accordingly. He publicly announces the bases he used. Alice and Bob then compare a subset of their measurement results, discarding inconsistent ones due to mismatched bases. By estimating the error rate, they can identify potential eavesdropping attempts. Finally, Alice and Bob perform error correction and privacy amplification to distill a shared cryptographic key."
        textMessage1 = tk.Message(self.InfoFrameBB84, text=text1,
                                 foreground="white", font=textFont,
                                 width=int(screenWidth * 0.6),
                                 justify="left", bg=secondaryOrange)
        textMessage1.pack(fill=ctk.BOTH, padx=4, pady=4)

        textMessage2 = tk.Message(self.InfoFrameBB84, text=text2,
                                  foreground="white", font=textFont,
                                  width=int(screenWidth * 0.6),
                                  justify="left", bg=secondaryOrange)
        textMessage2.pack(fill=ctk.BOTH, padx=4, pady=4)

        # Table Info Frame
        self.InfoFrameTable = ctk.CTkFrame(self.generalInfoFrame, corner_radius=9, fg_color=secondaryOrange)
        image = Image.open('assets/bb84table.jpg')
        image = image.resize((int(screenWidth * 0.5), int(screenWidth * 0.5)), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        imageLabel = tk.Label(self.InfoFrameTable, image=photo,background=secondaryOrange)
        imageLabel.image = photo
        imageLabel.pack(side=tk.TOP, padx=2, pady=2, anchor=tk.N)

        # -----------------------------------------
        # Show Default Frame
        self.showInfoFrameByName("1")

    def infoAction1(self):
        self.showInfoFrameByName("1")

    def infoAction2(self):
        self.showInfoFrameByName("2")

    def infoAction3(self):
        self.showInfoFrameByName("3")

    def infoAction4(self):
        self.showInfoFrameByName("4")

    def infoAction5(self):
        self.showInfoFrameByName("5")

    def showInfoFrameByName(self, name):
        # Show selected frame
        if name == "1":
            self.InfoFrameSim.pack(fill=ctk.BOTH, expand=True, padx=4, pady=4)
        else:
            self.InfoFrameSim.pack_forget()
        if name == "2":
            self.InfoFrameIntroduction.pack(fill=ctk.BOTH, expand=True, padx=4, pady=4)
        else:
            self.InfoFrameIntroduction.pack_forget()
        if name == "3":
            self.InfoFrameQKD.pack(fill=ctk.BOTH, expand=True, padx=4, pady=4)
        else:
            self.InfoFrameQKD.pack_forget()
        if name == "4":
            self.InfoFrameBB84.pack(fill=ctk.BOTH, expand=True, padx=4, pady=4)
        else:
            self.InfoFrameBB84.pack_forget()
        if name == "5":
            self.InfoFrameTable.pack(fill=ctk.BOTH, expand=True, padx=4, pady=4)
        else:
            self.InfoFrameTable.pack_forget()

    def goToFirstPage(self):
        self.grid_forget()
        firstFrame.pack()


class SimulationFrame(ctk.CTkFrame):
    currentSimStage = 0
    currentKey = []

    def __init__(self, master):
        ctk.CTkFrame.__init__(self, master,
                              width=int(screenWidth * 0.75), height=int(screenHeight * 0.85),
                              fg_color=mainOrange)
        self.pack()
        self.pack_propagate(False)

        # Create top frame for the "Back" button
        self.topFrame = ctk.CTkFrame(master=self, fg_color=secondaryOrange, corner_radius=9)
        self.topFrame.pack(fill=tk.BOTH, padx=4, pady=4)

        # Create "Back" button
        self.backButton = ctk.CTkButton(master=self.topFrame, command=self.goToFirstPage,
                                        width=int(screenWidth * 0.06), height=int(screenHeight * 0.03),
                                        text="Back",
                                        text_color="white", font=textFontBold,
                                        fg_color=mainBlue, hover_color=secondaryBlue,
                                        border_color="white", border_width=1)
        self.backButton.pack(side=tk.LEFT, padx=4, pady=4)

        # Create middle frame for simulation
        self.midFrame = ctk.CTkScrollableFrame(master=self,
                                               fg_color=secondaryOrange, corner_radius=9,
                                               scrollbar_button_color=mainOrange,
                                               scrollbar_button_hover_color=mainOrange)
        self.midFrame.pack(fill=tk.BOTH, expand=True, padx=4)

        # Create bottom frame for "Next" button
        self.bottomFrame = ctk.CTkFrame(master=self,
                                        fg_color=secondaryOrange, corner_radius=9)
        self.bottomFrame.pack(fill=tk.BOTH, padx=4, pady=4)

        self.nextButton = ctk.CTkButton(master=self.bottomFrame, command=self.showNextFrame,
                                        width=int(screenWidth * 0.06), height=int(screenHeight * 0.03),
                                        state="normal", text="Next",
                                        text_color="white", font=textFontBold,
                                        fg_color=mainBlue, hover_color=secondaryBlue,
                                        border_color="white", border_width=1)
        self.nextButton.pack(anchor=tk.CENTER, pady=4)

        # Create Frame List for measurement frames
        self.frameList = []

    def createSimInfoFrame(self):
        mainFrame = ctk.CTkFrame(master=self.midFrame, fg_color="white", corner_radius=9)
        mainFrame.pack(anchor=ctk.CENTER, fill=ctk.BOTH, pady=5, padx=100)

        topFrame = ctk.CTkFrame(master=mainFrame, fg_color=mainOrange)
        topFrame.pack(fill=tk.BOTH, padx=4, pady=4)
        bitsText = "As information page about protocol stated, at first Alice generates a random set of bits. This time Alice's random bits are:"
        bitsDescription = tk.Message(topFrame, text=bitsText,
                                     foreground="white", font=textFont,
                                     justify="center", width=int(screenWidth * 0.6),
                                     fg="white", background=mainOrange)
        bitsDescription.pack(pady=8)
        bitsLabel = ctk.CTkLabel(master=topFrame, text=info.aliceKeys,
                                 text_color="white", font=bigFontBold,
                                 justify="center", anchor="center", fg_color=mainOrange)
        bitsLabel.pack()

        baseText = "After that, Alice sends photons to Bob on different bases in quantum channel."
        baseDescription = ctk.CTkLabel(master=topFrame, text=baseText,
                                       text_color="white", font=textFont,
                                       justify="center", anchor="center", fg_color=mainOrange)
        baseDescription.pack(pady=8)

        tempAliceFrame = ctk.CTkFrame(master=mainFrame, fg_color=mainOrange)
        tempAliceFrame.pack(fill=tk.BOTH, padx=4, pady=4)

        aliceTextLabel = ctk.CTkLabel(master=tempAliceFrame, text="Alice's random chosen bases are:",
                                      text_color="white", font=textFont,
                                      justify="center", anchor="center", fg_color=mainOrange)
        aliceTextLabel.pack()

        aliceBaseFrame = ctk.CTkFrame(master=tempAliceFrame, fg_color=mainOrange)
        aliceBaseFrame.pack(anchor=ctk.CENTER)

        for base in info.aliceBases:
            imageName = './assets/diagonalbase.png' if base == "X" else './assets/rectilinearbase.png'
            imgSize = int(screenWidth * 0.025)
            img = ctk.CTkImage(light_image=Image.open(imageName), dark_image=Image.open(imageName),
                               size=(imgSize, imgSize))
            imgLabel = ctk.CTkLabel(aliceBaseFrame, image=img, text="", fg_color=mainOrange)
            imgLabel.pack(side=tk.LEFT, padx=2, pady=5)

        tempBobFrame = ctk.CTkFrame(master=mainFrame, fg_color=mainOrange)
        tempBobFrame.pack(fill=tk.BOTH, padx=4, pady=4)

        bobTextLabel = ctk.CTkLabel(master=tempBobFrame, text="Bob's random chosen bases are:",
                                    text_color="white", font=textFont,
                                    justify="center", anchor="center", fg_color=mainOrange)
        bobTextLabel.pack()

        bobBaseFrame = ctk.CTkFrame(master=tempBobFrame, fg_color=mainOrange)
        bobBaseFrame.pack(anchor=ctk.CENTER)

        for base in info.bobBases:
            imageName = './assets/diagonalbase.png' if base == "X" else './assets/rectilinearbase.png'
            imgSize = int(screenWidth * 0.025)
            img = ctk.CTkImage(light_image=Image.open(imageName), dark_image=Image.open(imageName),
                               size=(imgSize, imgSize))
            imgLabel = ctk.CTkLabel(bobBaseFrame, image=img, text="", fg_color=mainOrange)
            imgLabel.pack(side=tk.LEFT, padx=2, pady=5)

        self.frameList.append(mainFrame)

    def createSimFrame(self):
        frame = ctk.CTkFrame(master=self.midFrame, fg_color="white", corner_radius=9)
        frame.pack(anchor=ctk.CENTER, fill=ctk.BOTH, pady=8, padx=100)

        self.innerFrame = ctk.CTkFrame(master=frame, fg_color=mainOrange, corner_radius=9)
        self.innerFrame.pack(fill=ctk.BOTH, expand=True, padx=4, pady=4)

        self.innerFrame.columnconfigure(2, weight=1)

        titleLabel1 = ctk.CTkLabel(self.innerFrame, text="Alice's Bit",
                                   text_color="white", font=textFontBold,
                                   corner_radius=9, fg_color=secondaryOrange,
                                   width=int(screenWidth * 0.07))
        titleLabel1.grid(row=0, column=0, padx=3, pady=3, sticky="nsew")

        titleLabel2 = ctk.CTkLabel(self.innerFrame, text="Alice's Base",
                                   text_color="white", font=textFontBold,
                                   corner_radius=9, fg_color=secondaryOrange,
                                   width=int(screenWidth * 0.07))
        titleLabel2.grid(row=0, column=1, padx=3, pady=3, sticky="nsew")

        titleLabel3 = ctk.CTkLabel(self.innerFrame, text="Explanation",
                                   text_color="white", font=textFontBold,
                                   corner_radius=9, fg_color=secondaryOrange)
        titleLabel3.grid(row=0, column=2, padx=3, pady=3, sticky="ew")

        titleLabel4 = ctk.CTkLabel(self.innerFrame, text="Bob's Base",
                                   text_color="white", font=textFontBold,
                                   corner_radius=9, fg_color=secondaryOrange,
                                   width=int(screenWidth * 0.07))
        titleLabel4.grid(row=0, column=3, padx=3, pady=3, sticky="nsew")

        titleLabel5 = ctk.CTkLabel(self.innerFrame, text="Bob's Bit",
                                   text_color="white", font=textFontBold,
                                   corner_radius=9, fg_color=secondaryOrange,
                                   width=int(screenWidth * 0.07))
        titleLabel5.grid(row=0, column=4, padx=3, pady=3, sticky="nsew")

        # ---------------------------------------------------

        # Alice's Bit
        defLabel1 = ctk.CTkLabel(self.innerFrame, text=measurementList[self.currentSimStage - 2].aliceBit,
                                 text_color="white", font=bigFontBold,
                                 corner_radius=9, fg_color=secondaryOrange)
        defLabel1.grid(row=1, column=0, padx=3, pady=3, sticky="nsew", ipady=10)

        # Alice's Bases
        aliceImgPath = './assets/diagonalbase.png' if measurementList[self.currentSimStage - 2].aliceBase == "X" \
            else './assets/rectilinearbase.png'
        aliceImg = ctk.CTkImage(light_image=Image.open(aliceImgPath), dark_image=Image.open(aliceImgPath),
                                size=(int(screenWidth * 0.03), int(screenWidth * 0.03)))
        defLabel2 = ctk.CTkLabel(self.innerFrame, text="", image=aliceImg, corner_radius=9, fg_color=secondaryOrange)
        defLabel2.image = aliceImg
        defLabel2.grid(row=1, column=1, padx=3, pady=3, sticky="nsew")

        explanationText = ("Same Base Choice for Alice and Bob.\n Bit added to the key"
                           if measurementList[self.currentSimStage - 2].result
                           else
                           "Different base choice for Alice and Bob.\n No bit added to the key")
        defLabel3 = ctk.CTkLabel(master=self.innerFrame, text=explanationText,
                                 text_color="white", font=textFont,
                                 corner_radius=9, fg_color=secondaryOrange, justify="center")
        defLabel3.grid(row=1, column=2, padx=3, pady=3, sticky="nsew")

        bobImgPath = './assets/diagonalbase.png' if measurementList[self.currentSimStage - 2].bobBase == "X" \
            else './assets/rectilinearbase.png'
        bobImg = ctk.CTkImage(light_image=Image.open(bobImgPath), dark_image=Image.open(bobImgPath),
                              size=(int(screenWidth * 0.03), int(screenWidth * 0.03)))

        defLabel4 = ctk.CTkLabel(self.innerFrame, text="", image=bobImg, corner_radius=9, fg_color=secondaryOrange)
        defLabel4.image = bobImg
        defLabel4.grid(row=1, column=3, padx=3, pady=3, sticky="nsew")

        # def5Frame = ctk.CTkFrame(self.innerFrame, fg_color=secondaryOrange, corner_radius=9)
        # def5Frame.grid(row=1, column=4, padx=3, pady=3, sticky="nsew")

        text = (measurementList[self.currentSimStage - 2].aliceBit
                if measurementList[self.currentSimStage - 2].result
                else
                "No Bit \n Received")
        defLabel5 = ctk.CTkLabel(self.innerFrame, text=text,
                                 text_color="white",
                                 font=bigFontBold if measurementList[self.currentSimStage - 2].result else textFont,
                                 corner_radius=9, fg_color=secondaryOrange, justify="center")
        defLabel5.grid(row=1, column=4, padx=3, pady=3, sticky="nsew")

        # ---------------------------------------------------

        bottomFrame = ctk.CTkFrame(self.innerFrame, fg_color=secondaryOrange, corner_radius=9)
        bottomFrame.grid(row=2, column=0, columnspan=5, padx=3, pady=3, sticky="nsew")

        if measurementList[self.currentSimStage - 2].result:
            self.currentKey.append(measurementList[self.currentSimStage - 2].aliceBit)
            keyListToString = ''.join(map(str, self.currentKey))
            keyText = "Current key is:" "\n" + keyListToString
        else:
            if len(self.currentKey) == 0:
                keyText = "Currently key is empty."
            else:
                keyListToString = ''.join(map(str, self.currentKey))
                keyText = "Current key is:" "\n" + keyListToString

        keyDescriptionLabel = ctk.CTkLabel(master=bottomFrame, text=keyText,
                                           text_color="white", font=textFont)
        keyDescriptionLabel.pack(anchor=ctk.CENTER)

        self.frameList.append(frame)

    def createSimResultFrame(self):
        mainFrame = ctk.CTkFrame(master=self.midFrame, fg_color="white", corner_radius=9)
        mainFrame.pack(anchor=ctk.CENTER, fill=ctk.BOTH, pady=5, padx=100)

        topFrame = ctk.CTkFrame(master=mainFrame, fg_color=mainOrange)
        topFrame.pack(fill=tk.BOTH, padx=5, pady=3)
        resultText = "After measuring and comparing all qubits send by Alice to the Bob, Alice and Bob share their results on classical channel which can be hearable by anyone even Eve. As measurements show, generated key is:"
        resultDescription = tk.Message(topFrame, text=resultText,
                                       fg="white", font=textFont,
                                       justify="center", width=int(screenWidth * 0.44), background=mainOrange)
        resultDescription.pack(pady=3, padx=3)

        resultKey = ctk.CTkLabel(master=topFrame, text=info.resultKey,
                                 text_color="white", font=bigFontBold,
                                 justify="center", anchor="center", fg_color=mainOrange)
        resultKey.pack()

        resultText2 = "With this key, Alice and Bob can encrypt and decrypt files, messages or anything possible to transfer. Since quantum channel did not corrupted by any eavesdropper, It's secured."
        resultDescription2 = tk.Message(topFrame, text=resultText2,
                                        fg="white", font=textFont,
                                        justify="center", width=int(screenWidth * 0.44), background=mainOrange)
        resultDescription2.pack()

        self.frameList.append(mainFrame)

    def showNextFrame(self):
        # Increment the currentSimStage
        self.currentSimStage += 1

        if self.currentSimStage == 1:
            self.createSimInfoFrame()
        elif 1 < self.currentSimStage <= len(info.aliceBases) + 1:
            self.createSimFrame()
        elif self.currentSimStage == len(info.aliceBases) + 2:
            self.createSimResultFrame()
            self.nextButton.configure(state="disabled")

    def goToFirstPage(self):
        # Clear the data about previous simulation
        for frame in self.frameList:
            frame.pack_forget()
        self.frameList.clear()
        measurementList.clear()
        self.currentSimStage = 0
        self.currentKey.clear()
        self.nextButton.configure(state="normal")

        # Go To First Frame
        self.pack_forget()
        firstFrame.pack()


class MeasurementInfoClass:
    def __init__(self, qubitNo, aliceBit, aliceBase, bobBase, result):
        self.qubitNo = qubitNo
        self.aliceBit = aliceBit
        self.aliceBase = aliceBase
        self.bobBase = bobBase
        self.result = result

    def printResult(self):
        if self.result:
            print("Qubit No:{}, Same choice on basis: {}, Bit added to the Key: {}".format(
                self.qubitNo,
                self.aliceBase,
                self.aliceBit))
        else:
            print(
                "Qubit No:{}, Different Choice, Alice has {}, Bob has {}, No Bit added to the Key".format(
                    self.qubitNo,
                    self.aliceBase,
                    self.bobBase))


def BB84Simulation(bitSize):
    def TransferState(qc1, qc2):
        qs = qc1.qasm().split(sep=';')[4:-1]

        for index, instruction in enumerate(qs):
            qs[index] = instruction.lstrip()

        for instruction in qs:
            old_qr = int(instruction[5:-1])
            if instruction[0] == "x":
                qc2.x(quantumRegister[old_qr])
            elif instruction[0] == "h":
                qc2.h(quantumRegister[old_qr])
            elif instruction[0] == "m":
                pass
            else:
                raise Exception("Failed to Transfer State")

    n = bitSize
    quantumRegister = QuantumRegister(n, name='qr')
    classicalRegister = ClassicalRegister(n, name='cr')

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

    TransferState(alice, bob)

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
            measurementList.append(MeasurementInfoClass(qubitNo=qubit,
                                                        aliceBit=aliceKey[qubit],
                                                        aliceBase=basis[0],
                                                        bobBase=basis[1],
                                                        result=True))
            keptBits.append(qubit)
        else:
            measurementList.append(MeasurementInfoClass(qubitNo=qubit,
                                                        aliceBit=aliceKey[qubit],
                                                        aliceBase=basis[0],
                                                        bobBase=basis[1],
                                                        result=False))
            discardedBits.append(qubit)

    newAliceKey = [aliceKey[qubit] for qubit in keptBits]
    newBobKey = [bobKey[qubit] for qubit in keptBits]

    accuracy = 0
    for bit in zip(newAliceKey, newBobKey):
        if bit[0] == bit[1]:
            accuracy += 1

    if accuracy // len(newAliceKey) == 1:
        for frame in measurementList:
            frame.printResult()

        print("Generated Alice's key: ", newAliceKey)
        print("Generated Bob's key:   ", newBobKey)

        info.aliceKeys = aliceKey
        info.aliceBases = aliceTable
        info.bobBases = bobTable
        info.resultKey = newAliceKey
    else:
        print("Generated Alice's key is invalid: ", newAliceKey)
        print("Generated Bob's key is invalid: ", newBobKey)


if __name__ == "__main__":

    root = tk.Tk()
    root.title("Simulation")

    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()

    rootWidth = screenWidth * 0.75
    rootHeight = screenHeight * 0.85
    posX = (screenWidth / 2) - (rootWidth / 2)
    posY = (screenHeight / 2) - (rootHeight / 2)
    root.geometry('%dx%d+%d+%d' % (rootWidth, rootHeight, posX, posY))
    root.resizable(False, False)

    #Scaling the window for Windows 8/10 DPI issue
    root.tk.call('tk', 'scaling', 1.0)

    # First Frame
    firstFrame = FirstFrame(root)
    firstFrame.pack_propagate(False)

    # Simulation Frame
    simulationFrame = SimulationFrame(root)
    simulationFrame.pack_propagate(False)
    simulationFrame.pack_forget()

    # Information Frame
    infoFrame = InfoFrame(root)
    infoFrame.pack_propagate(False)
    infoFrame.pack_forget()

    # Start the tkinter event loop
    root.mainloop()
