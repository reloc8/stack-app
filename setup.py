import setuptools

from install import private_dependency, GITHUB_PERSONAL_ACCESS_TOKEN


with open('version', 'r') as version:

    setuptools.setup(
        name='app',
        version=version.readline(),
        author='Alessio Vierti',
        packages=setuptools.find_packages(exclude=['tests']),
        install_requires=[
            private_dependency(personal_access_token=GITHUB_PERSONAL_ACCESS_TOKEN,
                               repo_user='reloc8', repo_name='stack-data-mining',
                               package_name='data_mining_stack', package_version='1.0.0'),
            private_dependency(personal_access_token=GITHUB_PERSONAL_ACCESS_TOKEN,
                               repo_user='reloc8', repo_name='stack-data-processing',
                               package_name='data_processing_stack', package_version='1.1.0')
        ],
        python_requires='>=3.6'
    )
