# Hack to restart server, again
import os

from advfoss.site import app

if __name__ == "__main__":
    if 'OPENSHIFT_PYTHON_IP' in os.environ:
        host = os.environ['OPENSHIFT_PYTHON_IP']
        port = int(os.environ['OPENSHIFT_PYTHON_PORT'])
        app.run(host=host, port=port, threaded=True)
    else:
        app.debug = True
        app.run(threaded=True)
