# SpeechRecognitionWithSpectograms

**Sampling Rate**:
The rate at which we convert an analog signal to a digital signal i.e., the number of times per second an analog signal is measured or sampled to create a digital representation of the signal. Measured in Frequency

**Librosa:**
The Python library which we use to load, display, and process audio files.
Librosa loads data as a numpy array. And when we load an audio file it is generally normalized between -1 and 1. which you can see in the _.wavFile-SampleRate=16000-SA1_


**TIMIT Dataset:**
An audio dataset with .wav, .phn, .txt and .wrd files.

_.wav_ - A wave format in the shape of sphere-heads. 
Contains all the original values of the audio files which are normalized when you load with _Librosa_ as mentioned in its description.


