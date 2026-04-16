<h1 align="center">⚡ Line-Range-Deleter ⚡</h1>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=24&pause=1000&color=00F7FF&center=true&vCenter=true&width=850&lines=Fast+Line+Range+Deletion+Tool;Delete+Custom+Lines+From+Huge+Files;Simple+%7C+Fast+%7C+Buffered+Processing" alt="Typing SVG" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-Script-1f6feb?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Project-Line-Range-Deleter-00c853?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Mode-Large+File+Ready-6f42c1?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Speed-Fast-ff9800?style=for-the-badge" />
</p>

---

## ✨ About

**Line-Range-Deleter** is a fast and lightweight Python tool for deleting a custom range of lines from files.

It is built for handling **large text files** efficiently by using buffered file processing, making it suitable for huge logs, datasets, and wordlists.

---

## 🚀 Features

- ⚡ Delete any custom line range
- 📂 Works with large files
- 🧠 Buffered processing
- 🧹 Automatically replaces the original file
- 🎯 Simple command-line input
- 🔥 Optimized for deleting from line `1` to `N`

---

## 🛠️ Code

```python
import os
import shutil

BUF_SIZE = 16 * 1024 * 1024  # 16 MB buffer

def line_del(input_file, start_line, end_line):
    if start_line < 1 or end_line < start_line:
        raise ValueError("Invalid line range.")

    if not os.path.isfile(input_file):
        raise FileNotFoundError(f"File not found: {input_file}")

    temp_file = input_file + ".tmp"

    with open(input_file, "rb", buffering=BUF_SIZE) as fin, \
         open(temp_file, "wb", buffering=BUF_SIZE) as fout:

        if start_line == 1:
            for _ in range(end_line):
                if not fin.readline():
                    break
            shutil.copyfileobj(fin, fout, length=BUF_SIZE)
        else:
            current_line = 1
            while True:
                line = fin.readline()
                if not line:
                    break

                if current_line < start_line or current_line > end_line:
                    fout.write(line)

                current_line += 1

    os.replace(temp_file, input_file)
    print(f"Done. Lines {start_line} - {end_line} deleted from {input_file}")


if __name__ == "__main__":
    file_path = input("Enter file name: ").strip()
    start_line = int(input("Delete from line: ").strip())
    end_line = int(input("Delete to line: ").strip())

    line_del(file_path, start_line, end_line)
```

---

## ▶️ Usage

Run the script:

```bash
python delete.py
```

Then enter:

```text
Enter file name: data.txt
Delete from line: 1
Delete to line: 100000
```

---

## 📌 Example Use Cases

- Cleaning huge log files
- Removing broken headers
- Trimming exported text files
- Deleting unwanted sections from big datasets
- Editing large wordlists faster

---

## 🌊 Visual

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:00F7FF,100:6f42c1&height=130&section=header&text=Line-Range-Deleter&fontSize=38&fontColor=ffffff&animation=fadeIn" />
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:6f42c1,100:00F7FF&height=130&section=footer" />
</p>
