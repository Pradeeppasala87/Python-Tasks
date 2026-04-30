class WiFiDevice:
    def wifi(self):
        print("WiFi Connected")

class VoiceAssistant:
    def voice(self):
        print("Voice Control Enabled")

class SmartSpeaker(WiFiDevice, VoiceAssistant):
    def show(self):
        print("Smart Speaker Ready")

s = SmartSpeaker()
s.wifi()
s.voice()
s.show()
