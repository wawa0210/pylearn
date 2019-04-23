import click 
import subprocess
import os
import sys
import time
import docker
import powershellutils

@click.group()
def cli1():
    pass
@cli1.command(name='install',short_help='install dce-engine on windows',help='install dce-engine on windows') 
@click.option('--username', required=True,
        help ='This is a install username')
@click.option('--mobile', default ='18012345678', required=True,
        help ='This is a install mobile')
def hello(username,mobile): 
    click.echo('Hello, %s,your mobile is %s'  % (username,mobile))
    stdout,error = powershellutils.invoke_powershell('.\demo.ps1',subprocess.CREATE_NEW_CONSOLE)
    click.echo(stdout)

@click.group()
def cli2():
    pass
@cli2.command(name='uninstall',short_help='uninstall dce-engine on windows',help='uninstall dce-engine on windows') 
@click.option('--username', required=True,
        help ='This is a uninstall  username')
@click.option('--mobile', default ='18012345678', required=True,
        help ='This is a uninstall mobile')
def uninstall(username,mobile): 
    click.echo('Hello, %s,your mobile is %s'  % (username,mobile)) 

if __name__=="__main__":
        cli = click.CommandCollection(sources=[cli1, cli2])
        cli()