import { reactive, readonly } from 'vue'
import { useRouter } from 'vue-router'

const style = reactive({
	app: window.Telegram.WebApp
})

const apply = () => {
	const telegram = window.Telegram.WebApp
	const router = useRouter()

	// show only the back button except home route
	if (router.currentRoute.value.path === '/') {
		telegram.BackButton.hide()
	} else {
		telegram.BackButton.show()
	}

	// all styling
	style.app.headerColor = '#0CBBC5'
}

export default {
	style: readonly(style),
	apply : apply
}