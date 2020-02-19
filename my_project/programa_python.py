#!/usr/bin/env python3

import sys

print('Ola. Programa python com parametros:')
#comentario
#sys.argv contem uma lista de parametros

if len(sys.argv) < 3:
   print('>>>>> ERROR: Defina os parametros para calculo: [A] e [B]')
else:
   a = int(sys.argv[1])
   b = int(sys.argv[2])
   c = a+b

   print(f"A soma de {a} com {b} -> {c}")

