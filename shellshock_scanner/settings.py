BOT_NAME = 'ShellshockScanner'
USER_AGENT = 'MozilShellshockScanner (https://github.com/cdodd/shellshock-scanner)'

SPIDER_MODULES = ['shellshock_scanner.spiders']
NEWSPIDER_MODULE = 'shellshock_scanner.spiders'

DEFAULT_REQUEST_HEADERS = {
    'x-shellshock-scan': '() { :;}; echo x-shellshock-status: vulnerable',
}
