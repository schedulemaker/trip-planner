def _filter(schedules):

    for schedule in schedules:
        campusCol = []
        apart_Campuses = []
        
        # Check if a schedule have more than one campus
        for course in schedule:
            campus =course['campusName']
            campusCol.append(campus) 
            
            if campus != 'Main':
                apart_Campuses.append(schedule.index(course))
            
        if len(set(campusCol))==1:
            # pass: schedule contains only one campus
            return ("Pass 1")
        else:
            Checker(schedule,apart_Campuses)

            
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
                    
                    # pass2: schedule contains 1+ campuses, but not in the same day.
                    if (apartWD & crsWD == 0):
                        print("Pass 2")
                    elif ((apartWD & crsWD == apartWD)and (apartWD & crsWD == crsWD)):
                        print("Pass 2")
                    elif apartCRN == crsCRN:
                        print("Pass 2")
                    # needtoCheck: schedule contains 1+ campuses, and in the same day. 
                    else:
                        tripPlanner(crsInfo, apartInfo, crsWS, apartWS)
                        
                        
                        
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
    dstStartT = dstWS['startT']-dur
    dstEndT = dstWS['endT']+dur

    # fail: schedule contains 1+ campuses, and in the same day, and have a time conflict
    if srcEndT > dstStartT:
        print("Fail : FILTER REQUIRED")        
        print("src:" , src)
        print("dst: ", dst)
    # pass3: schedule contains 1+ campuses, and in the same day, but does not have a time conflict
    else:
        print("Pass 3")

    
    
    

            
    

# Currently just return 1 hour for every case. Need to be integrated with google map API dist_dur()   
def dist_dur(src,dst):
    return 0,100
                         
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

