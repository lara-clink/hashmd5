#!/bin/bash

salt="$y$j9T$5LImmws2fco9AeRmLSB2j0$"
senha="123admin"

hash=$(openssl passwd -crypt -salt "$salt" "$senha")

echo "Hash: $hash"
