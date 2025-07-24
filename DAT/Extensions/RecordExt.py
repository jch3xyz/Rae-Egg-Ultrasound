from TDStoreTools import StorageManager
import TDFunctions as TDF
import time

class RecordExt:
	"""
	RecordExt description
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp
		self.moviefileout = self.ownerComp.op('moviefileout1')
		self.timer = self.ownerComp.op('timer1')


	def Record(self):
		print("recording...")
		self.moviefileout.par.record = 1
		self.timer.par.start.pulse()
		return
	
	def Reset(self):
		print("done recording")
		self.moviefileout.par.record = 0
		return
	
	def FilePath(self):
		self.filepath = self.moviefileout.par.file.eval()
		print(self.filepath)
		return self.filepath

		