schedules = [
  [
    {
      "campus": "CC",
      "meetingTimes": [
        {
          "saturday": False,
          "weeks": [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16
          ],
          "endDate": "12/16/2020",
          "thursday": False,
          "building": "TUCC",
          "room": "00315",
          "instructors": [
            "Chris Cagle"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": True,
          "startTime": 1230,
          "endTime": 1350,
          "startDate": "08/24/2020",
          "monday": True
        }
      ],
      "isOpen": True,
      "courseName": "FMA-5671",
      "title": "Film History and Theory",
      "campusName": "Center City",
      "crn": 44774
    },
    {
      "campus": "MN",
      "meetingTimes": [
        {
          "saturday": False,
          "weeks": [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16
          ],
          "endDate": "12/16/2020",
          "thursday": False,
          "building": "SERC",
          "room": "00357",
          "instructors": [
            "Eugene Kwatny"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": True,
          "startTime": 1000,
          "endTime": 1150,
          "startDate": "08/24/2020",
          "monday": False
        },
        {
          "saturday": False,
          "weeks": [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16
          ],
          "endDate": "12/16/2020",
          "thursday": True,
          "building": "BEURY",
          "room": "00164",
          "instructors": [
            "Eugene Kwatny"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1230,
          "endTime": 1350,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 4308
    },
    {
      "campus": "MN",
      "meetingTimes": [
        {
          "saturday": False,
          "weeks": [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16
          ],
          "endDate": "12/16/2020",
          "thursday": False,
          "building": 'null',
          "room": 'null',
          "instructors": [],
          "sunday": False,
          "tuesday": False,
          "wednesday": False,
          "friday": False,
          "startTime": 0,
          "endTime": 0,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "attributes": {
        "description": "GenEd Race &amp; Diversity",
        "isZTCAttribute": False,
        "code": "GD",
        "class": "net.hedtech.banner.student.schedule.SectionDegreeProgramAttributeDecorator",
        "courseReferenceNumber": "25550",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Main",
      "crn": 25550
    },
    {
      "campus": "AMBR",
      "meetingTimes": [
        {
          "saturday": False,
          "weeks": [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16
          ],
          "endDate": "12/16/2020",
          "thursday": True,
          "building": "ANDRSN",
          "room": "00017",
          "instructors": [
            "Kyle Harris",
            "Kyle Suess"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1400,
          "endTime": 1520,
          "startDate": "08/24/2020",
          "monday": False
        },
        {
          "saturday": False,
          "weeks": [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16
          ],
          "endDate": "12/16/2020",
          "thursday": True,
          "building": "PEARMC",
          "room": "0P015",
          "instructors": [
            "Kyle Harris",
            "Kyle Suess"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": False,
          "friday": False,
          "startTime": 1730,
          "endTime": 1920,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "attributes": {
        "description": "_Core Science &amp; Technology A",
        "isZTCAttribute": False,
        "code": "SA",
        "class": "net.hedtech.banner.student.schedule.SectionDegreeProgramAttributeDecorator",
        "courseReferenceNumber": "2184",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Ambler",
      "crn": 2184
    }
  ],
  [
    {
      "campus": "CC",
      "meetingTimes": [
        {
          "saturday": False,
          "weeks": [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16
          ],
          "endDate": "12/16/2020",
          "thursday": False,
          "building": "TUCC",
          "room": "00315",
          "instructors": [
            "Chris Cagle"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1730,
          "endTime": 2050,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "FMA-5671",
      "title": "Film History and Theory",
      "campusName": "Ambler",
      "crn": 48905
    },
    {
      "campus": "CC",
      "meetingTimes": [
        {
          "saturday": False,
          "weeks": [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16
          ],
          "endDate": "12/16/2020",
          "thursday": False,
          "building": "SERC",
          "room": "00357",
          "instructors": [
            "Eugene Kwatny"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 900,
          "endTime": 1050,
          "startDate": "08/24/2020",
          "monday": False
        },
        {
          "saturday": False,
          "weeks": [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16
          ],
          "endDate": "12/16/2020",
          "thursday": True,
          "building": "BEURY",
          "room": "00164",
          "instructors": [
            "Eugene Kwatny"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1230,
          "endTime": 1350,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Center City",
      "crn": 4308
    },
    {
      "campus": "MN",
      "meetingTimes": [
        {
          "saturday": False,
          "weeks": [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16
          ],
          "endDate": "12/16/2020",
          "thursday": False,
          "building": 'null',
          "room": 'null',
          "instructors": [],
          "sunday": False,
          "tuesday": False,
          "wednesday": False,
          "friday": False,
          "startTime": 0,
          "endTime": 0,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "attributes": {
        "description": "GenEd Race &amp; Diversity",
        "isZTCAttribute": False,
        "code": "GD",
        "class": "net.hedtech.banner.student.schedule.SectionDegreeProgramAttributeDecorator",
        "courseReferenceNumber": "25550",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Main",
      "crn": 25550
    },
    {
      "campus": "MN",
      "meetingTimes": [
        {
          "saturday": False,
          "weeks": [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16
          ],
          "endDate": "12/16/2020",
          "thursday": True,
          "building": "ANDRSN",
          "room": "00017",
          "instructors": [
            "Kyle Harris",
            "Kyle Suess"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1400,
          "endTime": 1520,
          "startDate": "08/24/2020",
          "monday": False
        },
        {
          "saturday": False,
          "weeks": [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16
          ],
          "endDate": "12/16/2020",
          "thursday": False,
          "building": "PEARMC",
          "room": "0P015",
          "instructors": [
            "Kyle Harris",
            "Kyle Suess"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": False,
          "friday": True,
          "startTime": 1400,
          "endTime": 1550,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "attributes": {
        "description": "_Core Science &amp; Technology A",
        "isZTCAttribute": False,
        "code": "SA",
        "class": "net.hedtech.banner.student.schedule.SectionDegreeProgramAttributeDecorator",
        "courseReferenceNumber": "2606",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 2606
    }
  ]
]
#{src:{dst:[dur,dist]}}
print("Output Description:")
print("Pass 1 indicates schedule contains only one campus. Pass 2 indicates schedule contains 1+ campuses BUT not in the same day. Pass 3 indicates schedule contains 1+ campuses AND in the same day BUT does not have time conflict. \nFinally, Fail means schedule contains 1+ campuses AND in the same day AND have time conflict.\n")

print("tripPlanner Start:")
_filter(schedules)
        


