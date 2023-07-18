# \[Zavazadlo\] Portal

Portal is a simple static website which shows all active services. The list of services is created manually---you have to actually update the `index.html` file. As such, the whole thing is extremely simple. 

## Testing

When updating the `index.html` file, it is useful to test the changes locally. You can do that by going to the `www` directory and running:

```
python3 -m http.server 9000
```

## Deployment

The resulting docker image should simply serve the static website on port `80`. So you still need to configure it with a reverse proxy. Ideally, the access to this information should be authenticated, even though all relevant services linked by the website are all authenticated anyway.