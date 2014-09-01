# A thin ORM to make it easier to work with the database
from mongoengine import *  # An alternative ORM, which might be more trouble than it's worth
from datetime import datetime, timedelta
from random import randint
from pprint import pprint
import os
import json

connect('logtime')


class Log(Document):
    # Number of hours logged
    hours = IntField()
    # Which category this is logged under
    category = StringField()
    # When this was logged
    timestamp = DateTimeField()

    def __repr__(self):
        return "{} hours for {} on {}".format(self.hours, self.category, self.timestamp)
   

# def populate_db_with_TDs():
# 	"""
# 	For testing purposes, fill the database with example TDs.
# 	A similar function could be used in production. 
# 	"""
# 	with open("test_names.txt", 'r') as open_file:
# 		lines = open_file.readlines()
# 		for line in lines:
# 			fullname = line.split(", ")[0]
# 			TC = fullname.split("/")[~0]
# 			TS = fullname.split("/")[0]
# 			command = "make VARIANT=0 TGT=OPTIMAL test"
# 			for build in ["40_debug","3X_debug","40_release","3X_release"]:
# 				td = TD()
# 				td.create(TS, TC, build, "./Tests/"+fullname, command )
# 				td.update_time(0, randint(1000))
# 				td.save()
# 	return

# def empty_db_of_TDs():
# 	"""
# 	Clear the database of all TDs. Only for testing purposes.
# 	"""
# 	for td in TD.objects():
# 		td.delete()


# def empty_db_of_TRs():
# 	"""
# 	Clear the database of all TRs. Only for testing purposes.
# 	"""
# 	for tr in TR.objects():
# 		tr.delete()

# def getTD(oid):
# 	"""
# 	Shorthand to get a TD by id
# 	"""
# 	ret = TD.objects(id=oid)
# 	if len(ret)>0:
# 		return ret[0]
# 	else:
# 		return None

# def getTR(oid):
# 	"""
# 	Shorthand to get a TR by id
# 	"""
# 	ret = TR.objects(id=oid)
# 	if len(ret)>0:
# 		return ret[0]
# 	else:
# 		return None

# def getTR_fn(tr_fn):
# 	"""
# 	Get TR by fullname
# 	"""
# 	ret = TR.objects(fullname=tr_fn)
# 	if len(ret)>0:
# 		return ret[0]
# 	else:
# 		return None