#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int x;
    int y;
} Point;

int main() {
    Point *p = (Point *) malloc(sizeof(Point));
    if (p == NULL) {
        printf("You da fail!\n");
        return 1;
    }
    p->x = 10;
    p->y = 20;
    printf("Point coordinates: (%d, %d)\n", p->x, p->y);
    free(p);

    return 0;
}