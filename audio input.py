import pyaudio
import struct
import numpy as np
import matplotlib.pyplot as plt
%matplotlib tk

CHUNK=1024*4
FORMAT=pyaudio.paInt16
CHANNELS=1
RATE=44100

p=pyaudio.PyAudio()
stream=p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    output=True,
    frames_per_buffer=CHUNK
)

data=stream.read(CHUNK)
data #it gives bytes as output
# to get int data instead of byte data use data_int
data_int=struct.unpack(str(2*CHUNK)+'B', data)
#cretaes an array of the len(data_int) and then fills it with data
#len(data_int) gives the lenght of data wich is twice of chunk
#data_int
#0-255
fig,ax=plt.subplots()
#creates the subplots in the object plt
ax.plot(data_int,'-')
plt.show()
'''
data_int1=np.array(struct.unpack(str(2*CHUNK)+'B', data), dtype='b')[::2]
data_int1
fig,ax1=plt.subplots()
#creates the subplots in the object plt
ax1.plot(data_int1,'-')
plt.show()
'''


fig,ax=plt.subplots()
x=np.arange(0,2*CHUNK,2)
line, =ax.plot(np.random.rand(CHUNK))
ax.set_ylim(-149,140)
ax.set_xlim(0,CHUNK)
while True:
    data=stream.read(CHUNK)
    data_int1=np.array(struct.unpack(str(2*CHUNK)+'B', data), dtype='b') [::2]
    line.set_ydata(data_int1)#set y for loop
    fig.canvas.draw()#plot y and then flush it and then replot it
    fig.canvas.flush_events()
