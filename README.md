## Python Port Scanner

A simple and fast Python port scanner that checks all 65,535 ports and grabs service banners.

## Features

- Scans all 65,535 ports
- Shows which ports are open
- Tries to get service banners (like what software is running)
- Uses threads for fast scanning
- Shows how long the scan took

## How to Use

1. **Save the code** as `scanner.py`
2. **Run it** in your terminal:
   ```bash
   python3 banner-grabber.py
   ```
3. **Enter a website** when asked (like `google.com` or `127.0.0.1` for your own computer)
4. **Wait** for the scan to finish
5. **you will see the results** - which ports are open and what's running on them

## Important Notes

**Only scan websites you own or have permission to scan!**

Scanning without permission may be:
- Against the law
- Against website rules
- Considered an attack

**Use this tool responsibly and only for learning!**

##  Requirements

Just Python 3! Nothing else to install.

## Example Output

```
Enter the host: example.com
port 80 is open with banner HTTP/1.1 200 OK
port 443 is open 
Time Duration: 120.5 seconds
```

## Want to Help?

Found a bug or have ideas? 
- Message me on Instagram [@ynot.leonz](https://instagram.com/ynot.leonz)
- Or juz same minded ppl

## License

Free to use for learning and legal security testing.

---

**Remember:** Always get permission before scanning! 🔐

*Made with ❤️ by [@ynot.leonz](https://instagram.com/ynot.leonz)*
-
