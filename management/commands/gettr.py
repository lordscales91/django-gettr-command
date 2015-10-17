from django.core.management.commands import makemessages
"""
I love the Qt library, surely some Django developers love it too which could explain why the "events" are called "signals".
Sadly they follow the convention of naming the xgettext methods with an underscore '_'. It feels weird to me call any 
variable or method like that so, I've made this command which will add the tr keyword to the xgettext options.
"""
class Command(makemessages.Command):
    xgettext_options = makemessages.Command.xgettext_options + ['--keyword=tr']