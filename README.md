Тестовое задание: в аттаче (https://github.com/thakryptex/backend_test/blob/master/Backend_Test.pdf)

# Запуск кода на локальной машине #
---
1) Развернуть виртуальное окружение  
> virtualenv -p python3 env  
2) Активировать виртуальное окружение  
> source env/bin/activate  
3) Установить библиотеки  
> pip install -r requirements.txt  
4) Создать суперпользователя  
> ./manage.py createsuperuser  
5) Настроить crontab  
> crontab -e  
*/5 * * * * source /home/ubuntu/.bashrc && source /home/ubuntu/work/your-project/bin/activate && python /home/ubuntu/work/your-project/src/manage.py runcrons > /home/ubuntu/cronjob.log  
6) Запустить проект  
> ./manage.py runserver  
  
## Использование вебсокетов ##
Вебсокеты лучше всего использовать непосредственно внутри nginx. Можно использовать модуль push stream для nginx. Он позволит легко устанавливать различные ограничения на передаваемую информацию через вебсокет.  
  
Также можно использовать библиотеку django-websocket-redis. Данная библиотека работает с обязательным подключением к redis. Если проект планируется высоконагруженым, то желательно хранить сессии в нереляционном хранилище. 
django-websocket-redis позволяет работать достаточно стабильно с вебсокетами через uwsgi.  
