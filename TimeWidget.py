from tkinter import *
from tkinter.font import Font
import datetime
from hijri_converter import Hijri, Gregorian
import webbrowser as web
import pyautogui
from time import sleep
from pyIslam.praytimes import (PrayerConf, Prayer)


def quitWin(event):
    root.destroy()
    quit()


def timeFormat():
    currentTime = datetime.datetime.now()
    hour = currentTime.strftime('%I')
    minute = currentTime.minute
    second = currentTime.second
    period = currentTime.strftime('%p')

    if minute < 10:
        minute = '0' + str(minute)
    if second < 10:
        second = '0' + str(second)

    return str(hour) + ":" + str(minute) + ":" + str(second) + " " + str(period)


def dateFormat():
    currentTime = datetime.datetime.now()
    year = currentTime.year
    month = currentTime.month
    day = currentTime.day
    weekday = currentTime.weekday()

    hijri = Gregorian(year, month, day).to_hijri()

    weekdayList = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    monthList = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    monthHijriList = ['محرم', 'صفر', 'الأول ربيع', 'الثاني ربيع', 'الأول جمادي', 'الثاني جمادي', 'رجب', 'شعبان',
                      'رمضان', 'شوال', 'القعدة ذو', 'الحجة ذو']

    return "--- " + str(weekdayList[weekday]) + " " + str(day) + " " + str(monthList[month - 1]) + " " + str(
        year) + " ---\n--- " + str(hijri.year) + " " + str(monthHijriList[hijri.month - 1]) + " " + str(
        hijri.day) + " ---"


def courseFormat():
    global startCourse
    currentTime = datetime.datetime.now()
    courses = [
        {
            "courseName": "CPIT-370",
            "days": [6],
            "startTime": "11:00",
            "endTime": "12:40",
            "nextCourse": "CPIT-210"
        },
        {
            "courseName": "CPIT-210",
            "days": [6],
            "startTime": "17:00",
            "endTime": "18:40",
            "nextCourse": "OFF"
        },
        {
            "courseName": "CPIT-210",
            "days": [0, 2],
            "startTime": "09:00",
            "endTime": "10:40",
            "nextCourse": "CPIT-251"
        },
        {
            "courseName": "CPIT-251",
            "days": [0],
            "startTime": "13:00",
            "endTime": "14:40",
            "nextCourse": "OFF"
        },
        {
            "courseName": "CPIT-370",
            "days": [1, 3],
            "startTime": "11:00",
            "endTime": "12:40",
            "nextCourse": "OFF"
        },
        {
            "courseName": "CPIT-251",
            "days": [2],
            "startTime": "13:00",
            "endTime": "14:40",
            "nextCourse": "CPIT-251"
        },
        {
            "courseName": "CPIT-251",
            "days": [2],
            "startTime": "17:00",
            "endTime": "18:40",
            "nextCourse": "OFF"
        }
    ]
    # currentTime.weekday()
    # currentTime.strftime('%H:%M')
    if currentTime.weekday() in [4, 5]:
        return "=== WeekEnd ==="
    for course in courses:
        if currentTime.weekday() in course["days"]:
            if course["startTime"] <= currentTime.strftime('%H:%M') < course["endTime"]:
                # if course["courseName"] == "ISLS-401" and startCourse:
                #     try:
                #         web.open("https://lms.kau.edu.sa/")  # BlackBoard
                #         sleep(5)
                #         pyautogui.click(x=1234, y=736)  # Sign in
                #         sleep(5)
                #         pyautogui.click(x=811, y=220)  # Courses
                #         sleep(3)
                #         x, y = pyautogui.locateCenterOnScreen("course_name.png", confidence=0.9)  # Course name
                #         pyautogui.click(x, y)
                #         sleep(3)
                #         x, y = pyautogui.locateCenterOnScreen("vcu.png", confidence=0.9)  # VCU
                #         pyautogui.click(x, y)
                #         sleep(5)
                #         x, y = pyautogui.locateCenterOnScreen("main_session.png", confidence=0.9)  # Main session
                #         pyautogui.click(x, y)
                #         sleep(1)
                #         pyautogui.click(x, (y + 70))  # Current session
                #         sleep(1)
                #         x, y = pyautogui.locateCenterOnScreen("Join_session.png", confidence=0.9)  # Join session
                #         pyautogui.click(x, y)
                #         sleep(10)
                #         x, y = pyautogui.locateCenterOnScreen("Skip_audio.png", confidence=0.9)  # Skip audio test
                #         pyautogui.click(x, y)
                #         sleep(6)
                #         pyautogui.click(x=1882, y=985)  # Open menu
                #         sleep(1)
                #         pyautogui.click(x=1595, y=998)  # Show students
                #
                #     except:
                #         pass
                #     finally:
                #         startCourse = False

                # if course["courseName"] == "ISLS-301" and startCourse:
                #     web.open("https://lms.kau.edu.sa/")  # BlackBoard
                #     sleep(3)
                #     pyautogui.click(x=1234, y=736)  # Sign in
                #     sleep(5)
                #     pyautogui.click(x=811, y=220)  # Courses
                #     sleep(3)
                #     pyautogui.click(x=385, y=479)  # Course name
                #     sleep(3)
                #     pyautogui.click(x=1786, y=779)  # VCU
                #     sleep(5)
                #     pyautogui.click(x=1293, y=631)  # Main session
                #     sleep(1)
                #     pyautogui.click(x=1283, y=714)  # Current session
                #     sleep(1)
                #     pyautogui.click(x=333, y=560)  # Join session
                #     sleep(10)
                #     pyautogui.click(x=1883, y=170)  # Skip audio test
                #
                #     startCourse = False

                return "Now: " + course["courseName"] + " || Next: " + course["nextCourse"]
            elif course["startTime"] > currentTime.strftime('%H:%M'):
                startCourse = True
                return "Break"
            elif course["nextCourse"] == "OFF":
                startCourse = True
                return "End of the Lectures"
    return "Today is OFF"

