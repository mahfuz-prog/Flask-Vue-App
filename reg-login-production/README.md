### google cloud
- 

### server
- create `config.json` file on the server. dir `/etc/config.json`
- put key value pair according to `config.py`
```sh
{
    "SECRET_KEY":"",
    "SQLALCHEMY_DATABASE_URI":"sqlite:///project.db",
    "MAIL_USERNAME":"email",
    "MAIL_PASSWORD":"app password"
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
- update `axios.defaults.baseURL` to your domain from `main.js`
```sh
npm i
npm run build
```