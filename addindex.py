import os

root_dir = 'docs/source'
def add_index_loop(root_dir):
    item_list = os.listdir(root_dir)
    if 'index.rst' not in item_list:
        # add index
        index_file_dir = os.path.join(root_dir, 'index.rst')
        with open(index_file_dir, 'w') as f:
            f.write(f'{os.path.basename(root_dir)}\n'
                    f'----------------------------------------------------------\n'
                    f'.. toctree::\n'
                    f'  :maxdepth: 2\n')
            for item in item_list:
                if item.endswith('.rst'):
                    f.write(f'  {item[:-4]}\n')
                else:
                    sub_file_dir = os.path.join(root_dir, item)
                    if os.path.isdir(sub_file_dir):
                        f.write(f'  {item}/index\n')
    for item in item_list:
        file_dir = os.path.join(root_dir, item)
        if os.path.isdir(file_dir):
            add_index_loop(file_dir)
add_index_loop(root_dir)
