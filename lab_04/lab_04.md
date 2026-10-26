# Лабораторная работа №4. Основы работы с системой контроля версий Git и веб-сервисом GitHub

Министерство науки и высшего образования Российской Федерации  
Федеральное государственное автономное образовательное учреждение высшего образования «Омский государственный технический университет»  
Кафедра «Автоматизация и робототехника»

**Отчет по дисциплине:** «Программирование на языке Python»  
**Выполнил:** ст. гр. УТС-251т Курячий Андрей  
**Проверил:** доц., к.н. Ситников Д.В.  
**Город:** Омск, 2026

## 1. Цель работы
Изучить основы работы с распределенной системой контроля версий Git и веб-сервисом GitHub. Научиться инициализировать локальный репозиторий, создавать структуру проекта, фиксировать изменения с помощью коммитов и синхронизировать локальные файлы с удаленным репозиторием.

## 2. Краткие теоретические сведения
* **Git** — это распределенная система контроля версий, которая отслеживает изменения в файлах и позволяет откатываться к предыдущим состояниям кода.
* **GitHub** — облачная платформа для хостинга Git-репозиториев, обеспечивающая совместную работу и хранение резервных копий кода в сети.

**Основные этапы работы в Git:**
1. Изменение файлов в рабочей директории (*Working Directory*).
2. Индексация изменений — подготовка файлов к сохранению (*Staging Area*).
3. Фиксация изменений — запись снимка проекта в локальную историю (*Repository*).
4. Отправка изменений в облако — синхронизация с сервером (*Remote*).

## 3. Результаты выполнения работы
В ходе выполнения работы в командном окне были последовательно выполнены следующие команды для настройки структуры и отправки кода:

```console
C:\Users\admin\Python-Labs>git --version
git version 2.56.0.windows.3

C:\Users\admin>git config --global user.name "Курячий Андрей"

C:\Users\admin>git config --global user.email Kuryachiy07@mail.ru

C:\Users\admin>mkdir python-labs

C:\Users\admin>cd python-labs

C:\Users\admin\Python-Labs>git init

C:\Users\admin\Python-Labs>mkdir lab_01

C:\Users\admin\Python-Labs>git status
On branch main
Your branch is up to date with 'origin/main'.
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        "lab_01/ЛБ1 Курячий УТС-251т.md"
        "lab_02/ЛБ2 Курячий УТС-251т.markdown"
        "lab_03/ЛБ3 Курячий УТС-251т.markdown"
nothing added to commit but untracked files present (use "git add" to track)

C:\Users\admin\Python-Labs>git add .

C:\Users\admin\Python-Labs>git commit -m "Initial commit: create structure and lab_01"
[main 43a4ea9] Initial commit: create structure and lab_01
 3 files changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 "lab_01/ЛБ1 Курячий УТС-251т.md"
 create mode 100644 "lab_02/ЛБ2 Курячий УТС-251т.markdown"
 create mode 100644 "lab_03/ЛБ3 Курячий УТС-251т.markdown"

C:\Users\admin\Python-Labs>git remote add origin https://github.com/Attera0/Python-labs.git

C:\Users\admin\Python-Labs>git branch -M main

C:\Users\admin\Python-Labs>git push -u origin main
Enumerating objects: 12, done.
Counting objects: 100% (12/12), done.
Delta compression using up to 4 threads
Compressing objects: 100% (8/8), done.
Writing objects: 100% (8/8), 52.84 KiB | 13.21 MiB/s, done.
Total 8 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/Attera0/Python-Labs.git
   569ea89..43a4ea9  main -> main
branch 'main' set up to track 'origin/main'.
```

## Выводы по проделанной работе
В результате выполнения лабораторной работы были освоены практические навыки работы с консольными командами Git. Была успешно создана локальная структура проекта `Python-Labs` с подкаталогом `lab_01` и скриптом `main.py`. Настроен процесс индексации (`git add`) и фиксации изменений (`git commit`). Локальный репозиторий успешно связан с удаленным репозиторием на платформе GitHub, куда были отправлены все исходные файлы проекта (`git push`). Развернутая структура позволяет вести дальнейшую структурированную разработку последующих лабораторных работ.