import axios from 'axios'
import { inject } from 'vue'
import { useRouter } from 'vue-router'
import { useNotification } from '@kyvg/vue3-notification'


// redirect and notify
export class redirectNotify {
  constructor() {
    this.router = useRouter()
    this.notification = useNotification()
    this.path = '/'
    this.title = 'Sign Up Not Allowed'
    this.text = 'You already logged in!'
  }

  update(path, msg) {
    if (path) {
      this.path = path
    }

    if (msg) {
      this.title = msg.title
      this.text = msg.text
    } 
  }

  use() {
    this.router.push(this.path)
    this.notification.notify({ title: this.title, text: this.text, })
  }
}


// only logged in user content
export class loginRequired {
  constructor(path) {
    this.data = null
    this.path = path
    this.router = useRouter()
    this.notification = useNotification()
    // reactive store object
    this.store = inject("store")
  }

  async check() {
    try {
      this.data = await (await axios.get(this.path)).data
    } catch (err) {
      if (err.status === 401 || err.status === 403) {
        // reset reactive state
        this.store.resetState()
        this.data = null
      }
    }

    if (!this.data) {
      // redirect user to login view
      this.router.push('/log-in')
      this.notification.notify({ title: 'Log In Required', text: 'Login to access this page.' })
    } else {
      return this.data
    }
  }
}