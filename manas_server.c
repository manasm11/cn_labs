#include <unistd.h>
#include <stdio.h>
#include <sys/socket.h>

int main(int argc, char **argv) {
    int server_fd = socket(AF_INET, SOCK_STREAM, 0);
    printf(server_fd);
}