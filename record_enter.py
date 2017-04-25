"""
PyAudio example: Record a few seconds of audio and save to a WAVE
file.
"""
# -*- coding: utf-8 -*-
from array import array
import pyaudio
import wave
import sys
import time
from struct import pack

THRESHOLD_BEGIN = 1150
THRESHOLD_END = 700

def is_silent_begin(snd_data):
    "Returns 'True' if below the 'silent' threshold"
    return max(snd_data) < THRESHOLD_BEGIN

def is_silent_end(snd_data):
    "Returns 'True' if below the 'silent' threshold"
    return max(snd_data) < THRESHOLD_END

CHUNK = 1024 #bytes
FORMAT = pyaudio.paInt16
CHANNELS = 1 #1 single sound, 2 left and right sounds
RATE = 44100 #44100 Hz = samples/second
RECORD_SECONDS = 10 #second
WAVE_OUTPUT_FILENAME = sys.argv[1]+".wav"

if sys.platform == 'darwin':
    CHANNELS = 1

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK)

print("* recording") 

frames = array('h')

start_time = time.time()
start_speak = False
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):

    
    snd_data = array('h', stream.read(CHUNK))
    now = time.time() - start_time
    bool_silence_end = is_silent_end(snd_data)
    if (start_speak == False):
        bool_silence_begin = is_silent_begin(snd_data)

    if (bool_silence_end  and start_speak == True):
        print (max(snd_data))
        print("over")
        break;

    if (start_speak == True or False == bool_silence_begin ):
        print("-------ok------")
        print (max(snd_data))
        start_speak = True
        #data = stream.read(CHUNK)
        frames.extend(snd_data)

    if (now % 0.2 < 0.1):
        print('sec: %.2f ' % now)
        #print (max(snd_data))
        #print (abs(min(snd_data)))
   
    
        


print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

data = pack('<' + ('h'*len(frames)), *frames) #pack = string to binary ex:[x00\x00\xff]

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(data)
wf.close()

