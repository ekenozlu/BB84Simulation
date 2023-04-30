import tkinter as tk
import textwrap
import numpy as np
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute, BasicAer
from PIL import Image, ImageTk

n = 16
quantumRegister = QuantumRegister(n, name='qr')
classicalRegister = ClassicalRegister(n, name='cr')

measurementList = []


class FirstFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, width=600, height=500, background='navy')
        self.pack()

        self.start_button = tk.Button(self, text="Start Simulation", command=self.switch_to_second_frame)
        self.start_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.information_button = tk.Button(self, text="Learn About BB84 Protocol! ", command=self.show_info_frame)
        self.information_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

    def switch_to_second_frame(self):
        self.pack_forget()
        second_frame.pack()
        bb84Simulation()

    def show_info_frame(self):
        self.pack_forget()
        info_frame.pack()


class InfoFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, width=600, height=500, background='grey')
        self.pack()

        # Add other widgets to the frame as needed
        top_frame = tk.Frame(self)
        top_frame.pack(side=tk.TOP, padx=10, pady=10, anchor=tk.NW)
        # Create "Back" button
        self.back_button = tk.Button(top_frame, text="Back", command=self.switch_to_first_frame)
        self.back_button.pack(side=tk.LEFT)
        # Create "Next" button
        self.next_button = tk.Button(top_frame, text="Next", command=self.switch_to_info2)
        self.next_button.pack(side=tk.RIGHT)

        # Add text label
        text = "Quantum Key Distribution (QKD) is a method for securely distributing cryptographic keys between two parties - Alice and Bob - by using the principles of quantum mechanics. The BB84 protocol is one of the most well-known QKD protocols, developed by Charles Bennett and Gilles Brassard in 1984. The BB84 protocol works by using two quantum bits (qubits) - one to transmit the key and the other to verify its integrity. Alice randomly encodes the bits she wants to send to Bob using one of four possible states, which are chosen from two different bases. Each state represents a specific bit value, either a 0 or a 1. Bob then receives the encoded qubits and measures them in one of the two bases, chosen randomly. Once Bob has measured the qubits, Alice and Bob publicly compare the bases they used. If they used the same basis, Bob's measurement result reveals the value of the corresponding bit, and they can use it to form their shared secret key. If they used different bases, they discard the bit value and repeat the process until enough bits are obtained.The security of the BB84 protocol comes from the fact that any attempt to eavesdrop on the transmission will inevitably introduce errors that can be detected by Alice and Bob. According to the principles of quantum mechanics, any attempt to observe or measure a qubit will change its state, which can be detected by the parties. Thus, if an eavesdropper tries to intercept the qubits, they will introduce errors that will be detected during the verification process, allowing Alice and Bob to discard the affected bits and prevent the eavesdropper from obtaining any information about the key. QKD, and specifically the BB84 protocol, provides a method for securely distributing cryptographic keys that is resistant to interception or tampering. While still in its early stages of development, QKD has the potential to revolutionize the way in which secure communications are established and maintained, and it is an exciting area of research in both physics and computer science."
        wrapper = textwrap.TextWrapper(width=100)  # set the maximum width for each line
        wrapped_text = wrapper.fill(text)
        text_label = tk.Label(self, text=wrapped_text, width=300,height=500, justify="center", anchor="w", background="grey")
        text_label.pack(side=tk.TOP, padx=10, pady=10)

    def show_info_frame(self):
        # Hide any previously shown frames
        self.hide_all_frames()
        # Add the info_frame to the main window
        self.pack()

    def hide_all_frames(self):
        # Hide all frames in the main window
        self.pack_forget()

    def switch_to_first_frame(self):
        self.pack_forget()
        measurementList.clear()
        first_frame.pack()

    def switch_to_info2(self):
        # Hide all frames in the main window
        self.hide_all_frames()
        self.pack_forget()
        info_frame2.pack()

class InfoFrame2(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, width=600, height=500, background='white')
        self.pack()

        # Add other widgets to the frame as needed
        top_frame = tk.Frame(self)
        top_frame.pack(side=tk.TOP, padx=10, pady=10, anchor=tk.NW)
        # Create "Back" button
        self.back_button = tk.Button(top_frame, text="Back", command=self.switch_to_info1)
        self.back_button.pack(side=tk.LEFT)
        # Create "Next" button
        self.next_button = tk.Button(top_frame, text="Return to Homepage", command=self.switch_to_first_frame)
        self.next_button.pack(side=tk.RIGHT)
        # Load and resize the image
        image = Image.open('imagee.jpeg')
        image = image.resize((600,435), Image.LANCZOS)

        # Convert the image to a Tkinter-compatible format
        photo = ImageTk.PhotoImage(image)

        # Create a label to display the image
        image_label = tk.Label(self, image=photo)
        image_label.image = photo  # Keep a reference to the photo to avoid garbage collection

        # Add the label to the frame
        image_label.pack(side=tk.BOTTOM, padx=10, pady=10, anchor=tk.CENTER)

    def show_info_frame2(self):
        # Hide any previously shown frames
        self.hide_all_frames()

        # Add the info_frame to the main window
        self.pack()

    def hide_all_frames(self):
        # Hide all frames in the main window
        self.pack_forget()

    def switch_to_first_frame(self):
        self.pack_forget()
        first_frame.pack()

    def switch_to_info1(self):
        # Hide all frames in the main window
        self.pack_forget()
        info_frame.pack()


