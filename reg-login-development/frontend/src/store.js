// reactive object for state managemnet
// store and retrieve jwt token from localStorage
import axios from 'axios' 
import { reactive, readonly } from 'vue'

const state = reactive({
	token: localStorage.getItem('token')
})

const updateState = (token) => {
	state.token = token
	localStorage.setItem('token', token)
	axios.defaults.headers.common['x-access-token'] = token
}

const resetState = () => {
	state.token = null
	axios.defaults.headers.common['x-access-token'] = null
	localStorage.removeItem('token')
}

export default {
	state: readonly(state),
	resetState,
	updateState
}