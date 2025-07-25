from TDStoreTools import StorageManager
import TDFunctions as TDF

class StateExt:
	"""
	StateExt description
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp
		self.selectComp = op.select_state
		self.recordTimer = self.ownerComp.op('timer_whileRecording')

		# States
		self.Init = False
		self.Attract = False
		self.Ultrasound = False
		self.Record = False
		self.Download = False
		self.handActive = op('hand_active')[0].eval()

	def Initialize(self):
		print('initializing...')
		self.Init = False

		op.DOWNLOAD.Hide()

		self.GoToAttractOrUltrasound(self.handActive)
		return
	
	def GoToAttractOrUltrasound(self, hand_active):
		if self.Init == False and self.Record == False:
			if hand_active == 0:
				self.selectComp.par.selectpanel = 'ATTRACT'
				self.Attract = True
				self.Ultrasound = False
			else:
				self.selectComp.par.selectpanel = 'ULTRASOUND'
				self.Ultrasound = True
				self.Attract = False
		return
	
	def GoToRecord(self):
		if self.Ultrasound == True:
			self.Ultrasound = False
			self.Record = True
			print('recording...')
			self.selectComp.par.selectpanel = 'RECORD'
			op.RECORD.Record()
			self.recordTimer.par.start.pulse()
		return
	
	def GoToDownload(self):
		if self.Record == True:
			op.RECORD.Reset()
			self.Record = False
			self.Download = True
			print('going to download...')
			self.selectComp.par.selectpanel = 'DOWNLOAD'
			op.DOWNLOAD.StartPlayback()
		return

		