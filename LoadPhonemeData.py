#Loads the .phn file, and extracts the phoneme then checks the arpabet code and its number;
#if not found adds the phoneme to the list  

import librosa
import librosa.display
import matplotlib.pyplot as plt

# Load an audio file
file_path = r"D:\ASU\IntroductiontoDNN\TIMIT\TRAIN\DR1\FCJF0\SA1.phn"  # Update this to the path of your audio file


def load_phenome(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    print(lines)
    phenome_seq = []
    for line in lines:
        phenome = line.split(' ')[2].rstrip()
        print(phenome)
        arpabet_code = arpabet.get(phenome)
        if arpabet_code is not None:
            phenome_seq.append(arpabet_code)
    return phenome_seq

arpabet = {
    'aa': 0, 'ae': 1, 'ah': 2, 'ao': 3, 'aw': 4, 'ax': 5, 'ax-h': 6, 'axr': 7, 'ay': 8, 'b': 9,
    'bcl': 10, 'ch': 11, 'd': 12, 'dcl': 13, 'dh': 14, 'dx': 15, 'eh': 16, 'el': 17, 'em': 18,
    'en': 19, 'eng': 20, 'epi': 21, 'er': 22, 'ey': 23, 'f': 24, 'g': 25, 'gcl': 26, 'h#': 27,
    'hh': 28, 'hv': 29, 'ih': 30, 'ix': 31, 'iy': 32, 'jh': 33, 'k': 34, 'kcl': 35, 'l': 36,
    'm': 37, 'n': 38, 'ng': 39, 'nx': 40, 'ow': 41, 'oy': 42, 'p': 43, 'pau': 44, 'pcl': 45,
    'q': 46, 'r': 47, 's': 48, 'sh': 49, 't': 50, 'tcl': 51, 'th': 52, 'uh': 53, 'uw': 54,
    'ux': 55, 'v': 56, 'w': 57, 'y': 58, 'z': 59, 'zh': 60
}

load_phenome(file_path)
# print("test")