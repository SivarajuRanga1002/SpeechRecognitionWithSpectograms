# SpeechRecognitionWithSpectograms

**Sampling Rate**:
The rate at which we convert an analog signal to a digital signal i.e., the number of times per second an analog signal is measured or sampled to create a digital representation of the signal. Measured in Frequency

**Librosa:**
The Python library which we use to load, display, and process audio files.
Librosa loads data as a numpy array. And when we load an audio file it is generally normalized between -1 and 1. which you can see in the _.wavFile-SampleRate=16000-SA1_


**TIMIT Dataset:**
An audio dataset with .wav, .phn, .txt and .wrd files.

**_.wav_** - A wave format in the shape of sphere-heads. 
Contains all the original values of the audio files which are normalized when you load with _Librosa_ as mentioned in its description.

1. Example audio file

![wav_file SR=44100](https://github.com/SivarajuRanga1002/SpeechRecognitionWithSpectograms/assets/65248651/81dafd60-b5db-466a-87b4-be7ecde72278)

This audio file i.e., the _.wav_ format file has the amplitudes of audio signal at specific points in time


2. Spectrogram of the audio file

![Spectrogram-SA1](https://github.com/SivarajuRanga1002/SpeechRecognitionWithSpectograms/assets/65248651/3a6c5100-d014-4aeb-b9b4-7b886d289bcd)

When we convert an audio file from the time domain to the TIME AND FREQUENCY domain using FFT and then convert the amplitudes to decibels we get the Spectrogram.
_The output of the spectrogram is a 2D Matrix with data indicating the changes in Frequency and Time values_

**_.phn_** - This file holds the data on the available phoneme of the audio files recorded 

**_Arpabet Code_**
We assign the phoneme to their registered numerical values. If the machine can't find a phoneme that is in the list of the Arparbet codes, we append the phoneme to the Arpabet set and assign a value.


The 2D Spectrogram Matrix has the first column as the maximum length. Using KERAS we pad all the rest of the columns to match the maximum column length.


A Clear idea on how the data flows and how exactly the code is used with base concepts are mentioned in the PDF folder....


Results:







