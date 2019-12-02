cython -3 -w . main.py --embed
gcc -Os -I /usr/include/python3.6 -o Trpg-Linux main.c -lpython3.6 -lpthread -lm -lutil -ldl