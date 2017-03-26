
class Manufacturer(object):

	mID = None
	timestamp = None
	longitude = 0
	latitude = 0

	def __init__ (self, mID, timestamp, latitude, longitude):
		self.mID = mID
		self.timestamp = timestamp
		self.longitude = longitude
		self.latitude = latitude

class Drug(object):
	"""docstring for ClassName"""
	name = None
	expiration = None
	strength = 0

	def __init__(self, name, expiration, strength):
		self.name = name
		self.expiration = expiration
		self.strength = strength

class Patient(object):
	"""docstring for Patient"""
	pID = None
	name = None
	timestamp = None

	def __init__(self, pID, name, timestamp):
		self.pID = pID
		self.name = name
		self.timestamp = timestamp

class Pharmacy(object):
	"""docstring for Pharmacy"""
	phID = None
	name = None
	timestamp = None
	latitude = 0
	longitude = 0

	def __init__(self, phID, timestamp, longitude, latitude):
		self.phID = phID
		self.timestamp = timestamp
		self.latitude = latitude
		self.longitude = longitude
		
class Doctor(object):
	"""docstring for Doctor"""
	docID = None
	name = None
	timestamp = None
	refill = 0
	quantity = 0
	daily = 0

	def __init__(self, docID, name, timestamp, refill, quantity, daily):
		self.docID = docID
		self.name = name
		self.timestamp = timestamp
		self.refill = refill
		self.quantity = quantity
		self.daily = daily
	
class NFCdata(object):
	"""docstring for NFCdata"""
	manufacturer = None
	pharmacy = None
	patient = None
	doctor = None

	def __init__(self, manufacturer, patient, pharmacy, doctor):
		self.manufacturer = manufacturer
		self.pharmacy = pharmacy
		self.patient = patient
		self.doctor = doctor
		
