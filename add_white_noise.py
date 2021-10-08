import sys
import numpy as np
import librosa
import soundfile as sf

def add_white_noise(x, rate=0.002):
	return x + rate*np.random.randn(len(x))

if __name__ == '__main__':
	args = sys.argv

	if len(args) >= 2:
		file_name = args[1]
	else:
		print("usage: python add_white_noise.py [file_name] [rate]")
		exit
	
	if len(args) >= 3:
		rate = float(args[2])
	else:
		rate = 0.002

	y, sr = librosa.load(file_name)

	z = add_white_noise(y, rate)

	sf.write("white_" + file_name, z, sr)

	