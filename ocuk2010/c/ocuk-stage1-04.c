// Steve Phillips
// 2010.12.13
// OCUK Stage 1

#include <stdio.h>

int main() {

    //int MAX_NUM = 100;
    int MAX_NUM = 1500000;

    unsigned int chain_length, num, number;
    unsigned int longest_chain = 0;
    unsigned int longest_n = 0;

    for (num = 2; num < MAX_NUM; num++) {
	number = num;
	chain_length = 0;

	while (number != 1) {
  	    if (!(number & 1)) { // Even
		number >>= 1;
	    } else if (number & 1) { // Odd
		number += (number << 1) + 1;
	    }
	    chain_length += 1;

	    if (chain_length > longest_chain) {
		longest_chain = chain_length;
		longest_n = num;
	    }
	}
    }

    printf("n = %d generates chain length %d", longest_n, longest_chain);
    return 0;
}