def prayerTimes():
    currentTime = datetime.datetime.now()
    longitude = 39.249099
    latitude = 21.505190
    timezone = 3
    fajr_isha_method = 4
    asr_fiqh = 1

    pconf = PrayerConf(longitude, latitude, timezone, fajr_isha_method, asr_fiqh)
    pt = Prayer(pconf, datetime.date.today())

    prayersTime = [pt.last_third_of_night(), pt.fajr_time(), pt.sherook_time(), pt.dohr_time(), pt.asr_time(),
               pt.maghreb_time(), pt.ishaa_time(), pt.second_third_of_night(),
               pt.midnight()]

    prayerName = ["Qiyam", "Fajr", "Sherook", "Jumuah" if currentTime.weekday() == 4 else "Dohr", "Asr", "Maghreb", "Ishaa", "1st Third", "Midnight"]

    for currentPray in range(len(prayersTime)):
        if currentTime.strftime('%H:%M:%S') <= prayersTime[currentPray].strftime('%H:%M:%S'):
            hour = currentTime.hour
            minute = currentTime.minute
            second = currentTime.second

            remainingHours = (prayersTime[currentPray].hour - hour) - 1
            remainingMinutes = 59 + (prayersTime[currentPray].minute - minute)
            remainingSeconds = 60 + (prayersTime[currentPray].second - second)
            # print(remainingHours, remainingMinutes, remainingSeconds)

            if remainingSeconds >= 60:
                remainingMinutes += 1
                remainingSeconds -= 60
            if remainingMinutes >= 60:
                remainingHours += 1
                remainingMinutes -= 60

            remainingTime = ("0" if len(str(remainingHours)) == 1 else "") \
                            + str(remainingHours) \
                            + ":" + ("0" if len(str(remainingMinutes)) == 1 else "") \
                            + str(remainingMinutes) \
                            + ":" + ("0" if len(str(remainingSeconds)) == 1 else "") \
                            + str(remainingSeconds)

            return prayerName[currentPray] + ": " + str(prayersTime[currentPray].strftime('%I:%M %p')) \
                   + " || " + remainingTime + " ||"

    # print("Fajr      : " + str(pt.fajr_time()))
    # print("Sherook   : " + str(pt.sherook_time()))
    # print("Dohr      : " + str(pt.dohr_time()))
    # print("Asr       : " + str(pt.asr_time()))
    # print("Maghreb   : " + str(pt.maghreb_time()))
    # print("Ishaa     : " + str(pt.ishaa_time()))
    # print("1st third : " + str(pt.second_third_of_night()))
    # print("Midnight  : " + str(pt.midnight()))
    # print("Qiyam     : " + str(pt.last_third_of_night()))


startCourse = True
root = Tk()
root.wm_attributes('-transparentcolor', '#FFFFFF')

ws = root.winfo_screenwidth()
x = (ws / 2) - (500 / 2)

root.geometry('%dx%d+%d+%d' % (500, 400, x, 0))
root.config(bg='white')
root.overrideredirect(True)

timeFont = Font(size=35, family="Bahnschrift SemiBold")
dateFont = Font(size=17, family="Bahnschrift SemiBold")
prayerFont = Font(size=15, family="Bahnschrift SemiBold")
courseFont = Font(size=12, family="Bahnschrift SemiBold")

# Red: #E50914, Gold: #D5B038, Blue: #19E2EA, White: #F7FFFE, Light Blue: #B6D4CC
frontground = "#B6D4CC"
background = "#B6D4CF" # 000001

timeShow = Label(root, text=timeFormat(), bg=background, fg=frontground,
                 font=('ds-digital', 40, 'bold'))  # ('ds-digital', 40, 'bold')
dateShow = Label(root, text=dateFormat(), bg=background, fg=frontground, font=dateFont)
prayerShow = Label(root, text=prayerTimes(), bg=background, fg=frontground, font=prayerFont)
# courseShow = Label(root, text=courseFormat(), bg=background, fg=frontground, font=courseFont)
courseShow = Label(root, text="End of Semester", bg=background, fg=frontground, font=courseFont)

root.wm_attributes('-transparentcolor', background)
root.config(bg=background)
root.update()

timeShow.pack()
dateShow.pack()
prayerShow.pack()
courseShow.pack()

root.bind('<F12>', quitWin)


def update_labels():
    timeShow.config(text=timeFormat())
    dateShow.config(text=dateFormat())
    prayerShow.config(text=prayerTimes())
    # courseShow.config(text=courseFormat())
    root.after(1000, update_labels)


root.after(1000, update_labels)  # schedule the first update
root.mainloop()

# while True:
#     try:
#         timeShow.config(text=timeFormat())
#         timeShow.update()
#
#         dateShow.config(text=dateFormat())
#         dateShow.update()
#
#         prayerShow.config(text=prayerTimes())
#         prayerShow.update()
#
#         # courseShow.config(text=courseFormat())
#         # courseShow.update()
#     except:
#         quit()
