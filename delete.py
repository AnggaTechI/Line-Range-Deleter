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
