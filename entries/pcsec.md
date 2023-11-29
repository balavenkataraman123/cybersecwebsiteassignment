# Personal Cybersecurity practices


## Most common attacks and how to avoid them

### Malware

Malware is a type of software that is designed to cause harm to a computer system. It can take many forms, including viruses, worms, Trojan horses, and spyware. These malicious programs can cause a wide range of problems, from data loss and system crashes to identity theft and financial fraud.

To protect against malware, it is important to take a multi-layered approach. One of the most effective ways to prevent malware infections is to keep your computer and software up to date. This ensures that any known vulnerabilities are patched and that your system has the latest security features.

<img src="https://www.bleepstatic.com/content/hl-images/2022/03/31/Malware.jpg" height="200" />


An important step is to use anti-virus software. These programs can detect and remove malware from your system, and can also help to prevent new infections from occurring. It's important to keep your anti-virus software up to date, and to run regular scans to ensure that your system is free from malware.

Another way to protect against malware is to be cautious when downloading and installing software. Only download software from reputable sources, and be wary of any suspicious emails or pop-ups that ask you to download and install software. Additionally, it's important to be careful when using social networking sites, as malware can be spread through links and downloads on these platforms.

You can also use a firewall to protect your computer from malware. Firewalls can block incoming traffic and can help to prevent malware from communicating with command and control servers.



<img src="https://marvel-b1-cdn.bc0a.com/f00000000216283/www.fortinet.com/content/fortinet-com/en_us/resources/cyberglossary/malware/_jcr_content/par/c05_container_copy_c_405637578/par/c28_image.img.jpg/1615919193441.jpg" height="200" />

When you are doing something that you know has a high chance of infecting your computer with malware, such as downloading pirated media from lesser-known sources, it is a very useful trick to create a virtual machine specifically for that purpose. In this case, if it gets infected you can just reinstall it, without losing data on the host system. After that, once the downloaded files are verified to be safe, you can transfer them to your host machine to watch the content.

tools like VirtualBox make setting up VMs easy.

### Phishing

Phishing is a type of cyber attack that involves tricking individuals into providing sensitive information, such as passwords or financial information, by disguising as a trustworthy source. This can be done through various methods, including email, text message, or phone call.

One of the most effective ways to protect yourself from phishing attacks is to be aware of the different types of phishing and how they work. For example, email phishing often involves an attacker posing as a legitimate company or organization, and asking for personal information or login credentials. Phone phishing often involves an attacker posing as a customer service representative and asking for sensitive information.

Another important step is to be cautious when clicking on links or providing personal information. Do not click on links in unsolicited emails, and be wary of providing personal information over the phone or through a website. Before giving away any personal information, verify the authenticity of the requester by independently searching the company's contact information and not clicking on links provided in the email.

It is also important to use anti-virus and anti-phishing software, which can help to detect and block phishing attempts. These programs can also help to warn you when you visit a website that is known to be associated with phishing.

Additionally, you should enable two-factor authentication for your online accounts. This can make it much more difficult for attackers to gain access to your accounts, even if they manage to steal your password.

You can also educate yourself about the common tactics used in phishing attacks, such as creating a sense of urgency or using social engineering tactics. By being aware of these tactics, you can better recognize a phishing attempt when it occurs.



### Password attacks

If your password is simple or common, you are at risk of a password attack, such as a brute force attack or a dictionary attack.

Brute force attacks test every possible combination of password, so short passwords can be cracked relatively easily.

Dictionary attacks are a bit more sophisticated, and try out passwords out of a list of the most commonly used passwords. If your password is in this list of , [10000 most common passwords list](https://en.wikipedia.org/wiki/Wikipedia:10,000_most_common_passwords), it might be at risk.

Try out the [interractive password strength calculator](/interractive/pswd).

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

<img src="https://www.imperva.com/learn/wp-content/uploads/sites/13/2019/01/DNS-spoofing.jpg" height="300" />

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








