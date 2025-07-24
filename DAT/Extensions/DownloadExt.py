
from TDStoreTools import StorageManager
import TDFunctions as TDF
import time

class DownloadExt:
	"""
	DownloadExt description
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp
		self.timer = self.ownerComp.op('timer1')
		self.moviefilein = self.ownerComp.op('moviefilein1')
		self.folder = self.ownerComp.op('folder1')
		self.moviefilein.bypass = True
		
	
	def PathToRecording(self):
		#self.timer.par.start.pulse()
		self.filepath = self.folder[self.folder.numRows-1, 'path']
		print(self.folder.numRows-1, self.filepath)
		return self.filepath

	def Hide(self):
		self.moviefilein.bypass = True
		return
	
	def Show(self):
		self.moviefilein.bypass = False
		return
	
	def StartPlayback(self):
		self.timer.par.start.pulse()

