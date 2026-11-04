#include <stdio.h>
#include <orbis/libkernel.h>

int main(void)
{
    setvbuf(stdout, NULL, _IONBF, 0);
    printf("\nRIDA MUSIC - PS4 HOMEBREW\n");
    printf("-------------------------\n");
    printf("Native PS4 bootstrap loaded.\n");
    printf("Graphical player and streaming engine are the next milestone.\n");

    for (;;) {
        sceKernelUsleep(1000000);
    }
    return 0;
}
