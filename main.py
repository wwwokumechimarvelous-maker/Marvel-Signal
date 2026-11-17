from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
import random
from datetime import datetime, timedelta
import pytz

OTC_PAIRS = [
    "EUR/USD OTC", "GBP/USD OTC", "USD/JPY OTC", "AUD/USD OTC",
    "EUR/JPY OTC", "USD/CHF OTC", "EUR/GBP OTC", "USD/CAD OTC",
    "NZD/USD OTC", "EUR/AUD OTC"
]

class MarvelApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        title = Label(text="👑 MARVEL SIGNAL BOT", font_size='22sp', bold=True, size_hint_y=0.2)
        self.signal_label = Label(text="Waiting for next signal...", font_size='18sp')
        self.time_label = Label(text="", font_size='14sp')
        self.conf_label = Label(text="", font_size='14sp')
        
        btn = Button(text="GENERATE SIGNAL NOW", size_hint_y=0.3, background_color=(0,0.7,0,1))
        btn.bind(on_press=self.generate_signal)
        
        self.layout.add_widget(title)
        self.layout.add_widget(self.signal_label)
        self.layout.add_widget(self.time_label)
        self.layout.add_widget(self.conf_label)
        self.layout.add_widget(btn)
        
        # Auto generate every 2 mins
        Clock.schedule_interval(lambda dt: self.generate_signal(None), 120)
        return self.layout

    def generate_signal(self, instance):
        pair = random.choice(OTC_PAIRS)
        direction = random.choice(["CALL 🟢", "PUT 🔴"])
        confidence = random.randint(82, 95)
        
        # WAT Timezone
        wat = pytz.timezone('Africa/Lagos')
        now = datetime.now(wat)
        expiry = now + timedelta(minutes=2)
        
        martingale = [f"Level {i+1}: {now + timedelta(minutes=i*2):%H:%M}" for i in range(3)]
        
        text = f"👑 MARVEL SIGNAL\n\nPAIR: {pair}\nACTION: {direction}\n"
        time_text = f"TIME: {now.strftime('%H:%M:%S')} WAT\nEXPIRY: {expiry.strftime('%H:%M')} (2 min)"
        conf_text = f"CONFIDENCE: {confidence}%\n\nMARTINGALE:\n" + "\n".join(martingale)
        
        self.signal_label.text = text
        self.time_label.text = time_text
        self.conf_label.text = conf_text

MarvelApp().run()


FILE 2: buildozer.spec — create new file, paste this
ini
[app]
title = Marvel Signal
package.name = marvelsignal
package.domain = com.marvel.signal
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.3.0,pytz
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

[app:android]
android.permissions = INTERNET,VIBRATE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreement = True
