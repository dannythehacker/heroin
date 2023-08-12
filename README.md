# Hero-IN

<div align="center">
    <img src="https://github.com/MatrixByt3s/heroin/assets/119423081/099b71b6-7204-44b8-9cfb-5f1831ce3229" alt="Heroin Logo">
</div>

## Introduction

```Heroin``` is an educational Python script to demonstrates potential vulnerabilities related to insecure file serving in web applications.

## Features
- Easy to use interface for exploiting vulnerable servers
- Offers a controlled environment for hands-on practice.

## Usage

1. Clone the repository to your local machine:

   ```git clone https://github.com/MatrixByt3s/heroin.git```
   ```cd heroin```

2. Install the required dependencies:

   ```pip install -r requirements.txt```

3. Run the script by providing the target URL:

   ```python heroin.py <url>```

## Using the Script

```Heroin``` provides an interactive command-line interface for exploring vulnerabilities. Once you've provided the target URL and started the script, follow these steps:

1. **Exploit Identification**: The script will attempt to exploit vulnerabilities in the target's file-serving mechanism. It will display the progress as it attempts different exploit paths.

2. **Interactive Prompt**: After successfully exploiting the vulnerability, you will enter an interactive prompt. Here, you can execute various commands to interact with the target server.

3. **Commands**: The following commands are available within the interactive prompt:

   - ```cat [path]```: Display the content of a file.
   - ```exists [path]```: Check if a file exists.
   - ```dl [path] [filename]```: Download a file.

## Vulnerable Test Server

Included in the repository is a simple Flask server, located in the `vulnerable-server` directory. This server emulates an environment where file-serving vulnerabilities may be exploited. To set up and run the server:

1. Navigate to the `vulnerable-server` directory:

   ```cd vulnerable-server```

3. Start the server:

   ```python server.py```

Access media files using the URL pattern: ```http://127.0.0.1:5000/media/<filename>```. Use this server responsibly for educational purposes only.

## Disclaimer

```Heroin``` and the vulnerable test server are intended solely for educational and training purposes. They should only be used on systems for which you have explicit authorization. Unauthorized and malicious use is strictly prohibited. The author and contributors of this project do not endorse or encourage any illegal activities or unauthorized access.

## Contribute

Contributions to improve ```Heroin's``` educational value are welcome! Please submit pull requests with enhancements, fixes, or additional resources.
