### DNS poisoning

Websites on the internet are identified by IP addresses, similar to how buildings are identified by street addresses.

You can see how memorizing the IP addresses of all the websites you visit on a daily basis can be a pain, just like remembering all your friends' phone numbers.

Like a phone has a contacts directory so you can search by name to find a phone number, so does the internet

A DNS, or Domain Name system, is a system that finds an IP address from a URL you enter. For example, if you enter the URL of GitHub, ```https://www.github.com``` it redirects you to the IP 192.30.255.113 .

The directory of IPs to URLs are stored in DNS servers, although the most commonly used ones are stored as cache on your own computer.

(For more information on how the caching algorithm works, look up "Least Recently Used Cache")

These DNS servers can sometimes be attacked, so for example, That URL for GitHub can redirect to the IP address of a Different website, for example, 66.251.114.40

In a website that obviously looks very different, this is not much of a problem, but attackers can redirect people from bank websites to a sketchy phishing site.

For this reason, always be careful on a site you enter the credit card information, eg. e-commerce sites like Amazon, Aliexpress, DigiKey, etc., and bank websites.

Periodically clear your DNS cache as well, using the commands

```
sudo systemd-resolve --flush-caches
```

```
sudo resolvectl flush-caches
```

on Linux, Android and Mac. It is different on Windows.

<img src="/image/DNS-spoofing.jpg" height="300" />

Source: [Medium article](href="https://medium.com/mobile-development-group/dns-and-privacy-d50c59428cb2">Medium article)

### Ways you can use DNS modification

There is a locally stored DNS list on your computer, in the file path "etc/hosts". In this file, there is a list of IP addresses, and their corresponding URLs and hostnames.

Editing this file, and adding the line

```
127.0.0.1 www.instagram.com
```

redirects the URL to Instagram to your local machine IP address (127.0.0.1). When you type www.instagram.com in the browser, it will take you to a page that looks like this

![Blocked](/image/Screenshot from 2023-01-12 20-32-13.png)

The effect is that Instagram is blocked.

You can see the possibility of doing this to block all advertising sites.

Using root terminal on your phone from your PC, you can edit the hosts file of your phone to block out all advertising sites, so advertisements even in non-browser applications (where an ad-blocking extension can't be installed) can be blocked.

Similarly, a device can be connected to your router to also play the role of a modified DNS server. This is usually done with a Raspberry Pi Single Board Computer. A software called <a href="https://pi-hole.net/">PiHole</a> can be used. 