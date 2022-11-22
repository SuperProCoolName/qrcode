# QR Code Generator
Generate QR Code.

To install all necessary modules run this code in your command line: 

```bash
pip install pyzbar, pillow, validators, qrcode
```

# Usage
Download source code via using console
```
git clone https://github.com/SuperProCoolName/qrcode.git
```

To set text or link to generate QR Code simply run `qr_code.py`.

# Advanced usage
Set data in quotes to your needed text or link
```python
def main():
    data = input('Enter text or link: ')
```
If you entered link you will be asked whether or not you want to open it.

# Examples

```python
def main():
  data = 'github.com/SuperProCoolName/qrcode.git'
```