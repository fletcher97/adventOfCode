#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int min(int x, int y){
	return x < y ? x : y;
}

int getPaperAmount(int x, int y, int z){
	int ret = x * y * z;
	x <<= 1;
	y <<= 1;
	z <<= 1;
	if (x < y || x < z)
		ret += x + (y < z ? y : z);
	else
		ret += y + z;
	return ret;
}

int main(){
	char *line = NULL;
	size_t len = 0;
	size_t ret = 0;
	long read;
	while ((read = getline(&line, &len, stdin)) != -1){
		if (read < 5)
			continue;
		int x = atoi(strtok(line, "x"));
		int y = atoi(strtok(NULL, "x"));
		int z = atoi(strtok(NULL, "x"));
		ret += getPaperAmount(x, y, z);
		free(line);
		line = NULL;
	}
	printf("Total amount required: %zu\n", ret);
	return 0;
}
