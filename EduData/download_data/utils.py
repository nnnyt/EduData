# coding: utf-8
# create by tongshiwei on 2019-8-16
import tarfile
import zipfile

import rarfile


def decompress(file):
    for z in [".tar.gz", ".tar.bz2", ".tar.bz", ".tar.tgz", ".tar", ".tgz", ".zip", ".rar"]:
        if file.endswith(z):
            if z == ".zip":
                un_zip(file)
            elif z == ".rar":
                un_rar(file)
            else:
                un_tar(file)


def get_path(file):
    #  返回解压缩后的文件名
    for i in [".tar.gz", ".tar.bz2", ".tar.bz", ".tar.tgz", ".tar", ".tgz", ".zip", ".rar"]:
        file = file.replace(i, "")
    return file


def un_zip(file):
    zip_file = zipfile.ZipFile(file)
    uz_path = get_path(file)
    print(file + " is unzip to " + uz_path)
    for name in zip_file.namelist():
        zip_file.extract(name, uz_path)
    zip_file.close()


def un_rar(file):
    rar_file = rarfile.RarFile(file)
    uz_path = get_path(file)
    print(file + " is unrar to " + uz_path)
    rar_file.extractall(uz_path)


def un_tar(file):
    tar_file = tarfile.open(file)
    uz_path = get_path(file)
    print(file + " is untar to " + uz_path)
    tar_file.extractall(path=uz_path)
