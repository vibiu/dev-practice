#!/usr/bin/env bash

echo [INFO] Start redis server...
redis-server&

echo [INFO] Start celery...
celery -A cron.celery_task worker &

echo [INFO] Start gunicorn...
gunicorn -w 4 run:app