import sys
import os

def demo_sys():
    print(sys.version)

    #region Run this in two options -
    # 1. as a regular script : IDE or "py <scriptname>"
    # 2. in the interactive shell: Start shell as "py -i", then copy paste the below code there.
    print(f"{sys.flags.interactive=}")
    #endregion

    print(sys.platform)

    # print(sys.argv)
    # if len(sys.argv) != 3:
    #     sys.stderr.write("This is a binary operation, requiring 2 argument.")
    #     # print()
    #     return -1

    # sum = int(sys.argv[1]) + int(sys.argv[2])
    # return sum



def demo_os():
    curr_dir = os.getcwd()
    print(curr_dir)

    for item in os.listdir():
        print(item)

    new_dir = "demo_dir"
       
    demo_dir = os.path.join(curr_dir, new_dir)

    if os.path.exists(demo_dir):
        print("Folder already exists")
    else:
        os.mkdir(demo_dir)
        print(f"The folder was created at: {demo_dir}")

    new_file = "demo_file.txt"
    demo_file = os.path.join(demo_dir, new_file)
    print(demo_file)

    if os.path.exists(demo_file):
        mode = "w+"
        print("File already exists. Will open for modification...")
    else:
        mode = "w"
        print("File not found. Will open for creation...")

    # file = open(demo_file, mode=mode)
    # # File IO operations
    # file.close()

    with open(demo_file, mode=mode) as file:
        # File operations
        # file.seek(45)
        # file.write("This is the first line")
        # file.write("This is the second line")
        # # file.write("-------")

        # pos = file.tell()
        # print(f"{pos=}")        
        
        lines = ["first line\n", "second line\n", "third line\n"]

        # pos = file.tell()
        # print(f"{pos=}")
        file.writelines(lines)
        # pos = file.tell()
        # print(f"{pos=}")

    
    with open(demo_file, mode="r") as file:
        # data = file.read(512)
        # data = file.readline(512)
        data = file.readlines(512)
        file.seek(0)
        for line in file:
            print(line, end="")
        
        print(data)

    if os.path.exists(demo_file):
        os.remove(demo_file)
        print(f"Removed the file '{demo_file}'")
    else:
        print(f"File not found at '{demo_file}'")

    if os.path.exists(demo_dir):
        os.rmdir(demo_dir)
        print(f"Removed the directory, '{demo_dir}'")
    else:
        print(f"Couldn't find the directory, '{demo_dir}'")

if __name__ == "__main__":
    # sys.stdout = output_file
    # sys.stderr = error_file
    # sys.stdin = input_file
    # ret = demo_sys()
    # if ret == -1:
    #     print("Error")
    # print(f"Result={ret}")
    demo_sys()

    # demo_os()
