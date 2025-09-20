#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n) {
    int answer = 1;
    int slice = 6;
    
    while((slice*answer)%n != 0){
        answer += 1;
    }
    
    return answer;
}