carpBackend=backend/.env
KEY=$(chars='abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'; python -c "import secrets; print(''.join(secrets.choice('${chars}') for i in range(50)))")

echo $"SECRET_KEY=${KEY}" > $carpBackend
echo "CORS_ALLOWED_URL=localhost" >> $carpBackend
echo "IS_LOCAL_Q=local" >> $carpBackend
echo "ENGINE_DB=mysql" >> $carpBackend
echo "DB_NAME=regularizacion" >> $carpBackend
echo "DB_USER=root" >> $carpBackend
echo "DB_PASSWORD=jioska" >> $carpBackend
echo "DB_HOST=localhost" >> $carpBackend
echo "DB_PORT=3306" >> $carpBackend
