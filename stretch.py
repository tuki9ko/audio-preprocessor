import sys
import numpy as np
import librosa
import soundfile as sf

def stretch(x, rate=1.1):
	input_len = len(x)
	x = librosa.effects.time_stretch(x, rate)
	if len(x) > input_len:
		return x[:input_len]
	else:
		return np.pad(x, (0, max(0, input_len - len(x))), "constant")

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

	z = stretch(y, rate)

	sf.write("stretch_" + file_name, z, sr)
