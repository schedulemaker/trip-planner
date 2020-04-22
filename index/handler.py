import cache
#from googlemaps import Client as GoogleMaps
#import os

distdurCache, os, GoogleMaps = cache.exports()

MAP_KEY = os.environ['MAP_KEY']

"""
MAP_KEY = ''
keyfile = "MAP_KEY"

# Setup GoogleMaps before start
try:
    with open(keyfile, 'r+') as fh:
        MAP_KEY = fh.readline()
except FileNotFoundError:
    print('API key file does not exist. Exit the program.')
    exit()
"""
try:
    gmaps = GoogleMaps(MAP_KEY)
except ValueError:
    print('Invalid API key provided. Exit the program.')
    exit()



def lambda_handler(event, context):
    return _filter(event, context)
        
        
def _filter(event, context):
    schedules = event['schedule']

    for schedule in schedules:
        campusCol = []
        apart_Campuses = []
        
        # Check if a schedule have more than one campus
        for course in schedule:
            campus =course['campusName']
            campusCol.append(campus) 
            
            if campus != 'Main':
                apart_Campuses.append(schedule.index(course))
        
        # pass: schedule contains only one campus    
        if len(set(campusCol))==1:
            schedule.append({'tripPlanner':True, 'passCode':1})
        else:
            checker = Checker(schedule,apart_Campuses)
            schedule.append(checker)
    return schedules
    
    
def Checker(schedule,apart_Campuses):
 
    apartInfos = []
    for index in apart_Campuses:
        apartInfos.append(extractInfo(schedule[index]))
    for course in schedule:
        crsInfo = extractInfo(course)
        crsSche = crsInfo['weekSche']
        crsCRN = crsInfo['crn']
        for crsWS in crsSche:
            for apartInfo in apartInfos:
                for apartWS in apartInfo['weekSche']:
                    apartWD = apartWS['week_digit']
                    apartCRN = apartInfo['crn']
                    crsWD = crsWS['week_digit']
                    
                    # pass2: schedule contains 1+ campuses, but not in the same day or does  not have time conflict.
                    if (apartWD & crsWD == 0):
                        2
                    #elif ((apartWD & crsWD == apartWD) and (apartWD & crsWD == crsWD)):
                    #    return {'tripPlanner':False} 
                    elif apartCRN == crsCRN:
                        2
                    # needtoCheck: schedule contains 1+ campuses, and in the same day. 
                    else:
                        result = tripPlanner(crsInfo, apartInfo, crsWS, apartWS)
                        if not result:
                            return {'tripPlanner':False}
    return {'tripPlanner':True, 'passCode':2}  

def timeConverter(dstStartT, dstEndT, dur):
    s = dstStartT
    shr = int(s/100)*100
    smin = s - shr
    
    d = dur
    dhr = int(d/100)*100
    dmin = d - dhr
    
    e = dstEndT
    ehr = int(e/100)*100
    emin = e - ehr
    
    
    shr = shr-dhr
    if smin-dmin>=0:
        smin = smin-dmin
    else:
        shr = shr-100
        smin = smin +60
        smin = smin-dmin

    
    ehr = ehr+dhr
    if emin+dmin<60:
        emin = emin+dmin
    else:
        emin = emin+dmin
        ehr = ehr+ 100
        emin = emin-60
    
    
    dstStartT = shr+smin
    dstEndT = ehr+emin
    
    
    return dstStartT, dstEndT
    


                             
def tripPlanner(crsInfo, apartInfo, crsWS, apartWS):
    crsStartT = crsWS['startT']
    apartStartT = apartWS['startT']
   
    if crsStartT < apartStartT:
        src = crsInfo
        dst = apartInfo
        srcWS = crsWS
        dstWS = apartWS
    else:
        src = apartInfo
        dst = crsInfo
        srcWS = apartWS
        dstWS = crsWS
        
    dist, dur = dist_dur(src, dst)
    srcStartT = srcWS['startT']
    srcEndT = srcWS['endT']
    
    dstStartT = dstWS['startT']
    dstEndT = dstWS['endT']
    dstStartT, dstEndT = timeConverter(dstStartT, dstEndT,dur)

    # False: schedule contains 1+ campuses, and in the same day, and have a time conflict
    if srcEndT > dstStartT:
        return False
    # True: schedule contains 1+ campuses, and in the same day, but does not have a time conflict
    else:
        return True
        
def extractInfo(course):
    key = ['crn', 'campus', 'weekSche']
    WS_key = ['week_digit', 'startT', 'endT']

    weekSche = []
    mtTime= course['meetingTimes']
    for mtTime in mtTime:
        week_digit = 0
        if mtTime['monday']:
            week_digit+=2**6
        if mtTime['tuesday']:
            week_digit+=2**5
        if mtTime['wednesday']:
            week_digit+=2**4
        if mtTime['thursday']:
            week_digit+=2**3
        if mtTime['friday']:
            week_digit+=2**2
        if mtTime['saturday']:
            week_digit+=2**1
        if mtTime['sunday']:
            week_digit+=2**0
        WS_value = [week_digit, mtTime['startTime'], mtTime['endTime']]
        weekSche.append(dict(zip(WS_key, WS_value)))
    value = [course['crn'],course['campusName'], weekSche]

    info = dict(zip(key, value))
    return info
    
    
def dist_dur(src,dst): 
    university = os.environ['university']
    src_campus = src['campus']
    dst_campus = dst['campus']
    src_addr = university + " " + src_campus
    dst_addr = university + " " + dst_campus
    
    cacheKey = (src_addr,dst_addr)
    #check cache
    if cacheKey in distdurCache:
        dist, dur = distdurCache[cacheKey]
    else:
        distance, duration = getLatLng(src_addr,dst_addr)
       
        dist = distance['text']
        dur = duration['text']
        dur = durationFormat(dur)
        
        # add to cache
        distdurCache[cacheKey] = [dist,dur]
        #print("distdurCache :", distdurCache)

    return dist,dur

def durationFormat(dur):
    if 'hours' in dur:
        dur = dur.replace('hours','hour')
    if 'mins' in dur:
        dur = dur.replace('mins','min')
    if 'days' in dur:
        dur = dur.replace('days','day')

    S = dur.split()
    time = 0

    if 'hour' in S:
        time+=int(S[S.index('hour')-1])*100
    if 'min' in S:
        time+=int(S[S.index('min')-1])
    if 'day' in S:
        time += int(S[S.index('day')-1])*2400
    
    return time

    #dur format
    #'40 mins'
    #'1 hour 56 mins'
    #'1 day 17 hours'
    
    

def getLatLng(src_addr,dst_addr):
    
# Run geocode API to get lat and lng info 
    src_geocode = gmaps.geocode(src_addr)
    dst_geocode = gmaps.geocode(dst_addr)
    
    # Extract Lat and Lng info from geocode result
    srcLat = src_geocode[0]['geometry']['location']['lat']
    srcLng = src_geocode[0]['geometry']['location']['lng']
    
    dstLat = dst_geocode[0]['geometry']['location']['lat']
    dstLng = dst_geocode[0]['geometry']['location']['lng']
    
    src = (srcLat, srcLng)
    dst = (dstLat,dstLng)
    
    # Using distance API to find distance
    result = gmaps.distance_matrix(src, dst, mode='driving')
    distance = result['rows'][0]['elements'][0]['distance']
    duration = result['rows'][0]['elements'][0]['duration']
    #dist_dur = {'src_geocode': src_geocode, 'dst_geocode':dst_geocode,'result':result,'distance': distance,'duration': duration}
    dist_dur = [distance, duration]
    
    return dist_dur

