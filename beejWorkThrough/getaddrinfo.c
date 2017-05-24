// get address info for www.example.net

#include <sys/types.h>
#include <sys/socket.h>
#include <netdb.h>
#include <stdio.h>
#include <string.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <stdlib.h>

int main(){

	int status;
	struct addrinfo hints;
	struct addrinfo *servinfo;
	char ip4[INET_ADDRSTRLEN];		 // space to hold the IPv4 string

	memset(&hints, 0, sizeof(hints));
	hints.ai_family = AF_UNSPEC;
	hints.ai_socktype = SOCK_STREAM;
	hints.ai_flags = AI_PASSIVE;

	if((status = getaddrinfo("www.example.net", "3490", &hints, &servinfo)) != 0){
		fprintf(stderr, "getaddrinfo err: %s\n", gai_strerror(status));
		exit(1);
	}

	// this was segfaulting - no idea what changed
	inet_ntop(AF_INET, &(servinfo->ai_addr->sa_data), ip4, INET_ADDRSTRLEN);

	printf("%s\n", ip4);

	freeaddrinfo(servinfo);

}