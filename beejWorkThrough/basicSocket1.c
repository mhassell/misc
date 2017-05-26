#include <stdio.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netdb.h>
#include <arpa/inet.h>
#include <netinet/in.h>

int main(){

	int sockfd, newfd;
	int status;
	struct addrinfo hints, *res;
	char ipstr[INET6_ADDRSTRLEN];

	memset(&hints, 0, sizeof(hints));
	hints.ai_family = AF_UNSPEC;
	hints.ai_socktype = SOCK_STREAM;
	hints.ai_flags = AI_PASSIVE; 
	// AI_PASSIVE just binds to the IP of the local host, but can be set to a specified IP

	if((status = getaddrinfo(NULL, "3490", &hints, &res)) != 0){
		printf("Error %s\n", gai_strerror(status));
		return 1;
	}

	sockfd = socket(res->ai_family, res->ai_socktype, res->ai_protocol);

	if((status = bind(sockfd, res->ai_addr, res->ai_addrlen))!= 0){
		printf("Error binding to the socket\n");
		return 1;
	}

	if((status = listen(sockfd, 10))!=0){
		printf("Error listening\n");
		return 1;
	}


	while(1){

			if((newfd = accept(sockfd, res->ai_socktype, res->ai_addrlen))!=0){
			printf("Error accepting a connection\n");
			close(sockfd);
			return 1;
	}



	}

	
}