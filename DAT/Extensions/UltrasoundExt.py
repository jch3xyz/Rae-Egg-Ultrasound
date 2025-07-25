
from TDStoreTools import StorageManager
import TDFunctions as TDF

class UltrasoundExt:
	"""
	UltrasoundExt description
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp
		self.StartRecordingTooltip = op.HAND_OVERLAY.op('StartRecordingTooltip')
		self.HandIndicator = op.HAND_OVERLAY.op('comp3')

	