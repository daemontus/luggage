This is an extension of the `base-conda` image where we also enable VS code for remote access the same we do it in the `base-science` image.

### Build and publish

```
docker build -t daemontus/workspace-code-conda .
docker push daemontus/workspace-code-conda
```