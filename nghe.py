def nghe ():
    import speech_recognition as sr
    import gtts
    from playsound import playsound
    toi = ""
    tai = sr.Recognizer()
    with sr.Microphone() as mic:
        print("xin moi ban noi")
        audio_text = tai.listen(mic)
        print("robot : --------------")
    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    try:
    # using google speech recognition
        toi = tai.recognize_google(audio_text, language = "vi-VI")#"Text:  "+tai.recognize_google(audio_text, language = "vi-VI")
    except:
        toi = ""#"Text:  " + ""
    return str(toi) ;
