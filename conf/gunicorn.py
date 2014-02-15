import os
import multiprocessing

cart_dir = os.environ["OPENSHIFT_ADVANCED_PYTHON_DIR"]
tmp_dir = os.environ["OPENSHIFT_TMP_DIR"]


if os.environ["OPENSHIFT_PYTHON_WORKERS"]:
	works = os.environ["OPENSHIFT_PYTHON_WORKERS"]
else
	workers = multiprocessing.cpu_count() * 2 + 1

worker_class = "gevent"
daemon = True
bind = "unix:{0}run/appserver.sock".format(cart_dir)
pidfile = "{0}run/appserver.pid".format(cart_dir)

accesslog = "{0}logs/appserver.access.log".format(cart_dir)
errorlog = "{0}logs/appserver.error.log".format(cart_dir)

worker_tmp_dir = "{0}".format(tmp_dir)
tmp_upload_dir = "{0}".format(tmp_dir)