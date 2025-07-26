
from TDStoreTools import StorageManager
import TDFunctions as TDF
import re, sys

class MediaPipeExt:
	"""
	MediaPipeExt description
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp
		self.camList = self.ownerComp.par.Webcam.menuLabels
		self.regex = re.compile(r"FaceTime*", re.I)

	def SetCamera(self):
		if sys.platform == "darwin":
			index = -1 # default when no match is found
			for i, camera in enumerate(self.camList):
				if self.regex.search(camera):
					index = i
					break
			print(index)
			self.ownerComp.par.Webcam = index
		else:
			pass
		return
