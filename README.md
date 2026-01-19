# Daily-Task
current error 

INFO:     127.0.0.1:55307 - "POST /users/ HTTP/1.1" 500 Internal Server Error
ERROR:    Exception in ASGI application
Traceback (most recent call last):
  File "C:\Users\thaku\AppData\Local\Programs\Python\Python311\Lib\site-packages\uvicorn\protocols\http\httptools_impl.py", line 416, in run_asgi     
    result = await app(  # type: ignore[func-returns-value] 
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 
  File "C:\Users\thaku\AppData\Local\Programs\Python\Python311\Lib\site-packages\uvicorn\middleware\proxy_headers.py", line 60, in __call__
    return await self.app(scope, receive, send)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\thaku\AppData\Local\Programs\Python\Python311\Lib\site-packages\fastapi\applications.py", line 1135, in __call__
    await super().__call__(scope, receive, send)
  File "C:\Users\thaku\AppData\Local\Programs\Python\Python311\Lib\site-packages\starlette\applications.py", line 107, in __call__
    await self.middleware_stack(scope, receive, send)       
  File "C:\Users\thaku\AppData\Local\Programs\Python\Python311\Lib\site-packages\starlette\middleware\errors.py", line 186, in __call__
    raise exc
  File "C:\Users\thaku\AppData\Local\Programs\Python\Python311\Lib\site-packages\starlette\middleware\errors.py", line 164, in __call__
    await self.app(scope, receive, _send)
  File "C:\Users\thaku\AppData\Local\Programs\Python\Python311\Lib\site-packages\starlette\middleware\exceptions.py", line 63, in __call__
    await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
  File "C:\Users\thaku\AppData\Local\Programs\Python\Python311\Lib\site-packages\starlette\_exception_handler.py", line 53, in wrapped_app
    raise exc
  File "C:\Users\thaku\AppData\Local\Programs\Python\Python311\Lib\site-packages\starlette\_exception_handler.py", line 42, in wrapped_app
    await app(scope, receive, sender)
  File "C:\Users\thaku\AppData\Local\Programs\Python\Python311\Lib\site-packages\fastapi\middleware\asyncexitstack.py", line 18, in __call__
    await self.app(scope, receive, send)
  File "C:\Users\thaku\AppData\Local\Programs\Python\Python311\Lib\site-packages\starlette\routing.py", line 716, in __call__
    await self.middleware_stack(scope, receive, send)       
  File "C:\Users\thaku\AppData\Local\Programs\Python\Python311\Lib\site-packages\starlette\routing.py", line 736, in app
    await route.handle(scope, receive, send)
  File "C:\Users\thaku\AppData\Local\Programs\Python\Python311\Lib\site-packages\starlette\routing.py", line 290, in handle
    await self.app(scope, receive, send)
  File "C:\Users\thaku\AppData\Local\Programs\Python\Python311\Lib\site-packages\fastapi\routing.py", line 115, in app  
    await wrap_app_handling_exceptions(app, request)(scope, receive, send)
  File "C:\Users\thaku\AppData\Local\Programs\Python\Python311\Lib\site-packages\starlette\_exception_handler.py", line 53, in wrapped_app
    raise exc
  File "C:\Users\thaku\AppData\Local\Programs\Python\Python311\Lib\site-packages\starlette\_exception_handler.py", line 42, in wrapped_app
    await app(scope, receive, sender)
  File "C:\Users\thaku\AppData\Local\Programs\Python\Python311\Lib\site-packages\fastapi\routing.py", line 101, in app  
    response = await f(request)
               ^^^^^^^^^^^^^^^^
  File "C:\Users\thaku\AppData\Local\Programs\Python\Python311\Lib\site-packages\fastapi\routing.py", line 355, in app  
    raw_response = await run_endpoint_function(
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\thaku\AppData\Local\Programs\Python\Python311\Lib\site-packages\fastapi\routing.py", line 243, in run_endpoint_function
    return await dependant.call(**values)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\thaku\Desktop\day3 task\app\api\routes\user.py", line 11, in register    
    created = await create_user(db, user)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\thaku\Desktop\day3 task\app\crud\user.py", line 5, in create_user        
    existing = await db.users.find_one({"email": user.email})
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\thaku\AppData\Local\Programs\Python\Python311\Lib\concurrent\futures\thread.py", line 58, in run       
    result = self.fn(*self.args, **self.kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\thaku\AppData\Local\Programs\Python\Python311\Lib\site-packages\pymongo\synchronous\collection.py", line 1755, in find_one
    for result in cursor.limit(-1):
  File "C:\Users\thaku\AppData\Local\Programs\Python\Python311\Lib\site-packages\pymongo\synchronous\cursor.py", line 1289, in __next__
    return self.next()        
           ^^^^^^^^^^^        
  File "C:\Users\thaku\AppData\Local\Programs\Python\Python311\Lib\site-packages\pymongo\synchronous\cursor.py", line 1265, in next
    if len(self._data) or self._refresh():
                          ^^^^^^^^^^^^^^^
  File "C:\Users\thaku\AppData\Local\Programs\Python\Python311\Lib\site-packages\pymongo\synchronous\cursor.py", line 1213, in _refresh
    self._send_message(q)     
  File "C:\Users\thaku\AppData\Local\Programs\Python\Python311\Lib\site-packages\pymongo\synchronous\cursor.py", line 1108, in _send_message
    response = client._run_operation(
               ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\thaku\AppData\Local\Programs\Python\Python311\Lib\site-packages\pymongo\_csot.py", line 125, in csot_wrapper
    return func(self, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\thaku\AppData\Local\Programs\Python\Python311\Lib\site-packages\pymongo\synchronous\mongo_client.py", line 1938, in _run_operation   
    return self._retryable_read(
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\thaku\AppData\Local\Programs\Python\Python311\Lib\site-packages\pymongo\synchronous\mongo_client.py", line 2048, in _retryable_read  
    return self._retry_internal(
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\thaku\AppData\Local\Programs\Python\Python311\Lib\site-packages\pymongo\_csot.py", line 125, in csot_wrapper
    return func(self, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\thaku\AppData\Local\Programs\Python\Python311\Lib\site-packages\pymongo\synchronous\mongo_client.py", line 2014, in _retry_internal  
    ).run()
      ^^^^^
  File "C:\Users\thaku\AppData\Local\Programs\Python\Python311\Lib\site-packages\pymongo\synchronous\mongo_client.py", line 2763, in run
    return self._read() if self._is_read else self._write() 
           ^^^^^^^^^^^^       
  File "C:\Users\thaku\AppData\Local\Programs\Python\Python311\Lib\site-packages\pymongo\synchronous\mongo_client.py", line 2908, in _read
    self._server = self._get_server()
                   ^^^^^^^^^^^^^^^^^^
  File "C:\Users\thaku\AppData\Local\Programs\Python\Python311\Lib\site-packages\pymongo\synchronous\mongo_client.py", line 2856, in _get_server      
    return self._client._select_server(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\thaku\AppData\Local\Programs\Python\Python311\Lib\site-packages\pymongo\synchronous\mongo_client.py", line 1833, in _select_server   
    server = topology.select_server(
             ^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\thaku\AppData\Local\Programs\Python\Python311\Lib\site-packages\pymongo\synchronous\topology.py", line 428, in select_server
    server = self._select_server(
             ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\thaku\AppData\Local\Programs\Python\Python311\Lib\site-packages\pymongo\synchronous\topology.py", line 402, in _select_server        
    servers = self.select_servers(
              ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\thaku\AppData\Local\Programs\Python\Python311\Lib\site-packages\pymongo\synchronous\topology.py", line 298, in select_servers        
    server_descriptions = self._select_servers_loop(        
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^        
  File "C:\Users\thaku\AppData\Local\Programs\Python\Python311\Lib\site-packages\pymongo\synchronous\topology.py", line 359, in _select_servers_loop  
    raise ServerSelectionTimeoutError(
pymongo.errors.ServerSelectionTimeoutError: SSL handshake failed: ac-opomrzn-shard-00-00.rybr6zs.mongodb.net:27017: [SSL: TLSV1_ALERT_INTERNAL_ERROR] tlsv1 alert internal error (_ssl.c:1006) (configured timeouts: socketTimeoutMS: 20000.0ms, connectTimeoutMS: 20000.0ms),SSL handshake failed: ac-opomrzn-shard-00-01.rybr6zs.mongodb.net:27017: [SSL: TLSV1_ALERT_INTERNAL_ERROR] tlsv1 alert internal error (_ssl.c:1006) (configured timeouts: socketTimeoutMS: 20000.0ms, connectTimeoutMS: 20000.0ms),SSL handshake failed: ac-opomrzn-shard-00-02.rybr6zs.mongodb.net:27017: [SSL: TLSV1_ALERT_INTERNAL_ERROR] tlsv1 alert internal error (_ssl.c:1006) (configured timeouts: socketTimeoutMS: 20000.0ms, connectTimeoutMS: 20000.0ms), Timeout: 30s, Topology Description: <TopologyDescription id: 696e94378592b8d33a9a9bc7, topology_type: ReplicaSetNoPrimary, servers: [<ServerDescription ('ac-opomrzn-shard-00-00.rybr6zs.mongodb.net', 27017) server_type: Unknown, rtt: None, error=AutoReconnect('SSL handshake failed: ac-opomrzn-shard-00-00.rybr6zs.mongodb.net:27017: [SSL: TLSV1_ALERT_INTERNAL_ERROR] tlsv1 alert internal error (_ssl.c:1006) (configured timeouts: socketTimeoutMS: 20000.0ms, connectTimeoutMS: 20000.0ms)')>, <ServerDescription ('ac-opomrzn-shard-00-01.rybr6zs.mongodb.net', 27017) server_type: Unknown, rtt: None, error=AutoReconnect('SSL handshake failed: ac-opomrzn-shard-00-01.rybr6zs.mongodb.net:27017: [SSL: TLSV1_ALERT_INTERNAL_ERROR] tlsv1 alert internal error (_ssl.c:1006) (configured timeouts: socketTimeoutMS: 20000.0ms, connectTimeoutMS: 20000.0ms)')>, <ServerDescription ('ac-opomrzn-shard-00-02.rybr6zs.mongodb.net', 27017) server_type: Unknown, rtt: None, error=AutoReconnect('SSL handshake failed: ac-opomrzn-shard-00-02.rybr6zs.mongodb.net:27017: [SSL: TLSV1_ALERT_INTERNAL_ERROR] tlsv1 alert internal error (_ssl.c:1006) (configured timeouts: socketTimeoutMS: 20000.0ms, connectTimeoutMS: 20000.0ms)')>]>


