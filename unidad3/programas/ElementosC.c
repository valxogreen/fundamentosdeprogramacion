#include <stdio.h>

struct Alumno {
    char nombre[30];
    float promedio;
    void (*saludar)(struct Alumno *);
};
    void saludar(struct Alumno *a) {
        printf("hola, soy %s\n", a->nombre);
    }

int main() {
    struct Alumno a1 = {"Juan", 8.5, saludar};
    struct Alumno a2 = {"Maria", 9.0, saludar};
    a1.saludar(&a1);
    a2.saludar(&a2);
    return 0;
}
