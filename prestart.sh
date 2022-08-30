#! /usr/bin/env bash

echo 'Waiting for the database to start...'
sleep 5;

echo 'Run migrations...'
alembic upgrade head
