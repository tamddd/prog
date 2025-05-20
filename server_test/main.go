package main

import "net"

func main() {
	ln, err := net.Listen("tcp", ":8080")
	if err != nil {
		panic(err)
	}
	_, err = ln.Accept()
	if err != nil {
		panic(err)
	}

}
