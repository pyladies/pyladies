import static
import os

SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
app = static.Cling(os.path.join(SITE_ROOT, '_site'))
