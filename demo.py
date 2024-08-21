import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Listening...")
    audio = recognizer.listen(source)
    try:
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
driver = webdriver.Chrome()  # Replace with your preferred browser
driver.get("https://www.youtube.com")
search_box = driver.find_element(By.NAME, "search_query")  # Replace with the correct locator
search_box.send_keys(Keys.RETURN)

# Assuming the first video is the desired one
first_video = driver.find_element(By.ID, "video-title")  # Use By.ID for element with id "video-title"
first_video.click()