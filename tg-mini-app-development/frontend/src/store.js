// https://docs.telegram-mini-apps.com/platform/init-data
import { reactive, readonly } from 'vue'

const state = reactive({
	initDataRaw: '',
})

export default {
	state: readonly(state),
}