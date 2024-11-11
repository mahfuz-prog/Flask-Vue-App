### server
- create `config.json` file on the server. dir `/etc/config.json`
- put key value pair according to `config.py`
```sh
{
    "SECRET_KEY":"",
    "SQLALCHEMY_DATABASE_URI":"sqlite:///project.db",
    "BOT_TOKEN":"",
    "AUTHORIZATION_PREFIX":"",
}
```

### backend
- install & activate virtual environement
- install required packages from `requirements.txt`
```sh
pip install gunicorn
```

### frontend
- install dependency
- update `axios.defaults.baseURL` according to domain in `main.js`
```sh
npm i
npm run build
```

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
```