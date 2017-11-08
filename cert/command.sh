#!/bin/bash

certDir=/var/www/app/cert

# Check folder cert if not existing
if [ ! -f "$certDir/ssl.key" ]; then
    mkdir -p $certDir
    openssl genrsa 2048 > "$certDir/ssl.key"
    openssl req -new -x509 -nodes -days 365 -subj "/C=JP/ST=Hanoi/L=Hanoi City/O=CuiBap/OU=Divison/CN=CodeForFood" -key "$certDir/ssl.key" -out "$certDir/ssl.crt"
    chmod 700 "$certDir/ssl.key"
    chmod 700 "$certDir/ssl.crt"
fi
