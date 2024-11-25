# DirScribe 📂✍️

![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
[![PyPI version](https://badge.fury.io/py/dirscribe.svg)](https://badge.fury.io/py/dirscribe)

> 🔍 A powerful directory documentation tool that generates both tree views and content reports of your file system.

## 🌟 Features

- 🌳 Generate visual directory tree structures
- 📝 Extract and document file contents
- 🚀 Easy-to-use command line interface
- 📁 Support for nested directories
- 💾 Customizable output file location

## 🎯 Installation

```bash
pip install dirscribe
```

## 🚀 Quick Start

```bash
# Basic usage
dirscribe /path/to/directory

#Specify custom output file
dirscribe /path/to/directory -o custom_report.txt
```

## 📋 Output Example

The tool generates a comprehensive report that includes:

### 1. Directory Tree View

```bash
📂 project_root
├── 📂 src
│ ├── 📄 main.py
│ └── 📄 utils.py
├── 📂 tests
│ └── 📄 test_main.py
└── 📄 README.md
```

### 2. File Contents

```bash
================================================================================
FILE CONTENTS:
--------------------------------------------------------------------------------
File: src/main.py
...
[File contents here]
...
================================================================================
bash
dirscribe <directory_path> [-o OUTPUT_FILE]
Arguments:
directory_path Directory to scan
-o, --output Output file path (default: scan_report.txt)
To make this README even better:
Replace the placeholder links with your actual social media and GitHub links
Add actual screenshots of the tool in action
You could add these sections to the image links:
To add actual images:
Create a screenshots directory in your project
Add relevant screenshots
Update the image paths in the README
Would you like me to help you create any specific sections in more detail?
```


## 💻 Requirements

- Python 3.6 or higher
- No additional dependencies required

## 🛠️ Usage Options

- `-o, --output`: Specify the output file path (default: `scan_report.txt`)
- `-h, --help`: Display help information and usage instructions


## 📚 Example Use Cases

- 📊 Project documentation
- 🔍 Code review preparation
- 📁 File system auditing
- 📝 Content inventory

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. 🍴 Fork the repository
2. 🌿 Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. 📤 Push to the branch (`git push origin feature/AmazingFeature`)
5. 🔄 Open a Pull Request

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

## 👥 Authors

- Mohammad Sadegh Sirjani - [GitHub Profile](https://github.com/msadeqsirjani)

## 🙏 Acknowledgments

- 🌟 Inspired by the need for better directory documentation
- 🎨 Tree view ASCII art structure
- 📚 Python's os module

## 📞 Contact

Your Name - [@msadeqsirjani](https://twitter.com/msadeqsirjani)

Project Link: [https://github.com/msadeqsirjani/dirscribe](https://github.com/msadeqsirjani/dirscribe)

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/msadeqsirjani">Your Name</a>
</p>