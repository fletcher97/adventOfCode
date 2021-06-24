#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int min(int x, int y){
	return x < y ? x : y;
}

int getPaperAmount(int x, int y, int z){
	int ret = 0;
	ret += 2 * x * y;
	ret += 2 * x * z;
	ret += 2 * y * z;
	ret += min(min(x * y, x * z), y * z);
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
