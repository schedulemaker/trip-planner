import handler
import os
os.environ['university'] = 'temple university'

event = {'schedule': [
  [
    {
      "meetingTimes": [
        {
          "saturday": True,
          "thursday": False,
          "sunday": False,
          "tuesday": False,
          "wednesday": False,
          "friday": False,
          "startTime": 1000,
          "endTime": 1150,
          "startDate": "08/24/2020",
          "monday": False
        },
        {
          "saturday": False,
          "thursday": False,
          "sunday": False,
          "tuesday": False,
          "wednesday": False,
          "friday": True,
          "startTime": 1230,
          "endTime": 1350,
          "startDate": "08/24/2020",
          "monday": False
        }
      ],
      "campusName": "Main",
      "crn": 4308
    },

    {
      "meetingTimes": [
        {
          "saturday": True,
          "thursday": False,
          "sunday": False,
          "tuesday": False,
          "wednesday": False,
          "friday": False,
          "startTime": 1200,
          "endTime": 1520,
          "monday": False
        },
        {
          "saturday": False,
          "thursday": False,
          "sunday": False,
          "tuesday": False,
          "wednesday": False,
          "friday": False,
          "startTime": 1400,
          "endTime": 1550,
          "monday": False
        }
      ],

      "campusName": "Ambler",
      "crn": 2184
    },    {
      "meetingTimes": [
        {
          "saturday": True,
          "thursday": False,
          "sunday": False,
          "tuesday": False,
          "wednesday": False,
          "friday": False,
          "startTime": 0,
          "endTime": 0,
          "monday": False
        }
      ],
      "campusName": "Main",
      "crn": 25550
    }
  ]]}

print(handler.lambda_handler(event, None))

