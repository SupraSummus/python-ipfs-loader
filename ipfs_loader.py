from importlib.abc import MetaPathFinder, InspectLoader
from importlib.util import spec_from_loader
import urllib.request
import sys
import json
from functools import lru_cache


def ipfs_path_from_fullname(fullname):
    return fullname.replace('.', '/')


def ipfs_file_path_from_fullname(fullname, is_package):
    if is_package:
        return ipfs_path_from_fullname(fullname) + '/__init__.py'
    else:
        ipfs_path = ipfs_path_from_fullname(fullname)
        if ipfs_path.count('/') > 0:
            ipfs_path = ipfs_path + '.py'
        return ipfs_path


class IPFSLoader(InspectLoader):

    def __init__(self, finder, *args, **kwargs):
        self.finder = finder
        super().__init__(*args, **kwargs)

    @lru_cache(maxsize=1024)
    def is_package(self, path):
        try:
            with urllib.request.urlopen(
                self.finder.api_url + 'ls?arg=' + ipfs_path_from_fullname(path)
            ) as response:
                data = json.loads(response.read())['Objects']
                assert(len(data) == 1)
                return any([link['Name'] == '__init__.py' for link in data[0]['Links']])
        except urllib.error.HTTPError as err:
            # asserting that if `ls` failed and response is JSON it isn't a package
            data = json.loads(err.read())
            return False
        except Exception as err:
            raise ImportError('error checking is_package /ipfs/' + ipfs_path_from_fullname(path)) from err

    def get_source(self, path):
        ipfs_path = ipfs_file_path_from_fullname(
            path,
            self.is_package(path)
        )
        try:
            with urllib.request.urlopen(
                self.finder.api_url + 'cat?arg=' + ipfs_path
            ) as response:
                return response.read()
        except Exception as err:
            raise ImportError('couldn\'t import /ipfs/' + ipfs_path) from err


class IPFSFinder(MetaPathFinder):

    def __init__(self, api, *args, **kwargs):
        self.api_url = api
        self.loader = IPFSLoader(self)
        super().__init__(*args, **kwargs)

    def find_spec(self, fullname, path, target=None):
        return spec_from_loader(
            fullname,
            self.loader,
            origin='/ipfs/{}'.format(ipfs_path_from_fullname(fullname))
        )


def setup_loader(*args, **kwargs):
    sys.meta_path.append(IPFSFinder(*args, **kwargs))


if __name__ == '__main__':
    setup_loader('http://localhost:5001/api/v0/')
    filename = sys.argv[1]
    with open(filename, 'rb') as f:
        exec(compile(f.read(), filename, 'exec'), {})
