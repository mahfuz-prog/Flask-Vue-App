import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from "./store"
import theme from "./theme"
import axios from 'axios'

axios.defaults.baseURL = 'http://localhost:5000/api/'
axios.defaults.headers.common['Authorization'] = `tma ${store.state.initDataRaw}`

const app = createApp(App)

app.provide("store", store)
app.provide("theme", theme)

app.use(router)
app.mount('#app')