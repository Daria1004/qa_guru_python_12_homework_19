```
 Зарегистрировать аккаунт в https://browserstack.com

 Запустить автотест из занятия локально

 Разработать еще один автотест на открытие любой статьи
```

Для запуска разных окружениях, можно использовать команду:

Powershell:
```
$env:CONTEXT='bstack'; pytest
```

Bash:
```
CONTEXT='bstack' pytest
```

Доступные варианты окружения: `local_emulator`, `local_real`, `bstack`