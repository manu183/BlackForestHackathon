ASSI = True

import cv2
import json
import sys

from data.news import news_crawler
from data.calender import quickstart as calender
from data.mail import quickstart as mail
from data.weather import weather as weather_info
from face_recognition import face_recognizer as face_rec
from gui import gui

def detect_people():
	cam = cv2.VideoCapture(0)
	app = QApplication(sys.argv)
	gui = createGui()
	while ASSI:
		try:
			ret_val, img = cam.read()
			if not img is None:
				persons = face_rec.predict_labels(img)
				gui.updateLayout(persons)
				print(persons)
		except:
			continue
	sys.exit(app.exec_())

def main():
	print("Loading data...")
	news = []
	news.append(news_crawler.get_news('http://www.kit.edu/kit/pi_2017_142_autonomes-fahren-auf-dem-busbetriebshof.php'))
	news.append(news_crawler.get_news('https://www.eventrakete.de/offenburg/blackforest-hackathon/'))
	events = calender.get_events()
	emails = mail.get_mails()
	weather = weather_info.get_temperature()
	print("All data fetched")
	detect_people()

if __name__ == '__main__':
    main()