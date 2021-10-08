import sys
import numpy as np
import librosa
import soundfile as sf

def shift(x, rate=2):
	return np.roll(x, int(len(x)//rate))

if __name__ == '__main__':
	args = sys.argv

	if len(args) >= 2:
		file_name = args[1]
	else:
		print("usage: python shift.py [file_name] [rate]")
		exit
	
	if len(args) >= 3:
		rate = float(args[2])
	else:
		rate = 2

	y, sr = librosa.load(file_name)

	z = shift(y, rate)

	sf.write("shift_" + file_name, z, sr)
