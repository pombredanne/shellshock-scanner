BOT_NAME = 'ShellshockScanner'
USER_AGENT = 'ShellshockScanner'

SPIDER_MODULES = ['shellshock_scanner.spiders']
NEWSPIDER_MODULE = 'shellshock_scanner.spiders'

DEFAULT_REQUEST_HEADERS = {
    'x-shellshock-scan': '() { :;}; echo x-shellshock-status: vulnerable',
}
