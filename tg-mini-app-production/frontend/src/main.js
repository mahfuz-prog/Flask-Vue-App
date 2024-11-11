import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from "./store"
import axios from 'axios'
import theme from "./theme"
import conf from '/etc/config.json'

axios.defaults.baseURL = 'https://webwaymark.com/api/'
axios.defaults.headers.common['Authorization'] = `${conf.AUTHORIZATION_PREFIX} ${store.state.initDataRaw}`

const app = createApp(App)

app.provide("store", store)
app.provide("theme", theme)

app.use(router)
app.mount('#app')