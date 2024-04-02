import serial
import tkinter as tk
import tkinter.ttk as ttk
import serial.tools.list_ports as port_list

window = tk.Tk()
window.title("GUI Program")
window.minsize(width=600, height=300)

def serial_ports():
    ports_objects = port_list.comports()
    print(len(ports_objects))
    long_port_names = []
    for i in range (len(ports_objects)):
        long_port_names.append(str(ports_objects[i]))
    short_port_names = [i.split()[0] for i in long_port_names]
    return short_port_names

def on_select(event=None):
    global port
    port = cb.get()
    global ser
    ser = serial.Serial(port, 115200)
    print(ser)

def btn_get_rtc_time():
    global ser
    packet = bytearray()
    packet.append(0x55)
    packet.append(0x02)
    packet.append(0x03)
    packet.append(0x01)
    packet.append(0x06)
    packet.append(0xa3)
    packet.append(0xad)
    packet.append(0x10)
    ser.write(packet)

try:
    label = tk.Label(text="GET RTC TIME: ", font=("Arial", 14, "bold"))
    label.place(x=0.0, y=0.0)
    button = tk.Button(text="55-02-03-01-06-a3-ad-10", font=("Arial", 10, "bold"), command=btn_get_rtc_time)
    button.place(x=150, y=0)
    cb = ttk.Combobox(window, values=serial_ports())
    cb.place(x=350, y=0)
    cb.bind('<<ComboboxSelected>>', on_select)
    #input = tkinter.Entry(width=10)
    #input.pack()
    #print(input.get())
    window.mainloop()
finally:
    global ser
    ser.close()
    print("exiting")
