import os

def is_bootfile(filepath):
    with open(filepath, 'rb') as fd:
        text = fd.read(32)
        if(text[11:16] == b'\x42\x6F\x6F\x74\x30'):

            return True
        else:
            return False
        

def traverse(dirpath, nvar_dir):
    if(os.path.isdir(dirpath)):
        subfiles = os.listdir(dirpath)
        for filename in subfiles:
            filepath = os.path.join(dirpath, filename)
            traverse(filepath, nvar_dir)
    else:
        if(dirpath[-5:] == ".nvar" and is_bootfile(dirpath)):
            filename = dirpath.split("\\")[-1]
            content = []
            with open(dirpath, 'rb') as fd:
                content = fd.read()

            filepath = os.path.join(nvar_dir, filename)
            with open(filepath, 'wb') as fd:
                fd.write(content)

if __name__=='__main__':
    root_dir = "C:\\Users\\dfrc\\Desktop\\uefi files"
    nvar_dir = os.path.join(root_dir, "nvar_dir")

    if(not os.path.exists(nvar_dir)):
        os.mkdir(nvar_dir)

    traverse(root_dir, nvar_dir)
