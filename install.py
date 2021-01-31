import pip
import os
from typing import AnyStr


GITHUB_PERSONAL_ACCESS_TOKEN = os.getenv('GITHUB_PERSONAL_ACCESS_TOKEN')


def private_dependency(personal_access_token: AnyStr,
                       repo_user: AnyStr, repo_name: AnyStr,
                       package_name: AnyStr, package_version: AnyStr):
    """Defines a dependency from a private Github repository

    :param personal_access_token:   Github Personal Access Token
    :param repo_user:               Dependency repository user
    :param repo_name:               Dependency repository name
    :param package_name:            Dependency package name
    :param package_version:         Dependency repository release (tag)
    :return:                        The dependency specification for the install_requires field
    """

    return f'{package_name} @ ' \
           f'git+https://{personal_access_token}@github.com/' \
           f'{repo_user}/{repo_name}.git/@{package_version}#egg={package_name}-0'


if __name__ == '__main__':

    import data_processing_stack.dependencies
    import data_mining_stack.dependencies

    dependencies = data_mining_stack.dependencies.DEPENDENCIES + data_processing_stack.dependencies.DEPENDENCIES
    for dependency in dependencies:
        uri = private_dependency(
            personal_access_token=GITHUB_PERSONAL_ACCESS_TOKEN,
            repo_user='reloc8', repo_name=dependency.project_name,
            package_name=dependency.package_name, package_version=dependency.release_version
        )
        location = f'stack/lambda/{dependency.package_name}/{dependency.release_version}/python'
        args = ['install', uri, '-t', location]
        pip.main(args=args)
