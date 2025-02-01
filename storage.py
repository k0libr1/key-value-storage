import os
import json
import argparse
import tempfile

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', help='Ключ по котрому сохраняется/получается значение')
    parser.add_argument('--val', help='Сохраняемое значение')
    return parser.parse_args()

def read_data(storage_path):
    if not os.path.exists(storage_path):
        return {}
    with open(storage_path, 'r') as f:
        raw_data = f.read()
        if raw_data:
            return json.loads(raw_data)
        else:
            return {}

def write_data(storage_path, data):
    with open(storage_path, 'w') as f:
        f.write(json.dumps(data))

def get(storage_path, key):
    data = read_data(storage_path)
    print(data.get(key, []))

def put(storage_path, key, value):
    data = read_data(storage_path)
    data[key] = data.get(key, list())
    data[key].append(value)
    write_data(storage_path, data)

def main(storage_path):
    args = parse()

    if args.key and args.val:
        put(storage_path, args.key, args.val)
    elif args.key:
        get(storage_path, args.key)
    else:
        print('The program is called with invalid parameters.')

if __name__ == '__main__':
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    main(storage_path)
   


