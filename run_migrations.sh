#!/bin/bash

if [ ! -z "$MIGRATION_UP" ]; then
    alembic upgrade $MIGRATION_UP
elif [ ! -z "$MIGRATION_DOWN" ]; then
    alembic downgrade $MIGRATION_DOWN
fi
