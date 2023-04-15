# ssh-brute

Kullanıcı adı ve şifresi belirterek ssh servisini kaba kuvvet saldırısı yapmaya yarayan bir araçtır.

## Gereksinimler

ssh-brute aşağıdaki kütüphaneleri kullanır.

* Colorama
* Paramiko

## Kurulumu

Projeyi klonlamak için;

```python
git clone https://github.com/thealper2/ssh-brute.git
```
Gerekli kütüphaneleri kurmak için;

```python
python -m pip install -r requirements.txt
```

## Kullanımı

| Parametre | Kullanımı |
| --------- | --------- |
| -v        | Verbose. Çıktı göstermek için kullanılır. |
| -H        | Host. Hedefin IP adresini belirtmek için kullanılır. |
| -u        | User. Saldırı yapılacak kullanıcıyı belirtmek için kullanılır. |
| -U        | Userlist. Saldırı yapılacak kullanıcı adlarının bulunduğu listeyi belirtmek için kullanılır. |
| -p        | Password. Saldırı yapılacak kullanıcının parolasını belirtmek için kullanılır. |
| -P        | Passwordlist. Saldırı yapılacak kullanıcının parolalarının bulunduğu listeyi belirtmek için kullanılır. |

```bash
usage: ssh_brute.py [-h] [-u U] [-U U] [-p P] [-P P] [-v] -H H

SSH brute force

options:
  -h, --help  show this help message and exit
  -u U        single user
  -U U        user from file
  -p P        single password
  -P P        password from file
  -v          verbose
  -H H        host
```

## Örnekler

```python
python3 ssh_brute.py -H TARGET_IP -u root -p toor -v
python3 ssh_brute.py -H TARGET_IP -U users.txt -p password
python3 ssh_brute.py -H TARGET_IP -u root -P passwords.txt -v
python3 ssh_brute.py -H TARGET_IP -U users.txt -P passwords.txt -v
```
