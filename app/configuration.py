# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

class Config(object):
	"""
	Configuration base, for all environments.
	"""
	DEBUG = True
	TESTING = False
	DATABASE_URI = 'sqlite//'
	BOOTSTRAP_FONTAWESOME = True
	SECRET_KEY = "somethingsecret"
	CSRF_ENABLED = True

	#Get your reCaptche key on: https://www.google.com/recaptcha/admin/create
	#RECAPTCHA_PUBLIC_KEY = "6LffFNwSAAAAAFcWVy__EnOCsNZcG2fVHFjTBvRP"
	#RECAPTCHA_PRIVATE_KEY = "6LffFNwSAAAAAO7UURCGI7qQ811SOSZlgU69rvv7"
class DevelopmentConfig(Config):
	DEBUG = True
	import instance.config
	print("dev")
