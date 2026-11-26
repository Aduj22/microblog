#!/bin/sh

. .venv/bin/activate
while true; do
    if flask db upgrade; then
        break
    fi

    echo "Database is not ready. Retrying in 5 seconds..."
    sleep 5
done
exec gunicorn -b :5000 --access-logfile - --error-logfile - microblog:app