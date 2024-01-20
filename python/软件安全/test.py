import struct

def read_basic_info(f):
    """读取FAT32映像文件的基本信息"""
    f.seek(11, 0)
    bytes_per_sector = struct.unpack('H', f.read(2))[0]
    sectors_per_cluster = struct.unpack('B', f.read(1))[0]
    reserved_sectors = struct.unpack('H', f.read(2))[0]
    number_of_fats = struct.unpack('B', f.read(1))[0]
    f.seek(36, 0)
    sectors_per_fat = struct.unpack('I', f.read(4))[0]
    return bytes_per_sector, sectors_per_cluster, reserved_sectors, number_of_fats, sectors_per_fat

def find_file(f, filename_to_find, root_dir_sectors, bytes_per_sector):
    """查找文件的目录项"""
    f.seek(root_dir_sectors, 0)
    while True:
        dir_entry = f.read(32)
        if not dir_entry or dir_entry[0] == 0xE5 or dir_entry[0] == 0x00:
            break
        filename = dir_entry[0:11].decode('ascii').rstrip()
        if filename == filename_to_find.upper():
            return dir_entry
    return None

def get_cluster_chain(f, dir_entry, sectors_per_fat, fat_start, bytes_per_sector):
    """获取文件簇链"""
    start_cluster = struct.unpack('H', dir_entry[26:28])[0] | (
        struct.unpack('H', dir_entry[20:22])[0] << 16)
    cluster_chain = []
    current_cluster = start_cluster
    while current_cluster < 0x0FFFFFF8:
        cluster_chain.append(current_cluster)
        fat_offset = current_cluster * 4
        f.seek(fat_start * bytes_per_sector + fat_offset)
        current_cluster = struct.unpack('I', f.read(4))[0]
    return cluster_chain

def read_cluster_data(f, cluster_number, bytes_per_sector, sectors_per_cluster, data_start_sector):
    """读取指定簇的数据"""
    cluster_offset = (cluster_number - 2) * sectors_per_cluster
    cluster_sector = data_start_sector + cluster_offset
    f.seek(cluster_sector * bytes_per_sector)
    return f.read(sectors_per_cluster * bytes_per_sector)

def get_cluster_contents(file_path, filename_to_find, cluster_number_to_get):
    with open(file_path, 'rb') as f:
        bytes_per_sector, sectors_per_cluster, reserved_sectors, number_of_fats, sectors_per_fat = read_basic_info(f)
        fat_start = reserved_sectors
        data_start_sector = reserved_sectors + number_of_fats * sectors_per_fat
        root_dir_sectors = fat_start * bytes_per_sector

        dir_entry = find_file(f, filename_to_find, root_dir_sectors, bytes_per_sector)
        if dir_entry:
            cluster_chain = get_cluster_chain(f, dir_entry, sectors_per_fat, fat_start, bytes_per_sector)
            if cluster_number_to_get in cluster_chain:
                return read_cluster_data(f, cluster_number_to_get, bytes_per_sector, sectors_per_cluster, data_start_sector)
            else:
                print(f"Cluster number {cluster_number_to_get} not in the chain of {filename_to_find}")
                return None
        else:
            print(f"File {filename_to_find} not found.")
            return None

# 使用示例
if __name__ == '__main__':
    filepath = 'image.img'
    file_to_find = 'TEST    TXT'
    cluster_number = 3

    cluster_data = get_cluster_contents(filepath, file_to_find, cluster_number)
    if cluster_data:
        print(f"Data of cluster {cluster_number} in file {file_to_find}:")
        print(cluster_data)
    else:
        print(f"Unable to retrieve data for cluster {cluster_number}.")
