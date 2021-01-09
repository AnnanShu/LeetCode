#include<stdio.h>
#include <sys/types.h>
#include <sys/wait.h>


int main() {
    for (int i = 0; i < 3; i++) {
        fork();
        printf("+");
        fflush(stdout);
    }
    wait(NULL);
    wait(NULL);
    wait(NULL);
    return 0;
}