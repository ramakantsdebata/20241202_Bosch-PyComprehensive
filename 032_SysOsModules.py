import sys
import os

def demo_sys():
    print(sys.version)
    print(f"{sys.flags.interactive=}")
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



if __name__ == "__main__":
    # sys.stdout = output_file
    # sys.stderr = error_file
    # sys.stdin = input_file
    # ret = demo_sys()
    # if ret == -1:
    #     print("Error")
    # print(f"Result={ret}")
    # demo_sys()

    demo_os()
