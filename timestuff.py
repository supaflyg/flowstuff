#!/usr/bin/python

from datetime import datetime , date, timedelta
from dateutil.relativedelta import relativedelta

#d = date.today() - timedelta(days=3)
#e =  d - timedelta(days=22)

#print d,e

#for day in range(1,20):
#    date = date.today() - relativedelta(months=-day)


def flowtime(time, delta , deltaunit, interval):
    """ return a list of indexes, start time, and end time in epoch format.
	time = datetime object for start or end time  
	delta = number of units to subtract or add to time
	deltaunit = unit of time to subtract or add to time
	interval = 1hr or 5min flow data."""

    if interval == "5m":
	indexname = "flx_flows"
    elif interval == "1h":
	indexname = "lt_flowdata"
    else: 
	print "invalid interval"
	pass

    if deltaunit in ['M', 'months']:
	time2 = time + relativedelta(months=delta)
    elif deltaunit in ['d', 'days']:
	time2 = time + relativedelta(days=delta)
    elif deltaunit in ['h', 'hours']:
	time2 = time + relativedelta(hours=delta)

    time1se = int(time.strftime("%s")) * 1000 
    time2se = int(time2.strftime("%s")) * 1000
    if time1se > time2se:
	starttime = time1se
	endtime = time2se
	startdate = time
	daysdelta = divmod((time - time2).total_seconds(), 86400)
    else:
	starttime = time2se
	endtime = time1se
	startdate = time2
	daysdelta = divmod((time2 - time).total_seconds(), 86400)
    indexlist = []

    daycount = daysdelta[0]
    if daycount < 1:
	daycount = 1
    for unit in range(0, int(daycount)):
	    if interval == "1h":
		d = startdate - relativedelta(days=unit)
		print d
		indexlist.append("%s%s%s" % (indexname , d.year, str(d.month).zfill(2)))
	    elif interval == "5m":
		d = startdate - relativedelta(days=unit)
		indexlist.append("%s%s%s%s" % (indexname , d.year, str(d.month).zfill(2), str(d.day).zfill(2)))
    indexen =  list(set(indexlist))
    
    return indexen, time, time2, time1se, time2se

    

a = flowtime(datetime.now()-timedelta(9) , 15, "d", "5m")
print a
