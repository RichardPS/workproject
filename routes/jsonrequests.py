# -*- coding: UTF-8 -*-

from bottle import route
from json import dumps

# JSON requests
@route('/jsonsds')
def jsonsds():
    ''' get stats '''
    # Here call function to gather dictionary of required stats
    ''' dummy dictionary '''
    csd = {
    	'monthlaunch': 50,
    	'monthtarget': 75,
    	'yearlaunch': 500,
    	'yeartarget': 1000,
    }
    tsd = {
    	'turnround': 2,
    	'firstline': 'Chris Cameron',
    	'error': 1,
    	'small': 0,
    	'smallcharge': 2,
    	'admin': 3,
    	'admincharge': 1,
    }
    scores = {
    	'tsdspeed': 4.75,
    	'tsdquality': 4.8,
    	'tsdcs': 4.85,
    	'tsdave': 4.8,
    	'csdspeed': 4.5,
    	'csdquality': 4.9,
    	'csdcs': 4.75,
    	'csdave': 4.8,
    }
    issues = {
    	'currentissues': 'None at this time',
    }
    sdsjson = {
    	'csd': csd,
    	'tsd': tsd,
    	'scores': scores,
    	'issues': issues,
    }
    ''' return json object '''
    return dumps(sdsjson)