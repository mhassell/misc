#include "mex.h"
#include <sys/types.h>
#include <sys/socket.h>
#include <netdb.h>
#include <stdio.h>
#include <string.h>

class socket{
    
}

void echo(){

    char str[100];
    int listen_fd, comm_fd;
    struct sockaddr_in servaddr;

    listen_fd = socket(AF_INET, SOCK_STREAM,0);
    bzero(&servaddr, sizeof(servaddr));

    servaddr.sin_family = AF_INET;
    servaddr.sin_addr.s_addr = htons(INADDR_ANY);
    servaddr.sin_port = htons(22000);

    bind(listen_fd, (struct sockaddr *) &servaddr, sizeof(servaddr));

    mexPrintf("Listening");

    listen(listen_fd, 10);

    comm_fd = accept(listen_fd, (struct sockaddr *) NULL, NULL);
    mexPrintf("Connected");

    while(1)
    {
        bzero(str, 100);
        read(comm_fd, str, 100);
        mexPrintf("Echoing back - %s", str);
        write(comm_fd, str, strlen(str)+1);
    }

}