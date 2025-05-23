#!/bin/bash

# Настройки логирования
LOG_LEVEL="INFO"  # DEBUG, INFO, WARNING, ERROR
LOG_FILE=".github/logs/action.log"
LOG_FORMAT="%Y-%m-%d %H:%M:%S"
LOG_MAX_SIZE=10485760  # 10MB
LOG_MAX_FILES=5
LOG_COLORS=true

# Цвета для логирования
LOG_COLOR_DEBUG="\033[0;36m"  # Cyan
LOG_COLOR_INFO="\033[0;32m"   # Green
LOG_COLOR_WARN="\033[0;33m"   # Yellow
LOG_COLOR_ERROR="\033[0;31m"  # Red
LOG_COLOR_RESET="\033[0m"     # Reset

# Настройки презентаций
PRESENTATION_TYPES=(
    "lecture:📚:Лекция"
    "practice:💻:Практика"
    "additional:📌:Дополнительно"
)

# Настройки модулей
MODULE_PATTERNS=(
    "^[0-9]+-.*$"
    "^Модуль\ [0-9]+.*$"
)

# Настройки вывода
OUTPUT_HEADER="# Презентации курса

## О курсе
Этот репозиторий содержит презентации и материалы курса. Здесь вы найдете все необходимые материалы для изучения предмета, включая лекции, практические задания и дополнительные материалы.

## Структура курса
Курс разделен на модули, каждый из которых содержит несколько уроков. В каждом уроке вы найдете:
- 📚 Лекционные материалы
- 💻 Практические задания
- 📌 Дополнительные материалы (если есть)

## Как пользоваться
1. Выберите нужный модуль из списка ниже
2. Откройте интересующий вас урок
3. Скачайте необходимые материалы

## Обновления
Материалы регулярно обновляются. Дата последнего обновления указана рядом с каждым файлом.

## Содержание курса"
OUTPUT_SEPARATOR="---"

# Настройки Git
GIT_USER_NAME="GitHub Action"
GIT_USER_EMAIL="action@github.com"
GIT_COMMIT_MESSAGE="Update README.md"

# Настройки уведомлений
NOTIFY_ON_ERROR=true
NOTIFY_EMAIL="your-email@example.com"
NOTIFY_SLACK_WEBHOOK=""
NOTIFY_TELEGRAM_BOT_TOKEN=""
NOTIFY_TELEGRAM_CHAT_ID=""

# Настройки резервного копирования
BACKUP_ENABLED=true
BACKUP_DIR=".github/backups"
BACKUP_MAX_FILES=5
BACKUP_PREFIX="backup_"
BACKUP_SUFFIX=".tar.gz"

# Настройки метрик
METRICS_ENABLED=true
METRICS_FILE=".github/metrics/performance.json"
METRICS_RETENTION_DAYS=30 