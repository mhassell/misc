import telnetlib
import csv
import time

class Scanner:

	def __init__(self, hostname='127.0.0.1', port=7356, directory='/Users/matthewhassell/GitHub/misc', waitTime=2, signalStrength=-20):
		self.host = hostname
		self.port = port
		self.directory = directory
		self.waitTime = waitTime
		self.signalStrength = signalStrength

	def _update(self, msg):
		"""
		update the frequency/mode GQRX is listening to
		"""
		tn = telnetlib.Telnet(self.host, self.port)
		tn.write(('%s\n' % msg).encode('ascii'))
		response = tn.read_some().decode('ascii').strip()
		tn.write('c\n'.encode('ascii'))
		return response

	def scan(self):
		"""
		loop over the frequencies in the list, and stop if the frequency is active (signal strength is high enough)
		"""
		for freq in self.freqs.keys():
			self._set_freq(freq)
			self._set_mode(self.freqs[freq])
			while self._get_level() >= self.signalStrength:
				time.sleep(self.waitTime)


   	def load(self):
   		"""
   		read the csv file with the frequencies & modes in it into a dict{} where keys are the freq and values are the mode
   		"""
   		self.freqs = {}
   		with open('freq.csv','r') as csvfile:
   			reader = csv.reader(csvfile, delimiter = ',')
   			for row in reader:
   				freq = int(float(row[0].strip('.'))*1e6)  # convert to hz
   				self.freqs[freq] = row[1]     # add the freq to the dict as a key and the mode as the value


   	def _set_freq(self, freq):
   		return self._update("F %s" % freq)

   	def _set_mode(self, mode):
   		return self._update("M %s" % mode)

   	def _get_level(self):
   		return self._update("l")
