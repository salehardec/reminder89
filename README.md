Установка переменных окружения из файла .env
heroku config:set $(cat .env | sed '/^$/d; /#[[:print:]]\*$/d') -a reminder89
