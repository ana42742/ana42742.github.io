from fabric.api import *
import fabric.contrib.project as project
import os
import shutil
import sys
import socketserver

from pelican.server import ComplexHTTPRequestHandler

# Remote server configuration
production = 'root@localhost:22'
dest_path = '/var/www'

# Rackspace Cloud Files configuration settings
env.cloudfiles_username = 'my_rackspace_username'
env.cloudfiles_api_key = 'my_rackspace_api_key'
env.cloudfiles_container = 'my_cloudfiles_container'

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'
DEPLOY_PATH = env.deploy_path
env.msg = 'Update blog'   # Commit message

# Github Pages configuration
env.github_pages_branch = "master"

# Port for `serve`
SERVER = '127.0.0.1'
PORT = 8000

def clean():
    """Remove generated files"""
    if os.path.isdir(DEPLOY_PATH):
        shutil.rmtree(DEPLOY_PATH)
        os.makedirs(DEPLOY_PATH)

def build():
    """Build local version of site"""
    local('pelican -s pelicanconf.py')

def rebuild():
    """`build` with the delete switch"""
    local('pelican -d -s pelicanconf.py')

def regenerate():
    """Automatically regenerate site upon file modification"""
    local('pelican -r -s pelicanconf.py')

def serve():
    """Serve site at http://localhost:8000/"""
    os.chdir(env.deploy_path)

    class AddressReuseTCPServer(socketserver.TCPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(('', PORT), ComplexHTTPRequestHandler)

    sys.stderr.write('Serving on port {0} ...\n'.format(PORT))
    server.serve_forever()

def reserve():
    """`build`, then `serve`"""
    build()
    serve()

def preview():
    """Build production version of site"""
    local('pelican -s publishconf.py')

def cf_upload():
    """Publish to Rackspace Cloud Files"""
    rebuild()
    with lcd(DEPLOY_PATH):
        local('swift -v -A https://auth.api.rackspacecloud.com/v1.0 '
              '-U {cloudfiles_username} '
              '-K {cloudfiles_api_key} '
              'upload -c {cloudfiles_container} .'.format(**env))

# @hosts(production) > Removed
def publish(commit_message):
    """Automatic deploy  to GitHub Pages"""
    env.msg = commit_message
    env.GH_TOKEN = os.getenv('GH_TOKEN')
    env.TRAVIS_REPO_SLUG = os.getenv('TRAVIS_REPO_SLUG')
    clean()
    local('pelican -s publishconf.py')
    with hide('running', 'stdout', 'stderr'):
        local("ghp-import -m '{msg}' -b {github_pages_branch} {deploy_path}".format(**env))
        local("git push -fq https://{GH_TOKEN}@github.com/{TRAVIS_REPO_SLUG}.git {github_pages_branch}".format(**env))

def gh_pages():
    """Publish to GitHub Pages"""
    rebuild()
    local("ghp-import -b {github_pages_branch} {deploy_path} -p".format(**env))

def deploy():
    """Push to GitHub pages"""
    env.msg = "Build site"
    clean()
    preview()
    local("ghp-import -m '{msg}' -b {github_pages_branch} {deploy_path}".format(**env))
    local("git push origin {github_pages_branch}".format(**env))
