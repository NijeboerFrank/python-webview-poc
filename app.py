import time
import threading

import webview


class Api:
    def do_something(self):
        print("Wow click from javascript")

        print("Testing")

        return "Hello from python"

    def hallo(self):
        """Do some printing of lines and return a string"""
        print("Testing")
        return "Another hello function from Python"


def show_alert(window):
    time.sleep(5)
    window.evaluate_js("alert('hoi')")


api = Api()
window = webview.create_window("Gekke App", "vue-gui/dist/index.html", js_api=api)
t = threading.Thread(target=show_alert, args=[window])
t.start()

webview.start()


print("Done")
