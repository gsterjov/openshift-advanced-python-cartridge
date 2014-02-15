## OpenShift Advanced Python Cartridge

Inspired by the [Advanced Ruby Cartridge](https://github.com/openshift-cartridges/advanced-ruby-cartridge) this cartridge attempts to add support for the various WSGI-compliant python servers to the OpenShift platform.
It does this by combining a modified python cartridge with the [downloadable Nginx cartridge](https://github.com/gsterjov/openshift-nginx-cartridge) as a reverse proxy.


### Why?

The official python cartridge uses Apache and mod_wsgi to serve your app which isn't asynchronous and presents a problem for websockets. An alternative is to provide an app.py file which allows you to avoid mod_wsgi and use something like gevent, but that elimintates the ability to serve static files through a fast webserver like Apache or Nginx.


### Installation

To install this cartridge use the cartridge reflector when creating an app

	rhc create-app myapp http://cartreflect-claytondev.rhcloud.com/reflect?github=gsterjov/openshift-advanced-python-cartridge


### Usage

Using the cartridge isn't very different to the official python cartridge. Instead of providing a WSGI <code>application()</code> function at <code>wsig/application</code> you instead provide the <code>application()</code> function at <code>app.py</code>. This file will be used directly by all the available servers.

By default *wsgiref* is used so a working environment can be provided immediately. This is easily changed by setting the OPENSHIFT_PYTHON_SERVER environment variable and then restarting or redeploying the app.

	rhc env set OPENSHIFT_PYTHON_SERVER=gunicorn
	rhc app restart

Be aware, however, that restarting/redeploying after changing servers for the first time might take a fair amount of time. This is because the server packages get compiled and installed on an as needed basis. Gevent and Gunicorn (which is configured to use gevent as its workers), for example, needs to be compiled within the app as OpenShift doesn't provide it as a system level package.


### Supported servers

 - wsgiref
 - gevent
 - gunicorn


### Configuration

There is little to no configuration required as most of the details lay in the interaction between Nginx and the WSGI server package. All that is required is to define the <code>application()</code> function in <code>app.py</code>.
Any configuration for the server package will be exposed via environment variables.

#### Environment Variables

<code>OPENSHIFT_PYTHON_WORKERS</code> - The number of workers to spawn for packages like gunicorn. Default: <code>num_cpus * 2 + 1</code>


### Static files

Static files will be served from the <code>public/</code> directory. These files will be served directly by Nginx.