# R4C
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![openpyxl](https://img.shields.io/badge/-openpyxl-464646?style=flat-square&logo=openpyxl)](https://openpyxl.readthedocs.io/en/stable/)
Проект по учету произведенных роботов,а также выполняет некие операции связанные с этим процессом.
## Использование
Склонируйте репозиторий  
Создайте виртуальное окружение 
```
python -m venv venv
```
Активируйте виртуальное окружение
* Если у вас Linux/MacOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установите зависимости 
```
pip install -r requirements.txt
```
Запустите проект
```
py main.py
```

Данная программа имеет Endpoints:
```
POST .../api/create_robot/
{
    "model":"r2",
    "version":"x1",
    "created":"2022-12-31 23:59:59"
}
```
```
GET .../api/excel_report/
```
```
GET .../api/buy_robot/
{
    "customer":"email@em.em",
    "robot_serial":"r1x11"
}
```

## Над проектом работали
- [Дмитрий Луконин](https://wa.me/79153612056)