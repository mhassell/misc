// just sorta re-typing everything to get it under my fingers

struct addrinfo {
	// I assume the ai prefix means addrinfo

	int		ai_flags;					// AI_PASSIVE, AI_CANONNAME, etc
	int 	ai_family;					// AF_INET, AF_INET6, AF_UNSPEC
	int 	ai_socktype;				// SOCK_STREAM, SOCK_DGRAM
	int 	ai_protocol;				// 0 is any protocol
	size_t 	ai_addrlen;					// size of ai_addr in bytes
	struct 	sockaddr *ai_addr;			// struct sockaddr_in or _in6
	char 	*ai_canonname;				// full canonical hostname

	struct 	addrinfo *ai_next;			// next link in the linked list (??)

}


struct sockaddr {
	// this is the sockaddr in the struct addrinfo

	unisigned short sa_family;   		// address family, AF_xxx
	char			sa_data[14];		// 14 bytes of protocol address (why 14?)

}


struct sockaddr_in{
	// something easier to cast into a sockaddr
	
	short int 			sin_family;		// address family, AF_INET
	unsigned short int 	sin_port;		// port number
	struct in_addr 		sin_addr; 		// internet address
	unsigned char		sin_zero[8];   	// should the 8 be hard coded?

}