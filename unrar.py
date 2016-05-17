# -*- coding: utf-8 -*-
"""
Created on Tue May 17 08:49:33 2016

@author: xu gang
"""

import os

def unrar(source_dir, unzip_dir):
    #windows RAR解压缩命令
    rar_command = '"D:\\winrar\\WinRAR.exe" x %s * %s\\' % (source_dir, unzip_dir)
    os.system(rar_command)
    
if __name__ == "__main__":
    
    filepath = "D:\\pdb_ftp\\pdb"
    filegroups = os.listdir(filepath)
    
    total = 0
    
    unzip_dir = "D:\\pdb_ftp\\unrar"
    
    for filegroup in filegroups:
        
        files = os.listdir(filepath + "\\" + filegroup)
        
        for file_indiv in files:
            source_dir = filepath + "\\" + filegroup + "\\" + file_indiv
            total = total + 1
            unrar(source_dir, unzip_dir)
            #print file_indiv
        
    print "total:",total
    
    
