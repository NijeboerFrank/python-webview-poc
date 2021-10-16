import webview

class Api:

    def do_something(self):
        print("Wow click from javascript")
        return "Hello from python"

api = Api()
webview.create_window("Gekke App", "http://localhost:8080", js_api=api)
webview.start(debug=True)