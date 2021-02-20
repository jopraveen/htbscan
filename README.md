### See How it works 👇

### https://www.youtube.com/watch?v=1Va6ws_o5w4

### How to use ?

```python3 htbs.py <last digits of IP>```


### Make it simple

copy this file to your /usr/bin directory then simply run this like

```htbs <last digits of IP>```

### what means last digits ?

Here I made this script friendly for HTB users. So, HTB users can just use the last two/three digits of ip

instead of using full ip ```10.10.10.221``` they can simply use ```221``` 

### Non-HTB users 

You guys need to change the 16th line of this code
 
just remove ```10.10.10.``` there and make sure after removing it looks like ```ip = (''+sys.argv[1])```


### Change modes

In 27th line  ```cmd('nmap -sC -sV '+ip+' -p'+ports)```  you can change the modes. If you want an agressive scan then just modify it there.
Code is fully flexible. You can modify it as you want
