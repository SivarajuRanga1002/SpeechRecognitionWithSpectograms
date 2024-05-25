import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# Load an audio file
file_path = r"D:\ASU\IntroductiontoDNN\TIMIT\TRAIN\DR1\FCJF0\SA2.WAV"  # Update this to the path of your audio file
audio, sample_rate = librosa.load(file_path, sr=44100)  # sr=None ensures original sampling rate is used


stft = np.abs(librosa.stft(audio, n_fft=2048, hop_length=512))


spectrogram = librosa.amplitude_to_db(stft, ref=np.max)

print(spectrogram)

# plt.figure(figsize=(12, 8))
# librosa.display.specshow(spectrogram, sr=44100, hop_length=10000, x_axis='time', y_axis='log', cmap='coolwarm')
# plt.colorbar(format='%+2.0f dB')
# plt.title('Spectrogram (dB)')
# plt.xlabel('Time')
# plt.ylabel('Frequency')
# plt.show()

# # Display basic properties of the audio
# duration = len(audio) / sample_rate
# print(f"Sample Rate: {sample_rate} Hz")
# print(f"Total Duration: {duration} seconds")
# print(f"Number of Samples: {len(audio)}")

# print(len(audio))
# print(stft)

# Plot the waveform
# plt.figure(figsize=(10, 4))
# librosa.display.waveshow(audio[0:10000])
# plt.title('Waveform of Audio')
# plt.xlabel('Time (s)')
# plt.ylabel('Amplitude')
# plt.show()