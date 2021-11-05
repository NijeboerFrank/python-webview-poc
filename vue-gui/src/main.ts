import { createApp } from "vue";
import App from "./App.vue";

import router from "./router";
import store from "./store";

// Declare stuff for pywebview to work
// Always update this class with the code that's
// available in Python to use new functions
declare global {
  interface PywebviewAPI {
    do_something: () => Promise<string>;
  }
  interface Pywebview {
    api: PywebviewAPI;
  }
  interface Window {
    pywebview: Pywebview;
  }
}

const app = createApp(App)

app.use(store)
app.use(router)

app.mount('#app')
