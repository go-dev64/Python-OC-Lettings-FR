Installation
=============



In order to use Oc_lettings_Site you must have **Python 3.10** or more installed.

Download : :download:`Python 3.10 <https://www.python.org/downloads/release/python-3100/>`.

You have to a GITHUB account, Sentry account, GIT CLI.

Clone Project
----------------

Select your working directory and download Oc_lettings_site with the following command in your console:

.. code-block:: console

   (.venv) $ git clone https://github.com/go-dev64/Python-OC-Lettings-FR.git


Create virtual environment / Packages installtion
-------------------------------------------------

- Move in Python-OC-Lettings-FR repository, create and activate virtual environment with command:

.. code-block:: console

   $ cd /path/to/Python-OC-Lettings-FR
   $ python -m venv venv
   $ ./venv/Scripts/Activate.ps1
   (.venv) $ pip install -r requirements.txt


Sentry  
-------

It is an application monitoring and debugging platform.
To use Oc_lettings_site you have:

   - Create a sentry account.
   - Create a new DJANGO project.
   - Retrieve the given Sentry DNS key


Congifguration
---------------

In the root repository, create a **.env** folder to store sensitive data such as secret key django and Sentry DNS given like that:

.. code-block:: console

   SECRET_KEY_DJANGO='your secret key django'
   SENTRY_DNS='your sentry dns'


Get started
---------------------------

* To launch the Oc_lettings_site, type in your console:

.. code-block:: console

   (.venv) $ python manage.py runserver


* The console will display:

.. code-block:: console

   Performing system checks...
   System check identified no issues (0 silenced).
   October 19, 2023 - 15:45:15
   Django version 3.0, using settings 'oc_lettings_site.settings'
   Starting development server at http://127.0.0.1:8000/
   Quit the server with CTRL-BREAK.


* In your browser, enter **localhost:8000** or click on link inside a console.

 You are on Oc_lettings_site home page .

