const {createServer} = require("http");

let server = createServer((request, response) => {
	response.writeHead(200, {
		"Content-Type": "text/html"	});
	response.write(`
<h1>hello!</h1>
<p>${request.url}</p>`);
	response.end();
});

server.listen(8000);
console.log("listening!!!");
