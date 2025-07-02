from setuptools import setup, find_packages
import subprocess

def classes_cleanup():
    backup_init_cmd="cp pycp2k/classes/__init__.py pycp2k/classes/.__init__.py"
    subprocess.run(backup_init_cmd.split(),shell=True)
    rmall_cmd="rm -rf pycp2k/classes/*"
    subprocess.run(rmall_cmd.split(),shell=True)
    mv_cmd="mv pycp2k/classes/.__init__.py pycp2k/classes/__init__.py"
    subprocess.run(mv_cmd.split(),shell=True)


def setup_manual():
    classes_cleanup()
    setup(
        name='pycp2k',
        version='0.2.1',
        description='A python interface to CP2K',
        url='https://github.com/SINGROUP/pycp2k.git',
        author='Lauri Himanen',
        author_email='lauri.himanen@gmail.com',
        license='MIT',
        packages=find_packages(),
        install_requires=[
            'future',
            'numpy',
            'ase',
        ],
        zip_safe=False)

if __name__ == "__main__":
    setup_manual()
