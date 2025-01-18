#include <assert.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* readline();
char** split_string(char*);

// Complete the solve function below.
// Please store the size of the integer array to be returned in result_count pointer. For example,
// int a[3] = {1, 2, 3};
//
// *result_count = 3;
//
// return a;
//

int* solve(int a_count, int* a, int b_count, int* b, int* result_count) {
    *result_count = 2;
    int *cmp = malloc(2 * sizeof(int));
    *(cmp + 0) = 0;
    *(cmp + 1) = 0;
    for (int i = 0; i < a_count; i++) {
        if (*(a + i) > *(b + i)) {
            *(cmp + 0) += 1;
        } else if (*(b + i) > *(a + i)) {
            *(cmp + 1) += 1;
        }
    }
    return cmp;
}

int main(int argc, char *args){
    int a_count = 3, b_count = 3;
    int *a = malloc(3 * sizeof(int));
    *(a + 0) = 6;
    *(a + 1) = 7;
    *(a + 2) = 7;

    int *b = malloc(3 * sizeof(int));
    *(b + 0) = 6;
    *(b + 1) = 7;
    *(b + 2) = 7;

    for (int i = 0; i < a_count; i++) {
        printf("a[%d] = %d\n", i, *(a + i));
    }
    printf("---------------------\n");
    for (int i = 0; i < b_count; i++) {
        printf("b[%d] = %d\n", i, *(b + i));
    }
    printf("---------------------\n");

    int result_count;
    int *result = solve(a_count, a, b_count, b, &result_count);
    for (int i = 0; i < result_count; i++) {
        printf("%d", *(result + i));
        if (i != result_count - 1) {
            printf(" ");
        }
    }
    return 0;
}

/*

int main()
{
    FILE* fptr = fopen(getenv("OUTPUT_PATH"), "w");
    char** a_temp = split_string(readline());
    int* a = malloc(3 * sizeof(int));

    for (int i = 0; i < 3; i++) {
        char* a_item_endptr;
        char* a_item_str = *(a_temp + i);
        int a_item = strtol(a_item_str, &a_item_endptr, 10);
        if (a_item_endptr == a_item_str || *a_item_endptr != '\0') { exit(EXIT_FAILURE); }
        *(a + i) = a_item;
    }

    int a_count = 3;
    char** b_temp = split_string(readline());
    int* b = malloc(3 * sizeof(int));
    for (int i = 0; i < 3; i++) {
        char* b_item_endptr;
        char* b_item_str = *(b_temp + i);
        int b_item = strtol(b_item_str, &b_item_endptr, 10);
        if (b_item_endptr == b_item_str || *b_item_endptr != '\0') { exit(EXIT_FAILURE); }
        *(b + i) = b_item;
    }

    int b_count = 3;
    int result_count;
    int* result = solve(a_count, a, b_count, b, &result_count);

    for (int i = 0; i < result_count; i++) {
        fprintf(fptr, "%d", *(result + i));
        if (i != result_count - 1) {
            fprintf(fptr, " ");
        }
    }

    fprintf(fptr, "\n");
    fclose(fptr);
    return 0;
}

char* readline() {
    size_t alloc_length = 1024;
    size_t data_length = 0;
    char* data = malloc(alloc_length);

    while (true) {
        char* cursor = data + data_length;
        char* line = fgets(cursor, alloc_length - data_length, stdin);

        if (!line) { break; }
        data_length += strlen(cursor);

        if (data_length < alloc_length - 1 || data[data_length - 1] == '\n') { break; }
        size_t new_length = alloc_length << 1;
        data = realloc(data, new_length);

        if (!data) { break; }
        alloc_length = new_length;
    }

    if (data[data_length - 1] == '\n') {
        data[data_length - 1] = '\0';
    }

    data = realloc(data, data_length);
    return data;
}

char** split_string(char* str) {
    char** splits = NULL;
    char* token = strtok(str, " ");

    int spaces = 0;
    while (token) {
        splits = realloc(splits, sizeof(char*) * ++spaces);
        if (!splits) {
            return splits;
        }
        splits[spaces - 1] = token;
        token = strtok(NULL, " ");
    }
    return splits;
}

*/


