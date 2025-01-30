#include <stdio.h>
#include <x86intrin.h>

#define ARRAY_LENGTH 10

int main() {
    int arr[ARRAY_LENGTH] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int result = 0;

    __m128i sum = _mm_setzero_si128();

    for (int i = 0; i < ARRAY_LENGTH / 4 * 4; i += 4) {
        __m128i a = _mm_loadu_si128((__m128i *) &arr[i]);
        sum = _mm_add_epi32(sum, a);
    }

    for (int i = ARRAY_LENGTH / 4 * 4; i < ARRAY_LENGTH; i++) {
        result += arr[i];
    }

    int temp[4];
    _mm_storeu_si128((__m128i *) temp, sum);
    result += temp[0] + temp[1] + temp[2] + temp[3];

    printf("Result: %d\n", result);

    return 0;
}