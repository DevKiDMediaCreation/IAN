<?php
$server = new OpenSwoole\HTTP\Server("127.0.0.1", 8081);

$server->on("start", function (OpenSwoole\Http\Server $server) {
    echo("Server is started at http://127.0.0.1:8081\n");
});

$server->on("request", function (OpenSwoole\Http\Request $request, OpenSwoole\Http\Response $response) {
    $response->end("<h1>Hello Swoole. #".rand(1000, 9999)."</h1>");
});

$server->start();