class SecondFrame(tk.Frame):
    currentSimStage = 0

    def __init__(self, master):
        tk.Frame.__init__(self, master, width=600, height=500)
        self.pack()

        # Create top frame for the "Back" button
        top_frame = tk.Frame(self)
        top_frame.pack(side=tk.TOP, padx=10, pady=10, anchor=tk.NW)

        # Create "Back" button
        self.back_button = tk.Button(top_frame, text="Back", command=self.switch_to_first_frame)
        self.back_button.pack(side=tk.LEFT)

        # Create bottom frame for "Previous" and "Next" buttons
        bottom_frame = tk.Frame(self)
        bottom_frame.pack(side=tk.BOTTOM, padx=10, pady=10, anchor=tk.S)

        # Create "Next" button
        self.next_button = tk.Button(bottom_frame, text="Next",command=self.show_next_frame)
        self.next_button.pack(side=tk.LEFT)

        # Create a list to store the frames
        self.frameList = []

        # Create initial frame with 2x6 grid of labels
        # self.create_frame()

    def create_frame(self):
        # Create a new frame inside the main frame
        frame = tk.Frame(self)
        frame.pack(padx=10, pady=10)

        titleLabel1 = tk.Label(frame, text="Alice's Bit")
        titleLabel1.grid(row=0, column=0, padx=10, pady=10)

        titleLabel2 = tk.Label(frame, text="Alice's Base")
        titleLabel2.grid(row=0, column=1, padx=10, pady=10)

        titleLabel3 = tk.Label(frame, text="Explanation")
        titleLabel3.grid(row=0, column=2, padx=10, pady=10,columnspan=3)

        titleLabel4 = tk.Label(frame, text="Bob's Base")
        titleLabel4.grid(row=0, column=5, padx=10, pady=10)

        titleLabel5 = tk.Label(frame, text="Bob's Bit")
        titleLabel5.grid(row=0, column=6, padx=10, pady=10)

        # ---------------------------------------------------

        # Alice's Bit
        defLabel1 = tk.Label(frame, text=measurementList[self.currentSimStage-1].aliceBit)
        defLabel1.grid(row=1, column=0, padx=10, pady=10)

        # Alice's Bases
        defLabel2 = tk.Label(frame, text=measurementList[self.currentSimStage-1].aliceBase)
        defLabel2.grid(row=1, column=1, padx=10, pady=10)

        message = ("Same Base Choice for Alice and Bob, Bit added to the key"
                   if measurementList[self.currentSimStage-1].result
                   else
                   "Different base choice for Alice and Bob, no bit added to the key")
        defLabel3 = tk.Message(frame, text=message,width=100)
        defLabel3.grid(row=1, column=2, padx=10, pady=10,columnspan=3)

        defLabel4 = tk.Label(frame, text=measurementList[self.currentSimStage-1].bobBase)
        defLabel4.grid(row=1, column=5, padx=10, pady=10)

        defLabel5 = tk.Message(frame, text=measurementList[self.currentSimStage-1].aliceBit
                                                        if measurementList[self.currentSimStage-1].result
                                                        else
                                                        "No Bit Received")
        defLabel5.grid(row=1, column=6, padx=10, pady=10)

        # Create a 2x6 grid of labels inside the frame
        # for i in range(2):
        #    for j in range(6):
        #        label = tk.Label(frame, text="Text")
        #        label.grid(row=i, column=j, padx=10, pady=10)

        # Add the frame to the list of frames
        self.frameList.append(frame)

    def show_next_frame(self):
        # Increment the currentSimStage and set the previous button
        self.currentSimStage += 1

        # Create a new frame and show it
        self.create_frame()
        self.frameList[-1].pack()

    def switch_to_first_frame(self):
        self.pack_forget()
        measurementList.clear()
        first_frame.pack()


class MeasurementFrame:
    def __init__(self, qubitNo,aliceBit, aliceBase, bobBase, result):
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
    # print("Alice's Key: ", aliceKey)

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
            # print("Qubit No:{}, Same choice on basis: {}, Bit added to the Key: {}" .format(qubit, basis[0],aliceKey[qubit]))
            measurementList.append(MeasurementFrame(qubitNo=qubit,
                                                    aliceBit=aliceKey[qubit],
                                                    aliceBase=basis[0],
                                                    bobBase=basis[1],
                                                    result=True))
            keptBits.append(qubit)
        else:
            # print("Qubit No:{}, Different Choice, Alice has {}, Bob has {}, No Bit added to the Key" .format(qubit, basis[0], basis[1]))
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
    print('Percentage of qubits to be discarded according to table comparison: ', len(keptBits) / n)
    print('Measurement convergence by additional chance: ', acc / n)

    newAliceKey = [aliceKey[qubit] for qubit in keptBits]
    newBobKey = [bobKey[qubit] for qubit in keptBits]

    acc = 0
    for bit in zip(newAliceKey, newBobKey):
        if bit[0] == bit[1]:
            acc += 1

    print('Percentage of similarity between the keys: ', acc / len(newAliceKey))

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


if __name__ == "__main__":
    # Create main window
    root = tk.Tk()
    root.title("Simulation")
    root.resizable(False, False)

    # Create first frame
    first_frame = FirstFrame(root)

    # Create second frame
    second_frame = SecondFrame(root)
    second_frame.pack_propagate(False)
    second_frame.pack_forget()  # Hide second frame initially

    info_frame = InfoFrame(root)
    info_frame.pack_propagate(False)
    info_frame.pack_forget()

    info_frame2 = InfoFrame2(root)
    info_frame2.pack_propagate(False)
    info_frame2.pack_forget()

    # Start the tkinter event loop
    root.mainloop()
