import handler
import os
os.environ['university'] = 'temple university'
os.environ['key'] =None
event = {'schedule': [
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
          "tuesday": True,
          "wednesday": True,
          "friday": False,
          "startTime": 1600,
          "endTime": 1720,
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
          "building": None,
          "room": None,
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
      "campusName": "Main",
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
          "building": None,
          "room": None,
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
          "building": None,
          "room": None,
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
          "thursday": False,
          "building": "PEARMC",
          "room": "0P015",
          "instructors": [
            "Kyle Harris",
            "Ryan P. Thomson"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1200,
          "endTime": 1350,
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
          "building": "ANDRSN",
          "room": "00017",
          "instructors": [
            "Kyle Harris",
            "Ryan P. Thomson"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1400,
          "endTime": 1520,
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
        "courseReferenceNumber": "3175",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 3175
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
          "building": None,
          "room": None,
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
          "thursday": False,
          "building": "PEARMC",
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Nicholas S. Mirabito"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
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
          "building": "ANDRSN",
          "room": "00017",
          "instructors": [
            "Kyle Harris",
            "Nicholas S. Mirabito"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1400,
          "endTime": 1520,
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
        "courseReferenceNumber": "9079",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 9079
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
          "building": None,
          "room": None,
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
          "thursday": False,
          "building": "PEARMC",
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Gabriel Castillo"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": False,
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
          "building": "ANDRSN",
          "room": "00017",
          "instructors": [
            "Kyle Harris",
            "Gabriel Castillo"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1400,
          "endTime": 1520,
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
        "courseReferenceNumber": "20967",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 20967
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
          "building": None,
          "room": None,
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
            "Matthew R. Schofield"
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
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Matthew R. Schofield"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1800,
          "endTime": 1950,
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
        "courseReferenceNumber": "34793",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 34793
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
          "building": None,
          "room": None,
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
            "Aaron Jackson"
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
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Aaron Jackson"
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
        "courseReferenceNumber": "39178",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 39178
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
          "building": None,
          "room": None,
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
          "building": "PEARMC",
          "room": "0P148",
          "instructors": [
            "Jacqueline Phillips",
            "Brian Kopicko"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 800,
          "endTime": 920,
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
          "room": "0P016",
          "instructors": [
            "Jacqueline Phillips",
            "Brian Kopicko"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
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
        "courseReferenceNumber": "39814",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "campusName": "Main",
      "title": "Human Anatomy and Physiology I",
      "crn": 39814
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
      "campusName": "Main",
      "crn": 4308
    },
    {
      "campus": "AMB",
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "26674",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Ambler",
      "crn": 26674
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
      "campusName": "Main",
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
      "campusName": "Main",
      "crn": 4308
    },
    {
      "campus": "AMB",
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "26674",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Ambler",
      "crn": 26674
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
      "campusName": "Main",
      "crn": 4308
    },
    {
      "campus": "AMB",
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "26674",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Ambler",
      "crn": 26674
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
          "building": "PEARMC",
          "room": "0P015",
          "instructors": [
            "Kyle Harris",
            "Ryan P. Thomson"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1200,
          "endTime": 1350,
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
          "building": "ANDRSN",
          "room": "00017",
          "instructors": [
            "Kyle Harris",
            "Ryan P. Thomson"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1400,
          "endTime": 1520,
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
        "courseReferenceNumber": "3175",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 3175
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
      "campusName": "Main",
      "crn": 4308
    },
    {
      "campus": "AMB",
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "26674",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Ambler",
      "crn": 26674
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
          "building": "PEARMC",
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Nicholas S. Mirabito"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
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
          "building": "ANDRSN",
          "room": "00017",
          "instructors": [
            "Kyle Harris",
            "Nicholas S. Mirabito"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1400,
          "endTime": 1520,
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
        "courseReferenceNumber": "9079",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 9079
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
      "campusName": "Main",
      "crn": 4308
    },
    {
      "campus": "AMB",
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "26674",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Ambler",
      "crn": 26674
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
          "building": "PEARMC",
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Gabriel Castillo"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": False,
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
          "building": "ANDRSN",
          "room": "00017",
          "instructors": [
            "Kyle Harris",
            "Gabriel Castillo"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1400,
          "endTime": 1520,
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
        "courseReferenceNumber": "20967",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 20967
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
      "campusName": "Main",
      "crn": 4308
    },
    {
      "campus": "AMB",
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "26674",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Ambler",
      "crn": 26674
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
            "Matthew R. Schofield"
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
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Matthew R. Schofield"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1800,
          "endTime": 1950,
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
        "courseReferenceNumber": "34793",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 34793
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
      "campusName": "Main",
      "crn": 4308
    },
    {
      "campus": "AMB",
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "26674",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Ambler",
      "crn": 26674
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
            "Aaron Jackson"
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
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Aaron Jackson"
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
        "courseReferenceNumber": "39178",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 39178
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
      "campusName": "Main",
      "crn": 4308
    },
    {
      "campus": "AMB",
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "26674",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Ambler",
      "crn": 26674
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
          "building": "PEARMC",
          "room": "0P148",
          "instructors": [
            "Jacqueline Phillips",
            "Brian Kopicko"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 800,
          "endTime": 920,
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
          "room": "0P016",
          "instructors": [
            "Jacqueline Phillips",
            "Brian Kopicko"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
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
        "courseReferenceNumber": "39814",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "campusName": "Main",
      "title": "Human Anatomy and Physiology I",
      "crn": 39814
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
      "campusName": "Main",
      "crn": 4308
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "32525",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Center City",
      "crn": 32525
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
      "campusName": "Main",
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
      "campusName": "Main",
      "crn": 4308
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "32525",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Center City",
      "crn": 32525
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
      "campusName": "Main",
      "crn": 4308
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "32525",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Center City",
      "crn": 32525
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
          "building": "PEARMC",
          "room": "0P015",
          "instructors": [
            "Kyle Harris",
            "Ryan P. Thomson"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1200,
          "endTime": 1350,
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
          "building": "ANDRSN",
          "room": "00017",
          "instructors": [
            "Kyle Harris",
            "Ryan P. Thomson"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1400,
          "endTime": 1520,
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
        "courseReferenceNumber": "3175",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 3175
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
      "campusName": "Main",
      "crn": 4308
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "32525",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Center City",
      "crn": 32525
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
          "building": "PEARMC",
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Nicholas S. Mirabito"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
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
          "building": "ANDRSN",
          "room": "00017",
          "instructors": [
            "Kyle Harris",
            "Nicholas S. Mirabito"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1400,
          "endTime": 1520,
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
        "courseReferenceNumber": "9079",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 9079
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
      "campusName": "Main",
      "crn": 4308
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "32525",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Center City",
      "crn": 32525
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
          "building": "PEARMC",
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Gabriel Castillo"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": False,
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
          "building": "ANDRSN",
          "room": "00017",
          "instructors": [
            "Kyle Harris",
            "Gabriel Castillo"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1400,
          "endTime": 1520,
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
        "courseReferenceNumber": "20967",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 20967
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
      "campusName": "Main",
      "crn": 4308
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "32525",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Center City",
      "crn": 32525
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
            "Matthew R. Schofield"
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
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Matthew R. Schofield"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1800,
          "endTime": 1950,
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
        "courseReferenceNumber": "34793",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 34793
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
      "campusName": "Main",
      "crn": 4308
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "32525",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Center City",
      "crn": 32525
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
            "Aaron Jackson"
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
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Aaron Jackson"
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
        "courseReferenceNumber": "39178",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 39178
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
      "campusName": "Main",
      "crn": 4308
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "32525",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Center City",
      "crn": 32525
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
          "building": "PEARMC",
          "room": "0P148",
          "instructors": [
            "Jacqueline Phillips",
            "Brian Kopicko"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 800,
          "endTime": 920,
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
          "room": "0P016",
          "instructors": [
            "Jacqueline Phillips",
            "Brian Kopicko"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
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
        "courseReferenceNumber": "39814",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "campusName": "Main",
      "title": "Human Anatomy and Physiology I",
      "crn": 39814
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
          "building": "ANDRSN",
          "room": "00002",
          "instructors": [
            "Heather Levi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": True,
          "startTime": 1100,
          "endTime": 1150,
          "startDate": "08/24/2020",
          "monday": True
        }
      ],
      "isOpen": True,
      "attributes": {
        "description": "GenEd Race &amp; Diversity",
        "isZTCAttribute": False,
        "code": "GD",
        "class": "net.hedtech.banner.student.schedule.SectionDegreeProgramAttributeDecorator",
        "courseReferenceNumber": "40171",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Main",
      "crn": 40171
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
      "campusName": "Main",
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
          "building": "ANDRSN",
          "room": "00002",
          "instructors": [
            "Heather Levi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": True,
          "startTime": 1100,
          "endTime": 1150,
          "startDate": "08/24/2020",
          "monday": True
        }
      ],
      "isOpen": True,
      "attributes": {
        "description": "GenEd Race &amp; Diversity",
        "isZTCAttribute": False,
        "code": "GD",
        "class": "net.hedtech.banner.student.schedule.SectionDegreeProgramAttributeDecorator",
        "courseReferenceNumber": "40171",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Main",
      "crn": 40171
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
          "building": "ANDRSN",
          "room": "00002",
          "instructors": [
            "Heather Levi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": True,
          "startTime": 1100,
          "endTime": 1150,
          "startDate": "08/24/2020",
          "monday": True
        }
      ],
      "isOpen": True,
      "attributes": {
        "description": "GenEd Race &amp; Diversity",
        "isZTCAttribute": False,
        "code": "GD",
        "class": "net.hedtech.banner.student.schedule.SectionDegreeProgramAttributeDecorator",
        "courseReferenceNumber": "40171",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Main",
      "crn": 40171
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
          "building": "PEARMC",
          "room": "0P015",
          "instructors": [
            "Kyle Harris",
            "Ryan P. Thomson"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1200,
          "endTime": 1350,
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
          "building": "ANDRSN",
          "room": "00017",
          "instructors": [
            "Kyle Harris",
            "Ryan P. Thomson"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1400,
          "endTime": 1520,
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
        "courseReferenceNumber": "3175",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 3175
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
          "building": "ANDRSN",
          "room": "00002",
          "instructors": [
            "Heather Levi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": True,
          "startTime": 1100,
          "endTime": 1150,
          "startDate": "08/24/2020",
          "monday": True
        }
      ],
      "isOpen": True,
      "attributes": {
        "description": "GenEd Race &amp; Diversity",
        "isZTCAttribute": False,
        "code": "GD",
        "class": "net.hedtech.banner.student.schedule.SectionDegreeProgramAttributeDecorator",
        "courseReferenceNumber": "40171",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Main",
      "crn": 40171
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
          "building": "PEARMC",
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Nicholas S. Mirabito"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
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
          "building": "ANDRSN",
          "room": "00017",
          "instructors": [
            "Kyle Harris",
            "Nicholas S. Mirabito"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1400,
          "endTime": 1520,
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
        "courseReferenceNumber": "9079",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 9079
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
          "building": "ANDRSN",
          "room": "00002",
          "instructors": [
            "Heather Levi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": True,
          "startTime": 1100,
          "endTime": 1150,
          "startDate": "08/24/2020",
          "monday": True
        }
      ],
      "isOpen": True,
      "attributes": {
        "description": "GenEd Race &amp; Diversity",
        "isZTCAttribute": False,
        "code": "GD",
        "class": "net.hedtech.banner.student.schedule.SectionDegreeProgramAttributeDecorator",
        "courseReferenceNumber": "40171",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Main",
      "crn": 40171
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
            "Matthew R. Schofield"
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
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Matthew R. Schofield"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1800,
          "endTime": 1950,
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
        "courseReferenceNumber": "34793",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 34793
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
          "building": "ANDRSN",
          "room": "00002",
          "instructors": [
            "Heather Levi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": True,
          "startTime": 1100,
          "endTime": 1150,
          "startDate": "08/24/2020",
          "monday": True
        }
      ],
      "isOpen": True,
      "attributes": {
        "description": "GenEd Race &amp; Diversity",
        "isZTCAttribute": False,
        "code": "GD",
        "class": "net.hedtech.banner.student.schedule.SectionDegreeProgramAttributeDecorator",
        "courseReferenceNumber": "40171",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Main",
      "crn": 40171
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
            "Aaron Jackson"
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
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Aaron Jackson"
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
        "courseReferenceNumber": "39178",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 39178
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
          "building": "ANDRSN",
          "room": "00002",
          "instructors": [
            "Heather Levi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": True,
          "startTime": 1100,
          "endTime": 1150,
          "startDate": "08/24/2020",
          "monday": True
        }
      ],
      "isOpen": True,
      "attributes": {
        "description": "GenEd Race &amp; Diversity",
        "isZTCAttribute": False,
        "code": "GD",
        "class": "net.hedtech.banner.student.schedule.SectionDegreeProgramAttributeDecorator",
        "courseReferenceNumber": "40171",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Main",
      "crn": 40171
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
          "building": "PEARMC",
          "room": "0P148",
          "instructors": [
            "Jacqueline Phillips",
            "Brian Kopicko"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 800,
          "endTime": 920,
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
          "room": "0P016",
          "instructors": [
            "Jacqueline Phillips",
            "Brian Kopicko"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
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
        "courseReferenceNumber": "39814",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "campusName": "Main",
      "title": "Human Anatomy and Physiology I",
      "crn": 39814
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
          "room": "00359",
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
      "campusName": "Main",
      "crn": 24856
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
          "building": None,
          "room": None,
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
      "campusName": "Main",
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
          "room": "00359",
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
      "campusName": "Main",
      "crn": 24856
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
          "building": None,
          "room": None,
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
          "room": "00359",
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
      "campusName": "Main",
      "crn": 24856
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
          "building": None,
          "room": None,
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
          "thursday": False,
          "building": "PEARMC",
          "room": "0P015",
          "instructors": [
            "Kyle Harris",
            "Ryan P. Thomson"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1200,
          "endTime": 1350,
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
          "building": "ANDRSN",
          "room": "00017",
          "instructors": [
            "Kyle Harris",
            "Ryan P. Thomson"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1400,
          "endTime": 1520,
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
        "courseReferenceNumber": "3175",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 3175
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
          "room": "00359",
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
      "campusName": "Main",
      "crn": 24856
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
          "building": None,
          "room": None,
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
          "thursday": False,
          "building": "PEARMC",
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Nicholas S. Mirabito"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
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
          "building": "ANDRSN",
          "room": "00017",
          "instructors": [
            "Kyle Harris",
            "Nicholas S. Mirabito"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1400,
          "endTime": 1520,
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
        "courseReferenceNumber": "9079",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 9079
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
          "room": "00359",
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
      "campusName": "Main",
      "crn": 24856
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
          "building": None,
          "room": None,
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
          "thursday": False,
          "building": "PEARMC",
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Gabriel Castillo"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": False,
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
          "building": "ANDRSN",
          "room": "00017",
          "instructors": [
            "Kyle Harris",
            "Gabriel Castillo"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1400,
          "endTime": 1520,
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
        "courseReferenceNumber": "20967",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 20967
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
          "room": "00359",
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
      "campusName": "Main",
      "crn": 24856
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
          "building": None,
          "room": None,
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
            "Matthew R. Schofield"
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
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Matthew R. Schofield"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1800,
          "endTime": 1950,
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
        "courseReferenceNumber": "34793",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 34793
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
          "room": "00359",
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
      "campusName": "Main",
      "crn": 24856
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
          "building": None,
          "room": None,
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
            "Aaron Jackson"
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
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Aaron Jackson"
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
        "courseReferenceNumber": "39178",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 39178
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
          "room": "00359",
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
      "campusName": "Main",
      "crn": 24856
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
          "building": None,
          "room": None,
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
          "building": "PEARMC",
          "room": "0P148",
          "instructors": [
            "Jacqueline Phillips",
            "Brian Kopicko"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 800,
          "endTime": 920,
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
          "room": "0P016",
          "instructors": [
            "Jacqueline Phillips",
            "Brian Kopicko"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
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
        "courseReferenceNumber": "39814",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "campusName": "Main",
      "title": "Human Anatomy and Physiology I",
      "crn": 39814
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
          "room": "00359",
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
      "campusName": "Main",
      "crn": 24856
    },
    {
      "campus": "AMB",
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "26674",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Ambler",
      "crn": 26674
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
      "campusName": "Main",
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
          "room": "00359",
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
      "campusName": "Main",
      "crn": 24856
    },
    {
      "campus": "AMB",
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "26674",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Ambler",
      "crn": 26674
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
          "room": "00359",
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
      "campusName": "Main",
      "crn": 24856
    },
    {
      "campus": "AMB",
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "26674",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Ambler",
      "crn": 26674
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
          "building": "PEARMC",
          "room": "0P015",
          "instructors": [
            "Kyle Harris",
            "Ryan P. Thomson"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1200,
          "endTime": 1350,
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
          "building": "ANDRSN",
          "room": "00017",
          "instructors": [
            "Kyle Harris",
            "Ryan P. Thomson"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1400,
          "endTime": 1520,
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
        "courseReferenceNumber": "3175",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 3175
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
          "room": "00359",
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
      "campusName": "Main",
      "crn": 24856
    },
    {
      "campus": "AMB",
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "26674",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Ambler",
      "crn": 26674
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
          "building": "PEARMC",
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Nicholas S. Mirabito"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
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
          "building": "ANDRSN",
          "room": "00017",
          "instructors": [
            "Kyle Harris",
            "Nicholas S. Mirabito"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1400,
          "endTime": 1520,
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
        "courseReferenceNumber": "9079",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 9079
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
          "room": "00359",
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
      "campusName": "Main",
      "crn": 24856
    },
    {
      "campus": "AMB",
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "26674",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Ambler",
      "crn": 26674
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
          "building": "PEARMC",
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Gabriel Castillo"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": False,
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
          "building": "ANDRSN",
          "room": "00017",
          "instructors": [
            "Kyle Harris",
            "Gabriel Castillo"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1400,
          "endTime": 1520,
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
        "courseReferenceNumber": "20967",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 20967
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
          "room": "00359",
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
      "campusName": "Main",
      "crn": 24856
    },
    {
      "campus": "AMB",
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "26674",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Ambler",
      "crn": 26674
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
            "Matthew R. Schofield"
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
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Matthew R. Schofield"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1800,
          "endTime": 1950,
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
        "courseReferenceNumber": "34793",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 34793
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
          "room": "00359",
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
      "campusName": "Main",
      "crn": 24856
    },
    {
      "campus": "AMB",
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "26674",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Ambler",
      "crn": 26674
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
            "Aaron Jackson"
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
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Aaron Jackson"
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
        "courseReferenceNumber": "39178",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 39178
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
          "room": "00359",
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
      "campusName": "Main",
      "crn": 24856
    },
    {
      "campus": "AMB",
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "26674",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Ambler",
      "crn": 26674
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
          "building": "PEARMC",
          "room": "0P148",
          "instructors": [
            "Jacqueline Phillips",
            "Brian Kopicko"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 800,
          "endTime": 920,
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
          "room": "0P016",
          "instructors": [
            "Jacqueline Phillips",
            "Brian Kopicko"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
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
        "courseReferenceNumber": "39814",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "campusName": "Main",
      "title": "Human Anatomy and Physiology I",
      "crn": 39814
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
          "room": "00359",
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
      "campusName": "Main",
      "crn": 24856
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "32525",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Center City",
      "crn": 32525
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
      "campusName": "Main",
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
          "room": "00359",
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
      "campusName": "Main",
      "crn": 24856
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "32525",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Center City",
      "crn": 32525
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
          "room": "00359",
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
      "campusName": "Main",
      "crn": 24856
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "32525",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Center City",
      "crn": 32525
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
          "building": "PEARMC",
          "room": "0P015",
          "instructors": [
            "Kyle Harris",
            "Ryan P. Thomson"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1200,
          "endTime": 1350,
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
          "building": "ANDRSN",
          "room": "00017",
          "instructors": [
            "Kyle Harris",
            "Ryan P. Thomson"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1400,
          "endTime": 1520,
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
        "courseReferenceNumber": "3175",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 3175
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
          "room": "00359",
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
      "campusName": "Main",
      "crn": 24856
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "32525",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Center City",
      "crn": 32525
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
          "building": "PEARMC",
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Nicholas S. Mirabito"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
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
          "building": "ANDRSN",
          "room": "00017",
          "instructors": [
            "Kyle Harris",
            "Nicholas S. Mirabito"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1400,
          "endTime": 1520,
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
        "courseReferenceNumber": "9079",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 9079
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
          "room": "00359",
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
      "campusName": "Main",
      "crn": 24856
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "32525",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Center City",
      "crn": 32525
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
          "building": "PEARMC",
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Gabriel Castillo"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": False,
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
          "building": "ANDRSN",
          "room": "00017",
          "instructors": [
            "Kyle Harris",
            "Gabriel Castillo"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1400,
          "endTime": 1520,
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
        "courseReferenceNumber": "20967",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 20967
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
          "room": "00359",
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
      "campusName": "Main",
      "crn": 24856
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "32525",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Center City",
      "crn": 32525
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
            "Matthew R. Schofield"
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
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Matthew R. Schofield"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1800,
          "endTime": 1950,
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
        "courseReferenceNumber": "34793",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 34793
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
          "room": "00359",
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
      "campusName": "Main",
      "crn": 24856
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "32525",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Center City",
      "crn": 32525
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
            "Aaron Jackson"
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
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Aaron Jackson"
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
        "courseReferenceNumber": "39178",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 39178
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
          "room": "00359",
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
      "campusName": "Main",
      "crn": 24856
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "32525",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Center City",
      "crn": 32525
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
          "building": "PEARMC",
          "room": "0P148",
          "instructors": [
            "Jacqueline Phillips",
            "Brian Kopicko"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 800,
          "endTime": 920,
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
          "room": "0P016",
          "instructors": [
            "Jacqueline Phillips",
            "Brian Kopicko"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
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
        "courseReferenceNumber": "39814",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "campusName": "Main",
      "title": "Human Anatomy and Physiology I",
      "crn": 39814
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
          "room": "00359",
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
      "campusName": "Main",
      "crn": 24856
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
          "building": "ANDRSN",
          "room": "00002",
          "instructors": [
            "Heather Levi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": True,
          "startTime": 1100,
          "endTime": 1150,
          "startDate": "08/24/2020",
          "monday": True
        }
      ],
      "isOpen": True,
      "attributes": {
        "description": "GenEd Race &amp; Diversity",
        "isZTCAttribute": False,
        "code": "GD",
        "class": "net.hedtech.banner.student.schedule.SectionDegreeProgramAttributeDecorator",
        "courseReferenceNumber": "40171",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Main",
      "crn": 40171
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
      "campusName": "Main",
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
          "room": "00359",
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
      "campusName": "Main",
      "crn": 24856
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
          "building": "ANDRSN",
          "room": "00002",
          "instructors": [
            "Heather Levi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": True,
          "startTime": 1100,
          "endTime": 1150,
          "startDate": "08/24/2020",
          "monday": True
        }
      ],
      "isOpen": True,
      "attributes": {
        "description": "GenEd Race &amp; Diversity",
        "isZTCAttribute": False,
        "code": "GD",
        "class": "net.hedtech.banner.student.schedule.SectionDegreeProgramAttributeDecorator",
        "courseReferenceNumber": "40171",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Main",
      "crn": 40171
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
          "room": "00359",
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
      "campusName": "Main",
      "crn": 24856
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
          "building": "ANDRSN",
          "room": "00002",
          "instructors": [
            "Heather Levi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": True,
          "startTime": 1100,
          "endTime": 1150,
          "startDate": "08/24/2020",
          "monday": True
        }
      ],
      "isOpen": True,
      "attributes": {
        "description": "GenEd Race &amp; Diversity",
        "isZTCAttribute": False,
        "code": "GD",
        "class": "net.hedtech.banner.student.schedule.SectionDegreeProgramAttributeDecorator",
        "courseReferenceNumber": "40171",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Main",
      "crn": 40171
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
          "building": "PEARMC",
          "room": "0P015",
          "instructors": [
            "Kyle Harris",
            "Ryan P. Thomson"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1200,
          "endTime": 1350,
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
          "building": "ANDRSN",
          "room": "00017",
          "instructors": [
            "Kyle Harris",
            "Ryan P. Thomson"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1400,
          "endTime": 1520,
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
        "courseReferenceNumber": "3175",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 3175
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
          "room": "00359",
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
      "campusName": "Main",
      "crn": 24856
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
          "building": "ANDRSN",
          "room": "00002",
          "instructors": [
            "Heather Levi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": True,
          "startTime": 1100,
          "endTime": 1150,
          "startDate": "08/24/2020",
          "monday": True
        }
      ],
      "isOpen": True,
      "attributes": {
        "description": "GenEd Race &amp; Diversity",
        "isZTCAttribute": False,
        "code": "GD",
        "class": "net.hedtech.banner.student.schedule.SectionDegreeProgramAttributeDecorator",
        "courseReferenceNumber": "40171",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Main",
      "crn": 40171
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
          "building": "PEARMC",
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Nicholas S. Mirabito"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
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
          "building": "ANDRSN",
          "room": "00017",
          "instructors": [
            "Kyle Harris",
            "Nicholas S. Mirabito"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1400,
          "endTime": 1520,
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
        "courseReferenceNumber": "9079",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 9079
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
          "room": "00359",
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
      "campusName": "Main",
      "crn": 24856
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
          "building": "ANDRSN",
          "room": "00002",
          "instructors": [
            "Heather Levi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": True,
          "startTime": 1100,
          "endTime": 1150,
          "startDate": "08/24/2020",
          "monday": True
        }
      ],
      "isOpen": True,
      "attributes": {
        "description": "GenEd Race &amp; Diversity",
        "isZTCAttribute": False,
        "code": "GD",
        "class": "net.hedtech.banner.student.schedule.SectionDegreeProgramAttributeDecorator",
        "courseReferenceNumber": "40171",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Main",
      "crn": 40171
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
            "Matthew R. Schofield"
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
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Matthew R. Schofield"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1800,
          "endTime": 1950,
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
        "courseReferenceNumber": "34793",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 34793
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
          "room": "00359",
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
      "campusName": "Main",
      "crn": 24856
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
          "building": "ANDRSN",
          "room": "00002",
          "instructors": [
            "Heather Levi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": True,
          "startTime": 1100,
          "endTime": 1150,
          "startDate": "08/24/2020",
          "monday": True
        }
      ],
      "isOpen": True,
      "attributes": {
        "description": "GenEd Race &amp; Diversity",
        "isZTCAttribute": False,
        "code": "GD",
        "class": "net.hedtech.banner.student.schedule.SectionDegreeProgramAttributeDecorator",
        "courseReferenceNumber": "40171",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Main",
      "crn": 40171
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
            "Aaron Jackson"
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
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Aaron Jackson"
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
        "courseReferenceNumber": "39178",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 39178
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
          "room": "00359",
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
      "campusName": "Main",
      "crn": 24856
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
          "building": "ANDRSN",
          "room": "00002",
          "instructors": [
            "Heather Levi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": True,
          "startTime": 1100,
          "endTime": 1150,
          "startDate": "08/24/2020",
          "monday": True
        }
      ],
      "isOpen": True,
      "attributes": {
        "description": "GenEd Race &amp; Diversity",
        "isZTCAttribute": False,
        "code": "GD",
        "class": "net.hedtech.banner.student.schedule.SectionDegreeProgramAttributeDecorator",
        "courseReferenceNumber": "40171",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Main",
      "crn": 40171
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
          "building": "PEARMC",
          "room": "0P148",
          "instructors": [
            "Jacqueline Phillips",
            "Brian Kopicko"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 800,
          "endTime": 920,
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
          "room": "0P016",
          "instructors": [
            "Jacqueline Phillips",
            "Brian Kopicko"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
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
        "courseReferenceNumber": "39814",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "campusName": "Main",
      "title": "Human Anatomy and Physiology I",
      "crn": 39814
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
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
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
          "building": "TTLMAN",
          "room": "00302",
          "instructors": [
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1530,
          "endTime": 1650,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 29894
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
          "building": None,
          "room": None,
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
      "campusName": "Main",
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
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
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
          "building": "TTLMAN",
          "room": "00302",
          "instructors": [
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1530,
          "endTime": 1650,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 29894
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
          "building": None,
          "room": None,
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
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
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
          "building": "TTLMAN",
          "room": "00302",
          "instructors": [
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1530,
          "endTime": 1650,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 29894
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
          "building": None,
          "room": None,
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
          "thursday": False,
          "building": "PEARMC",
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Nicholas S. Mirabito"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
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
          "building": "ANDRSN",
          "room": "00017",
          "instructors": [
            "Kyle Harris",
            "Nicholas S. Mirabito"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1400,
          "endTime": 1520,
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
        "courseReferenceNumber": "9079",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 9079
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
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
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
          "building": "TTLMAN",
          "room": "00302",
          "instructors": [
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1530,
          "endTime": 1650,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 29894
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
          "building": None,
          "room": None,
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
          "thursday": False,
          "building": "PEARMC",
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Gabriel Castillo"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": False,
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
          "building": "ANDRSN",
          "room": "00017",
          "instructors": [
            "Kyle Harris",
            "Gabriel Castillo"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1400,
          "endTime": 1520,
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
        "courseReferenceNumber": "20967",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 20967
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
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
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
          "building": "TTLMAN",
          "room": "00302",
          "instructors": [
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1530,
          "endTime": 1650,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 29894
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
          "building": None,
          "room": None,
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
          "thursday": False,
          "building": "PEARMC",
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Shirin Hussain"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1200,
          "endTime": 1350,
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
          "building": "ANDRSN",
          "room": "00017",
          "instructors": [
            "Kyle Harris",
            "Shirin Hussain"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1400,
          "endTime": 1520,
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
        "courseReferenceNumber": "28709",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 28709
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
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
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
          "building": "TTLMAN",
          "room": "00302",
          "instructors": [
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1530,
          "endTime": 1650,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 29894
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
          "building": None,
          "room": None,
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
            "Matthew R. Schofield"
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
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Matthew R. Schofield"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1800,
          "endTime": 1950,
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
        "courseReferenceNumber": "34793",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 34793
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
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
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
          "building": "TTLMAN",
          "room": "00302",
          "instructors": [
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1530,
          "endTime": 1650,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 29894
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
          "building": None,
          "room": None,
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
            "Aaron Jackson"
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
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Aaron Jackson"
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
        "courseReferenceNumber": "39178",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 39178
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
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
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
          "building": "TTLMAN",
          "room": "00302",
          "instructors": [
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1530,
          "endTime": 1650,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 29894
    },
    {
      "campus": "AMB",
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "26674",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Ambler",
      "crn": 26674
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
      "campusName": "Main",
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
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
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
          "building": "TTLMAN",
          "room": "00302",
          "instructors": [
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1530,
          "endTime": 1650,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 29894
    },
    {
      "campus": "AMB",
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "26674",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Ambler",
      "crn": 26674
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
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
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
          "building": "TTLMAN",
          "room": "00302",
          "instructors": [
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1530,
          "endTime": 1650,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 29894
    },
    {
      "campus": "AMB",
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "26674",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Ambler",
      "crn": 26674
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
          "building": "PEARMC",
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Nicholas S. Mirabito"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
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
          "building": "ANDRSN",
          "room": "00017",
          "instructors": [
            "Kyle Harris",
            "Nicholas S. Mirabito"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1400,
          "endTime": 1520,
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
        "courseReferenceNumber": "9079",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 9079
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
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
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
          "building": "TTLMAN",
          "room": "00302",
          "instructors": [
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1530,
          "endTime": 1650,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 29894
    },
    {
      "campus": "AMB",
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "26674",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Ambler",
      "crn": 26674
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
          "building": "PEARMC",
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Gabriel Castillo"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": False,
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
          "building": "ANDRSN",
          "room": "00017",
          "instructors": [
            "Kyle Harris",
            "Gabriel Castillo"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1400,
          "endTime": 1520,
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
        "courseReferenceNumber": "20967",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 20967
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
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
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
          "building": "TTLMAN",
          "room": "00302",
          "instructors": [
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1530,
          "endTime": 1650,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 29894
    },
    {
      "campus": "AMB",
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "26674",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Ambler",
      "crn": 26674
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
          "building": "PEARMC",
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Shirin Hussain"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1200,
          "endTime": 1350,
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
          "building": "ANDRSN",
          "room": "00017",
          "instructors": [
            "Kyle Harris",
            "Shirin Hussain"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1400,
          "endTime": 1520,
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
        "courseReferenceNumber": "28709",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 28709
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
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
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
          "building": "TTLMAN",
          "room": "00302",
          "instructors": [
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1530,
          "endTime": 1650,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 29894
    },
    {
      "campus": "AMB",
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "26674",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Ambler",
      "crn": 26674
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
            "Matthew R. Schofield"
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
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Matthew R. Schofield"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1800,
          "endTime": 1950,
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
        "courseReferenceNumber": "34793",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 34793
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
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
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
          "building": "TTLMAN",
          "room": "00302",
          "instructors": [
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1530,
          "endTime": 1650,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 29894
    },
    {
      "campus": "AMB",
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "26674",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Ambler",
      "crn": 26674
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
            "Aaron Jackson"
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
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Aaron Jackson"
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
        "courseReferenceNumber": "39178",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 39178
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
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
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
          "building": "TTLMAN",
          "room": "00302",
          "instructors": [
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1530,
          "endTime": 1650,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 29894
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
          "building": "ANDRSN",
          "room": "00002",
          "instructors": [
            "Heather Levi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": True,
          "startTime": 1000,
          "endTime": 1050,
          "startDate": "08/24/2020",
          "monday": True
        }
      ],
      "isOpen": True,
      "attributes": {
        "description": "GenEd Race &amp; Diversity",
        "isZTCAttribute": False,
        "code": "GD",
        "class": "net.hedtech.banner.student.schedule.SectionDegreeProgramAttributeDecorator",
        "courseReferenceNumber": "30014",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Main",
      "crn": 30014
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
      "campusName": "Main",
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
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
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
          "building": "TTLMAN",
          "room": "00302",
          "instructors": [
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1530,
          "endTime": 1650,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 29894
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
          "building": "ANDRSN",
          "room": "00002",
          "instructors": [
            "Heather Levi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": True,
          "startTime": 1000,
          "endTime": 1050,
          "startDate": "08/24/2020",
          "monday": True
        }
      ],
      "isOpen": True,
      "attributes": {
        "description": "GenEd Race &amp; Diversity",
        "isZTCAttribute": False,
        "code": "GD",
        "class": "net.hedtech.banner.student.schedule.SectionDegreeProgramAttributeDecorator",
        "courseReferenceNumber": "30014",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Main",
      "crn": 30014
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
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
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
          "building": "TTLMAN",
          "room": "00302",
          "instructors": [
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1530,
          "endTime": 1650,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 29894
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
          "building": "ANDRSN",
          "room": "00002",
          "instructors": [
            "Heather Levi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": True,
          "startTime": 1000,
          "endTime": 1050,
          "startDate": "08/24/2020",
          "monday": True
        }
      ],
      "isOpen": True,
      "attributes": {
        "description": "GenEd Race &amp; Diversity",
        "isZTCAttribute": False,
        "code": "GD",
        "class": "net.hedtech.banner.student.schedule.SectionDegreeProgramAttributeDecorator",
        "courseReferenceNumber": "30014",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Main",
      "crn": 30014
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
          "building": "PEARMC",
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Nicholas S. Mirabito"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
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
          "building": "ANDRSN",
          "room": "00017",
          "instructors": [
            "Kyle Harris",
            "Nicholas S. Mirabito"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1400,
          "endTime": 1520,
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
        "courseReferenceNumber": "9079",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 9079
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
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
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
          "building": "TTLMAN",
          "room": "00302",
          "instructors": [
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1530,
          "endTime": 1650,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 29894
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
          "building": "ANDRSN",
          "room": "00002",
          "instructors": [
            "Heather Levi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": True,
          "startTime": 1000,
          "endTime": 1050,
          "startDate": "08/24/2020",
          "monday": True
        }
      ],
      "isOpen": True,
      "attributes": {
        "description": "GenEd Race &amp; Diversity",
        "isZTCAttribute": False,
        "code": "GD",
        "class": "net.hedtech.banner.student.schedule.SectionDegreeProgramAttributeDecorator",
        "courseReferenceNumber": "30014",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Main",
      "crn": 30014
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
          "building": "PEARMC",
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Shirin Hussain"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1200,
          "endTime": 1350,
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
          "building": "ANDRSN",
          "room": "00017",
          "instructors": [
            "Kyle Harris",
            "Shirin Hussain"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1400,
          "endTime": 1520,
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
        "courseReferenceNumber": "28709",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 28709
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
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
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
          "building": "TTLMAN",
          "room": "00302",
          "instructors": [
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1530,
          "endTime": 1650,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 29894
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
          "building": "ANDRSN",
          "room": "00002",
          "instructors": [
            "Heather Levi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": True,
          "startTime": 1000,
          "endTime": 1050,
          "startDate": "08/24/2020",
          "monday": True
        }
      ],
      "isOpen": True,
      "attributes": {
        "description": "GenEd Race &amp; Diversity",
        "isZTCAttribute": False,
        "code": "GD",
        "class": "net.hedtech.banner.student.schedule.SectionDegreeProgramAttributeDecorator",
        "courseReferenceNumber": "30014",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Main",
      "crn": 30014
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
            "Matthew R. Schofield"
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
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Matthew R. Schofield"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1800,
          "endTime": 1950,
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
        "courseReferenceNumber": "34793",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 34793
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
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
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
          "building": "TTLMAN",
          "room": "00302",
          "instructors": [
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1530,
          "endTime": 1650,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 29894
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
          "building": "ANDRSN",
          "room": "00002",
          "instructors": [
            "Heather Levi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": True,
          "startTime": 1000,
          "endTime": 1050,
          "startDate": "08/24/2020",
          "monday": True
        }
      ],
      "isOpen": True,
      "attributes": {
        "description": "GenEd Race &amp; Diversity",
        "isZTCAttribute": False,
        "code": "GD",
        "class": "net.hedtech.banner.student.schedule.SectionDegreeProgramAttributeDecorator",
        "courseReferenceNumber": "30014",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Main",
      "crn": 30014
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
            "Aaron Jackson"
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
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Aaron Jackson"
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
        "courseReferenceNumber": "39178",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 39178
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
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
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
          "building": "TTLMAN",
          "room": "00302",
          "instructors": [
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1530,
          "endTime": 1650,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 29894
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "32525",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Center City",
      "crn": 32525
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
      "campusName": "Main",
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
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
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
          "building": "TTLMAN",
          "room": "00302",
          "instructors": [
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1530,
          "endTime": 1650,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 29894
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "32525",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Center City",
      "crn": 32525
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
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
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
          "building": "TTLMAN",
          "room": "00302",
          "instructors": [
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1530,
          "endTime": 1650,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 29894
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "32525",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Center City",
      "crn": 32525
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
          "building": "PEARMC",
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Nicholas S. Mirabito"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
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
          "building": "ANDRSN",
          "room": "00017",
          "instructors": [
            "Kyle Harris",
            "Nicholas S. Mirabito"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1400,
          "endTime": 1520,
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
        "courseReferenceNumber": "9079",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 9079
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
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
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
          "building": "TTLMAN",
          "room": "00302",
          "instructors": [
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1530,
          "endTime": 1650,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 29894
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "32525",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Center City",
      "crn": 32525
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
          "building": "PEARMC",
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Gabriel Castillo"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": False,
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
          "building": "ANDRSN",
          "room": "00017",
          "instructors": [
            "Kyle Harris",
            "Gabriel Castillo"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1400,
          "endTime": 1520,
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
        "courseReferenceNumber": "20967",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 20967
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
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
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
          "building": "TTLMAN",
          "room": "00302",
          "instructors": [
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1530,
          "endTime": 1650,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 29894
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "32525",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Center City",
      "crn": 32525
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
          "building": "PEARMC",
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Shirin Hussain"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1200,
          "endTime": 1350,
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
          "building": "ANDRSN",
          "room": "00017",
          "instructors": [
            "Kyle Harris",
            "Shirin Hussain"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1400,
          "endTime": 1520,
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
        "courseReferenceNumber": "28709",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 28709
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
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
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
          "building": "TTLMAN",
          "room": "00302",
          "instructors": [
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1530,
          "endTime": 1650,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 29894
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "32525",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Center City",
      "crn": 32525
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
            "Matthew R. Schofield"
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
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Matthew R. Schofield"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1800,
          "endTime": 1950,
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
        "courseReferenceNumber": "34793",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 34793
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
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
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
          "building": "TTLMAN",
          "room": "00302",
          "instructors": [
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1530,
          "endTime": 1650,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 29894
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "32525",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Center City",
      "crn": 32525
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
            "Aaron Jackson"
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
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Aaron Jackson"
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
        "courseReferenceNumber": "39178",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 39178
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
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
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
          "building": "TTLMAN",
          "room": "00302",
          "instructors": [
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1530,
          "endTime": 1650,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 29894
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
          "building": "ANDRSN",
          "room": "00002",
          "instructors": [
            "Heather Levi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": True,
          "startTime": 1100,
          "endTime": 1150,
          "startDate": "08/24/2020",
          "monday": True
        }
      ],
      "isOpen": True,
      "attributes": {
        "description": "GenEd Race &amp; Diversity",
        "isZTCAttribute": False,
        "code": "GD",
        "class": "net.hedtech.banner.student.schedule.SectionDegreeProgramAttributeDecorator",
        "courseReferenceNumber": "40171",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Main",
      "crn": 40171
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
      "campusName": "Main",
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
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
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
          "building": "TTLMAN",
          "room": "00302",
          "instructors": [
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1530,
          "endTime": 1650,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 29894
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
          "building": "ANDRSN",
          "room": "00002",
          "instructors": [
            "Heather Levi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": True,
          "startTime": 1100,
          "endTime": 1150,
          "startDate": "08/24/2020",
          "monday": True
        }
      ],
      "isOpen": True,
      "attributes": {
        "description": "GenEd Race &amp; Diversity",
        "isZTCAttribute": False,
        "code": "GD",
        "class": "net.hedtech.banner.student.schedule.SectionDegreeProgramAttributeDecorator",
        "courseReferenceNumber": "40171",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Main",
      "crn": 40171
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
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
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
          "building": "TTLMAN",
          "room": "00302",
          "instructors": [
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1530,
          "endTime": 1650,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 29894
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
          "building": "ANDRSN",
          "room": "00002",
          "instructors": [
            "Heather Levi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": True,
          "startTime": 1100,
          "endTime": 1150,
          "startDate": "08/24/2020",
          "monday": True
        }
      ],
      "isOpen": True,
      "attributes": {
        "description": "GenEd Race &amp; Diversity",
        "isZTCAttribute": False,
        "code": "GD",
        "class": "net.hedtech.banner.student.schedule.SectionDegreeProgramAttributeDecorator",
        "courseReferenceNumber": "40171",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Main",
      "crn": 40171
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
          "building": "PEARMC",
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Nicholas S. Mirabito"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
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
          "building": "ANDRSN",
          "room": "00017",
          "instructors": [
            "Kyle Harris",
            "Nicholas S. Mirabito"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1400,
          "endTime": 1520,
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
        "courseReferenceNumber": "9079",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 9079
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
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
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
          "building": "TTLMAN",
          "room": "00302",
          "instructors": [
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1530,
          "endTime": 1650,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 29894
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
          "building": "ANDRSN",
          "room": "00002",
          "instructors": [
            "Heather Levi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": True,
          "startTime": 1100,
          "endTime": 1150,
          "startDate": "08/24/2020",
          "monday": True
        }
      ],
      "isOpen": True,
      "attributes": {
        "description": "GenEd Race &amp; Diversity",
        "isZTCAttribute": False,
        "code": "GD",
        "class": "net.hedtech.banner.student.schedule.SectionDegreeProgramAttributeDecorator",
        "courseReferenceNumber": "40171",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Main",
      "crn": 40171
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
          "building": "PEARMC",
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Shirin Hussain"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1200,
          "endTime": 1350,
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
          "building": "ANDRSN",
          "room": "00017",
          "instructors": [
            "Kyle Harris",
            "Shirin Hussain"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1400,
          "endTime": 1520,
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
        "courseReferenceNumber": "28709",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 28709
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
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
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
          "building": "TTLMAN",
          "room": "00302",
          "instructors": [
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1530,
          "endTime": 1650,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 29894
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
          "building": "ANDRSN",
          "room": "00002",
          "instructors": [
            "Heather Levi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": True,
          "startTime": 1100,
          "endTime": 1150,
          "startDate": "08/24/2020",
          "monday": True
        }
      ],
      "isOpen": True,
      "attributes": {
        "description": "GenEd Race &amp; Diversity",
        "isZTCAttribute": False,
        "code": "GD",
        "class": "net.hedtech.banner.student.schedule.SectionDegreeProgramAttributeDecorator",
        "courseReferenceNumber": "40171",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Main",
      "crn": 40171
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
            "Matthew R. Schofield"
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
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Matthew R. Schofield"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1800,
          "endTime": 1950,
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
        "courseReferenceNumber": "34793",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 34793
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
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
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
          "building": "TTLMAN",
          "room": "00302",
          "instructors": [
            "Tamer Aldwairi"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1530,
          "endTime": 1650,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 29894
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
          "building": "ANDRSN",
          "room": "00002",
          "instructors": [
            "Heather Levi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": True,
          "startTime": 1100,
          "endTime": 1150,
          "startDate": "08/24/2020",
          "monday": True
        }
      ],
      "isOpen": True,
      "attributes": {
        "description": "GenEd Race &amp; Diversity",
        "isZTCAttribute": False,
        "code": "GD",
        "class": "net.hedtech.banner.student.schedule.SectionDegreeProgramAttributeDecorator",
        "courseReferenceNumber": "40171",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Main",
      "crn": 40171
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
            "Aaron Jackson"
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
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Aaron Jackson"
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
        "courseReferenceNumber": "39178",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 39178
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
          "building": "SERC",
          "room": "00359",
          "instructors": [
            "Eugene Kwatny"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 38749
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
          "building": None,
          "room": None,
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
      "campusName": "Main",
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
          "building": "SERC",
          "room": "00359",
          "instructors": [
            "Eugene Kwatny"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 38749
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
          "building": None,
          "room": None,
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
          "building": "SERC",
          "room": "00359",
          "instructors": [
            "Eugene Kwatny"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 38749
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
          "building": None,
          "room": None,
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
          "thursday": False,
          "building": "PEARMC",
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Nicholas S. Mirabito"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
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
          "building": "ANDRSN",
          "room": "00017",
          "instructors": [
            "Kyle Harris",
            "Nicholas S. Mirabito"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1400,
          "endTime": 1520,
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
        "courseReferenceNumber": "9079",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 9079
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
          "building": "SERC",
          "room": "00359",
          "instructors": [
            "Eugene Kwatny"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 38749
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
          "building": None,
          "room": None,
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
          "thursday": False,
          "building": "PEARMC",
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Gabriel Castillo"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": False,
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
          "building": "ANDRSN",
          "room": "00017",
          "instructors": [
            "Kyle Harris",
            "Gabriel Castillo"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1400,
          "endTime": 1520,
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
        "courseReferenceNumber": "20967",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 20967
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
          "building": "SERC",
          "room": "00359",
          "instructors": [
            "Eugene Kwatny"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 38749
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
          "building": None,
          "room": None,
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
            "Matthew R. Schofield"
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
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Matthew R. Schofield"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1800,
          "endTime": 1950,
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
        "courseReferenceNumber": "34793",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 34793
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
          "building": "SERC",
          "room": "00359",
          "instructors": [
            "Eugene Kwatny"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 38749
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
          "building": None,
          "room": None,
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
            "Aaron Jackson"
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
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Aaron Jackson"
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
        "courseReferenceNumber": "39178",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 39178
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
          "building": "SERC",
          "room": "00359",
          "instructors": [
            "Eugene Kwatny"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 38749
    },
    {
      "campus": "AMB",
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "26674",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Ambler",
      "crn": 26674
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
      "campusName": "Main",
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
          "building": "SERC",
          "room": "00359",
          "instructors": [
            "Eugene Kwatny"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 38749
    },
    {
      "campus": "AMB",
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "26674",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Ambler",
      "crn": 26674
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
          "building": "SERC",
          "room": "00359",
          "instructors": [
            "Eugene Kwatny"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 38749
    },
    {
      "campus": "AMB",
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "26674",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Ambler",
      "crn": 26674
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
          "building": "PEARMC",
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Nicholas S. Mirabito"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
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
          "building": "ANDRSN",
          "room": "00017",
          "instructors": [
            "Kyle Harris",
            "Nicholas S. Mirabito"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1400,
          "endTime": 1520,
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
        "courseReferenceNumber": "9079",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 9079
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
          "building": "SERC",
          "room": "00359",
          "instructors": [
            "Eugene Kwatny"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 38749
    },
    {
      "campus": "AMB",
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "26674",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Ambler",
      "crn": 26674
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
          "building": "PEARMC",
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Gabriel Castillo"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": False,
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
          "building": "ANDRSN",
          "room": "00017",
          "instructors": [
            "Kyle Harris",
            "Gabriel Castillo"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1400,
          "endTime": 1520,
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
        "courseReferenceNumber": "20967",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 20967
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
          "building": "SERC",
          "room": "00359",
          "instructors": [
            "Eugene Kwatny"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 38749
    },
    {
      "campus": "AMB",
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "26674",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Ambler",
      "crn": 26674
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
            "Matthew R. Schofield"
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
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Matthew R. Schofield"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1800,
          "endTime": 1950,
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
        "courseReferenceNumber": "34793",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 34793
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
          "building": "SERC",
          "room": "00359",
          "instructors": [
            "Eugene Kwatny"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 38749
    },
    {
      "campus": "AMB",
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "26674",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Ambler",
      "crn": 26674
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
            "Aaron Jackson"
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
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Aaron Jackson"
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
        "courseReferenceNumber": "39178",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 39178
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
          "building": "SERC",
          "room": "00359",
          "instructors": [
            "Eugene Kwatny"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 38749
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
          "building": "ANDRSN",
          "room": "00002",
          "instructors": [
            "Heather Levi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": True,
          "startTime": 1000,
          "endTime": 1050,
          "startDate": "08/24/2020",
          "monday": True
        }
      ],
      "isOpen": True,
      "attributes": {
        "description": "GenEd Race &amp; Diversity",
        "isZTCAttribute": False,
        "code": "GD",
        "class": "net.hedtech.banner.student.schedule.SectionDegreeProgramAttributeDecorator",
        "courseReferenceNumber": "30014",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Main",
      "crn": 30014
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
      "campusName": "Main",
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
          "building": "SERC",
          "room": "00359",
          "instructors": [
            "Eugene Kwatny"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 38749
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
          "building": "ANDRSN",
          "room": "00002",
          "instructors": [
            "Heather Levi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": True,
          "startTime": 1000,
          "endTime": 1050,
          "startDate": "08/24/2020",
          "monday": True
        }
      ],
      "isOpen": True,
      "attributes": {
        "description": "GenEd Race &amp; Diversity",
        "isZTCAttribute": False,
        "code": "GD",
        "class": "net.hedtech.banner.student.schedule.SectionDegreeProgramAttributeDecorator",
        "courseReferenceNumber": "30014",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Main",
      "crn": 30014
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
          "building": "SERC",
          "room": "00359",
          "instructors": [
            "Eugene Kwatny"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 38749
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
          "building": "ANDRSN",
          "room": "00002",
          "instructors": [
            "Heather Levi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": True,
          "startTime": 1000,
          "endTime": 1050,
          "startDate": "08/24/2020",
          "monday": True
        }
      ],
      "isOpen": True,
      "attributes": {
        "description": "GenEd Race &amp; Diversity",
        "isZTCAttribute": False,
        "code": "GD",
        "class": "net.hedtech.banner.student.schedule.SectionDegreeProgramAttributeDecorator",
        "courseReferenceNumber": "30014",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Main",
      "crn": 30014
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
          "building": "PEARMC",
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Nicholas S. Mirabito"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
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
          "building": "ANDRSN",
          "room": "00017",
          "instructors": [
            "Kyle Harris",
            "Nicholas S. Mirabito"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1400,
          "endTime": 1520,
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
        "courseReferenceNumber": "9079",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 9079
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
          "building": "SERC",
          "room": "00359",
          "instructors": [
            "Eugene Kwatny"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 38749
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
          "building": "ANDRSN",
          "room": "00002",
          "instructors": [
            "Heather Levi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": True,
          "startTime": 1000,
          "endTime": 1050,
          "startDate": "08/24/2020",
          "monday": True
        }
      ],
      "isOpen": True,
      "attributes": {
        "description": "GenEd Race &amp; Diversity",
        "isZTCAttribute": False,
        "code": "GD",
        "class": "net.hedtech.banner.student.schedule.SectionDegreeProgramAttributeDecorator",
        "courseReferenceNumber": "30014",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Main",
      "crn": 30014
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
            "Matthew R. Schofield"
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
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Matthew R. Schofield"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1800,
          "endTime": 1950,
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
        "courseReferenceNumber": "34793",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 34793
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
          "building": "SERC",
          "room": "00359",
          "instructors": [
            "Eugene Kwatny"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 38749
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
          "building": "ANDRSN",
          "room": "00002",
          "instructors": [
            "Heather Levi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": True,
          "startTime": 1000,
          "endTime": 1050,
          "startDate": "08/24/2020",
          "monday": True
        }
      ],
      "isOpen": True,
      "attributes": {
        "description": "GenEd Race &amp; Diversity",
        "isZTCAttribute": False,
        "code": "GD",
        "class": "net.hedtech.banner.student.schedule.SectionDegreeProgramAttributeDecorator",
        "courseReferenceNumber": "30014",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Main",
      "crn": 30014
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
            "Aaron Jackson"
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
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Aaron Jackson"
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
        "courseReferenceNumber": "39178",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 39178
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
          "building": "SERC",
          "room": "00359",
          "instructors": [
            "Eugene Kwatny"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 38749
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "32525",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Center City",
      "crn": 32525
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
      "campusName": "Main",
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
          "building": "SERC",
          "room": "00359",
          "instructors": [
            "Eugene Kwatny"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 38749
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "32525",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Center City",
      "crn": 32525
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
          "building": "SERC",
          "room": "00359",
          "instructors": [
            "Eugene Kwatny"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 38749
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "32525",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Center City",
      "crn": 32525
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
          "building": "PEARMC",
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Nicholas S. Mirabito"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
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
          "building": "ANDRSN",
          "room": "00017",
          "instructors": [
            "Kyle Harris",
            "Nicholas S. Mirabito"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1400,
          "endTime": 1520,
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
        "courseReferenceNumber": "9079",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 9079
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
          "building": "SERC",
          "room": "00359",
          "instructors": [
            "Eugene Kwatny"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 38749
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "32525",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Center City",
      "crn": 32525
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
          "building": "PEARMC",
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Gabriel Castillo"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": False,
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
          "building": "ANDRSN",
          "room": "00017",
          "instructors": [
            "Kyle Harris",
            "Gabriel Castillo"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1400,
          "endTime": 1520,
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
        "courseReferenceNumber": "20967",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 20967
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
          "building": "SERC",
          "room": "00359",
          "instructors": [
            "Eugene Kwatny"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 38749
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "32525",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Center City",
      "crn": 32525
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
            "Matthew R. Schofield"
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
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Matthew R. Schofield"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1800,
          "endTime": 1950,
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
        "courseReferenceNumber": "34793",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 34793
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
          "building": "SERC",
          "room": "00359",
          "instructors": [
            "Eugene Kwatny"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 38749
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
          "building": None,
          "room": None,
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
        "courseReferenceNumber": "32525",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Center City",
      "crn": 32525
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
            "Aaron Jackson"
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
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Aaron Jackson"
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
        "courseReferenceNumber": "39178",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 39178
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
          "building": "SERC",
          "room": "00359",
          "instructors": [
            "Eugene Kwatny"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 38749
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
          "building": "ANDRSN",
          "room": "00002",
          "instructors": [
            "Heather Levi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": True,
          "startTime": 1100,
          "endTime": 1150,
          "startDate": "08/24/2020",
          "monday": True
        }
      ],
      "isOpen": True,
      "attributes": {
        "description": "GenEd Race &amp; Diversity",
        "isZTCAttribute": False,
        "code": "GD",
        "class": "net.hedtech.banner.student.schedule.SectionDegreeProgramAttributeDecorator",
        "courseReferenceNumber": "40171",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Main",
      "crn": 40171
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
      "campusName": "Main",
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
          "building": "SERC",
          "room": "00359",
          "instructors": [
            "Eugene Kwatny"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 38749
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
          "building": "ANDRSN",
          "room": "00002",
          "instructors": [
            "Heather Levi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": True,
          "startTime": 1100,
          "endTime": 1150,
          "startDate": "08/24/2020",
          "monday": True
        }
      ],
      "isOpen": True,
      "attributes": {
        "description": "GenEd Race &amp; Diversity",
        "isZTCAttribute": False,
        "code": "GD",
        "class": "net.hedtech.banner.student.schedule.SectionDegreeProgramAttributeDecorator",
        "courseReferenceNumber": "40171",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Main",
      "crn": 40171
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
          "building": "SERC",
          "room": "00359",
          "instructors": [
            "Eugene Kwatny"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 38749
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
          "building": "ANDRSN",
          "room": "00002",
          "instructors": [
            "Heather Levi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": True,
          "startTime": 1100,
          "endTime": 1150,
          "startDate": "08/24/2020",
          "monday": True
        }
      ],
      "isOpen": True,
      "attributes": {
        "description": "GenEd Race &amp; Diversity",
        "isZTCAttribute": False,
        "code": "GD",
        "class": "net.hedtech.banner.student.schedule.SectionDegreeProgramAttributeDecorator",
        "courseReferenceNumber": "40171",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Main",
      "crn": 40171
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
          "building": "PEARMC",
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Nicholas S. Mirabito"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
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
          "building": "ANDRSN",
          "room": "00017",
          "instructors": [
            "Kyle Harris",
            "Nicholas S. Mirabito"
          ],
          "sunday": False,
          "tuesday": True,
          "wednesday": False,
          "friday": False,
          "startTime": 1400,
          "endTime": 1520,
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
        "courseReferenceNumber": "9079",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 9079
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
          "building": "SERC",
          "room": "00359",
          "instructors": [
            "Eugene Kwatny"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 38749
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
          "building": "ANDRSN",
          "room": "00002",
          "instructors": [
            "Heather Levi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": True,
          "startTime": 1100,
          "endTime": 1150,
          "startDate": "08/24/2020",
          "monday": True
        }
      ],
      "isOpen": True,
      "attributes": {
        "description": "GenEd Race &amp; Diversity",
        "isZTCAttribute": False,
        "code": "GD",
        "class": "net.hedtech.banner.student.schedule.SectionDegreeProgramAttributeDecorator",
        "courseReferenceNumber": "40171",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Main",
      "crn": 40171
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
            "Matthew R. Schofield"
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
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Matthew R. Schofield"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1800,
          "endTime": 1950,
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
        "courseReferenceNumber": "34793",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 34793
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
          "building": "SERC",
          "room": "00359",
          "instructors": [
            "Eugene Kwatny"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": False,
          "startTime": 1300,
          "endTime": 1450,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "isOpen": True,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 38749
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
          "building": "ANDRSN",
          "room": "00002",
          "instructors": [
            "Heather Levi"
          ],
          "sunday": False,
          "tuesday": False,
          "wednesday": True,
          "friday": True,
          "startTime": 1100,
          "endTime": 1150,
          "startDate": "08/24/2020",
          "monday": True
        }
      ],
      "isOpen": True,
      "attributes": {
        "description": "GenEd Race &amp; Diversity",
        "isZTCAttribute": False,
        "code": "GD",
        "class": "net.hedtech.banner.student.schedule.SectionDegreeProgramAttributeDecorator",
        "courseReferenceNumber": "40171",
        "termCode": "202036"
      },
      "courseName": "ANTH-0831",
      "title": "Immigration and the American Dream",
      "campusName": "Main",
      "crn": 40171
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
            "Aaron Jackson"
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
          "room": "0P016",
          "instructors": [
            "Kyle Harris",
            "Aaron Jackson"
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
        "courseReferenceNumber": "39178",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 39178
    }
  ]
]
}

print(handler.lambda_handler(event, None))

