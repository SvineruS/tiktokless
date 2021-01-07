# tiktokless
Download tiktok video by url

## Example
```
vid = main("https://www.tiktok.com/@sinyaba/video/6867949158263721221")
with open('dude.mp4', 'wb') as f:
  f.write(vid)
```

### This is not a library but demo code.

- Open and close the session correctly if you are using the async version.
- COOKIES (sync) or SESSION (async) store data between requests. Without it you will get additional load
