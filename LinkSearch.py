message = str("this is the link to betweener https//:www.googleplaystroe.com?id=tk.tekporacademy.betweener follow for more exiting stuff this  for more exiting stuff"  );
a = int(message.index("http"));
t = bool(message.__contains__("http"))
b = int(message.index(" ", a-1));
c = int(0)
links = [];
while t:
    if b < a:
        c = int(message.index(" ", a))
        link = str(message[a:c]);
        if link.__contains__("//:www.") & link.__contains__("."):
            links.append(link);
        message = message[c:len(message)]
        if message.__contains__("http"):
            a = int(message.index("http"));
            b = int(message.index(" ", a - 1));
        try:
            t = int(message.__contains__("http"))
        finally:
            y = bool(True);
print(links);