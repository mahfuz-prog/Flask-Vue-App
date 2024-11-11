### backend
- install & activate virtual environement
- install required packages from `requirements.txt`
- add environment variable according to `config.py`

### frontend
- install dependency
- add datastring in store.js `initDataRaw`

### validate datastring in js
`npm install crypto-js`
```sh
import CryptoJS from 'crypto-js'

export default function validate(dataString, TELEGRAM_BOT_TOKEN) {
    let initData = new URLSearchParams(dataString)
    let hash = initData.get("hash")
    let user = JSON.parse(initData.get("user"))
    let dataToCheck = []
    initData.sort()
    initData.forEach((val, key) => key !== "hash" && dataToCheck.push(`${key}=${val}`))

    let secret = CryptoJS.HmacSHA256(TELEGRAM_BOT_TOKEN, "WebAppData");
    let _hash = CryptoJS.HmacSHA256(dataToCheck.join("\n"), secret).toString(CryptoJS.enc.Hex)

    let status = hash === _hash
    return [status, user]
}