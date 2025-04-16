import schedule
import time

def periodico(scheduler, interval, action, actionargs=()):
	scheduler.enter(interval, 1, periodic,
			(scheduler, interval, action, actionargs))
	action(*actionargs)

periodico(scheduler, 3600, query_rate_limit)

