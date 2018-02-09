Install json-server

```
npm install -g json-server
```

cd to mock_omdb

run json-server


```
json-server --watch movies.json --middlewares omdb.js --routes routes.json
```

Needs custom routes and middleware to create OMDB behavior.
Alternative approach - set up a mini python server with http.server

if testing with curl, remember that & is a special character to the command line and should be escaped \&
