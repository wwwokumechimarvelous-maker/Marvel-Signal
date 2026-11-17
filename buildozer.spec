[app]
title = Marvel AI Signal
package.name = marvelaisignal
package.domain = com.marvel.aisignal
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
icon.filename = %(source.dir)s/icon.png

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreement = True
