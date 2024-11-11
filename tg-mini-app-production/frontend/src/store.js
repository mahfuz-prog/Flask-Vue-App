// https://docs.telegram-mini-apps.com/platform/init-data

import { reactive, readonly } from 'vue'
import { retrieveLaunchParams } from '@telegram-apps/sdk'

const { initDataRaw, initData } = retrieveLaunchParams()

const state = reactive({
	initData: initData,
	initDataRaw: initDataRaw,
})

export default {
	state: readonly(state),
}